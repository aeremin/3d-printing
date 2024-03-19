from cqgridfinity import *
import cadquery as cq
def blades_holder_9mm():
    solid_thickness = 5
    height_u = 3
    box = GridfinityBox(3, 1, 3, holes=True, unsupported_holes=True, solid=True,
                        solid_ratio=solid_thickness / (height_u * constants.GRHU)).cq_obj
    l = 90
    h = 16
    bump_l = 3
    bump_h = 3
    box = (box.faces("<Z[1]").workplane(invert=True)
           .rect(l, h).cutBlind(solid_thickness)
           .pushPoints([((l + bump_l) / 2, 0), (-(l + bump_l) / 2, 0)]).rect(bump_l, h + 2 * bump_h).cutBlind(solid_thickness)
           )
    return box

def blades_holder_18mm():
    solid_thickness = 5
    height_u = 3
    box = GridfinityBox(3, 1, 3, holes=True, unsupported_holes=True, solid=True,
                        solid_ratio=solid_thickness / (height_u * constants.GRHU)).cq_obj
    l = 121
    h = 25
    box = (box.faces("<Z[1]").workplane(invert=True)
           .rect(l, h).cutBlind(solid_thickness)
           .rect(l, h).cutBlind(-height_u * constants.GRHU)
           )
    return box


cq.exporters.export(blades_holder_9mm(), 'blades_holder_9mm.stl')
cq.exporters.export(blades_holder_18mm(), 'blades_holder_18mm.stl')
