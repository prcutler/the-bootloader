# TBL E1 Script - Tod

## FullControl GCode Generator

Okay, we all know how 3D printers normally work: you got a 3D model in your computer,
you run it through a "slicer" program that chops it up vertically, like a deli slicer,
then creates instructions to "draw" in plastic each of those slices.
Those instructions, called GCODE, are sent to the 3d printer as one file.

So a 3d printer is really more of a 2D printer that stacks a bunch of 2d printed layers on top of each other.
(in fact there was a 3d printer that used printer paper, a CNC knife, and glue to make 3d prints)
The benefit of this approach is that any 3d object can be sliced up, without knowing how
the object is built.  The downside is you can't have graceful curves that move in three dimensions.

But the 3d printer CAN move in all three dimensions at once!
The 3d printer nozzle could move up and down, while moving around in a plane,
creating 3d structures that are impossible with traditional slicing approaches.
There have been various research projects showing this,
but the most approachable I just came across is the FullControl Design Library.

Go to FullControl dot XYZ to check it out.

It's a web-based demonstration of an upcoming open source Python library.
The 3d model viewer has a beautiful, almost cyberpunk, aesthetic with purples and blues.
The site currently has a collection of hand-picked generative 3d designs.
You pick one, modify its design parameters, click "generate", and you get GCODE directly downloaded
from  your browser. No need for a slicer program!

I've started playing with it and it's really fun. I can't wait to play with the library itself.

[FullControl Design Library](https://fullcontrol.xyz) and https://twitter.com/FullControlXYZ


## Belay -

We're both big fans of CircuitPython and Micropython, Python that runs directly on tiny
microcontroller boards, but if you're coming from desktop Python,
you can be in a rude awakening for the many limitations that embedded Python has.

Sometimes you don't need a fully-standalone device running by itself,
but a "smart peripheral" that you can control via your desktop computer.
So you could then write a custom protocol between your device and your computer,
with custom parsing code on both sides.

Or you can use Belay.

Belay is a desktop Python library that lets you quickly interact with
a CircuitPython/Micropython board. From your PC, you can read inputs, toggle pins,
light up Neopixels, etc.

How it works is you write CircuitPython or Micropython *inside* your desktop Python code,
using a special function decorator to indicate that this function should run on the board,
rather than on your computer.

It's a very elegant solution for when you need/want to stay in desktop Python,
but need to interact with remote I/O.

If you're from the Arduino world, you might think this sounds a little like Firmata.
Firmata is a protocol that lets you remotely control an Arduino running the Firmata sketch.
It's very powerful, but is fixed in its function. Belay can do that, but goes one step further
by allowing you to run any code you want on your board, from your Python

[Belay library for CPython to control Micropython/CircuitPython](https://github.com/BrianPugh/belay)


##
