from cqgridfinity import *
import cadquery as cq

d = 15
l = 140
wall_thickness = 2

height_u = 3

finger_hole_size = 20

box: cq.Workplane = GridfinityBox(4, 1, height_u, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=((d / 2 - 1.5) / ((height_u - 1) * constants.GRHU))).cq_obj

box = (box.faces("<Z[1]").workplane()
       .transformed(rotate=cq.Vector(0, 90, 0))
       .rarray(1, d + wall_thickness, 1, 2)
       .cylinder(l, d / 2, combine="cut")
       .faces("<Z[1]").workplane().rect(finger_hole_size, 2 * d + 3 * wall_thickness).cutBlind(-d / 2 + 0.6)
       )

cq.exporters.export(box, 'flux_pen_x2.stl')
