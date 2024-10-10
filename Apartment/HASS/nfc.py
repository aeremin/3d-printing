import cadquery as cq

board_dimensions = (102, 54, False)
floor_thickness = 3
wall_thickness = 1.2
inside_height = 13


lower = (cq.Workplane().rect(*board_dimensions).offset2D(wall_thickness).extrude(floor_thickness + inside_height)
         .faces("-Z").workplane(offset=floor_thickness, invert=True).tag("bottom").rect(*board_dimensions).extrude(inside_height, combine="cut")
         .workplaneFromTagged("bottom").pushPoints([(66, 9), (15, 51)]).circle(1.5).extrude(inside_height)
         )

cutter_beeper = cq.Workplane().pushPoints([(25, board_dimensions[1])]).box(13, wall_thickness, floor_thickness + inside_height, centered=False)
cutter_usb = cq.Workplane(origin=(0, 0, floor_thickness + inside_height - 4)).pushPoints([(83, -wall_thickness)]).box(8, wall_thickness, 4, centered=False)

lower = lower.cut(cutter_beeper).cut(cutter_usb)

cq.exporters.export(lower, 'lower.stl')

lip_height = 2.0
ceiling_thickness = 0.4

upper = (cq.Workplane().rect(*board_dimensions).offset2D(2 * wall_thickness).extrude(ceiling_thickness + lip_height)
        .faces("-Z").workplane(offset=ceiling_thickness, invert=True).tag("top").rect(*board_dimensions).offset2D(wall_thickness).extrude(lip_height, combine="cut")
)

cutter_usb = cq.Workplane().pushPoints([(9, - 2 * wall_thickness)]).box(13, wall_thickness + 2 , 4, centered=False)
cutter_led = cq.Workplane().pushPoints([(82, -wall_thickness)]).box(6, 7, 4, centered=False)

upper = upper.cut(cutter_usb).cut(cutter_led)

cq.exporters.export(upper, 'upper.stl')