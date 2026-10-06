# Stardance submission audit

Target: X tier, up to USD 600, reviewed case by case. A funding ceiling is not an
automatic entitlement or a reason to inflate the bill of materials.

Sources checked October 5, 2026:
- https://stardance.hackclub.com/resources/tiers
- https://stardance.hackclub.com/resources/shipping-hardware

## Files included

- `CAD/octopus-2026-10-05.stl`: author's current Shapr3D tessellated export.
- `CAD/simulation/octopus-contact-demo.blend`: rig and baked cube-contact concept.
- `CAD/legacy/`: earlier chassis and disk concept, kept separately from the current design.
- `firmware/iss_assistant/iss_assistant.ino`: single-servo controller prototype.
- `docs/wiring.svg`: ESP32-S3 signal and sensor wiring for that prototype.
- `docs/octopus-concept.png`: render of the current geometry and contact demo,
  not a complete assembly with electronics.

The Blender motion is kinematic. The cube responds to the driven tentacles, but
its force does not back-drive the servo rig. Joint pivots were inferred rather
than measured bearing axes. This is not proof of hardware payload, torque,
reliability, or space qualification. The STL and Blender model do not replace
the required complete STEP assembly.

## Submission blockers

| Requirement | Current evidence | Work still required |
| --- | --- | --- |
| Complete STEP assembly including electronics | STL shell/segments and Blender concept only | Export original CAD assembly with chosen servos, boards, screen, power system, mounts, joints, and tendon routing |
| Root CSV BOM with purchase links | No exact parts or prices selected | Finalize models, quantities, supplier links, unit/extended prices, shipping and taxes |
| Firmware/software present | Single-servo joystick/FSR draft | Resolve number of actuators; implement matching arm control and Pi/display functionality |
| README description and motivation | Author's existing text retained | Author to clarify purpose, current design, limitations, and build sequence |
| Images, wiring, README BOM table | One existing embedded image; prototype wiring added | Add full electronics-included assembly image and completed BOM table |
| Feedback from other people | No feedback record supplied | Obtain and record real feedback and resulting design changes |
| PCB sources, if a custom PCB is used | No PCB supplied | Supply native project and manufacturing files if a PCB is designed; otherwise document module wiring |
| X-tier polish/complexity | Early CAD and firmware prototype | Demonstrate a mechanically buildable design, integrated electronics, and a justified budget |

The program explicitly disallows AI-generated READMEs. The existing README was
not rewritten. This audit and technical work must not be represented as the
author's independent work or as an approved submission. No feedback, build
photos, qualification evidence, or logged work hours were invented.

## Decisions needed

1. Exact ESP32-S3 board variant, servo model and actuator count.
2. Power supply/battery, protection, connectors, and expected simultaneous load.
3. Raspberry Pi model, display, and actual control function.
4. Final arm transmission, return/unfurl mechanism, bearing axes, and mounting.
5. Editable CAD location and STEP export with electronics included.

Nothing has been submitted for funding. The highest tier can only be requested
after the design and evidence meet the requirements; a reviewer decides approval.
