#!/bin/sh

# Function to check and install dependencies
install_dependencies() {
  local dependency_file=$(full_path "$1/dependency")
  for package in $(cat "$dependency_file" | tr '\n' ' '); do
    # Skip empty lines
    if [ -z "$package" ]; then
      continue
    fi
    # Check if the package is not in installed_dependencies
    if ! is_installed $package; then
      if [ -d $(full_path "$package") ]; then
        # Check for a dependency file in the directory
        if [ -f $(full_path "/$package/dependency") ]; then
          install "$package"
        fi
      else
        echo "Dependency $package not found in base/appList or as a directory."
        exit 1
      fi
    fi
  done <"$dependency_file"

}

is_installed() {
  if echo "$installed_dependencies" | grep -qw "$1" || grep -q "$1" $app_list; then
    echo "$1 is already installed"
    return 0
  else
    echo "$1 is not installed"
    return 1
  fi
}

install() {
  if ! is_installed $1; then
    echo "Installing $1"
    # Check for a dependency file in the directory
    if [ -f $(full_path "$1/dependency") ]; then
      echo "Checking and installing dependencies for $1"
      install_dependencies "$1"
    fi
    echo "Running install.sh in directory: $1"
    (cd $(full_path "$1") && ./install.sh)
    installed_dependencies="$installed_dependencies $1"
  fi
}

full_path() {
  echo "$script_dir/$1"
}

# Get the directory of the script
script_dir="$(dirname "$0")"
app_list="$script_dir/base/appList"
# Declare an array to track installed dependencies
installed_dependencies=""

# Recursively check directories in the script's directory
find "$script_dir" -mindepth 1 -type d | while read -r dir; do
  # Check if the directory contains an install.sh file
  if [ -f "$dir/install.sh" ]; then
    base_dir=$(basename "$dir")
    install "$base_dir"
  fi
done