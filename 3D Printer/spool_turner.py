import cadquery as cq

R = 26
r = 6
shaft_r = 5
intercenter_distance = R + r + 12

shaft_length = 50
spool_depth = 40
thickness = 3

test = (cq.Workplane().box(intercenter_distance, 2 * r, thickness, centered=(False, True, True))
        .faces(">Z").workplane().pushPoints([(0, 0)]).circle(shaft_r).extrude(shaft_length)
          .pushPoints([(0, 0)]).circle(R).extrude(-spool_depth)
          .pushPoints([(intercenter_distance, 0)]).circle(r).extrude(-spool_depth))

cq.exporters.export(test, 'spool_turner.stl')
