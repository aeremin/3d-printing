import cadquery as cq

hole_width = 21
hole_thickness = 9.5
hole_depth = 28

spool_holder_diameter = hole_width
spool_holder_length = 80

spool_holder_hole_side = 10
spool_holder_hole_depth = 10

stopper_thickness = 5
stopper_diameter = 40

spool_holder_base = cq.Workplane().box(hole_width, hole_depth + spool_holder_diameter / 2, hole_thickness,
                                       centered=(True, False, False))
spool_holder = (
  cq.Workplane(origin=(0, hole_depth + spool_holder_diameter / 2, 0))
  .cylinder(spool_holder_length + hole_thickness, spool_holder_diameter / 2, centered=(True, True, False))
  .faces(">Z").workplane().rect(spool_holder_hole_side, spool_holder_hole_depth).cutBlind(-spool_holder_hole_depth)
).union(spool_holder_base)

cq.exporters.export(spool_holder, 'a1mini_spool_holder.stl')

eps = 0.1
stopper = (cq.Workplane().cylinder(stopper_thickness, stopper_diameter / 2)
           .faces(">Z").workplane()
           .rect(spool_holder_hole_side - eps, spool_holder_hole_side - eps).extrude(spool_holder_hole_depth - eps))

cq.exporters.export(stopper, 'a1mini_spool_holder_stopper.stl')

tube_diameter = 4.4
tube_hole_offset = 30

tube_holder_base = cq.Workplane().box(hole_width, hole_depth, hole_thickness,
                                       centered=(True, False, False))
tube_holder = (
  cq.Workplane(origin=(hole_width / 2 - tube_diameter, hole_depth + tube_diameter, 0)).rect(2 * tube_diameter, 2 * tube_diameter).extrude(hole_thickness + tube_diameter + tube_hole_offset)
  .faces(">X").workplane().pushPoints([(0, hole_thickness + tube_hole_offset)]).hole(tube_diameter)
).union(tube_holder_base)

cq.exporters.export(tube_holder, 'a1mini_tube_holder.stl')