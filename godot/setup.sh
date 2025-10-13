#!/bin/sh

#cd $(dirname "$0") #if someone using pyenv this behaves funny. just assume user is in root

echo $(pwd)
echo "Updating git submodules"
git submodule update --init --recursive --remote

echo "Building rust lib"
python libvpuppr/build.py --debug

echo "Copying gdextension files"

rm libvpuppr.gdextension
cp libvpuppr/libvpuppr.gdextension .

