import cadquery as cq
from Apartment.Skadis.hook import skadis_hook

pocket_depth = 20
pocket_width = 60
pocket_height = 50
wall_thickness = 2

holder = (
  cq.Workplane()
    .box(2 * wall_thickness + pocket_depth, 2 * wall_thickness + pocket_width, wall_thickness + pocket_height, centered=(False, True, False))
    .faces(">Z").rect(pocket_depth, pocket_width).cutBlind(-pocket_height)
)

interhook_distance = 40
hook1 = skadis_hook().translate((wall_thickness, interhook_distance / 2, wall_thickness + pocket_height))
hook2 = skadis_hook().translate((wall_thickness, -interhook_distance / 2, wall_thickness + pocket_height))

portemonnaie = holder.union(hook1).union(hook2)

cq.exporters.export(portemonnaie, "portemonnaie.stl")