#!/bin/sh

# Function to check and install dependencies
install_dependencies() {
  local dependency_file=$(full_path "$1/dependency")
  for package in $(cat "$dependency_file" | tr '\n' ' '); do
    # Skip if the package is in installed_list
    if is_installed $package; then
      continue
    fi
    # Exit if the package is not in the appList file or is a directory
    if ! [ -d $(full_path "$package") ]; then
      echo "Dependency $package not found in base/appList or as a directory."
      exit 1
    fi
    # if there is a dependency file in the directory, install it
    if [ -f $(full_path "/$package/dependency") ]; then
      install "$package"
    fi
  done
}

is_installed() {
  if echo "$installed_list" | grep -qw "$1"; then
    return 0
  else
    return 1
  fi
}

install() {
  if is_installed $1; then
    return 0
  fi

  echo "Installing $1"
  # Check for a dependency file in the directory
  if [ -f $(full_path "$1/dependency") ]; then
    echo "Checking and installing dependencies for $1"
    install_dependencies "$1"
  fi

  echo "Running install.sh in directory: $1"
  (cd $(full_path "$1") && ./install.sh)
  installed_list="$installed_list $1"
}

install_base_apps() {
  # Check if the file exists
  if [ ! -f "$app_list" ]; then
    echo "$app_list does not exist"
    exit 1
  fi

  # Read package names from the file and store them in a space-separated string
  packages=$(cat "$app_list" | tr '\n' ' ')

  # Use dpkg to query the status of all packages and store the result in a variable
  dpkg_status=$(dpkg -l $packages 2>/dev/null)

  # Use a loop to install packages that are not already installed
  for package in $packages; do
    if ! echo "$dpkg_status" | grep -q "ii  $package"; then
      echo "Installing $package..."
      # sudo apt-get -y install "$package"

    else
      echo "$package is already installed."
    fi
    installed_list="$installed_list $package"
  done
}

full_path() {
  echo "$current_dir/$1"
}

# Get the directory of the script
current_dir=$(pwd)
app_list=$(full_path "/base/appList")
# Declare an array to track installed dependencies
installed_list=""

sudo apt-get update
sudo apt-get -y upgrade

install_base_apps

# Recursively check directories in the script's directory
find "$current_dir" -mindepth 1 -type d | while read -r dir; do
  # Check if the directory contains an install.sh file
  if [ -f "$dir/install.sh" ]; then
    base_dir=$(basename "$dir")
    install "$base_dir"
  fi
done
