import cadquery as cq

eps = 0.001

delta = 0.2

switch_width = 35 + delta
switch_height = 92 + delta
switch_thickness = 11
switch_corner_radius = 3


groove_from = 4.5
groove_to = 8.5
groove_width = 24
groove_height = 1.4

groove = cq.Workplane().box(groove_to - groove_from, groove_width, groove_height, centered=(False, True, False))\
    .translate(cq.Vector(switch_height - groove_to, 0, -groove_height)).faces("<Z").edges().fillet(groove_height-eps)

switch_tool = cq.Workplane()\
    .box(switch_height, switch_width, switch_thickness, centered=(False, True, False)).edges("|Z").fillet(switch_corner_radius)\
    .union(groove)

holder_padding = 4.5

holder = cq.Workplane().box(switch_height + 2 * holder_padding, switch_width + 2 * holder_padding, 6, centered=(False, True, False)).\
    translate(cq.Vector(-holder_padding, 0, -1.6)).cut(switch_tool)

wall_switch_part = cq.Workplane().cylinder(6, 22, centered=(True, True, False))\
    .faces("<Z").workplane(invert=True).box(24, 26, 6, centered=(True, True, False), combine="cut")\
    .faces("<Z").workplane(-0.2).pushPoints([(17, 0), (-17, 0)]).hole(8.3, 2)\
    .translate((66, 0, -6 - 1.6))


combined = holder.union(wall_switch_part).faces("<Z[1]").workplane(-0.4).\
    pushPoints([(49, 5), (49, -5)]).hole(8.3, 2)
    
cq.exporters.export(combined, "combined.stl")    

wall_switch_cover = cq.Workplane().cylinder(7, 22, centered=(True, True, False))\
    .faces("<Z").workplane(invert=True).box(24.6, 26.6, 6, centered=(True, True, False), combine="cut")\
    .faces("<Z").workplane(-0.2).pushPoints([(17, 0), (-17, 0)]).hole(8.3, 2).faces(">Z").fillet(3)
    
cq.exporters.export(wall_switch_cover, "wall_switch_cover.stl")
