import math

import cadquery as cq

BOX_LENGTH = 282
BOX_WIDTH = 242
BOX_HEIGHT = 75

CHAOS_TOKEN_DIAMETER = 25 + 0.2
CHAOS_TOKEN_THICKNESS = 2.1 + 0.3

CHAOS_TOKEN_CAPSULE_DIAMETER = 32.4 + 0.2
CHAOS_TOKEN_CAPSULE_THICKNESS = 6 + 0.1

TURN_COUNTER_TOKEN_INNER_DIAMETER = 25 + 0.3
TURN_COUNTER_THICKNESS = 2.1 + 0.2

WALL_THICKNESS = 2
FLOOR_THICKNESS = 2

STANDEES_BOX_OUTER_WIDTH = 85
STANDEES_BOX_OUTER_LENGTH = 45 + 2 * WALL_THICKNESS
STANDEES_BOX_OUTER_HEIGHT = 44 + FLOOR_THICKNESS

CARDS_BOX_OUTER_WIDTH = 98
CARDS_BOX_OUTER_LENGTH = 119.5

CAPSULES_BOX_OUTER_WIDTH = STANDEES_BOX_OUTER_WIDTH
CAPSULES_BOX_OUTER_LENGTH = CARDS_BOX_OUTER_LENGTH - STANDEES_BOX_OUTER_LENGTH
CAPSULES_BOX_OUTER_HEIGHT = math.ceil(CHAOS_TOKEN_CAPSULE_DIAMETER) + FLOOR_THICKNESS

print("--- Stats ---")
print(f"Box length gap: {BOX_LENGTH - 2 * CARDS_BOX_OUTER_WIDTH - STANDEES_BOX_OUTER_WIDTH}")
print(f"Box width gap: {BOX_WIDTH - 2 * CARDS_BOX_OUTER_LENGTH}")
print(f"Capsules box height: {CAPSULES_BOX_OUTER_HEIGHT}, length gap: {CAPSULES_BOX_OUTER_LENGTH - 2 * WALL_THICKNESS - 2 * CHAOS_TOKEN_CAPSULE_DIAMETER}")

def base_box(outer_width, outer_length, outer_height):
  bbox = cq.Workplane().box(outer_width, outer_length, outer_height)
  cutter = cq.Workplane(origin=(0, 0, FLOOR_THICKNESS)).box(outer_width - 2 * WALL_THICKNESS, outer_length - 2 * WALL_THICKNESS,
                                                            outer_height).edges("|Z").fillet(2)
  return bbox.edges("|Z").fillet(4).cut(cutter)

def standees_box():
  return (base_box(STANDEES_BOX_OUTER_WIDTH, STANDEES_BOX_OUTER_LENGTH, STANDEES_BOX_OUTER_HEIGHT)
          .faces(">X").workplane().pushPoints([(0, 15)]).slot2D(60, 20, 90).cutThruAll().edges("|X and >Z and (>>Y[6] or >>Y[-7])").fillet(4)
          )

def chaos_capsules_box():
  return (base_box(CAPSULES_BOX_OUTER_WIDTH, CAPSULES_BOX_OUTER_LENGTH, CAPSULES_BOX_OUTER_HEIGHT)
          .faces(">X").workplane().pushPoints([(0, 20)]).slot2D(60, 30, 90).cutThruAll().edges("|X and >Z and (>>Y[6] or >>Y[-7])").fillet(4)
          )


cq.exporters.export(standees_box(), 'standees_box.stl')
cq.exporters.export(chaos_capsules_box(), 'chaos_capsules_box.stl')
