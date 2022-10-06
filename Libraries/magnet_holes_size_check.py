import cadquery as cq

# Results:
# - it seems to be fine to use depth as is (at least when it's multiple of 0.2)
# - using diameter = diameter of magnet + 0.3 gives good results

def plank_with_holes(sizes):
    padding = 2
    max_diameter = max([diameter for diameter, depth in sizes])
    max_depth = max([depth for diameter, depth in sizes])
    total_diameters = sum([diameter for diameter, depth in sizes])
    r = cq.Workplane("XY").box(max_diameter + 2 * padding,
                               total_diameters + (len(sizes) + 1) * padding,
                               max_depth + padding,
                               centered=(True, False, False))
    f = r.faces(">Z").workplane().center(0, padding / 2)
    for i, (diameter, depth) in enumerate(sizes):
        f = f.center(0, (diameter + padding) / 2)
        r = f.hole(diameter, depth)
        f = r.faces(">Z").workplane().center(0, (diameter + padding) / 2)
    return r

hole_size_check = plank_with_holes([(8, 2), (4, 3), (7, 5)])
embedding_magnet_check = cq.Workplane("XY").box(12, 12, 4).faces(">Z").workplane(offset=-0.2).hole(diameter=8.3, depth=2.0)
