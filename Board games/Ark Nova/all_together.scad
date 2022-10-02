v_dist = 0;

module CardsHolders(n = 4) {
  translate([42.377, -31.94, 0]) {
    for (i = [0:n - 1]) {
      translate([i * (72 + v_dist), 0, 0]) import("5266169/AN_card_holder.stl");
    }
  }
}

module Universities() {
  translate([66.94, 34.71, 0]) rotate([0, 0, 90])  import("5266169/AN_universities.stl");
}

module Venom() {
  translate([35, 44, 0]) import("5266169/AN_bonus+venom.stl");
}

module Credits(n = 2) {
  for (i = [0:n - 1]) {
    translate([103.37, 11.5 + i * (49 + v_dist), 0]) import("5266169/AN_credits.stl");
  }
}

module Enclosures(n = 2) {
  translate([81, 24.9, 0]) {
    for (i = [0:n - 1]) {
      translate([0, i * (43 + v_dist), 0]) import("5266169/AN_enclosures.stl");
    }
  }
}

module SpecialEnclosures() {
  translate([38.8, 65.2, 0]) import("5266169/AN_specials_2.stl");
}

module PlayerBoxes(n = 4) {
  for (i = [0:n-1]) {
    translate([i * (72 + v_dist), 0, 0]) {
      import("5543151/player_cover_smaller.stl");
      translate([36, 57.25, -9]) rotate([0, 180, 0]) import("5543151/player_pieces.stl");
    }
  }
}

module Assembly() {
  color("green") {
    CardsHolders();
    translate([0, 100 + 69 + 2* 49, 0]) Enclosures();
    translate([212, 100, 0]) SpecialEnclosures();
  }
  color("blue") {
    translate([0, 100, 0]) Universities();
    translate([131, 100, 0]) Venom();
    translate([0, 100 + 69, 0]) Credits();
  }
  translate([0, 100, 20]) PlayerBoxes();
}

Assembly();