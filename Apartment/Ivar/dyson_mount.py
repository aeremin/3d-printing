import cadquery as cq
from typing import Tuple, List


def connector():
    plank_w = 10.2
    plank_h = 41.9
    width = 20
    thickness = 2
    overhang = 10
    interhole_distance = 125
    hole_distance_from_edge = 6

    m4_diameter = 4
    m4_nut_side_distance = 7.3
    m4_nut_thickness = 3.2
    bolt_length = 12

    total_height = interhole_distance + 2 * hole_distance_from_edge
    total_width = plank_w + 2 * thickness

    nut_hole_depth = total_width - bolt_length + m4_nut_thickness

    bolt_centers = [(-interhole_distance / 2, 0), (interhole_distance / 2, 0)]

    main_part = (
        cq.Workplane()
        .box(total_width, total_height, width)
        .faces(">X").workplane().pushPoints(bolt_centers)
            .hole(m4_diameter)
        .faces(">X").workplane().pushPoints(bolt_centers)
            .polygon(6, m4_nut_side_distance, circumscribed=True).cutBlind(-nut_hole_depth)
    )

    cutter = (
        cq.Workplane()
        .box(plank_w, plank_h, width)
        .pushPoints([((plank_w + thickness) / 2, 0, 0)])
        .box(thickness, plank_h - 2 * overhang, width)
    )

    return main_part.cut(cutter)

r = connector()
cq.exporters.export(connector(), 'dyson_mount.stl')
