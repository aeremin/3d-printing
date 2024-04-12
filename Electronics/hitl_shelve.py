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
               .assemble().vertices().fillet(2)
               )

    mount = (cq.Sketch().push([(158, 137), (158, 94), (200, 137), (200, 94)])
             .circle(1.9 / 2)
             )
    
    holes = (cq.Sketch()
             .rectFromTwoCorners((177, 92), (196, 144))
             .rectFromTwoCorners((161, 131), (172, 137))
             .rectFromTwoCorners((158, 140), (174, 143))
             .assemble()
             )    

    return (w.transformed(offset=(-155, 148, 0), rotate=(180, 0, 0)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(-PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )

def render_lock(w: cq.Workplane) -> cq.Workplane:
    outline = (cq.Sketch()
               .rectFromTwoCorners((104.5, 54.5), (184.5, 150.5))
               .assemble()
               )

    mount = (cq.Sketch().push([(107.5, 132.5), (107.5, 58.25), (151.25, 58.25), (178.5, 132.5)])
             .circle(2.1 / 2)
             )
    

    holes = (cq.Sketch()
             .rectFromTwoCorners((108, 64.5), (118, 69))
             .rectFromTwoCorners((114, 97.5), (117.5, 108.5))
             .rectFromTwoCorners((106.5, 120), (112, 128.5))
             .rectFromTwoCorners((106, 136.5), (126, 139))
             .rectFromTwoCorners((130, 142), (140, 147.5))
             .rectFromTwoCorners((144.5, 131.5), (170.5, 141))
             .rectFromTwoCorners((179.5, 106), (182.5, 124.5))
             .assemble()
             )

    return (w.workplaneFromTagged("top")
            .transformed(offset=(-104.5 + 3, 150.5 + 2, 0), rotate=(180, 0, 0)).tag("local")
            .placeSketch(outline).cutBlind(THICKNESS / 2)
            .workplaneFromTagged("local").transformed(offset=(0, 0, THICKNESS / 2)).placeSketch(mount).extrude(-PIN_HEIGHT)
            .workplaneFromTagged("local").placeSketch(holes).cutThruAll()
            )

def lock_shelf() -> cq.Workplane:
    return render_lock(generic_shelf())

a = lock_shelf()

