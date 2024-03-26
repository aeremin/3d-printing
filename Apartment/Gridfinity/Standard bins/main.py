from cqgridfinity import *

GridfinityBox(1, 3, 4, scoops=False, labels=False, holes=True, unsupported_holes=True).save_stl_file()
GridfinityBox(1, 4, 5, scoops=False, labels=False, holes=True, unsupported_holes=True).save_stl_file()
GridfinityBox(1, 4, 7, scoops=False, labels=False, holes=True, unsupported_holes=True).save_stl_file()
GridfinityBox(1, 1, 2, length_div=1, scoops=True, labels=True, holes=True, unsupported_holes=True).save_stl_file()

sizes = [
    (1, 1, 6),
    (1, 2, 6),
    (2, 1, 6),
    (2, 2, 6),
    (1, 1, 3),
    (1, 1, 2),
    (1, 3, 3),
]

for l, w, h in sizes:
    GridfinityBox(l, w, h, scoops=True, labels=True, holes=True, unsupported_holes=True).save_stl_file()
    GridfinityBox(l, w, h, scoops=True, holes=True, unsupported_holes=True).save_stl_file()

