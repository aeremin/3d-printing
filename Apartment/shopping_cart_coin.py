import cadquery as cq

d = 27.4
thickness = 2

hole_diameter = 3
hole_distance_from_edge = 3

coin = cq.Workplane = (
    cq.Workplane().cylinder(thickness, d / 2).faces(">Z").workplane()
    .pushPoints([(d / 2 -  hole_distance_from_edge - hole_diameter / 2, 0)]).hole(hole_diameter)
)

cq.exporters.export(coin, 'shopping_cart_coin.stl')