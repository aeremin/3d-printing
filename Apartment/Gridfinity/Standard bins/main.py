from cqgridfinity import *
import cadquery as cq

def save_deterministic(b: GridfinityBox):
    cq.exporters.export(b.cq_obj, f'{b.filename()}.stl')

save_deterministic(GridfinityBox(1, 3, 4, scoops=False, labels=False, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(1, 4, 5, scoops=False, labels=False, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(1, 4, 7, scoops=False, labels=False, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(1, 1, 2, length_div=1, scoops=True, labels=True, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(2, 6, 7, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(2, 2, 8, holes=True, unsupported_holes=True))
save_deterministic(GridfinityBox(1, 4, 9, holes=True, unsupported_holes=True))

sizes = [
    (1, 1, 6),
    (1, 2, 6),
    (2, 1, 2),
    (2, 1, 3),
    (2, 1, 4),
    (2, 1, 5),
    (2, 1, 6),
    (2, 2, 6),
    (1, 1, 3),
    (1, 1, 4),
    (1, 1, 5),
    (1, 1, 2),
    (3, 1, 3),
]

for l, w, h in sizes:
    save_deterministic(GridfinityBox(l, w, h, scoops=True, labels=True, holes=True, unsupported_holes=True))
    save_deterministic(GridfinityBox(l, w, h, scoops=True, holes=True, unsupported_holes=True))


