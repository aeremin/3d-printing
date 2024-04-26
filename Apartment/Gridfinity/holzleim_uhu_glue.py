import cadquery as cq
from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

d = 39
l = 114

box = (GridfinityBoxWithHoles(3, 1, 7, solid_thickness=d / 2 - 1.5).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG)
       .transformed(rotate=cq.Vector(0, 90, 0))
       .cylinder(l, d / 2, combine="cut")
       )

cq.exporters.export(box, 'holzleim_uhu_glue.stl')
