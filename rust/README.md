# Vpuppr Rust Lib

A [GDExtension](https://docs.godotengine.org/en/stable/tutorials/scripting/gdextension/what_is_gdextension.html) made
with [godot-rust](https://github.com/godot-rust/gdext) for [vpuppr](https://github.com/Menithal/vpuppr).

This repository is meant to be used as a git submodule in the main vpuppr repository.

This is resurrected version of the original repository that got archived and abandoned and adapted to work with the Godot 4.5 and modern godot-rust.

You may find the original archived version [here](https://github.com/virtual-puppet-project/vpuppr).


## Building

Run `python build.py --help` for possible options. This is a simple wrapper around
`cargo build` and `cargo build --release` that also renames the output libraries
to `libvpuppr.dll` or `libvpuppr.so` depending on platform.

## License

MPL-2.0

