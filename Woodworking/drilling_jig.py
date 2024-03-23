import cadquery as cq

drill_hole_tolerance_horizontal_side = 0.3
drill_hole_tolerance_vertical_side = 0.2

scratch_awl_hole_diameter = 2
scratch_awl_hole_csk_diameter = 4
scratch_awl_hole_csk_angle = 45

# wood_thickness is a thickness of the piece which will only have screw in it (not the fitting itself), i.e.
# the piece which is not "in the corner" of the final furniture.
#
# bolt_length is either 24 (green bolts) or 34 (blue ones)
def hettich_cam_fitting_jig(wood_thickness = 40, bolt_length = 24):
  jig_thickness = 3
  recommended_wood_half_thickness = 7.5
  forstner_hole_d = 15 + drill_hole_tolerance_horizontal_side
  bolt_shaft_d = 8 + drill_hole_tolerance_vertical_side
  bolt_hole_d = 5 + drill_hole_tolerance_vertical_side
  jig_width = 25

  bolt_hole_part_l = wood_thickness - recommended_wood_half_thickness + bolt_hole_d / 2 + 7

  horizontal = (cq.Workplane("XY")
        .pushPoints([(0, -jig_thickness - bolt_hole_part_l)]).rect(jig_width,
                                                bolt_hole_part_l +
                                                jig_thickness + bolt_length + forstner_hole_d / 2 + 7,
                                                centered=(True, False))
        .extrude(-jig_thickness)
        .faces(">Z").workplane()
        .pushPoints([(0, bolt_length)]).hole(forstner_hole_d, jig_thickness)
        .pushPoints([(0, - wood_thickness + recommended_wood_half_thickness - jig_thickness)]).hole(bolt_hole_d, jig_thickness)
        .faces("<Z").workplane()
        .pushPoints([(0, -2), (0, jig_thickness + 2)]).cskHole(scratch_awl_hole_diameter, scratch_awl_hole_csk_diameter, scratch_awl_hole_csk_angle)
        )

  vertical = (cq.Workplane("XZ")
        .pushPoints([(0, -jig_thickness)]).rect(jig_width, jig_thickness + recommended_wood_half_thickness + bolt_shaft_d / 2 + 7, centered=(True, False))
        .extrude(jig_thickness)
        .faces("<Y").workplane()
        .pushPoints([(0, recommended_wood_half_thickness)]).hole(bolt_shaft_d, jig_thickness)
        )

  return vertical.union(horizontal)

def hettich_hinge_jig():
  jig_thickness = 3
  half = (
    cq.Workplane()
      .line(0, 25).line(45, 0).line(0, 15).line(3 + 30, 0).line(20, -40).close()
      .extrude(jig_thickness)
    .faces("<Z").workplane()
    .pushPoints([(45 - 37, -16)]).hole(5 + drill_hole_tolerance_horizontal_side)
    .pushPoints([(45 + 3 + 21.5, 0)]).hole(35 + drill_hole_tolerance_horizontal_side, jig_thickness)
    .pushPoints([(45 - 2, 0), (45 + 3 + 2, 0), (45 + 3 + 27.5, -26)]).cskHole(scratch_awl_hole_diameter, scratch_awl_hole_csk_diameter, scratch_awl_hole_csk_angle)
    .faces(">Z").workplane()
    .pushPoints([(45, 0)]).rect(3, 25 + 15, centered=False).extrude(2 * jig_thickness)
  )
  return half.union(half.mirror("XZ"))

# https://www.jumbo.ch/de/bauen-renovieren/holz/holzplatten--holzzuschnitt/holzspanplatten/spanplatten/oecoplan-span-eiche-19-mm/p/3463392
# or
# https://www.jumbo.ch/de/bauen-renovieren/holz/holzplatten--holzzuschnitt/holzspanplatten/spanplatten/oecoplan-span-buche-19-mm/p/3463393
cq.exporters.export(hettich_cam_fitting_jig(wood_thickness = 19), 'hettich_cam_fitting_jig_19.stl')


cq.exporters.export(hettich_cam_fitting_jig(wood_thickness = 40), 'hettich_cam_fitting_jig_40.stl')
cq.exporters.export(hettich_hinge_jig(), 'hettich_hinge_jig.stl')
