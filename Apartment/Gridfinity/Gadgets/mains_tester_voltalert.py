from cqgridfinity import *
import cadquery as cq
from Libraries import polyline_util

height_u = 4

voltalert_thickness = 20
slot_depth = 8

box: cq.Workplane = GridfinityBox(4, 1, height_u, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=(slot_depth / ((height_u - 1) * constants.GRHU))).cq_obj

l = polyline_util.PolylineFromOffsets((-155 / 2, -27 / 2))
l.add_point(60, 0).add_point(0, 3).add_point(50, 0).add_point(45, 4).add_point(0, 10)
l.add_point(-35, 10).add_point(-120, 0)

box = box.faces("<Z[1]").workplane().polyline(l.points).close().cutBlind(-slot_depth)

cq.exporters.export(box, 'voltalert.stl')