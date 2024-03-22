import math

from cqgridfinity import *
import cadquery as cq

total_height = 70

first_layer_height = 7
first_layer_radius = 90 / 2

second_layer_height = 4
second_layer_radius = 116 / 2

third_layer_height = 16
third_layer_side_radius = 31.5
third_layer_side_angle_offset = 20
third_layer_angle_between_side_holes = 66 + 127

box: cq.Workplane = GridfinityBox(4, 3, 1 + math.ceil(total_height / constants.GRHU), holes=True, unsupported_holes=True, solid=True,
                solid_ratio=(first_layer_height + second_layer_height + third_layer_height - 1) / total_height).cq_obj
top_layer_tag = "top_layer"

box = (box.faces("<Z[1]").workplane().tag(top_layer_tag)
     .hole(2 * first_layer_radius, first_layer_height + second_layer_height + third_layer_height)
     .workplaneFromTagged(top_layer_tag).hole(2 * second_layer_radius, second_layer_height + third_layer_height)
     .workplaneFromTagged(top_layer_tag).polarArray(54.3, third_layer_side_angle_offset, third_layer_angle_between_side_holes, 2)
     .hole(2 * third_layer_side_radius, third_layer_height)
     )
cq.exporters.export(box, 'aito.stl')
