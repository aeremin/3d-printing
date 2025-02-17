import cadquery as cq

from Libraries.polyline_util import PolylineFromOffsets

HEIGHT = 35

# (0,0,0) point is positioned in the middle of the upper attachment line
def skadis_hook():
  thickness = 4.5
  rear_lower_peg_length = 6
  rear_upper_hook_depth = 5.2
  rear_downtick_length = 12

  l = PolylineFromOffsets()
  l.add_point(0, -HEIGHT)
  l.add_point(-thickness - rear_lower_peg_length, 0)
  l.add_point(0, thickness)
  l.add_point(rear_lower_peg_length, 0)
  l.add_point(0, HEIGHT - 2 * thickness)
  l.add_point(-rear_upper_hook_depth, 0)
  l.add_point(0, -rear_downtick_length + thickness)
  l.add_point(-thickness, 0)
  l.add_point(0, rear_downtick_length)

  return cq.Workplane("XZ").polyline(l.points).close().extrude(thickness).edges().fillet(0.5).translate((0, thickness / 2, 0))