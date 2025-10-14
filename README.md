## Vpuppr

# NOTE THIS DOES NOT WORK YET, recovery in progress.

VTuber software made with Godot.

This is a recovery effort to get vpuppr to run on godot 4.5 using latest godot-rust conventions and possibly take over maintenance, used as a learning opportunity to  learn the intricities of godot, and godot-rust AND rust (no experience in ANY of them) while trying to make something this repo maintainer wants to also use, spurred with the recent migration to linux, preferring a native one-click-all solution than running multiple compatability layers and apps.

## Status

General:

- [x] Pathfind project status after 2 years of dependency rot
- [x] Use latest godot-rust conventions (monorepo)
- [x] Recover vpuppr
	- [x] Build against latest rust and godot-rust (gdext)
		- [x] Fix binding issues that have appeared
	- [x] Does this run on godot 4.5 ?
		- [x] Update Addons!
			- [x] VRM and Godot-M-Toon-Shader
			- [x] RenIK
			- [ ] GDMP on HOLD: Have not updated due to latest just outright crashing Godot 4.5.
	- [x] Successfully Runs
- [ ] bugs bugs bugs
	- [ ] Buttons no worky
	- [ ] VRM Model file selector does now show up for Linux.


# Modern State:
- [ ] VRM model loading
- [ ] Receive tracking data
- [ ] Map tracking data onto a VRM model
- [ ] GUI (half-implemented)
- [ ] Save data

# Tracking Status

- [ ] [MediaPipe](https://github.com/google/mediapipe)
- [ ] [iFacialMocap](https://www.ifacialmocap.com/)
- [ ] [MeowFace](https://play.google.com/store/apps/details?id=com.suvidriel.meowface)
- [ ] [VTube Studio](https://denchisoft.com/)
- [ ] [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace)
- [ ] [Mouse tracking](https://github.com/virtual-puppet-project/mouse-tracker)
- [ ] [Lip sync](https://github.com/virtual-puppet-project/real-time-lip-sync-gd)

## Building From Source

Prerequisites:

* Godot 4.5.x
* Rust 1.90+
* Python 3.8+ (any 3.x version is probably fine)

1. In `rust/` run `crate build` (debug)
2. Run `godot/`

When ever updating the rust side, make sure to run the compile. Changes should be automatically reloaded into godot due to libvpuppr.gdextension configuration

In order to build GDMP, follow the instructions in [that repo](https://github.com/j20001970/GDMP).



## Contributing

Please see [the document about contributing](CONTRIBUTING.md).

Various technical documents are stored under the `docs` directory.


## Reasoning 

### Monorepository

Previously, Vpuppr was separated into two parts and used submodules. We had libVpuppr and Vpuppr. 
Since both are linked, and  libVpupper was unlikely going to be used elsewehere, both were combined instead of kept separate to keep development pipelines straight forward 
without having to swap around repositories or submodules.

This should also match the conventions used by modern godot-rust projects and match their examples.

History should have been maintained during the monorepository merge.


## Considerations 

### Change from V-sekai/RenIK to monxa/GodotIK.

While RenIK seems to be kept uptodate, its public documentation is non-existant as of 10-2025 (even just basic implementation example!), with the previous version used in VPuppr being 2 years old and has logical source code available. 

The recovery effort has no time to start digging further into a library that does not put any documentations online nor have any working examples. 