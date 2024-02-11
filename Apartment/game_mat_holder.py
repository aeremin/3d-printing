import cadquery as cq

def roll_holder(roll_diameter: float, has_bottom: bool = True):
    roll_radius = roll_diameter / 2
    height = 54
    wall_thickness = 1
    bottom_thickness = 3 if has_bottom else 0

    tape_width = 20
    tape_thickness = 1

    base_width = 30
    base_thickness = 10

    chamfer_r = 3

    return (cq.Workplane()
            .sketch()
            .circle(roll_radius + wall_thickness, mode="a")
            .push([(roll_radius, 0)])
            .rect(base_thickness, base_width, mode="a", tag="base")
            .vertices(">X", tag="base").fillet(chamfer_r)
            .push([(roll_radius + (base_thickness - tape_thickness) / 2, 0)])
            .rect(tape_thickness, tape_width, mode="s")
            .finalize()
            .extrude(height)
            .faces(">Z")
            .workplane()
            .hole(roll_diameter, height - bottom_thickness)
    )

cq.exporters.export(roll_holder(54, has_bottom=True), 'frostpunk_bottom.stl')
cq.exporters.export(roll_holder(54, has_bottom=False), 'frostpunk_top.stl')

cq.exporters.export(roll_holder(80, has_bottom=True), 'nemesis_playermat_bottom.stl')
cq.exporters.export(roll_holder(80, has_bottom=False), 'nemesis_playermat_top.stl')
