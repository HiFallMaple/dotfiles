#!/bin/bash

source_line="deb http://archive.ubuntu.com/ubuntu noble main universe"

# check if the source line exists in the file
grep -qF "$source_line" /etc/apt/sources.list

# if not found, append it to the file
if [[ $? -ne 0 ]]; then
	echo "$source_line" | sudo tee -a /etc/apt/sources.list >/dev/null
	echo "Add source to /etc/apt/sources.list"
	cat > /etc/apt/preferences.d/fzf <<EOL
Package: *
Pin: release n=noble
Pin-Priority: -1

Package: fzf
Pin: release n=noble
Pin-Priority: 1001
EOL
	echo "Add preferences to /etc/apt/preferences.d/fzf"
	apt-get update
else
	echo "Source is already in /etc/apt/sources.list"
fi
