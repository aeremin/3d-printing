import cadquery as cq
from Apartment.Gridfinity.common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

w = 19.5
l = 164

depth = 13

box = GridfinityBoxWithHoles(4, 1, 8, solid_thickness=depth).to_cq().workplaneFromTagged(TOP_SURFACE_TAG).rect(l,
                                                                                                               w).cutBlind(
  -depth)

cq.exporters.export(box, 'obi_knife.stl')
