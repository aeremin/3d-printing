import Libraries.boxes as boxes
import cadquery as cq

def x_dimension(o):
    return o.val().BoundingBox().xlen

def y_dimension(o):
    return o.val().BoundingBox().ylen

# Can be downloaded from here https://www.wfonts.com/font/tolkien.
# Need to be installed for all users (right click the file, "Install for all users") for script to work.
font = "Tolkien"
section_names_free_people = ("Regular", "Leader", "Elite")
unit_box_height = 29

elves_rohan_box_sections = (34, 43, 70)
elves_rohan_box_width = 88

gondor_northmen_box_sections = (35, 39, 41)
gondor_northmen_box_width = 96

def cards_box():
    section_width = 132
    wall_thickness = 1.2
    horizontal_section_length = 71
    horizontal_section_height = 58
    vertical_section_length = 34
    vertical_section_height = horizontal_section_height + 20
    cutter_fillet_radius = 4

    bbox = cq.Workplane().box(2 * section_width + 3 * wall_thickness,
                              vertical_section_length + horizontal_section_length + 3 * wall_thickness,
                              vertical_section_height, centered=False)
    for i in range(2):
        for j in range(2):
            c = cq.Workplane(origin=(wall_thickness + i * (section_width + wall_thickness),
                                     wall_thickness + j * (horizontal_section_length + wall_thickness),
                                     wall_thickness)).box(section_width,
                                                          horizontal_section_length if j == 0 else vertical_section_length,
                                                          vertical_section_height - wall_thickness, centered=False)
            bbox = bbox.cut(c)
    cutter = cq.Workplane(origin=(0, 0, 58)).box(2 * section_width + 3 * wall_thickness,
                                                 horizontal_section_length + wall_thickness,
                                                 vertical_section_height - horizontal_section_height, centered=False)
    bbox = bbox.cut(cutter)
    cutter_shape = cq.Workplane("XZ").polyline([(0, -25), (30, -25), (35, 0), (45, 0), (45, 10), (0, 10)]).mirrorY()\
        .extrude(-1000).edges("|Y").fillet(cutter_fillet_radius)
    bbox = bbox.cut(cutter_shape.translate((wall_thickness + section_width / 2, horizontal_section_length, vertical_section_height)))
    bbox = bbox.cut(cutter_shape.translate((2 * wall_thickness + 3 * section_width / 2, horizontal_section_length, vertical_section_height)))

    cutter_shape = cq.Workplane("XZ").polyline(
        [(0, -horizontal_section_height), (20, -horizontal_section_height), (25, 0), (35, 0), (35, 10), (0, 10)]).mirrorY()\
        .extrude(-wall_thickness).faces(">Z[1]").edges("|Y").fillet(cutter_fillet_radius)
    cutter_shape = cutter_shape.union(cq.Workplane().cylinder(2 * horizontal_section_height, 20))
    bbox = bbox.cut(cutter_shape.translate((wall_thickness + section_width / 2, 0, horizontal_section_height)))
    bbox = bbox.cut(cutter_shape.translate((2 * wall_thickness + 3 * section_width / 2, 0, horizontal_section_height)))

    return bbox

cq.exporters.export(cards_box(), "cards.stl")

elves = boxes.sectioned_box_with_text("Elves", elves_rohan_box_width,
                                      list(zip(section_names_free_people, elves_rohan_box_sections)),
                                      unit_box_height, font=font)
cq.exporters.export(elves, "elves.stl")

rohan = boxes.sectioned_box_with_text("Rohan", elves_rohan_box_width,
                                      list(zip(section_names_free_people, elves_rohan_box_sections)),
                                      unit_box_height, font=font)
cq.exporters.export(rohan, "rohan.stl")

gondor = boxes.sectioned_box_with_text("Gondor", gondor_northmen_box_width,
                                       list(zip(section_names_free_people, gondor_northmen_box_sections)),
                                       unit_box_height, font=font)
cq.exporters.export(gondor, "gondor.stl")

northmen = boxes.sectioned_box_with_text("The North", gondor_northmen_box_width,
                                         list(zip(section_names_free_people, gondor_northmen_box_sections)),
                                         unit_box_height, font=font)
cq.exporters.export(northmen, "northmen.stl")

tokens_box_height = 17
dice_and_control = boxes.sectioned_box_with_text("", elves_rohan_box_width,
                                                 [("Free Peoples\n      Dice", 47.50), ("Shadow Dice", 47.50), ("Control", 18)],
                                                 tokens_box_height, font=font)
cq.exporters.export(dice_and_control, "dice_and_control.stl")

other_tokens = boxes.sectioned_box_with_text("", elves_rohan_box_width,
                                             [("", 41), ("", 41), ("", 30)],
                                             tokens_box_height, font=font)
cq.exporters.export(other_tokens, "other_tokens.stl")

minions_hunt = boxes.sectioned_box_with_text("", 117,
                                             [("Hunt", 27), ("Minions", 57)],
                                             25, font=font)
cq.exporters.export(minions_hunt, "minions_hunt.stl")

nazgul = boxes.sectioned_box_with_text("", 64,
                                       [("Nazgul", 86)],
                                       unit_box_height, font=font)
cq.exporters.export(nazgul, "nazgul.stl")

companions = boxes.sectioned_box_with_text("", 68,
                                           [("Companions", 64 - 2.4)],
                                           unit_box_height, font=font, font_size=12)
cq.exporters.export(companions, "companions.stl")

dwarves = boxes.sectioned_box_with_text("Dwarves", 64,
                                        list(zip(section_names_free_people, [27, 38, 41])),
                                        unit_box_height, font=font)
cq.exporters.export(dwarves, "dwarves.stl")

shadow_units_box_width = 128
section_names_shadow = ("Elite", "Regular")
sauron_section_sizes = [38, 57]
isengard_section_sizes = [38, 32]
easterlings_section_sizes = [53, 40]

total_shadow_boxes_length = sum(sauron_section_sizes) + sum(isengard_section_sizes) + sum(easterlings_section_sizes) + \
                            1.2 * (len(sauron_section_sizes) + 1 + len(isengard_section_sizes) + 1 + len(easterlings_section_sizes) + 1)

print("Total length of shadow boxes: %.2f/270" % total_shadow_boxes_length)

sauron_units = boxes.sectioned_box_with_text("Sauron", shadow_units_box_width,
                                             list(zip(section_names_shadow, sauron_section_sizes)),
                                             unit_box_height, font=font)
cq.exporters.export(sauron_units, "sauron_units.stl")

isengard_units = boxes.sectioned_box_with_text("Isengard", shadow_units_box_width,
                                               list(zip(section_names_shadow, isengard_section_sizes)),
                                               unit_box_height, font=font)
cq.exporters.export(isengard_units, "isengard_units.stl")

easterlings_units = boxes.sectioned_box_with_text("Southrons\nEasterlings", shadow_units_box_width,
                                                  list(zip(section_names_shadow, easterlings_section_sizes)),
                                                  unit_box_height, font=font, font_size=11)
cq.exporters.export(easterlings_units, "easterlings_units.stl")

shadow_factions_section_names = ("Spiders", "Dunledings", "Corsairs")
shadow_factions_section_sizes = (41, 40.4, 63)
free_people_section_names = ("Ents", "Dead Men", "Eagles")
free_people_factions_section_sizes = (46.4, 35, 63)

shadow_factions = boxes.sectioned_box_with_text("", gondor_northmen_box_width,
                                                list(zip(shadow_factions_section_names, shadow_factions_section_sizes)),
                                                unit_box_height, font=font)
cq.exporters.export(shadow_factions, "shadow_factions.stl")

free_peoples_factions = boxes.sectioned_box_with_text("", gondor_northmen_box_width,
                                                list(zip(free_people_section_names, free_people_factions_section_sizes)),
                                                unit_box_height, font=font)
cq.exporters.export(free_peoples_factions, "free_peoples_factions.stl")

total_factions_layer_length = sum(gondor_northmen_box_sections) + sum(shadow_factions_section_sizes) + \
                            1.2 * (len(gondor_northmen_box_sections) + 1 + len(shadow_factions_section_sizes) + 1)
print("Total length of faction layer: %.2f/270" % total_factions_layer_length)