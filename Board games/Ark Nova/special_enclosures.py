import Libraries.boxes as boxes
import cadquery as cq

width = 76
length = 157
height = 20

a = boxes.hexagonal_floor_holes_box(width, length, height, 1.5, 2, 5).translate((width / 2, length / 2, height / 2))
cq.exporters.export(a, "special_enclosures.stl")
