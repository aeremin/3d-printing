union() {
    import("Return To Organizer/Part_1.stl");
    import("Return To Organizer/Part_2-4.stl");
    translate([56, 0, 0]) import("Return To Organizer/Part_2-4.stl");
    translate([2 * 56, 0, 0]) import("Return To Organizer/Part_2-4.stl");
    translate([2 * 56, 0, 0]) import("Return To Organizer/Part_5.stl");
    
    // To glue joints together.
    translate([56, 0, -1]) cube([200, 50, 2], true);
}