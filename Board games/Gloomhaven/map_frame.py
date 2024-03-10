from typing import Tuple, List

import cadquery as cq
import math

from Libraries.polyline_util import PolylineFromOffsets

# Parameters
half_size = 280
map_thickness = 3

frame_width = 15
frame_thickness = 9

groove_depth = 5

grove_overhang_angle = math.radians(70)

dovetail_depth = 8
dovetail_small_width = 5
dovetail_large_width = 7
dovetail_thickness = frame_thickness * 2 / 3

finger_width = 6

# Derived sizes
inner_half_size = half_size - groove_depth
outer_half_size = inner_half_size + frame_width

def cotan(angle):
    return math.tan(math.pi / 2 - angle)

def dovetail_joint(depth, small_width, large_width, thickness):
    return cq.Workplane().polyline([
        (0, small_width / 2),
        (depth, large_width / 2),
        (depth, -large_width / 2),
        (0, -small_width / 2),
    ]).close().extrude(thickness)

hanging_bolt_shaft_diameter = 4
hanging_bolt_head_diameter = 8
hanging_hole_offset = 10.5

def add_hanging_hole(w: cq.Workplane) -> cq.Workplane:
    return w.pushPoints([(0, 0)]).hole(hanging_bolt_shaft_diameter, 2) \
            .pushPoints([(0, 0, -2)]).hole(hanging_bolt_head_diameter, 3.2) \
            .pushPoints([(0, 3.5, 0)]).hole(hanging_bolt_head_diameter, 5.2)

if 'show_object' not in globals():
    def show_object(*args, **kwargs):
        pass

l = PolylineFromOffsets()
l.add_point(inner_half_size, 0)
l.add_point(0, -frame_width)
l.add_point(- (inner_half_size + frame_width), 0)
l.add_point(0, inner_half_size + frame_width)
l.add_point(frame_width, 0)
frame_template = cq.Workplane().polyline(l.points).close().extrude(frame_thickness)

map_tool = cq.Workplane("XY", (-groove_depth, -groove_depth, (frame_thickness - map_thickness) / 2)) \
    .rect(2 * half_size, 2 * half_size, False) \
    .extrude(map_thickness + groove_depth * cotan(grove_overhang_angle)) \
    .faces("+Z").edges() \
    .chamfer(groove_depth * cotan(grove_overhang_angle), groove_depth)

dovetail = dovetail_joint(dovetail_depth, dovetail_small_width, dovetail_large_width, dovetail_thickness)
finger = dovetail_joint(dovetail_depth, finger_width, finger_width, dovetail_thickness)

eps = 0.24
dovetail_hole= dovetail_joint(dovetail_depth + eps, dovetail_small_width + eps, dovetail_large_width + eps, dovetail_thickness + 0.6)
finger_hole = dovetail_joint(dovetail_depth + eps, finger_width + eps, finger_width + eps, dovetail_thickness + 0.6)


frame_lb = frame_template\
    .union(finger.translate((inner_half_size, - frame_width / 2 - 1.8)))\
    .cut(dovetail_hole.rotate((0, 0, 0), (0, 0, 1), 270).translate((-frame_width/ 2 - 1.8, inner_half_size)))\
    .cut(map_tool)

frame_rb = frame_template\
    .union(dovetail.translate((inner_half_size, - frame_width / 2 - 1.8)))\
    .cut(finger_hole.rotate((0, 0, 0), (0, 0, 1), 270).translate((-frame_width/ 2 - 1.8, inner_half_size)))\
    .rotate((inner_half_size, inner_half_size, 0), (inner_half_size, inner_half_size, 1), 90)\
    .cut(map_tool)

frame_rt = add_hanging_hole(frame_template\
    .union(finger.translate((inner_half_size, - frame_width / 2 - 1.8)))\
    .cut(dovetail_hole.rotate((0, 0, 0), (0, 0, 1), 270).translate((-frame_width/ 2 - 1.8, inner_half_size)))\
    .rotate((inner_half_size, inner_half_size, 0), (inner_half_size, inner_half_size, 1), 180)\
    .cut(map_tool).faces("<Z").workplane(origin=(2 * inner_half_size + hanging_hole_offset, 2 * inner_half_size + 5)))

frame_lt = add_hanging_hole(frame_template\
    .union(dovetail.translate((inner_half_size, - frame_width / 2 - 1.8)))\
    .cut(finger_hole.rotate((0, 0, 0), (0, 0, 1), 270).translate((-frame_width/ 2 - 1.8, inner_half_size)))\
    .rotate((inner_half_size, inner_half_size, 0), (inner_half_size, inner_half_size, 1), 270)\
    .cut(map_tool).faces("<Z").workplane(origin=(-hanging_hole_offset, 2 * inner_half_size + 5)))

print(f'Distance between hanging holes is {2 * (inner_half_size + hanging_hole_offset)}')

show_object(map_tool, "map", options={"alpha": 0.8, "color": (64, 164, 223)})
show_object(frame_lb, "frame_left_bottom", options={"alpha": 0.3})
show_object(frame_rb, "frame_right_bottom", options={"alpha": 0.3})
show_object(frame_lt, "frame_left_top", options={"alpha": 0.3})
show_object(frame_rt, "frame_right_top", options={"alpha": 0.3})

cq.exporters.export(frame_lb, 'frame_left_bottom.stl')
cq.exporters.export(frame_rb, 'frame_right_bottom.stl')
cq.exporters.export(frame_lt, 'frame_left_top.stl')
cq.exporters.export(frame_rt, 'frame_right_top.stl')

