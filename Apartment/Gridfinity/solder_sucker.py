from cqgridfinity import *
import cadquery as cq

d = 13
l = 150

height_u = 3

box: cq.Workplane = GridfinityBox(4, 1, height_u, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=((d / 2) / ((height_u - 1) * constants.GRHU))).cq_obj

box = (box.faces("<Z[1]").workplane()
       .transformed(rotate=cq.Vector(0, 90, 0))
       .cylinder(l, d / 2, combine="cut")
       )

cq.exporters.export(box, 'solder_sucker.stl')
