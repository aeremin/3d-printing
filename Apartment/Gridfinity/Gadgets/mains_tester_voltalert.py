import cadquery as cq
from Libraries import polyline_util
from Apartment.Gridfinity.common import GridfinityBoxWithHoles, TOP_SURFACE_TAG

voltalert_thickness = 20
slot_depth = 8

l = polyline_util.PolylineFromOffsets((-155 / 2, -27 / 2))
l.add_point(60, 0).add_point(0, 3).add_point(50, 0).add_point(45, 4).add_point(0, 10)
l.add_point(-35, 10).add_point(-120, 0)

box = (GridfinityBoxWithHoles(4, 1, 4,
                              solid_thickness=slot_depth).to_cq().workplaneFromTagged(TOP_SURFACE_TAG).polyline(
  l.points).close().cutBlind(-slot_depth))

cq.exporters.export(box, 'voltalert.stl')
