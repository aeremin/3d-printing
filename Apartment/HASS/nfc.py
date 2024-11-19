import cadquery as cq

board_width = 50
board_dimensions = (board_width, 77, False)
floor_thickness = 2
wall_thickness = 1.2
inside_height = 7
holes = [(board_width / 2, 35), (board_width / 2, 35 + 23)]
hole_diameter = 2.4
beeper_center = (board_width / 2 + 19.25, 35 - 6.5)

lower = (cq.Workplane().rect(*board_dimensions).offset2D(wall_thickness).extrude(floor_thickness + inside_height)
         .faces("-Z").workplane(offset=floor_thickness, invert=True).tag("bottom").rect(*board_dimensions).extrude(inside_height, combine="cut")
         .workplaneFromTagged("bottom").pushPoints(holes).circle(hole_diameter / 2).extrude(inside_height - 1)
         .workplaneFromTagged("bottom").pushPoints([beeper_center]).slot2D(12, 3, 90).cutBlind(-1)
         )

cutter_usb = cq.Workplane(origin=(0, 0, floor_thickness)).pushPoints([(-wall_thickness, 7)]).box(wall_thickness, 12, inside_height, centered=False)

lower = lower.cut(cutter_usb)

cq.exporters.export(lower, 'lower.stl')

ceiling_thickness = 1
board_thickness = 2

actual_board_width = 41
leftover_space = (board_width - actual_board_width) / 2 - 0.2

upper = (cq.Workplane().rect(*board_dimensions).extrude(ceiling_thickness)
        .faces("+Z").workplane().tag("bottom")
         .pushPoints(holes).circle(hole_diameter / 2 + 0.1).pushPoints(holes).circle(3.5).extrude(inside_height - ceiling_thickness - board_thickness)
         .workplaneFromTagged("bottom").pushPoints([(leftover_space / 2, holes[1][1]), (board_width - leftover_space / 2, holes[1][1])]).rect(leftover_space, 34)
         .pushPoints([(board_width, 0)]).rect(-20, 6, centered=False).extrude(inside_height - ceiling_thickness)
)

cutter_beeper = cq.Workplane().pushPoints([(board_width - beeper_center[0], beeper_center[1])]).cylinder(15, 6)

upper = upper.cut(cutter_beeper)

cq.exporters.export(upper, 'upper.stl')

# Box for cards

cards_box_dimensions = (56, 14, False)
cards_box_height = 40

cards_box = (cq.Workplane().rect(*cards_box_dimensions).offset2D(wall_thickness).extrude(cards_box_height)
        .faces("-Z").workplane(offset=1, invert=True).rect(*cards_box_dimensions).extrude(cards_box_height, combine="cut")
        .faces("<Y").workplane(centerOption="CenterOfMass").pushPoints([(0, 12)]).slot2D(1.1 * cards_box_height, cards_box_dimensions[0] / 2, angle=90).cutBlind(-wall_thickness)
)

cq.exporters.export(cards_box, 'cards_box.stl')