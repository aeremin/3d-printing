import cadquery as cq
import math


def rotation_matrix(degrees):
    r = cq.Matrix()
    r.rotateZ(math.pi * degrees / 180)
    return r


def simple_box(width, length, height, wall_thickness=2, floor_thickness=2, fillet=0):
    bbox = cq.Workplane().box(width, length, height)
    cutter = cq.Workplane(origin=(0, 0, floor_thickness)).box(width - 2 * wall_thickness, length - 2 * wall_thickness,
                                                              height)
    if fillet:
        cutter = cutter.faces("<Z").fillet(fillet)
    return bbox.cut(cutter)


def hexagonal_floor_holes_box(width, length, height, wall_thickness=2, floor_thickness=2, fillet=0):
    box = simple_box(width, length, height, wall_thickness, floor_thickness, fillet)

    hole_diameter = 12
    holes_padding = math.cos(math.pi / 6)

    w1 = cq.Vector(0, hole_diameter / 2 + holes_padding).transform(rotation_matrix(30))
    w2 = w1.transform(rotation_matrix(60))

    v1 = w1 + w2
    v2 = 2 * w1 - w2

    max_iterations = int(cq.Vector(width / 2, length / 2).Length / v1.Length)
    centers = []
    for x in range(-max_iterations, max_iterations + 1):
        for y in range(-max_iterations, max_iterations + 1):
            v = x * v1 + y * v2
            if abs(v.x) <= width / 2 - wall_thickness - fillet - hole_diameter / 2 and abs(
                    v.y) <= length / 2 - wall_thickness - fillet - hole_diameter / 2:
                centers.append(v)

    return box.faces("<Y").workplane(centerOption="CenterOfMass").pushPoints([(0, 3)]).hole(10).faces("<Z").workplane(
        centerOption="CenterOfMass").pushPoints(centers).polygon(6, hole_diameter).cutThruAll()
