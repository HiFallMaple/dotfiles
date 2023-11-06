#!/bin/bash
echo "Install: du-dust"
# Add installation commands here

# GitHub repository URL
github_repo="https://github.com/bootandy/dust"

# Use curl to fetch the release page content of the GitHub repository
github_page=$(curl -s "$github_repo/releases")

# Use grep to extract the latest release version
latest_release=$(echo "$github_page" | grep -oE "/releases/tag/v[0-9]+\.[0-9]+\.[0-9]+" | head -n 1)

# Extract the version number (e.g., 0.8.6)
version=$(echo "$latest_release" | grep -oE "[0-9]+\.[0-9]+\.[0-9]")

# Build the download URL for the .deb file
deb_url="https://github.com/bootandy/dust/releases/download/v$version/du-dust_"$version"_amd64.deb"

# Print the .deb file download URL
echo "Latest .deb file URL: $deb_url"

# Download the .deb file to a temporary location
wget "$deb_url" -O /tmp/du-dust.deb

# Install the .deb file using apt-get
sudo apt-get install -y /tmp/du-dust.deb

rm /tmp/du-dust.deb