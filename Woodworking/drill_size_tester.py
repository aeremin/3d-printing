import cadquery as cq

sizes = iter([15.0, 15.1, 15.2, 15.3, 15.4])

r = (cq.Workplane().box(100, 20, 6).faces(">Z").workplane()
     .rarray(20, 1, 5, 1)
     .eachpoint(
        lambda loc: cq.Workplane().cylinder(12, next(sizes) / 2).val().located(loc),
        combine="cut"
     ))

cq.exporters.export(r, '15mm_0.1_step.stl')