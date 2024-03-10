import cadquery as cq

def pcb_holder(slots, spacing, length):
    pcb_thickness = 1.7
    groove_depth = 2
    floor_thickness = 2
    total_width = slots * spacing
    side = (
        cq.Sketch()
        .rect(total_width, floor_thickness + groove_depth)
        .push([(0, floor_thickness / 2)])
        .rarray(spacing, 0, slots, 1)
        .rect(pcb_thickness, groove_depth, mode = "s")
    )
    
    return cq.Workplane(cq.Plane.XZ()).placeSketch(side).extrude(length)

cq.exporters.export(pcb_holder(slots=5, spacing=16, length=70), 'nrf52840_lock.stl')
cq.exporters.export(pcb_holder(slots=5, spacing=16, length=43), 'smart_usb.stl')
cq.exporters.export(pcb_holder(slots=4, spacing=16, length=70), 'nrf_devkits.stl')
cq.exporters.export(pcb_holder(slots=5, spacing=5, length =41), 'nfc_st25r3911b_breakout.stl')