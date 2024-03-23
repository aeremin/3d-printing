from cqgridfinity import *

sizes = [
    (1, 1, 6),
    (1, 2, 6),
    (2, 1, 6),
    (2, 2, 6),
    (1, 1, 3),
]

for l, w, h in sizes:
    GridfinityBox(l, w, h, scoops=True, labels=True, holes=True, unsupported_holes=True).save_stl_file()
    GridfinityBox(l, w, h, scoops=True, holes=True, unsupported_holes=True).save_stl_file()

