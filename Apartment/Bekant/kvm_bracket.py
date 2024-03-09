import cadquery as cq

def bracket_for_box(box_width, box_height, ears_length = 30, bracket_width = 15, bracket_thickness = 3):
    m3_diameter = 3
    hole_offset = (box_width  + bracket_thickness + ears_length) / 2

    return (cq.Workplane().box(box_width + 2 * ears_length, box_height + bracket_thickness, bracket_width, centered=(True, False, True))
        .cut(cq.Workplane().pushPoints([(0, bracket_thickness)]).box(box_width, box_height, bracket_width, centered=(True, False, True)))
        .cut(cq.Workplane().pushPoints([(-hole_offset, 0), (+hole_offset, 0)]).box(ears_length - bracket_thickness, box_height, bracket_width, centered=(True, False, True)))
        .faces("<Y[1]").workplane().pushPoints([(-hole_offset, 0), (+hole_offset, 0)]).cskHole(m3_diameter, 2 * m3_diameter, 90)
        )

def kvm_bracket():
    kvm_width = 270
    kvm_height = 26
    return bracket_for_box(kvm_width, kvm_height)

def printer_powerbrick_bracket():
    return bracket_for_box(box_width=70, box_height=35, ears_length=24)


cq.exporters.export(kvm_bracket(), 'kvm_bracket.stl')
cq.exporters.export(printer_powerbrick_bracket(), 'printer_powerbrick_bracket.stl')
