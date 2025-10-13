#!/bin/sh

echo $(pwd)

echo "Building rust lib"

python libvpuppr/build.py --debug

echo "Copying gdextension files"

cp libvpuppr/libvpuppr.gdextension .

