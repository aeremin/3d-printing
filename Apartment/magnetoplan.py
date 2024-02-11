import cadquery as cq

def holding_stick():
    width = 12
    groove_width = 7
    thickness = 3
    groove_thickness = 2
    length = 60
    bolt_hole_diameter = 6
    bolt_hole_distance = 32
    return cq.Workplane().rect(length, width, centered=False).extrude(thickness)\
        .faces(">Z").workplane(centerOption="CenterOfMass").rect(length, groove_width).extrude(groove_thickness)\
        .faces(">Z").workplane(origin=(bolt_hole_distance, width / 2)).hole(bolt_hole_diameter).translate((0, 0, -thickness - groove_thickness))

def bottle_holder():
    bottle_diameter = 51
    floor_thickness = 2.4
    walls_thickness = 2
    height = 25
    r = bottle_diameter / 2 + walls_thickness
    return holding_stick().translate((0, 4, 0)).mirror("XY").rotate((0, 0, 0), (0, 1, 0), -90) .union(
        cq.Workplane().pushPoints([(r, r)]).circle(r).extrude(floor_thickness + height).pushPoints([(0, 0)]).rect(r, r, centered=False).extrude(floor_thickness + height)\
        .faces(">Z").workplane(origin=(r, r)).hole(bottle_diameter, height)
    ).mirror("YZ")

cq.exporters.export(holding_stick(), 'magnetoplan_holding_stick.stl')

cq.exporters.export(bottle_holder(), 'magnetoplan_bottle_holder.stl')

