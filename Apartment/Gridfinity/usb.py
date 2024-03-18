import cadquery as cq
from cqgridfinity import GridfinityBox

usb_a_width = 12
usb_a_height = 4.5
usb_a_wall_thickness = 0.4
usb_a_slot_thickness = 2.0
usb_a_outer_depth = 13.5
usb_a_inner_depth = 8

usb_c_width = 8.2
usb_c_height = 2.4
usb_c_outer_depth = 6

tolerance = 0.4

max_usb_a_height = 62

usb_a_box = GridfinityBox(2, 2, 12, holes=True, unsupported_holes=True, solid=True, solid_ratio=0.2).cq_obj
usb_a_box = usb_a_box.faces("<Z[1]").workplane().rarray(1, 11, 1, 8).rect(usb_a_width + tolerance, usb_a_height + tolerance).extrude(max_usb_a_height)
cq.exporters.export(usb_a_box, 'usb_a_box.stl')
