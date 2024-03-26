from cqgridfinity import *
import cadquery as cq

d = 24
l = 67

box: cq.Workplane = GridfinityBox(1, 1, 2, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=1).cq_obj

box = (box.faces("<Z[1]").workplane()
       .hole(d, 10)
       )

cq.exporters.export(box, 'foldedspace_glue.stl')
