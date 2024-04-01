import cadquery as cq

d = 32
r = 5.7 / 2

r = cq.Workplane().box(d, 2 * r, 2).faces("<Z").workplane(invert=True).rarray(d, 1, 2, 1).circle(r).extrude(20)

cq.exporters.export(r, 'pitch_tester.stl')