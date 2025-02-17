import cadquery as cq

from Apartment.Ivar import consts

THICKNESS = 5
HEIGHT = 42
MOUNTING_HOLE_SPACING = 61.5
MOUNTING_PLATE_OFFSET = 90
MOUNTING_HOLE_DIAMETER = 4
PIN_LENGTH = 20

MOUNTING_PLATE_RADIUS = 68
MOUNTING_PLATE_CENTER_X = consts.POLE_WIDTH / 2 + THICKNESS + MOUNTING_PLATE_OFFSET

base = (
    cq.Sketch()
    .segment((-(consts.POLE_WIDTH / 2 + THICKNESS),  HEIGHT / 2),
             (-(consts.POLE_WIDTH / 2 + THICKNESS), -HEIGHT / 2))
    .segment((MOUNTING_PLATE_CENTER_X, -MOUNTING_PLATE_RADIUS))
    .arc((MOUNTING_PLATE_CENTER_X + MOUNTING_PLATE_RADIUS, 0), (MOUNTING_PLATE_CENTER_X,  MOUNTING_PLATE_RADIUS))
    .close().assemble()
    .push([(consts.POLE_WIDTH / 2 + THICKNESS + 20, 0)])
    .rarray(0, 20, 1, 2)
    .circle(MOUNTING_HOLE_DIAMETER / 2, mode="s")
    .push([(MOUNTING_PLATE_CENTER_X, 0)])
    .circle(MOUNTING_HOLE_SPACING / 2, mode="c", tag="mounting_holes_positions").wires(tag="mounting_holes_positions")
    .distribute(4)
    .circle(MOUNTING_HOLE_DIAMETER / 2, mode="s")
    .push([(MOUNTING_PLATE_CENTER_X, 50)])
    .circle(9, mode="s")
)

result = (cq.Workplane().placeSketch(base).extrude(THICKNESS)
          .faces(">Z").workplane()
          .rarray(consts.HORIZONTAL_HOLE_SPACING, consts.VERTICAL_HOLE_SPACING, 2, 2)
          .cylinder(PIN_LENGTH, consts.HOLE_DIAMETER / 2, centered = (True, True, False))
          .rarray(consts.POLE_WIDTH + THICKNESS, 0, 2, 1)
          .rect(THICKNESS, HEIGHT).extrude(consts.POLE_DEPTH)
)
cq.exporters.export(result, 'ubiquiti_mount.stl')
