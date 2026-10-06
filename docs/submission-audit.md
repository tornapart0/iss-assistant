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
- `CAD/build_reference.FCMacro` and `CAD/reference-parts.json`: FreeCAD builder
  and sourced reference component dimensions/budget inputs.
- `CAD/reference/`: native FreeCAD and STEP reference layout, plus round-trip
  geometry verification. This is not a fabrication-ready integrated assembly.
- `BOM.csv` and `docs/bom.md`: core/full quantities, links, prices, availability
  and explicit allowances. Core budget USD 191.40; full budget USD 289.10.
- `docs/cad-reference.md`: CAD scope, regeneration and remaining engineering work.

Current packaging limitation: controller E01Controller1 has 0 mm shell clearance,
despite no nominal solid-volume overlaps. Its contact/mounting is unresolved.
The Pi is an external reference above the shell and requires mount/protection.

The Blender motion is kinematic. The cube responds to the driven tentacles, but
its force does not back-drive the servo rig. Joint pivots were inferred rather
than measured bearing axes. This is not proof of hardware payload, torque,
reliability, or space qualification. The STL and Blender model do not replace
the required complete STEP assembly. The added FreeCAD/STEP reference layout
preserves the author geometry and positions simplified electronics envelopes.
It still lacks measured mounts, joints, tendon routing, return mechanism,
harness and full component geometry; it is not the completed required assembly.

## Submission blockers

| Requirement | Current evidence | Work still required |
| --- | --- | --- |
| Complete STEP assembly including electronics | FreeCAD/STEP reference layout with 25 author pieces and simplified electronics envelopes | Resolve envelope allowances, packaging interference, mounts, joint retention, returns and tendon routing; obtain original author STEP/native CAD |
| Root CSV BOM with purchase links | Root BOM CSV with core/full quantities, links, prices and explicit budget allowances | Select stocked servos, exact material/harness/protection/fastener parts and obtain supplier/checkout quotes; replace all allowances |
| Firmware/software present | Single-servo joystick/FSR draft | Resolve number of actuators; implement matching arm control and Pi/display functionality |
| README description and motivation | Author's existing text retained | Author to clarify purpose, current design, limitations, and build sequence |
| Images, wiring, README BOM table | Prototype wiring and reference assembly renders/BOM table in technical docs | Complete integrated CAD/wiring; author to add the required images and BOM table to their own README |
| Feedback from other people | No feedback record supplied | Obtain and record real feedback and resulting design changes |
| PCB sources, if a custom PCB is used | No PCB supplied | Supply native project and manufacturing files if a PCB is designed; otherwise document module wiring |
| X-tier polish/complexity | Early CAD and firmware prototype | Demonstrate a mechanically buildable design, integrated electronics, and a justified budget |

The program explicitly disallows AI-generated READMEs. The existing README was
not rewritten. This audit and technical work must not be represented as the
author's independent work or as an approved submission. No feedback, build
photos, qualification evidence, or logged work hours were invented.

## Decisions needed

1. Confirm proposed ESP32-S3 DevKitC-1-N8R8 and MG90D reference choices; find
   stocked servos after testing torque/travel, and choose two- or four-arm scope.
2. Power supply/battery, protection, connectors, and expected simultaneous load.
3. Confirm proposed Pi Zero 2 W/ILI9341 display and implement their actual function.
4. Final arm transmission, return/unfurl mechanism, bearing axes, and mounting.
5. Editable CAD location and STEP export with electronics included.

Nothing has been submitted for funding. The highest tier can only be requested
after the design and evidence meet the requirements; a reviewer decides approval.
