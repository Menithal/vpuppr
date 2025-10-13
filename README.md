# Vpuppr

VTuber software made with Godot.

This is a recovery effort to get vpuppr to run on godot 4.5 using latest gdext conventions and possibly take over maintenance.

## Status

General:

- [x] Pathfind project status after decay
- [x] Use latest godot-rust conventions (monorepo)
- [ ] Recover vpuppr
	- [x] Build against latest rust and godot-rust (gdext)
		- [ ] Fix binding issues that have appeared
	- [ ] Does this run on godot 4.5 ?


# Legacy Status:
- [x] VRM model loading
- [x] Receive tracking data
- [x] Map tracking data onto a VRM model
- [ ] GUI (half-implemented)
- [ ] Save data

# Tracking Status

- [x] [MediaPipe](https://github.com/google/mediapipe)
- [x] [iFacialMocap](https://www.ifacialmocap.com/)
- [x] [MeowFace](https://play.google.com/store/apps/details?id=com.suvidriel.meowface)
- [x] [VTube Studio](https://denchisoft.com/)
- [ ] [OpenSeeFace](https://github.com/emilianavt/OpenSeeFace)
- [ ] [Mouse tracking](https://github.com/virtual-puppet-project/mouse-tracker)
- [ ] [Lip sync](https://github.com/virtual-puppet-project/real-time-lip-sync-gd)

## Building From Source

Prerequisites:

* Godot 4.5.x
* Rust 1.90+
* Python 3.8+ (any 3.x version is probably fine)

1. Run `python3 build.py` or `. build.sh`. 
	This will run `crate build` (debug) in `rust/` and move the resulting build to godot.
2. Run `godot/`

When ever updating the rust side, make sure to run the build script. This should automatically be hot reloaded on build.

In order to build GDMP, follow the instructions in [that repo](https://github.com/j20001970/GDMP).



## Contributing

Please see [the document about contributing](CONTRIBUTING.md).

Various technical documents are stored under the `docs` directory.


## Reasoning 

### Monorepository

Previously, Vpuppr was separated into two parts and used submodules. We had libVpuppr and Vpuppr. 
Since both are linked, and  libVpupper was unlikely going to be used elsewehere, both were combined instead of kept separate to keep development pipelines straight forward 
without having to swap around repositories or submodules.

This should also match the conventions used by modern godot-rust projects and match their examples,
even if gdextensions no longer support relative pathing OUTSIDE of the godot project.

History should have been maintained during the monorepository merge.