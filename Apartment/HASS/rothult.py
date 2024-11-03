import cadquery as cq

mounting_hole_diameter = 5 - 0.2
mounting_hole_distance = 64.5
width = mounting_hole_diameter + 0.4
bottom_thickness = 2
total_height = 30
height_before_pin = 2.5
height_after_pin = 8
width_around_pin = 3
pin_width = 10 + 0.2

pin_fixator = (cq.Workplane().slot2D(mounting_hole_distance + width, width).extrude(bottom_thickness)
               .faces(">Z").workplane().tag("base")
               .rect(pin_width + 2 * width_around_pin, width).extrude(height_before_pin)
               .rarray(pin_width + width_around_pin, 1, 2, 1).rect(width_around_pin, width).extrude(height_after_pin)
               .workplaneFromTagged("base")
               .rarray(mounting_hole_distance, 1, 2, 1).circle(mounting_hole_diameter / 2).extrude(total_height)
               )

cq.exporters.export(pin_fixator, 'pin_fixator.stl')