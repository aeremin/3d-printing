import cadquery as cq

def table(inset_length, inset_width, legroom = 660):
    inset_padding = 90
    leg_width = inset_padding

    table_thickness = 770 - 630

    full_length = inset_length + 2 * inset_padding
    full_width = inset_width + 2 * inset_padding

    leg_center_x = full_length / 2 - leg_width / 2
    leg_center_y = full_width / 2 - leg_width / 2

    return cq.Workplane().box(full_length, full_width, table_thickness).faces("<Z").workplane()\
        .pushPoints([(-leg_center_x, -leg_center_y),
                     (leg_center_x, -leg_center_y),
                     (leg_center_x, leg_center_y),
                     (-leg_center_x, leg_center_y)]).rect(leg_width, leg_width).extrude(legroom)

big_denis = table(2000, 1070)
cq.exporters.export(big_denis, 'big_denis.step')