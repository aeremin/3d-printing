import math

from cqgridfinity import *
import cadquery as cq
from Apartment.Gridfinity.common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

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

box = (GridfinityBoxWithHoles(5, 3, height_u, solid_thickness=handle_r).to_cq()
       .workplaneFromTagged(TOP_SURFACE_TAG).pushPoints([((total_l - working_part_l) / 2, 0)])
       .rect(working_part_l, n_files * 2 * handle_r + (n_files - 1) * interval_between).cutBlind(
  - (middle_r - working_part_offset))
       .workplaneFromTagged(TOP_SURFACE_TAG).transformed(offset=(total_l / 2 - working_part_l, 0, 0), rotate=(0, 90, 0))
       .rarray(1, 2 * handle_r + interval_between, 1, n_files).hole(2 * middle_r, middle_l)
       .workplaneFromTagged(TOP_SURFACE_TAG).transformed(offset=(total_l / 2 - working_part_l - middle_l, 0, 0),
                                                         rotate=(0, 90, 0))
       .rarray(1, 2 * handle_r + interval_between, 1, n_files).hole(2 * handle_r, handle_l)
       .workplaneFromTagged(TOP_SURFACE_TAG).pushPoints([(-total_l / 2 + 37, 0)])
       .rect(finger_hole_size, n_files * 2 * handle_r + (n_files + 1) * interval_between).cutBlind(-handle_r)

       )

cq.exporters.export(box, 'key_files.stl')
