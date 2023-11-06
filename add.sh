#!/bin/bash

# Check if folder names are provided as parameters
if [ $# -lt 1 ]; then
	echo "Please provide one or more folder names as parameters."
	exit 1
fi

# Iterate through provided folder names
for folder_name in "$@"; do
	# Check if the folder doesn't exist, create it
	if [ ! -d "$folder_name" ]; then
		mkdir -p "$folder_name"
		echo "$folder_name: folder created"
	else
		echo "$folder_name: folder already exists"
	fi

	# Check if install.sh file already exists
	if [ ! -f "$folder_name/install.sh" ]; then
		# Create install.sh if it doesn't exist
		cat <<EOL >"$folder_name/install.sh"
#!/bin/bash
echo "Install: $folder_name"
# Add installation commands here
EOL
		chmod +x "$folder_name/install.sh"
		esho "$folder_name: install.sh created"
	else
		echo "$folder_name: install.sh already exists"
	fi

	# Check if uninstall.sh file already exists
	if [ ! -f "$folder_name/uninstall.sh" ]; then
		# Create uninstall.sh if it doesn't exist
		cat <<EOL >"$folder_name/uninstall.sh"
#!/bin/bash
echo "Uninstall: $folder_name"
# Add uninstallation commands here
EOL
		chmod +x "$folder_name/uninstall.sh"
		echo "$folder_name: uninstall.sh created"
	else
		echo "$folder_name: uninstall.sh already exists"
	fi

	# Check if dependency file already exists
	if [ ! -f "$folder_name/dependency" ]; then
		# Create dependency file if it doesn't exist
		touch "$folder_name/dependency"
		echo "$folder_name: dependency file created"
	else
		echo "$folder_name: dependency file already exists"
	fi

	# Check if dotfile directory already exists
	if [ ! -d "$folder_name/dotfile" ]; then
		# Create dotfile directory if it doesn't exist
		mkdir -p "$folder_name/dotfile"
		echo "$folder_name: dotfile directory created"
	else
		echo "$folder_name: dotfile directory already exists"
	fi

	# Check if linkList file already exists
	if [ ! -f "$folder_name/dotfile/linkList" ]; then
		# Create linkList file if it doesn't exist
		touch "$folder_name/dotfile/linkList"
		echo "$folder_name: dotfile/linkList file created"
	else
		echo "$folder_name: dotfile/linkList file already exists"
	fi

	echo ""

done