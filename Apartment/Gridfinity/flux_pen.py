from cqgridfinity import *
import cadquery as cq

from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

d = 15
l = 140
wall_thickness = 2

finger_hole_size = 20

box = (GridfinityBoxWithHoles(4, 1, 3, solid_thickness=d / 2 - 1.5).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG)
       .transformed(rotate=cq.Vector(0, 90, 0))
       .rarray(1, d + wall_thickness, 1, 2)
       .cylinder(l, d / 2, combine="cut")
       .faces("<Z[1]").workplane().rect(finger_hole_size, 2 * d + 3 * wall_thickness).cutBlind(-d / 2 + 0.6)
       )

cq.exporters.export(box, 'flux_pen_x2.stl')
