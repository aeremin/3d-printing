import cadquery as cq

box_distance_between_holes = 47
box_holes_offset = 10
box_hole_diameter = 3
bracket_thickness = 5
m3_nut_side_distance = 5.7
m3_nut_side_thickness = 2
tower_height = 35
tower_distance = 52
tower_diameter = 10

def socket_adapter():
    return (
        cq.Workplane()
        .box(tower_distance + tower_diameter, 2 * box_holes_offset + tower_diameter, bracket_thickness)
        .faces(">Z").workplane().hole(4)
        .faces(">Z").workplane(origin=(0, -box_holes_offset))
        .rarray(box_distance_between_holes, 0, 2, 1)
        .hole(box_hole_diameter)
        .faces(">Z").workplane(origin=(0, 0))
        .rarray(tower_distance, 0, 2, 1).cylinder(tower_height - bracket_thickness, tower_diameter / 2, centered=(True, True, False))
        .faces(">Z").workplane().rarray(tower_distance, 0, 2, 1).hole(box_hole_diameter)
    )

cq.exporters.export(socket_adapter(), 'socket_adapter.stl')