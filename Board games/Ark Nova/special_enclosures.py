import Libraries.boxes as boxes
import cadquery as cq

a = boxes.hexagonal_floor_holes_box(76, 131, 20, 1.5, 2, 5).translate((76 / 2, 131 / 2, 20 / 2))
cq.exporters.export(a, "special_enclosures.stl")
