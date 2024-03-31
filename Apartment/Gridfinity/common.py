from cqgridfinity import *
import cadquery as cq

TOP_SURFACE_TAG = "top_surface"

class GridfinityBoxWithHoles(GridfinityBox):
  def __init__(self,
               length_u: int,
               width_u: int,
               height_u: int,
               solid: bool = False,
               solid_thickness: float = 0,
               scoops: bool = False,
               labels: bool = False,
               no_lip: bool = False,
               ):
    solid_ratio = solid_thickness / ((height_u - 1) * constants.GRHU)
    super().__init__(length_u, width_u, height_u, holes=True, unsupported_holes=True,
                     solid=solid, solid_ratio=solid_ratio, scoops=scoops, labels=labels, no_lip=no_lip)

  def to_cq(self) -> cq.Workplane:
    r: cq.Workplane = self.cq_obj
    return r.faces("<Z[1]").workplane().tag(TOP_SURFACE_TAG)
