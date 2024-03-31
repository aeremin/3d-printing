import math

import cadquery as cq
from cqgridfinity import *

def leg_holder(holes: list[bool]) -> cq.Workplane:
  p1: cq.Workplane = (
    cq.Workplane("XZ").sketch().rect(10, 32).push([(0, 11)]).rect(6, 10, mode="s")
    .reset().vertices(">Y and (not >X or <X)").fillet(2)
    .finalize()
    .extrude(8))

  p2 = cq.Workplane("XY").pushPoints([(-15, 0, -16)]).box(25, 20,2, centered=False)

  hole_distance = 5
  hole_diameter = 2.7
  first_row_offset = 7.5
  second_row_offset = first_row_offset + 4

  all_hole_centers = [(10 - 2.5, second_row_offset)] + [(10 - 2.5 - i * hole_distance, first_row_offset) for i in range(5)]
  hole_centers = [center for en, center in zip(holes, all_hole_centers) if en]

  p2 = p2.faces(">Z").workplane().pushPoints(hole_centers).circle(hole_diameter / 2).extrude(5)

  return p1.union(p2)

def roll_holder(diameter: float, nominal_width: float, holes: list[bool]) -> cq.Workplane:
  distance_forward = 61
  distance_backward = diameter / 2
  between_legs = nominal_width + 4
  overhang_left = 6
  overhang_right = 12.5

  total_length = distance_forward + distance_backward
  total_width = overhang_left + between_legs + overhang_right

  length_units = math.ceil(total_length / constants.GRU)
  width_units = math.ceil(total_width / constants.GRU)


  offset_x = (distance_forward - distance_backward) / 2
  offset_y = (overhang_right - between_legs - overhang_left) / 2

  r : cq.Workplane = GridfinityBox(length_units, width_units , 6, holes=True, unsupported_holes=True).cq_obj
  r = (r.faces("<Z[1]").workplane().tag("floor").pushPoints([(offset_x - (diameter / 2 + distance_forward) / 2,
                                                 offset_y + between_legs / 2 + 2)]).rect(1.2, nominal_width + 6).extrude(10)
       .faces("<Z[1]").workplane(centerOption="CenterOfMass").rect(0.4, nominal_width + 5).cutBlind(-15)
       .workplaneFromTagged("floor").pushPoints([(offset_x, offset_y + between_legs)]).rect(40, 10).extrude(2)
      )
  r = r.union(leg_holder(holes).translate((offset_x, offset_y, 21)))

  return r

cq.exporters.export(roll_holder(46, 29, [True, True, True, True, False, False]), 'small_labels_sample.stl')
cq.exporters.export(roll_holder(81, 50, [False, False, True, False, False, False]), 'dk_22223.stl')
cq.exporters.export(roll_holder(61, 62, [False, True, False, True, False, False]), 'dk_22205.stl')
cq.exporters.export(roll_holder(48, 62, [True, True, True, False, False, False]), 'black_red_sample.stl')
