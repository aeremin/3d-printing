difference() {
    union() {
        translate([0, -131, 0]) import("special_enclosures.stl");

        translate([38.8, 65.2, 0]) { 
          import("5266169/AN_specials_2.stl");
        }
    }
    
    cube([50, 1000, 1000], true);

}

render(3);