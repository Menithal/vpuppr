#!/bin/sh

echo $(pwd)

echo "Building rust lib"

rm libvpuppr/libvpuppr.gdextension .
python libvpuppr/build.py --debug

echo "Copying gdextension files"

rm libvpuppr.gdextension
cp libvpuppr/libvpuppr.gdextension .

