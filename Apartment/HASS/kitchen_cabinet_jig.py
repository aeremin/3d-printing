import cadquery as cq

mounting_hole_diameter = 35 - 0.2
mounting_hole_depth = 12
distance_from_edge = 6.2
distance_between_edges = 2
thickness = 3
awl_diameter = 2
jig_width = mounting_hole_diameter * 1.2

mounting_hole_offset = distance_from_edge + mounting_hole_diameter / 2

jig_old_side =  (cq.Workplane().tag("base")
                 .rect(mounting_hole_offset, jig_width, centered=(False, True)).extrude(thickness)
                 .workplaneFromTagged("base").pushPoints([(mounting_hole_offset, -mounting_hole_diameter / 2)])
                 .radiusArc((mounting_hole_offset, mounting_hole_diameter / 2), mounting_hole_diameter / 2).close().extrude(mounting_hole_depth)
                 .workplaneFromTagged("base").rect(-distance_between_edges, jig_width, centered=(False, True)).extrude(thickness + mounting_hole_depth)
)

jig_new_side = (
    cq.Workplane().pushPoints([(-distance_between_edges, 0)]).rect(-1.2 * mounting_hole_offset, 6, centered=(False, True)).extrude(thickness)
    .faces(">Z").workplane(origin=(-distance_between_edges - mounting_hole_offset, 0, 0)).hole(awl_diameter)
)

jig = jig_old_side.union(jig_new_side)

cq.exporters.export(jig, 'jig.stl')