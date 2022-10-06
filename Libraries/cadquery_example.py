import cadquery as cq

SEPARATOR_THICKNESS = 1.6
TOKEN_WIDTH = 35.5
BOX_WIDTH = 59
BOX_DEPTH = 166
NUM_TOKENS = [1, 1, 6, 4, 4, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 3, 2, 2, 2, 2, 4, 2, 2]
CUT_OFF_WIDTH = 2

def hole_size(n: int) -> int:
  return n * 2.3 + (0.2 if n <= 2 else 0)

def base_box(eps = 0):
  f = cq.Workplane("XY").box(BOX_DEPTH, BOX_WIDTH - 2 * CUT_OFF_WIDTH + 2 * eps, 10, centered=[False, True, False])

  l = f.faces(">Y").workplane(centerOption="CenterOfMass")
  f = l.center(0, -5).rect(BOX_DEPTH, 6, centered=[True, False]).extrude(2)
  f = f.union(l.center(0, 3).rect(40 + 2 * eps, 2).extrude(0.8, taper=45, combine=False))

  r = f.faces("<Y").workplane(centerOption="CenterOfMass")
  f = r.center(0, -5).rect(BOX_DEPTH, 6, centered=[True, False]).extrude(2)
  f = f.union(r.center(0, 3).rect(40 + 2 * eps, 2).extrude(0.8, taper=45, combine=False))

  f = f.faces(">Z").workplane(centerOption="CenterOfMass").center(3.25 - BOX_DEPTH / 2, 0)

  for i, n in enumerate(NUM_TOKENS):
    hole_depth = hole_size(n)

    t = f.center(0, 14 * (i % 2 - 0.5))
    t.rect(hole_depth, TOKEN_WIDTH, centered=[False, True])
    f = f.center(hole_depth + SEPARATOR_THICKNESS, 0)

  f = f.cutBlind(-8)
  return f


def lid():
  f = cq.Workplane("XY").box(BOX_DEPTH, BOX_WIDTH, 34, centered=[False, True, False]).translate([0, 0, 6])
  f = f.faces("<Z").rect(BOX_DEPTH - 2, BOX_WIDTH - 3.6).cutBlind(32)
  f = f.faces(">Z").workplane().center(BOX_DEPTH / 2, 0).text("MONSTER TOKENS", 12, -0.4)
  return f - base_box(0.2)

box = base_box()
lid = lid()
