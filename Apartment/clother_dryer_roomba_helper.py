import cadquery as cq

profile = cq.Sketch().trapezoid(20, 23, 155)

r = cq.Workplane("YZ").placeSketch(profile).extrude(290).faces(">X").workplane().pushPoints([(0, 1)]).slot2D(23, 19.4, 90).cutThruAll()


cq.exporters.export(r, 'clothes_dryer_roomba_helper.stl')