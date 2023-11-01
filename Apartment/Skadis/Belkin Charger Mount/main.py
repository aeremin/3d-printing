from typing import Tuple, List

import cadquery as cq

charger_height = 80.4
charger_thickness = 30.6
charger_peg_length = 30

overall_thickness = 4.5
hook_height = 35
rear_lower_peg_length = 6
rear_upper_hook_depth = 5.2
rear_downtick_length = 12

distance_to_leg = 6.5
leg_diameter = 8
leg_thickness = 1.5

class PolylineFromOffsets:
    points: List[Tuple[float, float]]

    def __init__(self):
        self.points = [(0, 0)]
    def add_point(self, x: float, y: float):
        last_x, last_y = self.points[-1]
        self.points.append((last_x + x, last_y + y))

l = PolylineFromOffsets()
l.add_point(charger_thickness + 1.5 * overall_thickness, 0)
l.add_point(0, charger_peg_length)
l.add_point(-1.5 *overall_thickness, 0)

l.add_point(0, -(-overall_thickness + charger_peg_length - leg_diameter - distance_to_leg))
l.add_point(leg_thickness, 0)
l.add_point(0, -leg_diameter)
l.add_point(-leg_thickness, 0)
l.add_point(0, -distance_to_leg)

l.add_point(-charger_thickness, 0)
l.add_point(0, charger_height)
l.add_point(charger_thickness, 0)

l.add_point(0, -distance_to_leg)
l.add_point(leg_thickness, 0)
l.add_point(0, -leg_diameter)
l.add_point(-leg_thickness, 0)
l.add_point(0, -(-overall_thickness + charger_peg_length - leg_diameter - distance_to_leg))

l.add_point(1.5 * overall_thickness, 0)
l.add_point(0, charger_peg_length)
l.add_point(-2.5 * overall_thickness - charger_thickness, 0)
l.add_point(0, -(charger_height + 2 * overall_thickness - hook_height))
l.add_point(-rear_lower_peg_length, 0)
l.add_point(0, -overall_thickness)
l.add_point(rear_lower_peg_length, 0)
l.add_point(0, - hook_height + 2 * overall_thickness)
l.add_point(-rear_upper_hook_depth, 0)
l.add_point(0, rear_downtick_length - overall_thickness)
l.add_point(-overall_thickness, 0)
l.add_point(0, -rear_downtick_length)

hook = cq.Workplane().polyline(l.points).close().extrude(overall_thickness).edges().fillet(0.5)

cq.exporters.export(hook, "hook.stl")