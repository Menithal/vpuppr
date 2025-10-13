# /usr/bin/env python

"""
Utility script for building consistent shared libraries for vpuppr.
"""

import os
from os import path
import subprocess
from argparse import ArgumentParser
from typing import Union, List
from enum import Enum
import platform
import shutil


def get_output_dir() -> Union[str, None]:
    """
    The output path for `cargo build`.
    """
    script_dir: str = path.dirname(__file__)
    output_dir: str = path.join(script_dir, "rust/target")

    return output_dir if path.isdir(output_dir) else None


class BuildFlag(Enum):
    DEBUG = 0
    RELEASE = 1


def move_file_if_os(file_path: str, os_type: str, flag: BuildFlag) -> bool:
    if not path.exists(file_path): return False
    
    print(os_type, "file exists, attempting to copy" )
    
    script_dir: str = path.dirname(__file__)
    godot_bin_dir: str = path.join(path.join(script_dir, "godot/bin/" ), "debug/" if flag == BuildFlag.DEBUG else "release/")

    os.makedirs(godot_bin_dir, exist_ok=True)
    
    shutil.copy(file_path, godot_bin_dir)
    print("Success. Open Godot Window and continue working")
    return True
 



def build(flag: BuildFlag) -> None:
    command: List[str] = ["cargo", "build"]

    if flag == BuildFlag.RELEASE:
        command.append("--release")

    os.chdir("./rust")

    ret = subprocess.run(command, text=True)

    if ret.returncode != 0:
        raise Exception("Failed to build: {}".format(ret.stderr))

    output_dir = get_output_dir()
    if not output_dir:
        raise Exception("Unable to get output directory")

    if flag == BuildFlag.DEBUG:
        output_dir = "{}/debug".format(output_dir)
    elif flag == BuildFlag.RELEASE:
        output_dir = "{}/release".format(output_dir)
    else:
        raise Exception("Bad build flag: {}".format(flag))

    if not path.isdir(output_dir):
        raise Exception(
            "{} does not exist, the build probably failed".format(output_dir))

    print(output_dir)
    

    if move_file_if_os(path.join(output_dir, "libvpuppr.so"), "Linux", flag): return
    if move_file_if_os(path.join(output_dir, "libvpuppr.dll"), "Windows", flag): return

    # Double check how this works in mac. Not sure.
    if move_file_if_os(path.join(output_dir, "libvpuppr.dyasm"), "Mac", flag): return




def main() -> None:
    # Make sure we are building in the correct directory
    os.chdir(path.dirname(__file__))

    parser = ArgumentParser("libvpuppr-build")
    parser.add_argument("--debug", action="store_true",
                        help="Build the lib in debug mode")
    parser.add_argument("--release", action="store_true",
                        help="Build the lib in release mode")

    args = parser.parse_args()

    changed = False

    # NOTE: I know it's possible to configure argparse to do this automatically, and I don't care
    if args.debug:
        changed = True
        build(BuildFlag.DEBUG)
    if args.release:
        changed = True
        build(BuildFlag.RELEASE)

    if not changed:
        raise Exception("An option must be selected")


if __name__ == "__main__":
    main()