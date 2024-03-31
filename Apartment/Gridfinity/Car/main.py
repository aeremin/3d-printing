import cadquery as cq

shelve = (cq.Workplane()
 .pushPoints([(700, 300)])
 .lineTo(700, 40).radiusArc((670, 10), 30)
 .lineTo(470, 10).lineTo(372, 76).lineTo(358, 300).close().extrude(4)
)

cq.exporters.export(shelve, 'shelve.stl')
