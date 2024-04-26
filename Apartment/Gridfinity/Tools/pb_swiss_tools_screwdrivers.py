import cadquery as cq

from cqgridfinity import *
from Apartment.Gridfinity.common import GridfinityBoxWithHoles

handle_diameter = 24
handle_radius = handle_diameter / 2

shaft_holding_tower_length = 40
shaft_holding_tower_length_offset = 30
shaft_holding_tower_width_offset = 30

handle_holding_tower_length_offset = 45 + shaft_holding_tower_length + shaft_holding_tower_length_offset

def side_sketch(radius: float, width: float) -> cq.Sketch:
  hw = width / 2
  return (cq.Sketch()
          .segment((-hw, 0), (hw, 0))
          .segment((hw, handle_radius))
          .segment((radius, handle_radius))
          .arc((0, handle_radius), radius, 0, -180)
          .segment((-hw, handle_radius))
          .segment((-hw, 0))
          .assemble()
          )


def handle_holding_tower() -> cq.Workplane:
  tower_width = 20
  handle_groove_diameter_small = 13.4
  handle_groove_diameter_large = 16.3
  handle_groove_length = 14
  return cq.Workplane("XZ").placeSketch(side_sketch(handle_groove_diameter_small / 2,
                                                    tower_width),
                                        side_sketch(handle_groove_diameter_large / 2,
                                                    tower_width).moved(
                                          cq.Location(cq.Vector(0, 0, -handle_groove_length))),
                                        ).loft()


def shaft_holding_tower(radius: float) -> cq.Workplane:
  tower_width = 10
  return cq.Workplane("XZ").placeSketch(side_sketch(radius,
                                                    tower_width),
                                        side_sketch(radius,
                                                    tower_width).moved(
                                          cq.Location(cq.Vector(0, 0, -shaft_holding_tower_length))),
                                        ).loft()


x_offset = constants.GRU - shaft_holding_tower_width_offset
shaft_holding_tower_y_offset = 2.5 * constants.GRU - shaft_holding_tower_length_offset
handle_holding_tower_y_offset = 2.5 * constants.GRU - handle_holding_tower_length_offset

r = (GridfinityBoxWithHoles(2, 5, 5).to_cq()
     .union(shaft_holding_tower(4 / 2).rotate((0, 0, 0), (0, 0, 1), 180).translate(
  (x_offset, shaft_holding_tower_y_offset, constants.GRHU)))
     .union(shaft_holding_tower(5 / 2).translate((-x_offset, -shaft_holding_tower_y_offset, constants.GRHU)))
     .union(handle_holding_tower().rotate((0, 0, 0), (0, 0, 1), 180).translate(
  (x_offset, handle_holding_tower_y_offset, constants.GRHU)))
     .union(handle_holding_tower().translate((-x_offset, -handle_holding_tower_y_offset, constants.GRHU)))
     )

cq.exporters.export(r, "pb_swiss_tools_screwdrivers.stl")
