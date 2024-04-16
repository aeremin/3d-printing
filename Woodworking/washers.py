import cadquery as cq

for_ivar = cq.Workplane().cylinder(2.4, 8).faces(">Z").workplane().hole(6)
cq.exporters.export(for_ivar, 'for_ivar.stl')

for_drawer = cq.Workplane().cylinder(2.2, 8).faces(">Z").workplane().hole(6)
cq.exporters.export(for_drawer, 'for_drawer.stl')

