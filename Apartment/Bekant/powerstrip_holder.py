import cadquery as cq

def powerstrip_holder():
    length = 40
    width = 20
    thickness = 8

    magnet_diameter = 5.1
    magnet_height = 8.5

    return cq.Workplane().box(width, thickness, length).faces(">Z").workplane().hole(magnet_diameter, magnet_height)

cq.exporters.export(powerstrip_holder(), 'powerstrip_holder.stl')
