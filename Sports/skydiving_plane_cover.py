import cadquery as cq

METAL_HOLE_DIAMETER = 4.8 - 0.2
ROD_THICKNESS = 2.9 + 0.4
OUTER_DIAMETER = 8
LENGTH = 254 / (10 + 10)

outer_cylinder = cq.Workplane().cylinder(LENGTH, OUTER_DIAMETER / 2).faces(">Z").hole(ROD_THICKNESS)
inner_cylinder = cq.Workplane().cylinder(LENGTH - 1, METAL_HOLE_DIAMETER / 2).faces(">Z").hole(ROD_THICKNESS)

closing_cylinder = (cq.Workplane().cylinder(LENGTH / 2, OUTER_DIAMETER / 2).faces(">Z").workplane().
                    cylinder(LENGTH / 2, METAL_HOLE_DIAMETER / 2, centered=(True, True, False)).faces(">Z").hole(ROD_THICKNESS, LENGTH / 2))

cq.exporters.export(outer_cylinder, 'skydiving_plane_outer_cylinder.stl')
cq.exporters.export(inner_cylinder, 'skydiving_plane_inner_cylinder.stl')
cq.exporters.export(closing_cylinder, 'skydiving_plane_closing_cylinder.stl')
