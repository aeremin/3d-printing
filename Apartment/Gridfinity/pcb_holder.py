import cadquery as cq
from cqgridfinity import GridfinityBox
from cqgridfinity import  constants
import math

def gridfinity_pcb_holder(slots, spacing, length, width):
    pcb_thickness = 1.7
    groove_depth = 2
    total_width = slots * spacing
    unit_height = 1 + math.ceil(width / constants.GRHU)
    unit_width = math.ceil(total_width / constants.GRU)
    unit_length = math.ceil(length / constants.GRU)
    box = GridfinityBox(unit_width, unit_length,  unit_height, holes=True, unsupported_holes=True).cq_obj
    box = box.faces("<Z[1]").workplane(offset=-groove_depth).rarray(spacing, 1, slots, 1).rect(pcb_thickness, length).cutBlind(width + constants.GRHU)
    h = 12
    v = h * math.sqrt(3)
    nv = math.floor((unit_height * constants.GRHU) / v)
    nh1 = math.floor((unit_length * constants.GRU) / h) - 1
    nh2 = math.floor((unit_width * constants.GRU) / h) - 1
    box = (box
           .faces("<X")
             .workplane(centerOption="CenterOfMass").transformed(rotate=(0, 0, 90))
             .rarray(v, h, nv, nh1).polygon(6, h - 1).cutThruAll().rarray(v, h, nv - 1, nh1 - 1).polygon(6, h - 1).cutThruAll()
          .faces("<Y")
             .workplane(centerOption="CenterOfMass").transformed(rotate=(0, 0, 90))
             .rarray(v, h, nv, nh2).polygon(6, h - 1).cutThruAll().rarray(v, h, nv - 1, nh2 - 1).polygon(6, h - 1).cutThruAll()           
        )
    return box
    
cq.exporters.export(gridfinity_pcb_holder(5, 16, 97, 80), 'gridfinity_nrf52840_lock.stl')
cq.exporters.export(gridfinity_pcb_holder(5, 16, 45, 53), 'gridfinity_smart_usb.stl')
cq.exporters.export(gridfinity_pcb_holder(5, 5, 41.2, 82), 'gridfinity_nfc_st25r3911b_breakout.stl')
cq.exporters.export(gridfinity_pcb_holder(4, 16, 138, 64), 'gridfinity_nrf_devkits.stl')
