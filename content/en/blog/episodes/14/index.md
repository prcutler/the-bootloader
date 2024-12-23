---
date: 2024-11-04
title: "Welcome Kevin Santo Cappuccio"
linkTitle: "Episode 14 - November 4, 2024"
description: "Welcome Kevin Santo Cappuccio"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Welcome to our second guest, Kevin Santo Cappuccio, the creator of Jumperless.

Join our newsletter!  Keep up with the show and what Paul and Tod are up to. 
Visit [The Bootloader's newsletter page](https://buttondown.com/thebootloader) to browse the archives or subscribe.

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px; overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/welcome-kevin-santo-cappuccio/embed"></iframe>

## Show Notes

### 00:27 Welcome Kevin Santo Cappuccio and the Jumperless v5

Kevin is the creator of the [Jumperless breadboard](https://www.crowdsupply.com/architeuthis-flux/jumperless-v5) 
and we were thrilled to have him on the show.  You can 
[follow Kevin on Mastodon here](https://hackaday.social/@ArchiteuthisFlux).

### 6:20 The UNO Plus+ (Kevin #1)

The [UNO Plus+](https://hackaday.io/project/189785-uno-plus) from John Loeffler is what the Arduino UNO should've
been all along. It's the same shape and hardware as the Arduino UNO, with the added bonus of LEDs on every pin to
show you the state.

I like shoveling a bunch of decorative LEDs onto things as much as the next guy, but I think when you're actually
using them to convey information while still looking nice, it's 1000 times cooler.

The whole "is this pin actually doing what I think it should be doing?" thing while debugging is sooo common.
I really thought it would become less of an issue as I gained experience, but I'm pretty sure it happens to me
even *more* now.

If John could code, and was just using another microcontroller and addressables, I wouldn't trust this thing as
far as I could throw it. But luckily, he can't. So he did the whole thing with *ton* of LM339 comparitors,
and I'll trust the hell out of those. [They came out in the 70s, so I'd grant them honorary 7400 series status as
far as chips go.] If that LED is on, I'd be as sure as I am of anything that the pin is high.

Another cool thing he did was to make the plastic header shrouds out of clear plastic with opaque separators
to act as a light pipe. So it's not like an LED next to a pin lighting up, **the pin itself** is. It's a weird
way to put it, but it kinda feels "immersive"?, like the pin lighting up is also what makes the signal go high.

And taking advantage of how cheap full color PCBs have gotten, along with the huge surface area of an Arduino UNO,
he actually puts the full pin reference on the board, like the one you'd find on the internet with the alternate
functions for all the pins and stuff. I have no idea why Arduino didn't do that originally, but then again,
the Unos' pin headers are misaligned by twentieth of an inch so what should we expect.



### 10:36 Manyfold (Paul #1)

[Manyfold](https://manyfold.app) is a self-hosted solution to organize and share your files for 3D
printing.  It's also connected to the Fediverse, allowing you to follow instances (aka server) or
creators.  You can run it in single-user mode or multi-user.  You can also make files public or private,
which is great for saving models you might have paid for but don't or can't share publicly.

* [Suported file formats](https://manyfold.app/manual/supported_formats.html) include 3MF, Blender,
FreeCAD, OpenSCAD, STEP, STL, OBJ, GCode, BMP, GIF, JPG, PNG, SVG, and even video files in MP4 or MPEG.
It also support Markdown, PDF, and text files.

* [Demo instance](https://try.manyfold.app)
* [Public instances](https://manyfold.app/instances.html)
* [GitHub repository](https://github.com/manyfold3d/manyfold)
* [FLOSS Weekly podcast episode with James Smith](https://hackaday.com/2024/10/23/floss-weekly-episode-806-manyfold-the-dopamine-of-open-source/)


### 13:52 Quake on a SparkFun Thing Plus Matter board (Tod #1)

[next-hack.com got Quake running on a Feather-sized board](https://next-hack.com/index.php/2024/09/22/quake-port-to-sparkfun-and-arduino-nano-matter-boards-using-only-276-kb-ram/)

We've all seen the "Doom ported to *insert tiny electronics here*". Those are all
good hacks. Doom's game engine isn't real 3D though, more like 2.5D:
the enemies are 2D sprites and level geometry is perturbations of a 2D plane.
But the game Quake, id software's follow-up effort, was real 3D:
fully-polygonal monsters and game world.
Real 3D can be tough, so I figured it'd be awhile before we saw a port of Quake to tiny microcontrollers.

And yet, the folks at nexxt-hack.com have Quake running on a SparkFun Thing Plus Matter board.
This board is in the Feather format (0.9" x 2") and sports a MGM240P wireless module
for doing Bluetooth and Matter wireless protocols. This module also sports a EFR32MG24 chip,
which is a 32-bit ARM Cortex-M33 processor at 39 MHz, 1.5MB flash and 256 kB of RAM.
(This is essentially the same specs as the new RP2350 from RasPi, so maybe we'll see Quake on an
Adafruit Feather soon?)

After proving the idea using the SparkFun board, they designed a complete Quake-playing
gamepad with built-in screen, joysticks, sound, and battery.
This time using the Arduino Nano Matter board (which has a similar MGM240-series module on it)
Oh also: you can do BLE-based multiplayer and it runs at 35 fps at 320 x 240.

This is so impressive since the original Doom required a 486 with 4 MB of RAM,
and they're doing it in 256 kB of RAM with a Blueooth stack!

You can download the schematic, board files, and bill-of-materials from their site if you want to build your own.

* [SparkFun Thing Plus Matter board](https://www.sparkfun.com/products/20270)
* [Writeup on the Silabs.com tech blog](https://community.silabs.com/s/share/a5UVm000000Vi1ZMAS/quake-ported-to-arduino-nano-matter-and-sparkfun-thing-plus-matter-boards?language=en_US)
* [Next-hack gamepad using Arduino Nano Matter board](https://next-hack.com/index.php/2024/09/21/the-gamepad-an-open-source-diy-handheld-gaming-console/)
* [Next-hack gamepad design files](https://github.com/next-hack/TheGamepadDesignFiles)


### 18:00 Evolvable Hardware (Kevin #2)

[Evolvable Hardware](https://evolvablehardware.org/history.html)

* Been around since 1990
* Developed at the University of Sussex by Adrian Thompson
* Used a XE6200 FPGA (100 gates - 10x10 FPGA)
* Project IceStorm is reverse engineering a modern FPGA


### 23:18 FlexiPi Kickstarter (Paul #2)

The FlexiPi is a new Raspberry Pi Pico with a few tricks up its sleeve.  First - it's flexible,
hence the name and wafer thin.  It also includes a few upgrades from the original Raspberry Pi Pico, including
using USB-C instead of Micro-USB and a programmable Neopixel built-in.  Otherwise, the pinout stays
the same as the popular Pico.

It currently has a [Kickstarter campaign](https://www.kickstarter.com/projects/top-diy/flexico-flexible-raspberry-pi-pico)
running through November 24th.  It also includes three digital books with it: Getting Started with a Raspberry Pi PIco,
and MicroPython and CircuitPython guides. They've already reached their funding goal, having raised about $7000.
Remember, it is a Kickstarter and backing the project doesn't always guarantee delivery.

**Update** Since recording, the FlexiPi Kickstarter project was suspended by Kickstarter and the reasons why are
unknown.  To stay updated on the project, [you can sign up for their newsletter here](http://bit.ly/4e5uFVL).

* [Tom's Hardware coverage](https://www.tomshardware.com/raspberry-pi/flexpi-kickstarter-promises-flexible-raspberry-pi-pico-with-a-few-upgrades?utm_source=pocket_shared)


### 25:11 EMMG MIDI Synth (Tod #2)

A hacker in our community, Johnathan Bisson / @bjonnh, created the
[EMMG Midi Synth](https://www.bjonnh.net/project/emmg_midi_synth_controller/) as
a teaching tool for a [Workshop on MIDI and music synthesis](https://github.com/bjonnh/2024_emmg_workshop_midi) at the
Pumping Station One hackerspace in Chicago

The workshop taught what MIDI is, from down at the signalling level to how it's used by performers.
The board each student got was custom-designed. It has 8 pots, 12 captouch pads, an OLED display and stereo audio out, 
all driven with a USB-C 16MB Pico clone. The workshop also talks about how GPIOs work and how capsense works. Looks 
like it was pretty great!

And the board has a secret mode: if you power it up with a switch held down, it's also a full synth
using the really interesting Pra32-u synth engine for Pico. It's four voice paraphonic with built in chorus and 
delay effects. It sounds realy nice.

But selfishly what brought this to my attention is Johnathan sent me one!
He based his design on a few of my experiments, my "pico-test-syth", "picoslidertoy", and "eight-by".

By having 8 pots instead of two, his board solves one of the ongoing problems I've been dealing with for 
"pico-test-synth": pots are terrible if you want to have them control multiple parameters. They're absolute controls, 
unlike rotary encoders. So you have to keep saving "pot position" state any time you change the set of parameter. 
I should've used rotary encoders or just went with more pots.

The designs for his board are all up on the project github, including a nice writeup of his development process and 
the OpenSCAD files for the custom knobs he made.

* [EMMG MIDI Synth homepage](https://www.bjonnh.net/project/emmg_midi_synth_controller/)
* [Workshop notes](https://github.com/bjonnh/2024_emmg_workshop_midi)
* [Workshop slides](https://bjonnh.github.io/2024_emmg_workshop_midi/presentation/#/)
* [Pra32-u synth engine](https://github.com/risgk/digital-synth-pra32-u)
* [pico-test-synth](https://github.com/todbot/pico_test_synth) – my test platform for playing with synths on a Pico
* [picoslidertoy](https://github.com/todbot/picoslidertoy)
* [eight_by](https://github.com/todbot/eight_by) – my yet-to-used take of adding 8-pots to a single analog in using 
analog mux chip
