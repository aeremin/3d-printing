import math

from cqgridfinity import *
import cadquery as cq

handle_r = 9
handle_l = 55

middle_r = 6
middle_l = 9

working_part_offset = 4
working_part_l = 113

n_files = 6
interval_between = 2

finger_hole_size = 20

total_l = handle_l + middle_l + working_part_l

height_u = 1 + math.ceil(2 * handle_r / constants.GRHU)

box: cq.Workplane = GridfinityBox(5, 3, height_u, holes=True, unsupported_holes=True, solid=True,
                solid_ratio=(handle_r / ((height_u - 1) * constants.GRHU))).cq_obj

top_layer_tag = "top_layer"
box = (box.faces("<Z[1]").workplane(centerOption="CenterOfMass").tag(top_layer_tag)
       .pushPoints([((total_l - working_part_l) / 2, 0)])
       .rect(working_part_l, n_files * 2 * handle_r + (n_files - 1) * interval_between).cutBlind(- (middle_r - working_part_offset))
       .workplaneFromTagged(top_layer_tag).transformed(offset=(total_l / 2 - working_part_l, 0, 0), rotate=(0, 90, 0))
       .rarray(1, 2 * handle_r + interval_between, 1, n_files).hole(2 * middle_r, middle_l)
       .workplaneFromTagged(top_layer_tag).transformed(offset=(total_l / 2 - working_part_l - middle_l, 0, 0), rotate=(0, 90, 0))
       .rarray(1, 2 * handle_r + interval_between, 1, n_files).hole(2 * handle_r, handle_l)
       .workplaneFromTagged(top_layer_tag).pushPoints([(-total_l / 2 + 37, 0)])
       .rect(finger_hole_size, n_files * 2 * handle_r + (n_files + 1) * interval_between).cutBlind(-handle_r)
       )

cq.exporters.export(box, 'key_files.stl')
