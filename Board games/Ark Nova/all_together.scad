v_dist = 0;

module CardsHolders() {
  for (i = [0:3]) {
    translate([i * (72 + v_dist), 0, 0]) import("5266169/AN_card_holder.stl");
  }
}

module Universities() {
  translate([24.55, 166.5 + v_dist, 0]) rotate([0, 0, 90])  import("5266169/AN_universities.stl");
}

module Venom() {
  translate([123.6 + v_dist, 175.9 + v_dist, 0]) import("5266169/AN_bonus+venom.stl");
}

module Credits() {
  for (i = [0:1]) {
    translate([61, 212.3 + i * (49 + v_dist) + 2 * v_dist, 0]) import("5266169/AN_credits.stl");
  }
}

module Enclosures() {
  for (i = [0:1]) {
    translate([38.64, 323.7 + i * (43 + v_dist) + 4 * v_dist, 0]) import("5266169/AN_enclosures.stl");
  }
}

module SpecialEnclosures() {
  translate([208.4 + 3 * v_dist, 197.1 + v_dist, 0]) import("5266169/AN_specials_2.stl");
}

module PlayerBoxes() {
  for (i = [0:3]) {
    translate([i * (72 + v_dist), 100 + v_dist, 20 + v_dist]) {
      import("5543151/player_cover_smaller.stl");
      translate([36, 57.25, -9]) rotate([0, 180, 0]) import("5543151/player_pieces.stl");
    }
  }
}

PlayerBoxes();

translate([42.377, -31.94, 0]) {
  color("green") {
    CardsHolders();
    Enclosures();
    SpecialEnclosures();
  }
  color("blue") {
    Universities();
    Venom();
    Credits();
  }
}
