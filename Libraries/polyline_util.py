from typing import List, Tuple


class PolylineFromOffsets:
    points: List[Tuple[float, float]]

    def __init__(self, start_point: Tuple[float, float] = (0, 0)):
        self.points = [start_point]

    def add_point(self, x: float, y: float):
        last_x, last_y = self.points[-1]
        self.points.append((last_x + x, last_y + y))
        return self