import math

import cadquery as cq

BOX_LENGTH = 282
BOX_WIDTH = 241
BOX_HEIGHT = 70

CHAOS_TOKEN_DIAMETER = 25 + 0.4
CHAOS_TOKEN_THICKNESS = 2.1 + 0.3

CHAOS_TOKEN_CAPSULE_DIAMETER = 32.4 + 0.2
CHAOS_TOKEN_CAPSULE_THICKNESS = 6 + 0.1

CHAOS_BAG_HEIGHT = 30

TURN_COUNTER_TOKEN_INNER_DIAMETER = 25 + 0.3
TURN_COUNTER_THICKNESS = 2.1 + 0.2

WALL_THICKNESS = 2
FLOOR_THICKNESS = 2

STANDEES_BOX_OUTER_WIDTH = 85
STANDEES_BOX_OUTER_LENGTH = 47 + 2 * WALL_THICKNESS
STANDEES_BOX_OUTER_HEIGHT = 44 + FLOOR_THICKNESS

TURN_COUNTER_BOX_OUTER_WIDTH = STANDEES_BOX_OUTER_WIDTH
TURN_COUNTER_BOX_OUTER_LENGTH = STANDEES_BOX_OUTER_LENGTH
TURN_COUNTER_BOX_OUTER_HEIGHT = 4 * TURN_COUNTER_THICKNESS + FLOOR_THICKNESS

LINKS_BOX_OUTER_WIDTH = STANDEES_BOX_OUTER_WIDTH
LINKS_BOX_OUTER_LENGTH = STANDEES_BOX_OUTER_LENGTH
LINKS_BOX_OUTER_HEIGHT = BOX_HEIGHT - STANDEES_BOX_OUTER_HEIGHT - TURN_COUNTER_BOX_OUTER_HEIGHT

CARDS_BOX_OUTER_WIDTH = 98
CARDS_BOX_OUTER_LENGTH = 119.5

CAPSULES_BOX_OUTER_WIDTH = STANDEES_BOX_OUTER_WIDTH
CAPSULES_BOX_OUTER_LENGTH = 70.5
CAPSULES_BOX_OUTER_HEIGHT = math.ceil(CHAOS_TOKEN_CAPSULE_DIAMETER) + FLOOR_THICKNESS

DAMAGE_BOX_OUTER_WIDTH = CAPSULES_BOX_OUTER_WIDTH
DAMAGE_BOX_OUTER_LENGTH = CAPSULES_BOX_OUTER_LENGTH
DAMAGE_BOX_OUTER_HEIGHT = (BOX_HEIGHT - CAPSULES_BOX_OUTER_HEIGHT) / 2

CHAOS_TOKEN_BOX_OUTER_WIDTH = STANDEES_BOX_OUTER_WIDTH
CHAOS_TOKEN_BOX_OUTER_LENGTH = 2 * CHAOS_TOKEN_DIAMETER
CHAOS_TOKEN_BOX_OUTER_HEIGHT = 16.9 + FLOOR_THICKNESS

RESOURCES_BOX_OUTER_LENGTH = CAPSULES_BOX_OUTER_WIDTH
RESOURCES_BOX_OUTER_WIDTH = BOX_WIDTH - STANDEES_BOX_OUTER_LENGTH - CAPSULES_BOX_OUTER_LENGTH
RESOURCES_BOX_OUTER_HEIGHT = BOX_HEIGHT - CHAOS_BAG_HEIGHT - DAMAGE_BOX_OUTER_HEIGHT


print("--- Stats ---")
print(f"Box length gap: {BOX_LENGTH - 2 * CARDS_BOX_OUTER_WIDTH - STANDEES_BOX_OUTER_WIDTH}")
print(f"Box width gap: {BOX_WIDTH - STANDEES_BOX_OUTER_LENGTH - CAPSULES_BOX_OUTER_LENGTH - DAMAGE_BOX_OUTER_LENGTH - CHAOS_TOKEN_BOX_OUTER_LENGTH}")
print(f"Capsules box height: {CAPSULES_BOX_OUTER_HEIGHT}, length gap: {CAPSULES_BOX_OUTER_LENGTH - 2 * WALL_THICKNESS - 2 * CHAOS_TOKEN_CAPSULE_DIAMETER}")
print(f"Links box height: {LINKS_BOX_OUTER_HEIGHT}")
print(f"Resources box height: {RESOURCES_BOX_OUTER_HEIGHT}, damage box height: {DAMAGE_BOX_OUTER_HEIGHT}")

print(f"Chaos token box: {CHAOS_TOKEN_BOX_OUTER_WIDTH} x {CHAOS_TOKEN_BOX_OUTER_LENGTH} x {CHAOS_TOKEN_BOX_OUTER_HEIGHT}")

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

def damage_box():
  bbox = cq.Workplane().box(DAMAGE_BOX_OUTER_WIDTH, DAMAGE_BOX_OUTER_LENGTH, DAMAGE_BOX_OUTER_HEIGHT)
  d = (DAMAGE_BOX_OUTER_WIDTH - 3 * WALL_THICKNESS) / 3
  l = DAMAGE_BOX_OUTER_LENGTH - 2 * WALL_THICKNESS
  cutter1 = (cq.Workplane(origin=(-DAMAGE_BOX_OUTER_WIDTH / 2 + WALL_THICKNESS, 0, FLOOR_THICKNESS)).box(d, l, DAMAGE_BOX_OUTER_HEIGHT, centered=(False, True, True))
            .faces("<Z").fillet(10).edges("|Z").fillet(2))
  cutter2 = (cq.Workplane(origin=(- DAMAGE_BOX_OUTER_WIDTH / 2 + d + 2 * WALL_THICKNESS, 0, FLOOR_THICKNESS)).box(2 * d, l, DAMAGE_BOX_OUTER_HEIGHT, centered=(False, True, True))
             .faces("<Z").fillet(10).edges("|Z").fillet(2))
  return bbox.edges("|Z").fillet(4).cut(cutter1).cut(cutter2)

def resources_box():
  bbox = cq.Workplane().box(RESOURCES_BOX_OUTER_WIDTH, RESOURCES_BOX_OUTER_LENGTH, RESOURCES_BOX_OUTER_HEIGHT)
  d = (RESOURCES_BOX_OUTER_WIDTH - 4 * WALL_THICKNESS) / 4
  l = RESOURCES_BOX_OUTER_LENGTH - 2 * WALL_THICKNESS
  cutter1 = (cq.Workplane(origin=(-RESOURCES_BOX_OUTER_WIDTH / 2 + WALL_THICKNESS, 0, FLOOR_THICKNESS)).box(d, l, RESOURCES_BOX_OUTER_HEIGHT, centered=(False, True, True))
            .faces("<Z").fillet(10).edges("|Z").fillet(2))
  cutter2 = (cq.Workplane(origin=(- RESOURCES_BOX_OUTER_WIDTH / 2 + d + 2 * WALL_THICKNESS, 0, FLOOR_THICKNESS)).box(d, l, RESOURCES_BOX_OUTER_HEIGHT, centered=(False, True, True))
             .faces("<Z").fillet(10).edges("|Z").fillet(2))
  cutter3 = (cq.Workplane(origin=(- RESOURCES_BOX_OUTER_WIDTH / 2 + 2 * d + 3 * WALL_THICKNESS, 0, FLOOR_THICKNESS)).box(2 * d, l, RESOURCES_BOX_OUTER_HEIGHT, centered=(False, True, True))
             .faces("<Z").fillet(10).edges("|Z").fillet(2))
  return bbox.edges("|Z").fillet(4).cut(cutter1).cut(cutter2).cut(cutter3)

def turn_counter_box():
  i_prism = 0
  def prism(loc: cq.Location) -> cq.Shape:
    nonlocal i_prism
    tokens = 4 if i_prism == 0 else 3
    i_prism += 1
    return cq.Workplane().polygon(8, TURN_COUNTER_TOKEN_INNER_DIAMETER, circumscribed=True).extrude(
      -tokens * TURN_COUNTER_THICKNESS).val().located(loc)


  bbox = (cq.Workplane().box(TURN_COUNTER_BOX_OUTER_WIDTH, TURN_COUNTER_BOX_OUTER_LENGTH, TURN_COUNTER_BOX_OUTER_HEIGHT)
          .edges("|Z").fillet(4)
          .faces(">Z").workplane()
          .rarray(TURN_COUNTER_TOKEN_INNER_DIAMETER + WALL_THICKNESS, TURN_COUNTER_BOX_OUTER_LENGTH - TURN_COUNTER_TOKEN_INNER_DIAMETER, 3, 2)
          .eachpoint(prism, combine="cut")
          .rarray(TURN_COUNTER_TOKEN_INNER_DIAMETER + WALL_THICKNESS, TURN_COUNTER_BOX_OUTER_LENGTH, 3, 2)
          .slot2D(35, 11, 90).cutThruAll()
          )
  return bbox

def chaos_token_box():
  bbox = (cq.Workplane().box(CHAOS_TOKEN_BOX_OUTER_WIDTH, CHAOS_TOKEN_BOX_OUTER_LENGTH, CHAOS_TOKEN_BOX_OUTER_HEIGHT)
          .edges("|Z").fillet(4)
          .faces(">Z").workplane()
          .rarray(CHAOS_TOKEN_DIAMETER + WALL_THICKNESS, CHAOS_TOKEN_DIAMETER, 3, 2)
          .hole(CHAOS_TOKEN_DIAMETER, CHAOS_TOKEN_BOX_OUTER_HEIGHT - FLOOR_THICKNESS)
          .rarray(CHAOS_TOKEN_DIAMETER + WALL_THICKNESS, CHAOS_TOKEN_BOX_OUTER_LENGTH, 3, 2)
          .slot2D(35, 11, 90).cutThruAll()
          )
  return bbox


def links_box():
  bbox = cq.Workplane().box(LINKS_BOX_OUTER_WIDTH, LINKS_BOX_OUTER_LENGTH, LINKS_BOX_OUTER_HEIGHT)
  cutter = cq.Workplane(origin=(0, 0, FLOOR_THICKNESS)).box(LINKS_BOX_OUTER_WIDTH - 2 * WALL_THICKNESS, LINKS_BOX_OUTER_LENGTH - 2 * WALL_THICKNESS,
                                                            LINKS_BOX_OUTER_HEIGHT).faces("<Z").fillet(8).edges("|Z").fillet(2)
  return bbox.edges("|Z").fillet(4).cut(cutter)

cq.exporters.export(standees_box(), 'standees_box.stl')
cq.exporters.export(chaos_capsules_box(), 'chaos_capsules_box.stl')
cq.exporters.export(damage_box(), 'damage_box.stl')
cq.exporters.export(links_box(), 'links_box.stl')
cq.exporters.export(turn_counter_box(), 'turn_counter_box.stl')
cq.exporters.export(chaos_token_box(), 'chaos_token_box.stl')
cq.exporters.export(resources_box(), 'resources_box.stl')
