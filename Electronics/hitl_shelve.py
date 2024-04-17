
import cadquery as cq

MAX_PCB_LENGTH = 100
MAX_PCB_WIDTH = 85

CABLE_PASS_AREA_WIDTH = 15
CABLE_PASS_AREA_LENGTH = 70
CABLE_PASS_AREA_PIN_WIDTH = 5
CABLE_PASS_AREA_FULL_HOLE_LENGTH = 15

DEBUGGER_AREA_WIDTH = 55

TOTAL_WIDTH = MAX_PCB_WIDTH + CABLE_PASS_AREA_WIDTH + DEBUGGER_AREA_WIDTH
TOTAL_LENGTH = MAX_PCB_LENGTH

THICKNESS = 2
PIN_HEIGHT = 5


def _rectFromTwoCorners(self, p1, p3):
    x1, y1 = p1
    x2, y2 = p3
    p2 = (x1, y2)
    p4 = (x2, y1)
    return self.segment(p1, p2).segment(p3).segment(p4).segment(p1)


cq.Sketch.rectFromTwoCorners = _rectFromTwoCorners


def generic_shelf() -> cq.Workplane:
    result = (
        cq.Workplane().box(TOTAL_WIDTH, TOTAL_LENGTH, THICKNESS, centered=False)
        .faces(">Z").workplane().tag("top")
        # Cable area
        .pushPoints([(MAX_PCB_WIDTH, (TOTAL_LENGTH - CABLE_PASS_AREA_LENGTH) / 2)])
        .vLine(CABLE_PASS_AREA_LENGTH).hLine(CABLE_PASS_AREA_WIDTH).vLine(-CABLE_PASS_AREA_LENGTH)
        .hLine(-(CABLE_PASS_AREA_WIDTH - CABLE_PASS_AREA_PIN_WIDTH) / 2)
        .vLine(CABLE_PASS_AREA_LENGTH - CABLE_PASS_AREA_FULL_HOLE_LENGTH).hLine(-CABLE_PASS_AREA_PIN_WIDTH)
        .vLine(-CABLE_PASS_AREA_LENGTH + CABLE_PASS_AREA_FULL_HOLE_LENGTH)
        .close().cutThruAll()
    )
    result = render_bmp_board(result.faces(tag="top").workplane(origin=(TOTAL_WIDTH - DEBUGGER_AREA_WIDTH + 1, 2)))
    return result


def render_bmp_board(w: cq.Workplane) -> cq.Workplane:
    outline = (cq.Sketch()
               .rectFromTwoCorners((155, 148), (206, 83))
               .assemble(mode="c", tag="exact_outline").wires(tag="exact_outline").offset(0.25)
               )

    mount = (cq.Sketch().push([(158, 137), (158, 94), (200, 137), (200, 94)])
             .circle(1.9 / 2)
             )

    holes = (cq.Sketch()
             .rectFromTwoCorners((177, 92), (196, 144))
             .rectFromTwoCorners((160, 130), (173, 138))
             .rectFromTwoCorners((157, 139), (175, 144))
             .assemble()
             )

    return (w.transformed(offset=(-155, 148, 0), rotate=(180, 0, 0)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(
        -PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )


def render_lock(w: cq.Workplane) -> cq.Workplane:
    outline = (cq.Sketch()
               .rectFromTwoCorners((104.5, 54.5), (184.5, 150.5))
               .assemble(mode="c", tag="exact_outline").wires(tag="exact_outline").offset(0.25)
               )
    mount = (cq.Sketch().push([(107.5, 132.5), (107.5, 58.25), (181, 58.25), (181, 132.5)])
             .circle(2.1 / 2)
             )

    holes = (cq.Sketch()
             .rectFromTwoCorners((108, 64.5), (118, 69))
             .rectFromTwoCorners((114, 97.5), (117.5, 108.5))
             .rectFromTwoCorners((106.5, 120), (112, 128.5))
             .rectFromTwoCorners((106, 136.5), (126, 139))
             .rectFromTwoCorners((130, 142), (140, 147.5))
             .rectFromTwoCorners((179.5, 106), (182.5, 124.5))
             .rectFromTwoCorners((154, 134), (181, 142))
             .assemble()
             )

    return (w.workplaneFromTagged("top")
            .transformed(offset=(-104.5 + 3, 150.5 + 2, 0), rotate=(180, 0, 0)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(
        -PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )


def render_firefly(w: cq.Workplane) -> cq.Workplane:
    outline = (cq.Sketch()
               .segment((124, 80), (176, 80))
               .arc((191.1789, 82.4632), (204.8, 89.6))
               .arc((206, 92), (204.8, 94.4))
               .arc((191.1789, 101.5368), (176, 104))
               .segment((124, 104))
               .arc((108.8211, 101.5368), (95.2, 94.4))
               .arc((94, 92), (95.2, 89.6))
               .arc((108.8211, 82.4632), (124, 80))
               .assemble(mode="c", tag="exact_outline").wires(tag="exact_outline").offset(0.25)
               )

    mount = (cq.Sketch().push([(178.6, 101.8), (178.6, 82.2), (121.4, 82.2), (121.4, 101.8)])
             .circle(2.1 / 2)
             )

    holes = (cq.Sketch()
             .rectFromTwoCorners((123.4, 80), (176.6, 104))
             .rectFromTwoCorners((176.6, 88), (190.8, 97))
             .segment((186.8, 82.9), (190, 82.2))
             .segment((191.3, 88.1))
             .segment((188.2, 88.8))
             .segment((186.8, 82.9))             
             .arc((184.4, 86.6), 5, 0, 360)
             .segment((192.8, 83.8), (202.6, 88.8))
             .segment((200, 93.8))
             .segment((190.2, 88.8))
             .segment((192.8, 83.8))
             .assemble()
             )

    return (w.workplaneFromTagged("top")
            .transformed(offset=(15, 220, 0)).transformed(rotate=(180, 0, 50)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(
        -PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )

def render_usb_power_meter(w: cq.Workplane) -> cq.Workplane:
    outline = (cq.Sketch()
               .rectFromTwoCorners((100, 56), (137, 100))
               .assemble(mode="c", tag="exact_outline").wires(tag="exact_outline").offset(0.25)
               )

    mount = (cq.Sketch().push([(135, 98), (102, 98), (102, 58), (135, 58)])
             .circle(1.9 / 2)
             )

    holes = (cq.Sketch()
             .rectFromTwoCorners((119.5, 94.5), (129.5, 99.5))
             .rectFromTwoCorners((60, 64), (104.5, 78))
             .assemble()
             )

    return (w.workplaneFromTagged("top")
            .transformed(offset=(-60 + 3, 100 + 2, 0), rotate=(180, 0, 0)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(
        -PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )


def lock_shelf() -> cq.Workplane:
    return render_lock(generic_shelf())


def firefly_shelf() -> cq.Workplane:
    return render_firefly(generic_shelf())

def usb_power_meter_shelf() -> cq.Workplane:
    return render_usb_power_meter(generic_shelf())

a = (
    cq.Assembly()
    .add(firefly_shelf(), loc=cq.Location((0, 0, 0)), name="firefly", color=cq.Color("green"))
    .add(lock_shelf(), loc=cq.Location((0, 0, 30)), name="lock", color=cq.Color("green"))
)

t = firefly_shelf()

cq.exporters.export(firefly_shelf(), 'firefly_shelf.stl')
cq.exporters.export(usb_power_meter_shelf(), 'usb_power_meter_shelf.stl')
cq.exporters.export(lock_shelf(), 'lock_shelf.stl')

#show_object(a)
