# TBL E1 Script - Tod

## FullControl GCode Generator

Okay, we all know how 3D printers normally work: you got a 3D model in your computer,
you run it through a "slicer" that chops it up vertically, like a deli slicer,
then it makes instructions to "draw" each of those slices.  All those instructions,
called GCODE, are sent to the 3d printer as one file.

So a 3d printer is really more of a 2D printer that stacks a bunch of 2d printed layers on top of each other
(in fact there was a 3d printer that used printer paper, a CNC knife, and glue)

But the 3d printer can really move in all three dimensions at once!
The 3d printer nozzle can move up and down while moving around in a plane,
creating 3d structures that are impossible with traditional slicing approaches.
There have been various research projects showing this,
but the most approachable I just came across is the FullControl Design Library.

It's a simple web-based demonstration of an upcoming open source Python library.
At the moment you can pick from a variety of cool generative 3d designs, modify their parameters,
and generate GCODE in your browser. No need for a slicer program.

I've started playing with it and it's really fun. I can't wait to play with the library itself.

[FullControl Design Library](https://fullcontrol.xyz) and https://twitter.com/FullControlXYZ

## Belay -
