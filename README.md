
Modifications for the Sovol Zero 3D Printer
===========================================

This is a repository of design files and STL for the Sovol Zero
3D Printer.

https://www.sovol3d.com/products/sovol-zero-3d-printer

These designs were developed using CAD Query:

https://github.com/CadQuery/cadquery

The dimensions used in the Python files are all in millimeters.

All files are intended to print on a Sovol Zero.

Exhaust Adapter
---------------

This is a work in progress.

This adapter connects a portable AC exhaust kit to the vent
fan on the side of the Sovol Zero.

There are replacement portable AC unit exhaust kits which have a
window adapter and 5.125in (5 1/8 in) plastic exhaust hose. These
are from vendors such as "Perfect Aire" or "Pro Aire".

This adapter is sized to fit *inside* the hose. The adapter 
attaches to the side of the Sovol Zero using strong magnets glued
to the flat adapter plate.

The holes in the adapter plate are to line up with the screws below
the fan on the Sovol Zero. 

This alpha version needs two significant improvements:

* Change the cone section to not use a `.hole()` and instead subtract
a smaller cone using `.cut()`.
* Add screw threads. For the 5.125in hose, the thread pitch should
be around 15.9mm.

With the design as-is, the hose fits on tight, and a little fabric tape
is all that is needed to secure the hose to the adapter.

Use whatever strong magnets that are available, such as from an old
hard drive.


Bowden Tube Cap
---------------

This is a tight-fitting cap for a 4mm diameter Bowden tube.

Filter Adapter
--------------

Using a commonly available 10in square HVAC filter, this replaces
the top glass plate of the Sovol Zero.  It is intended for use
when the Zero should normally be left open while printing, such as for
PLA when a warmer chamber temperature is not needed. By allowing
the heat to escape up and out of the Zero, the glass door can then
be kept closed. This should hopefully prevent emission of
micro-particles into the work environment.

Note that these 10in square filters are actually 9.75 inches on a
side. The "HDX 1005 797 469" (from Home Depot) is one such filter.

When slicing using Orca Slicer, there are warnings about a floating
cantilever, but it seems to print just fine. Note the changed infill
direction.

Print 4 of the filter adapter corners and 4 of the slot connectors,
lightly sand the mating surfaces and glue them together.

To prevent the filament tube from rubbing on the underside of the
filter, use some window screen and 1/8th inch screen spline to 
attach the screen material to the bottom of the filter adapter.
