#!/bin/sh

convert_home_path_full() {
	echo "$1" | sed "s|~/|$HOME/|g"
}

convert_home_path_short() {
	echo "$1" | sed "s|$HOME|~|g"
}

link() {
	lines=$(cat "$1/dotfile/linkList" | tr ' ' ',' | tr '\n' ' ')
	# Read the linkList file line by line
	for line in $lines; do
		if [ $(echo "$line" | awk -F',' '{print NF}') -ne 2 ]; then
			echo "Error: "$1"/dotfile/linkList: \""$line"\" line should contain exactly two space-separated path names"
		else
			# Split the line into two path names
			path1="$1/dotfile/"$(echo "$line" | awk -F',' '{print $1}')
			path2=$(echo "$line" | awk -F',' '{print $2}')
			full_path1=$(convert_home_path_full $path1)
			full_path2=$(convert_home_path_full $path2)
			short_path1=$(convert_home_path_short $path1)
			short_path2=$(convert_home_path_short $path2)
			echo "Link $short_path1 to $short_path2"
			if isExist "$full_path1"; then
				if isExist "$full_path2"; then
					# ask for replace
					read -r -p "Do you want to replace $short_path2 with $short_path1? (Y/n)" answer
					# default answer is yes
					if [ "$answer" = "" ] || [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
						# Replace the file
						rm -r "$full_path2"
						echo "Remove $short_path2"
					else
						echo "Skipped $short_path2"
						continue
					fi
				fi
				# Create a symbolic link
				parent_path=$(dirname "$path")
				if [ ! -d "$parent_path" ]; then
					mkdir -p "$parent_path"
				fi
				ln -s "$full_path1" "$full_path2"
				echo "Created a symbolic link from $short_path1 to $short_path2\n"
			fi
		fi
	done
}

isExist() {
	if [ -e "$1" ]; then
		echo "$1 already exists"
		return 0
	else
		echo "$1 does not exist"
		return 1
	fi
}

# Get the directory of the script
current_dir="$(pwd)"
dirs=$(find "$current_dir" -mindepth 1 -type d)

# Recursively check directories in the script's directory
for dir in $dirs; do
	# Check if the directory contains an install.sh file
	if [ -d "$dir/dotfile" ]; then
		if [ -f "$dir/dotfile/linkList" ]; then
			# echo "$dir/dotfile/linkList found"
			link "$dir"
		else
			echo "Error: $dir/dotfile/linkList not found\n Skipping $dir"
		fi
	fi
done
