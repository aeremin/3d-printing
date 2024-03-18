from cqgridfinity import *
import cadquery as cq

box = GridfinityBox(4, 2, 6, holes=True, unsupported_holes=True, solid=True, solid_ratio=0.7).cq_obj
box = box.faces("<Z[1]").workplane().rect(145, 61).cutBlind(-24)
cq.exporters.export(box, 'truvo.stl')
