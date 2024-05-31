import cadquery as cq

wood_thickness = 19
hole_offset = 60
after_hole_distance = 10
jig_thickness = 2
jig_height = 25
hole_tolerance = 0.2

def jig_side():
  hole_radius = 5
  return (cq.Workplane()
   .pushPoints([(-jig_thickness, 0)])
   .box(jig_thickness + hole_offset + after_hole_distance, 2 * jig_thickness + wood_thickness, wood_thickness + jig_height,
        centered=(False, True, False))
   .faces(">Z").workplane(centerOption="ProjectedOrigin").pushPoints([(hole_offset, 0)]).hole(hole_radius + hole_tolerance)
  ).cut(cq.Workplane().box(hole_offset + after_hole_distance, wood_thickness, wood_thickness, centered=(False, True, False)))

cq.exporters.export(jig_side(), 'jig_side.stl')

def jig_floor(hole_radius = 7):
  return (cq.Workplane()
   .pushPoints([(-jig_thickness, 0)])
   .box(jig_thickness + hole_offset + after_hole_distance, 2 * jig_thickness + wood_thickness, wood_thickness + jig_height,
        centered=(False, True, False))
   .faces(">Z").workplane(centerOption="ProjectedOrigin").pushPoints([(hole_offset, 0)]).hole(hole_radius + hole_tolerance)
  ).cut(cq.Workplane().pushPoints([(0, -jig_thickness)]).box(hole_offset + after_hole_distance, wood_thickness + 2 * jig_thickness, wood_thickness, centered=(False, True, False)))

cq.exporters.export(jig_floor(), 'jig_floor.stl')
cq.exporters.export(jig_floor(hole_radius=10), 'jig_floor_screw_head.stl')