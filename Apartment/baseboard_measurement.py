import cadquery as cq

thickness = 10

baseboard_thickness = 15
baseboard_height = 60

offset = 15

baseboard = cq.Workplane().rect(baseboard_thickness, baseboard_height, centered=False).extrude(thickness)
tool = cq.Workplane().rect(baseboard_thickness + offset, baseboard_height + offset, centered=False).extrude(thickness)\
        .cut(baseboard)

cq.exporters.export(tool, 'baseboard_measurement.stl')

