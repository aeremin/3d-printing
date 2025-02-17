import cadquery as cq
import Apartment.Skadis.hook as hook

tablet_width = 155
tablet_thickness = 8.5
skipped_sections = 2
section_width = 40
compartment_width = (tablet_width - skipped_sections * section_width) / 2
pocket_height = 29
wall_thickness = 2

side_bezel = 10
bottom_bezel = 16

print("Compartment width:", compartment_width)

holder = (
  cq.Workplane()
    .box(tablet_thickness + 2 * wall_thickness, compartment_width + wall_thickness, pocket_height + wall_thickness, centered=False)
    .cut(
      cq.Workplane().box(tablet_thickness, compartment_width, pocket_height, centered=False).translate((wall_thickness, 0, wall_thickness))
    )
    .cut(
      cq.Workplane().box(tablet_thickness + wall_thickness, compartment_width, pocket_height, centered=False).translate((wall_thickness, -side_bezel, wall_thickness + bottom_bezel))
    )
)

tablet_holder_half = holder.union(
  hook.skadis_hook().translate((wall_thickness, section_width / 2, hook.HEIGHT))
)

cq.exporters.export(tablet_holder_half, "tablet_holder_half.stl")