#!/bin/bash

# Installing Dependencies
sudo apt update && apt upgrade
sudo apt install build-essential -y
sudo apt install libssl-dev -y
sudo apt install libgmp-dev -y

# Inisiating Installation
echo -e "Cloning The Keyhunt Repository"
git clone https://github.com/albertobsd/keyhunt.git
echo -e "Building The Program"
cd keyhunt
make
PATH="$PATH:."
pip install Requests==2.31.0
chmod +x run_main.sh
chmod +x run_notif.sh
cd ..
