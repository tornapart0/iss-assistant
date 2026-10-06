"""Run with FreeCADCmd to check the saved native model and STEP independently."""
import json
from pathlib import Path

import FreeCAD as App
import Part


root = Path(__file__).resolve().parents[1]
folder = root / 'CAD/reference'
report = json.loads((folder / 'verification.json').read_text())
doc = App.openDocument(str(folder / 'octopus-reference-assembly.FCStd'))
parts = [obj for obj in doc.Objects if obj.isDerivedFrom('Part::Feature')]
assert len(parts) == report['exported_solids'] == 47
assert len([obj for obj in parts if obj.BOM_ID == 'M01']) == 25
assert all(obj.Shape.isValid() and len(obj.Shape.Solids) == 1 for obj in parts)
by_name = {obj.Name: obj for obj in parts}
for record in report['components']:
    obj = by_name[record['name']]
    assert obj.Label == record['label']
    assert obj.BOM_ID == record['bom_id']
    assert abs(obj.Shape.Volume - record['volume_mm3']) < 0.001
    if 'envelope_mm' in record:
        assert all(abs(a - b) < 0.001 for a, b in zip(obj.Placement.Base, record['placement_mm']))
        assert [obj.Length.Value, obj.Width.Value, obj.Height.Value] == record['envelope_mm']
step = Part.read(str(folder / 'octopus-reference-assembly.step'))
assert step.isValid() and len(step.Solids) == len(parts)
assert abs(sum(obj.Shape.Volume for obj in parts) - step.Volume) < 0.01
assert report['step_valid'] and not report['packaging_interferences']
if report['nominal_minimum_shell_clearance_mm'] <= 0.001:
    assert report['surface_contacts'], 'Do not omit unresolved surface contacts from the report'
print('Saved native model and STEP verified: 47 valid solids; no nominal solid-volume overlap')
print('Unresolved surface contacts:', report['surface_contacts'])
