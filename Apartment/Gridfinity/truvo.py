from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG
import cadquery as cq

box = (GridfinityBoxWithHoles(4, 2, 6, solid_ratio=0.7).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG).rect(145, 61).cutBlind(-24))
cq.exporters.export(box, 'truvo.stl')
