import Libraries.boxes as boxes
import cadquery as cq

# Can be downloaded from here https://www.wfonts.com/font/tolkien.
# Need to be installed for all users (right click the file, "Install for all users") for script to work.
free_people_font = "Tolkien"
section_names = ("Regular", "Leader", "Elite")
unit_box_height = 29

elves_rohan_box_sections = (34, 43, 70)
elves_rohan_box_width = 88

elves = boxes.sectioned_box_with_text("Elves", elves_rohan_box_width,
                                      list(zip(section_names, elves_rohan_box_sections)),
                                      unit_box_height, font=free_people_font)
cq.exporters.export(elves, "elves.stl")

