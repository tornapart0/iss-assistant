"""Render the reference layout in Blender from FreeCAD's verified placements."""
import json
from pathlib import Path

import bpy
from mathutils import Vector


root = Path(__file__).resolve().parents[1]
report = json.loads((root / 'CAD/reference/verification.json').read_text())
assert report['step_valid']
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_mesh.stl(filepath=str(root / 'CAD/octopus-2026-10-05.stl'))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.separate(type='LOOSE')
bpy.ops.object.mode_set(mode='OBJECT')
shell = None
for obj in list(bpy.context.scene.objects):
    obj.scale = (0.001, 0.001, 0.001)
    bpy.context.view_layer.update()
    if obj.dimensions.z > 0.06:
        shell = obj
        obj.color = (0.75, 0.78, 0.80, 1)
    else:
        obj.color = (0.28, 0.62, 0.65, 1)
assert shell is not None
colors = {'E01': (0.25, 0.55, 0.35), 'E02': (0.24, 0.31, 0.40),
          'E03': (0.43, 0.38, 0.45), 'E04': (0.74, 0.53, 0.17),
          'P01': (0.25, 0.55, 0.35), 'P02': (0.08, 0.14, 0.18)}
for part in report['components']:
    if 'envelope_mm' not in part:
        continue
    size = Vector(part['envelope_mm']) * 0.001
    origin = Vector(part['placement_mm']) * 0.001
    bpy.ops.mesh.primitive_cube_add(size=1, location=origin + size / 2)
    obj = bpy.context.object
    obj.name = part['name']
    obj.dimensions = size
    obj.color = (*colors.get(part['bom_id'], (0.35, 0.38, 0.40)), 1)

camera_data = bpy.data.cameras.new('ReferenceCamera')
camera = bpy.data.objects.new('ReferenceCamera', camera_data)
bpy.context.scene.collection.objects.link(camera)
camera.location = (0.55, -0.58, 0.65)
camera.rotation_euler = (Vector((0.02, 0.13, 0.018)) - camera.location).to_track_quat('-Z', 'Y').to_euler()
camera_data.type = 'ORTHO'
camera_data.ortho_scale = 0.56
camera_data.clip_start = 0.001
scene = bpy.context.scene
scene.camera = camera
scene.render.engine = 'BLENDER_WORKBENCH'
scene.display.shading.light = 'STUDIO'
scene.display.shading.color_type = 'OBJECT'
scene.display.shading.show_shadows = True
scene.display.shading.show_cavity = True
scene.display.shading.background_type = 'WORLD'
scene.world = bpy.data.worlds.new('ReferenceBackground')
scene.world.color = (0.91, 0.93, 0.94)
scene.render.resolution_x = 1600
scene.render.resolution_y = 1200
scene.render.resolution_percentage = 100
scene.render.filepath = str(root / 'docs/reference-layout.png')
bpy.ops.render.render(write_still=True)
shell.hide_render = True
for part in report['components']:
    if 'envelope_mm' in part and part['bom_id'] not in {'E01', 'E02', 'P01', 'P02'}:
        bpy.data.objects[part['name']].hide_render = True
camera.location = (0.37, -0.30, 0.38)
camera.rotation_euler = (Vector((-0.01, 0.09, 0.03)) - camera.location).to_track_quat('-Z', 'Y').to_euler()
camera_data.ortho_scale = 0.38
scene.render.filepath = str(root / 'docs/reference-interior.png')
bpy.ops.render.render(write_still=True)
