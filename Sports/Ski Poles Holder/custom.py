import cadquery as cq
import math


diameter = 16.2
thickness = 3
connector_thickness = 6
intercenter_distance = 38
height = 12

arc_radius = (diameter / 2 + thickness / 2)
angle = math.radians(30)
x = intercenter_distance / 2 + arc_radius * math.cos(angle)
y = arc_radius * math.sin(angle)

half = (cq.Workplane()
     .pushPoints([(x, y)]).threePointArc((intercenter_distance / 2 - arc_radius, 0), (x, -y)).offset2D(thickness / 2, "arc")
     .pushPoints([(0, 0)]).rect(intercenter_distance - diameter, connector_thickness)
     .extrude(height)
     )
full = half.union(half.mirror("YZ"))

cq.exporters.export(full, 'custom_full.stl')