include <components.scad>

v_dist = 0;

module Assembly() {
  color("green") {
    CardsHolders(v_dist);
    translate([0, 4 * v_dist + 100 + 69 + 2* 49, 0]) Enclosures(v_dist);
    translate([1 * v_dist + 212, 3 * v_dist + 100 + 96, 0]) SpecialEnclosures();
  }
  color("blue") {
    translate([0, 3 * v_dist + 100 + 96 + 2, 0]) Universities();
    translate([131, 3 * v_dist + 100 + 96 + 2, 0]) Venom();
    translate([0, 1 * v_dist + 100, 1 * v_dist + 17]) Credits(v_dist);
  }
  translate([0, 1 * v_dist + 100, 0]) PlayerBoxes(4);
}

Assembly();