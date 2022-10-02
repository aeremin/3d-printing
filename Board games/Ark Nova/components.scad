module CardsHolders(d, n = 4) {
  translate([42.377, -31.94, 0]) {
    for (i = [0:n - 1]) {
      translate([i * (72 + d), 0, 0]) import("5266169/AN_card_holder.stl");
    }
  }
}

module Universities() {
  translate([66.94, 34.71, 0]) rotate([0, 0, 90])  import("5266169/AN_universities.stl");
}

module Venom() {
  translate([35, 44, 0]) import("5266169/AN_bonus+venom.stl");
}

module Credits(d, n = 2) {
  for (i = [0:n - 1]) {
    translate([103.37, 11.5 + i * (49 + d), 0]) import("5266169/AN_credits.stl");
  }
}

module Enclosures(d, n = 2) {
  translate([81, 24.9, 0]) {
    for (i = [0:n - 1]) {
      translate([0, i * (43 + d), 0]) import("5266169/AN_enclosures.stl");
    }
  }
}

module SpecialEnclosures() {
  translate([38.8, 65.2, 0]) import("5266169/AN_specials_2.stl");
}

module PlayerBoxes(d, n = 4) {
  for (i = [0:n-1]) {
    translate([i * (72 + d), 0, 0]) {
      import("5543151/player_cover_smaller.stl");
      translate([36, 57.25, -9]) rotate([0, 180, 0]) import("5543151/player_pieces.stl");
    }
  }
}
