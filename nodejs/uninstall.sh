#!/bin/bash
echo "Uninstall: nodejs"
# Add uninstallation commands here

sudo apt-get purge nodejs &&\
rm -r /etc/apt/sources.list.d/nodesource.list &&\
rm -r /etc/apt/keyrings/nodesource.gpg