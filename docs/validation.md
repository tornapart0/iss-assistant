# Validation record

Checked October 5, 2026. This records software checks, not a hardware test.

## Firmware

Arduino CLI with Arduino-ESP32 3.3.12:

| Board target | Result | Flash | Static RAM |
| --- | --- | --- | --- |
| `esp32:esp32:esp32s3` | Compile passed | 290013 bytes / 1310720 | 22256 bytes / 327680 |
| `esp32:esp32:esp32` | Compile passed | 279540 bytes / 1310720 | 22228 bytes / 327680 |

No board was flashed. Servo pulse timing, real ADC readings, force calibration,
mechanical endpoints, torque, thermal behavior, and power loading remain untested.

## Blender contact concept

Blender 3.5.1, 220 frames, Earth gravity. With tentacle rigid-body colliders
enabled, the cube moves from approximately `(0.04434, 0.22265, 0.00772)` m after
landing to `(0.04165, 0.14809, 0.00773)` m at frame 65. With those colliders
removed, its XY position stays approximately `(0.04434, 0.22265)` m.
This comparison isolates tentacle contact from gravity/floor effects.

The rigid-body cache was then baked, saved, and reloaded. It remains baked; the
reloaded frame-65 cube position is approximately `(0.04127, 0.14778, 0.00741)` m.
The small trajectory difference is between bake and interactive simulation runs.
The simulation does not model a real tendon transmission or servo loads.

`docs/octopus-concept.png` was rendered and visually inspected. It shows only
the current shell, segments and contact props; no electronics assembly exists.
`docs/wiring.svg` passed XML parsing. `git diff --check` passed.
