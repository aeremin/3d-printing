import math

import cadquery as cq
from cqgridfinity import *
from common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

diameter = 20.4
height_u = 8

slot_depth = 8

box = GridfinityBoxWithHoles(1, 1, height_u,
                             solid_thickness=slot_depth).to_cq().workplaneFromTagged(TOP_SURFACE_TAG).polarArray(
  2 / 3 * diameter, 45, 180, 2).hole(diameter, slot_depth)

h = 12
v = h * math.sqrt(3)
nv = math.floor((height_u * constants.GRHU) / v)
nh1 = math.floor((1 * constants.GRU) / h) - 1
nh2 = math.floor((1 * constants.GRU) / h) - 1
box = (box
       .faces("<X")
       .workplane(centerOption="CenterOfMass").transformed(rotate=(0, 0, 90))
       .rarray(v, h, nv, nh1).polygon(6, h - 1).cutThruAll().rarray(v, h, nv - 1, nh1 - 1).polygon(6,
                                                                                                   h - 1).cutThruAll()
       .faces("<Y")
       .workplane(centerOption="CenterOfMass").transformed(rotate=(0, 0, 90))
       .rarray(v, h, nv, nh2).polygon(6, h - 1).cutThruAll().rarray(v, h, nv - 1, nh2 - 1).polygon(6,
                                                                                                   h - 1).cutThruAll()
       )

cq.exporters.export(box, 'pcb_spring_holder.stl')
