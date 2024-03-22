import cadquery as cq

drill_hole_tolerance_horizontal_side = 0.3
drill_hole_tolerance_vertical_side = 0.2

def hettich_cam_fitting_jig(wood_thickness = 40, bolt_length = 24):
  jig_thickness = 10
  recommended_wood_half_thickness = 9
  forstner_hole_d = 15 + drill_hole_tolerance_horizontal_side
  bolt_shaft_d = 8 + drill_hole_tolerance_vertical_side
  bolt_hole_d = 5 + drill_hole_tolerance_vertical_side
  jig_width = 25
  r1 = (cq.Workplane("XZ")
        .pushPoints([(0, -jig_thickness)]).rect(jig_width, wood_thickness + jig_thickness, centered=(True, False))
        .extrude(jig_thickness)
        .faces("<Y").workplane(centerOption="ProjectedOrigin")
        .pushPoints([(0, recommended_wood_half_thickness)]).hole(bolt_shaft_d, jig_thickness)
        .pushPoints([(0, wood_thickness - recommended_wood_half_thickness)]).hole(bolt_hole_d, jig_thickness)
        )

  r2 = (cq.Workplane("XY")
        .pushPoints([(0, -jig_thickness)]).rect(jig_width, wood_thickness + jig_thickness, centered=(True, False))
        .extrude(-jig_thickness)
        .faces(">Z").workplane(centerOption="ProjectedOrigin")
        .pushPoints([(0, bolt_length)]).hole(forstner_hole_d, jig_thickness)
        .faces("<Z").workplane(centerOption="ProjectedOrigin")
        .rect(8.1, -15, centered=(True, False)).cutBlind(-2 * jig_thickness, taper=21)
        )
  return r1.union(r2)

def hettich_cam_fitting_jig(wood_thickness = 40, bolt_length = 24):
  jig_thickness = 10
  recommended_wood_half_thickness = 9
  forstner_hole_d = 15 + drill_hole_tolerance_horizontal_side
  bolt_shaft_d = 8 + drill_hole_tolerance_vertical_side
  bolt_hole_d = 5 + drill_hole_tolerance_vertical_side
  jig_width = 25
  r1 = (cq.Workplane("XZ")
        .pushPoints([(0, -jig_thickness)]).rect(jig_width, wood_thickness + jig_thickness, centered=(True, False))
        .extrude(jig_thickness)
        .faces("<Y").workplane(centerOption="ProjectedOrigin")
        .pushPoints([(0, recommended_wood_half_thickness)]).hole(bolt_shaft_d, jig_thickness)
        .pushPoints([(0, wood_thickness - recommended_wood_half_thickness)]).hole(bolt_hole_d, jig_thickness)
        )

  r2 = (cq.Workplane("XY")
        .pushPoints([(0, -jig_thickness)]).rect(jig_width, wood_thickness + jig_thickness, centered=(True, False))
        .extrude(-jig_thickness)
        .faces(">Z").workplane(centerOption="ProjectedOrigin")
        .pushPoints([(0, bolt_length)]).hole(forstner_hole_d, jig_thickness)
        .faces("<Z").workplane(centerOption="ProjectedOrigin")
        .rect(8.1, -15, centered=(True, False)).cutBlind(-2 * jig_thickness, taper=21)
        )
  return r1.union(r2)

def hettich_hinge_jig():
  jig_thickness = 3
  half = (
    cq.Workplane()
      .line(0, 25).line(45, 0).line(0, 15).line(3 + 30, 0).line(20, -40).close()
      .extrude(jig_thickness)
    .faces("<Z").workplane()
    .pushPoints([(45 - 37, -16)]).hole(5 + drill_hole_tolerance_horizontal_side)
    .pushPoints([(45 + 3 + 21.5, 0)]).hole(35 + drill_hole_tolerance_horizontal_side, jig_thickness)
    .pushPoints([(45 - 2, 0), (45 + 3 + 2, 0), (45 + 3 + 27.5, -26)]).cskHole(2, 4, 45)
    .faces(">Z").workplane()
    .pushPoints([(45, 0)]).rect(3, 25 + 15, centered=False).extrude(2 * jig_thickness)
  )
  return half.union(half.mirror("XZ"))

cq.exporters.export(hettich_cam_fitting_jig(), 'hettich_cam_fitting_jig.stl')
cq.exporters.export(hettich_hinge_jig(), 'hettich_hinge_jig.stl')

