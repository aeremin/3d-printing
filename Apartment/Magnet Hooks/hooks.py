import cadquery as cq

magnet_hole_diameter = 6.4
magnet_hole_depth = 2.0
magnet_hole_height_offset = 0.2

def hook():
    path = cq.Workplane("XZ").line(0, 3).radiusArc((16, 3), 8).line(0, -3)
    section = cq.Workplane("XY").circle(4)
    return (section.sweep(path)
            .faces("<Z").workplane(offset=-magnet_hole_height_offset).rarray(16, 0, 2, 1, center=False)
            .hole(magnet_hole_diameter, magnet_hole_depth))

cq.exporters.export(hook(), 'hook.stl')