from cqgridfinity import *
import cadquery as cq
from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

d = 24
l = 67

box = (GridfinityBoxWithHoles(1, 1, 2, solid_thickness=7).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG).hole(d, 10))

cq.exporters.export(box, 'foldedspace_glue.stl')
