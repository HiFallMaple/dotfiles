#!/bin/sh

convert_home_path_full() {
	echo "$1" | sed "s|~/|$HOME/|g"
}

convert_home_path_short() {
	echo "$1" | sed "s|$HOME|~|g"
}

link() {
	local lines=$(cat "$1/dotfile/linkList" | tr ' ' ',' | tr '\n' ' ')
	# Read the linkList file line by line
	for line in $lines; do
		echo ""
		if [ $(echo "$line" | awk -F',' '{print NF}') -ne 2 ]; then
			echo "Error: "$1"/dotfile/linkList: \""$line"\" line should contain exactly two space-separated path names"
			exit 1
		fi
		# Split the line into two path names
		local path1="$1/dotfile/"$(echo "$line" | awk -F',' '{print $1}')
		local path2=$(echo "$line" | awk -F',' '{print $2}')
		local src_full_path=$(convert_home_path_full $path1)
		local dest_full_path=$(convert_home_path_full $path2)
		local src_short_path=$(convert_home_path_short $path1)
		local dest_short_path=$(convert_home_path_short $path2)
		echo "Link $src_short_path to $dest_short_path"

		if ! isExist "$src_full_path"; then
			echo "$src_short_path does not exist. Please check the file or directory is in the correct location."
			continue
		fi

		if ! isExist "$dest_full_path"; then
			# Create a symbolic link
			create_link "$src_short_path" "$src_full_path" "$dest_short_path" "$dest_full_path"
			continue
		fi

		local answer="";
		# ask for replace
		read -r -p "$dest_short_path already exists. Do you want to replace? (Y/n)" answer
		# default answer is yes
		if [ "$answer" = "" ] || [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
			# Replace the file
			rm -r "$dest_full_path"
			create_link "$src_short_path" "$src_full_path" "$dest_short_path" "$dest_full_path"
			echo "Replace $dest_short_path"
		else
			# Skip the file
			echo "Skip $dest_short_path"
		fi

	done
}

# parameters: $1: src_short_path, $2: src_full_path, $3: dest_short_path, $4: dest_full_path
create_link() {
	local src_short_path=$1
	local src_full_path=$2
	local dest_short_path=$3
	local dest_full_path=$4

	local parent_path=$(dirname "$dest_full_path")
	if [ ! -d "$parent_path" ]; then
		echo "Create directory $parent_path"
		mkdir -p "$parent_path"
	fi
	ln -s "$src_full_path" "$dest_full_path"
	echo "Created a symbolic link from $src_short_path to $dest_short_path"
}

isExist() {
	if [ -e "$1" ]; then
		return 0
	else
		return 1
	fi
}

# Get the directory of the script
current_dir="$(pwd)"
dirs=$(find "$current_dir" -mindepth 1 -type d)

# Recursively check directories in the script's directory
for dir in $dirs; do
	# Check if the directory contains an install.sh file
	if ! [ -d "$dir/dotfile" ]; then
		continue
	fi

	if ! [ -f "$dir/dotfile/linkList" ]; then
		echo "Error: $dir/dotfile/linkList not found\n Skipping $dir"
		continue
	fi
	
	link "$dir"
done
