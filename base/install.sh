#!/bin/sh

# sudo apt-get update
# sudo apt-get -y upgrade

# Get the file name parameter
list_file="appList"

# Get the directory of the script
script_dir="$(dirname "$0")"

# Construct the full path to the file in the script's directory
list_file="$script_dir/$list_file"

# Check if the file exists
if [ ! -f "$list_file" ]; then
  echo "$list_file does not exist"
  exit 1
fi

# Read package names from the file and store them in a space-separated string
packages=$(cat "$list_file" | tr '\n' ' ')

# Use dpkg to query the status of all packages and store the result in a variable
dpkg_status=$(dpkg -l $packages 2>/dev/null)

# Use a loop to install packages that are not already installed
for package in $packages; do
  if ! echo "$dpkg_status" | grep -q "ii  $package"; then
    echo "Installing $package..."
    apt-get -y install "$package"
  else
    echo "$package is already installed."
  fi
done
