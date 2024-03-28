from cqgridfinity import *
import cadquery as cq

w = 19.5
l = 164

depth = 13

height_u = 8

box: cq.Workplane = GridfinityBox(4, 1, height_u, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=(depth / ((height_u - 1) * constants.GRHU))).cq_obj

box = box.faces("<Z[1]").workplane().rect(l, w).cutBlind(-depth)

cq.exporters.export(box, 'obi_knife.stl')
