import cadquery as cq

def drill_diameter_tester(diameter):
    sizes = iter([diameter, diameter + 0.1, diameter + 0.2, diameter + 0.3, diameter + 0.4])
    u = diameter + 5
    return (cq.Workplane().box(5 * u, u, 6).faces(">Z").workplane()
         .rarray(u, 1, 5, 1)
         .eachpoint(
            lambda loc: cq.Workplane().cylinder(12, next(sizes) / 2).val().located(loc),
            combine="cut"
         ))

cq.exporters.export(drill_diameter_tester(5), '5mm_0.1_step.stl')
cq.exporters.export(drill_diameter_tester(8), '8mm_0.1_step.stl')
cq.exporters.export(drill_diameter_tester(15), '15mm_0.1_step.stl')
