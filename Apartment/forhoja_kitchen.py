import cadquery as cq
from typing import Tuple, List

class PolylineFromOffsets:
    points: List[Tuple[float, float]]

    def __init__(self):
        self.points = [(0, 0)]

    def add_point(self, x: float, y: float):
        last_x, last_y = self.points[-1]
        self.points.append((last_x + x, last_y + y))

def stopper():
    plank_w = 15.4
    plank_h = 40.2
    height = 30
    width = 15
    thickness_small = 0.8
    thickness_large = 1.6

    l = PolylineFromOffsets()
    l.add_point(plank_w, 0)
    l.add_point(0, -plank_h)
    l.add_point(-plank_w / 2, 0)
    l.add_point(0, -thickness_small)
    l.add_point(plank_w / 2 + thickness_large, 0)
    l.add_point(0, plank_h + thickness_small + thickness_large)
    l.add_point(-plank_w - 2 * thickness_large , 0)
    l.add_point(0, - thickness_large - plank_h - height)
    l.add_point(thickness_large, 0)
    l.add_point(0, height + plank_h)

    return (
        cq.Workplane().polyline(l.points).close().extrude(width)
    )

r = stopper()
cq.exporters.export(stopper(), 'forhoja_stopper.stl')
