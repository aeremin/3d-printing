import cadquery as cq

INNER_DIAMETER = 4.2
OUTER_DIAMETER = 8
LENGTH = 254 / (10 + 10)

r = cq.Workplane().cylinder(LENGTH, OUTER_DIAMETER / 2).faces(">Z").hole(INNER_DIAMETER)

cq.exporters.export(r, 'sample_4.stl')
