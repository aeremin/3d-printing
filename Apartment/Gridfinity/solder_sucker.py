import cadquery as cq
from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

d = 13
l = 150

b = (GridfinityBoxWithHoles(4, 1, 3,
                            solid_thickness=d / 2).to_cq()
     .workplaneFromTagged(TOP_SURFACE_TAG).workplane()
     .transformed(rotate=cq.Vector(0, 90, 0))
     .cylinder(l, d / 2, combine="cut")
     )

cq.exporters.export(b, 'solder_sucker.stl')
