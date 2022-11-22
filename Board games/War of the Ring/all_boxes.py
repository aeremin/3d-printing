import Libraries.boxes as boxes
import cadquery as cq

# Can be downloaded from here https://www.wfonts.com/font/tolkien.
# Need to be installed for all users (right click the file, "Install for all users") for script to work.
free_people_font = "Tolkien"
section_names = ("Regular", "Leader", "Elite")
unit_box_height = 29

elves_rohan_box_sections = (34, 43, 70)
elves_rohan_box_width = 88

gondor_northmen_box_sections = (35, 39, 41)
gondor_northmen_box_width = 96

elves = boxes.sectioned_box_with_text("Elves", elves_rohan_box_width,
                                      list(zip(section_names, elves_rohan_box_sections)),
                                      unit_box_height, font=free_people_font)
cq.exporters.export(elves, "elves.stl")

rohan = boxes.sectioned_box_with_text("Rohan", elves_rohan_box_width,
                                      list(zip(section_names, elves_rohan_box_sections)),
                                      unit_box_height, font=free_people_font)
cq.exporters.export(rohan, "rohan.stl")

gondor = boxes.sectioned_box_with_text("Gondor", gondor_northmen_box_width,
                                       list(zip(section_names, gondor_northmen_box_sections)),
                                       unit_box_height, font=free_people_font)
cq.exporters.export(gondor, "gondor.stl")

northmen = boxes.sectioned_box_with_text("The North", gondor_northmen_box_width,
                                         list(zip(section_names, gondor_northmen_box_sections)),
                                         unit_box_height, font=free_people_font)
cq.exporters.export(northmen, "northmen.stl")
