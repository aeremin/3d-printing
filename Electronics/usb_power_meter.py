import cadquery as cq

l = 40
w = 33
offset = 5
hole_diameter = 2
hole_tolerance = 0.1

test = (cq.Workplane().box(l + 2 * offset, w + 2 * offset, 2).faces(">Z").rect(l, w, forConstruction=True)
        .vertices().cylinder(6, (hole_diameter - hole_tolerance) / 2, centered=(True, True, False)))

cq.exporters.export(test, 'usb_power_meter_test.stl')
