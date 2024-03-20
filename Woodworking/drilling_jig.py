import cadquery as cq

drill_hole_tolerance_horizontal_side = 0.3
drill_hole_tolerance_vertical_side = 0.2

forstner_hole_d = 15 + drill_hole_tolerance_horizontal_side
bolt_shaft_d = 8 + drill_hole_tolerance_vertical_side
bolt_hole_d = 5 + drill_hole_tolerance_vertical_side

bolt_length = 24 # 34 is another option

jig_thickness = 10
jig_width = 25

wood_thickness = 40

recommended_wood_half_thickness = 9

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

jig = r1.union(r2)

cq.exporters.export(jig, 'drilling_jig.stl')