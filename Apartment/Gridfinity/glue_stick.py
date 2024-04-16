from cqgridfinity import *
import cadquery as cq
from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

d = 29
l = 103

box = (GridfinityBoxWithHoles(3, 1, 5, solid_thickness=d / 2 - 1.5).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG)
       .transformed(rotate=cq.Vector(0, 90, 0))
       .cylinder(l, d / 2, combine="cut")
       .faces("<Z[1]").workplane().rarray(l, 1, 2, 1).sphere(10, combine="cut")
       )

cq.exporters.export(box, 'glue_stick.stl')
