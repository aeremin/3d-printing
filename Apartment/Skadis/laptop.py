import cadquery as cq
from Apartment.Skadis.hook import skadis_hook

laptop_width = 323
laptop_thickness = 16
skipped_sections = 5
section_width = 40
compartment_width = (laptop_width - skipped_sections * section_width) / 2
pocket_height = 60
wall_thickness = 2

print("Compartment width:", compartment_width)

holder = (
  cq.Workplane()
    .box(laptop_thickness + 2 * wall_thickness, compartment_width + wall_thickness, pocket_height + wall_thickness, centered=False)
    .cut(
      cq.Workplane().box(laptop_thickness, compartment_width, pocket_height, centered=False).translate((wall_thickness, 0, wall_thickness))
    )
)

hook1 = skadis_hook().translate((wall_thickness, section_width / 2, pocket_height + wall_thickness))
hook2 = skadis_hook().translate((wall_thickness, section_width + section_width / 2, pocket_height + wall_thickness))

laptop_holder_half = holder.union(hook1).union(hook2)

cq.exporters.export(laptop_holder_half, "laptop_holder_half.stl")