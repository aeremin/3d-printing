import Libraries.boxes as boxes
import cadquery as cq

elves = boxes.sectioned_box_with_text("Elves", 88, [("Regular", 34), ("Leader", 43), ("Elite", 70)], 29, font="Tolkien")
cq.exporters.export(elves, "elves.stl")

