#!/bin/bash

# update apt
sudo apt-get update

# Packages
# For Jammy (22.04) , apt no prompt please
sudo DEBIAN_FRONTEND=noninteractive apt install -y bison build-essential cmake flex git libedit-dev \
libllvm14 llvm-14-dev libclang-14-dev python3 zlib1g-dev libelf-dev libfl-dev python3-distutils

# For Lua support
sudo apt-get -y install luajit luajit-5.1-dev

# Install and compile BCC
git clone https://github.com/iovisor/bcc.git
mkdir bcc/build; cd bcc/build
sudo cmake ..
sudo make
sudo make install
sudo cmake -DPYTHON_CMD=python3 .. # build python3 binding
pushd src/python/
make
sudo make install
popd