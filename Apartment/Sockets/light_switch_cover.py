import cadquery as cq

def light_switch_cover(w: float, h: float):
    depth = 4.8
    thickness = 1
    wall_thickness = 1.6

    return (
        cq.Workplane()
        .box(w + 2 * wall_thickness, h + 2 * wall_thickness, depth + thickness)
        .faces(">Z").workplane()
        .rect(w, h).cutBlind(-depth, taper=7)
        .faces("<Z").workplane().text("НЕТ", 16, -2 * thickness, combine = "cut")
    )

width = 39
height = 24

cq.exporters.export(light_switch_cover(width, height), 'light_switch_cover_half.stl')
cq.exporters.export(light_switch_cover(width, width), 'light_switch_cover_full.stl')
