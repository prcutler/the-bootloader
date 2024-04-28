---
date: 2024-04-29
title: "Episode 8: Built from the ground up"
linkTitle: "Episode 8"
description: "Built from the ground up"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
## Welcome
Welcome to The Bootloader.  

[Full transcript available here](https://thebootloader.net/blog/2024/04/29/episode-8-transcript/).

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/built-from-the-ground-up/embed/dark"></iframe>
# Show Notes

## Episode Intro

Welcome!  

## Meet the Maker: Carrie Sundra of Alpenglow Industries (Paul #1)

If you visit the About page on Alpenglow Industries’ website, Alpenglow mission statement is to  ***To Teach You About Electronics Without Gatekeeping***.  It goes on to say:

*We are passionate about representation in electronics - the field is still overwhelmingly white and male with only ~[10% of electrical engineers identifying as women](https://www.zippia.com/electrical-engineer-jobs/demographics/)~.  Having worked in the field for over 20 years, we know how much gatekeeping and hostility there can be.  We aim to provide a welcoming space where adults can learn about electronics without judgment or any previous experience.*

Homepage:  https://www.alpenglowindustries.com
[Through-Hole Soldering Kits](https://www.alpenglowindustries.com/collections/through-hole-soldering-kits)
Surface mount soldering kits: [SMT Soldering Kits](https://www.alpenglowindustries.com/collections/smt-soldering-kits)
YouTube channel:  [Alpenglow Industries](https://www.youtube.com/alpenglowindustries)

## SynthUX Academy and Daisy Seed (Tod #1)

Have you ever wanted to learn to make *real* high-quality synthesizers, 
not just the low-fi toys I've been goofing around with in CircuitPython or Arduino w/ Mozzi? 

Then you should know about Daisy Seed from ElectroSmith : https://electro-smith.com/

Daisy Seed is a little $25 Arduino-looking board that is designed explicitly for 
audio manipulation and generation.  It's becoming a core component of many 
musical instruments from guitar pedals, to Eurorack modules, to stand-alone
synthesizer keyboards.  

The Daisy Seed board features a Cortex M7-class chip with 65 MB of RAM, stereo
audio I/O at 24-bit @ 96 kHz, twelve 16-bit ADC pins and two 12-bit DACs
for controls, and 31 GPIOs.  And it fits on a breadboard!

It's got a well-done Arduino library, a C++ DSP library, and you can even
run Pd and Max patches on it. ElectroSmith libraries provide all the 
components you need to make a synth: oscillators, envelopes, filters, sequencers,
delays, reverbs, etc. And [some good docs too](https://github.com/electro-smith/DaisyWiki/wiki)!

I've been wanting "level up" my knowledge of Daisy Seed, but I need a push. 
And that push has been the [SynthUX Academy](https://www.synthux.academy/).
They're a non-profit based in the Netherlands that offers in-person and 
online [classes](https://learn.synthux.academy/) for how to make synthesizers. 
Many of their classes are available for [free on Youtube](https://www.youtube.com/@SynthuxAcademy) 
and their [class code is on github](https://github.com/Synthux-Academy). 


## The Microdot web framework (Paul #2)

The Microdot web framework was created by Miguel Grinberg, who wrote the Flask Mega Tutorial - Flask being a popular Python web framework.  Microdot’s home page describes it as *“The impossibly small web framework for Python and MicroPython”* and is inspired by Flask. What’s interesting is that it can run on both CPython as well as a microcontroller running MicroPython.

Microdot project page: https://github.com/miguelgrinberg/microdot
[Microdot documentation](https://microdot.readthedocs.io/en/latest/)
The Flask Mega-Tutorial:  [The Flask Mega-Tutorial, Part I: Hello, World!](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
MicroPython awesome-list for web servers: [Awesome MicroPython](https://awesome-micropython.com/#web)

## ARM Assembly Deep-dives by Carlynorama (Tod #2)

What's lower-level programming than CircuitPython?  Arduino maybe? 
Lower-level than that? Probably C code calling a C vendor SDK. 
Now what's lower than even that?  C code manipulating a chip's I/O directly, 
I'd say. And the lowest level? [Assembly language](https://en.wikipedia.org/wiki/Assembly_language).

[Carlynorama](https://www.whynotestflight.com/) has been doing a deep-dive on 
ARM assembly language lately.  (disclosure: she's my wife)

She started with 
[an ATtiny45 in bare AVR C](https://www.whynotestflight.com/excuses/hello-led-on-an-avr-attiny45-in-c/)
to set up the chip and blink an LED.  She's really familar with AVR from the original Arduino,
so it was a natural jumping off point.  On AVR, doing bare C to twiddle chip registers
is very close to assembly language, since much of the work is figuring out which
registers to twiddle to make something happen. Besides her real target was ARM chips.

For the SAMD21 ARM chips like what's in the QT Py M0 or Trinket M0, she decided to start 
with assembly, in order to really understand how these chips work compared to AVR.
The Cortex-M0+ ARM chips are more complicated than AVR, and the ARM instruction set is huge. 
But (confusingly) the Cortex-M0+ core in these chips only get a subset of the ARM instructions,
making all the documentation about "ARM assembly" frustrating to read until you know 
which instructions are allowed for your chip.

But in about a week she's gone from knowing no ARM assembly to 
[getting an M0 chip up and blinking an LED](https://www.whynotestflight.com/excuses/its-alive-samd21e18a-assembly-no-sdk/), 
[reading a button input](https://www.whynotestflight.com/excuses/and-now-for-3-ways-to-set-an-internal-pullup/), 
and being able to monitor it all via [GDB](https://sourceware.org/gdb/).
Along the way she's been using
[online ARM simulators](https://cpulator.01xz.net/?sys=arm-de1soc) 
and teasing how STM32 ARM chip setup differs from SAMD21 setup.

I've been watching from the sidelines, learning a little along the way, following her blog. 
And it's been fascinating. You can really see how enormously powerful these chips are
when you're down at the lowest level like this.  It makes you appreciate all the work
that's going on when you say `pinMode(pin, INPUT_PULLUP)` or `button = DigitalInOut(board.GP14)`.

Her next steps I think are moving to some bigger ARM chips and to try out the 
[Clang/LLVM](https://clang.llvm.org/) compiler system instead of the 
[GCC-based tools](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) she's currently using. 

## One Year With the Bambu Labs P1P (Paul #3)

Paul shares his experience after owning a the Bambu Labs P1P 3D printer.

The Bootloader Episode 1: [Episode 1: Rock Stars are Just Like Us](https://thebootloader.net/blog/2022/09/26/episode-1-rock-stars-are-just-like-us/)
[Bambu Lab P1 Series | Reliable Out-of-the-Box Performance](https://bambulab.com/en-us/p1?product=p1p)
[P1 Series](https://wiki.bambulab.com/en/p1)
Bambu extends software and bug fix support until 2027 and 2029 respectively in a [turnaround](https://www.tomshardware.com/3d-printing/bambu-lab-printer-firmware-updates-have-limited-timeline) [Reddit thread](https://www.reddit.com/r/BambuLab/comments/1cco9v0/bambu_have_massively_extended_the_software_update/)


##  Let's talk about Capacitive Touch Sensors and Sliders (Tod #3)

I have been experimenting with capacitive touch sensors for a while now. 
They can be a really fun and easy sensor to add to your project and require 
almost zero extra components if you have something like CircuitPython's `touchio` 
library to help out. 

Captouch sensors work by treating the touch pad as a capacitor that the microcontroller
charges up (by setting the pad's pin HIGH) and then seeing how long that capacitor
takes to discharge and go LOW. When you put your finger on the pad, the capacitance
increases and it takes longer to discharge.  By watching for that change you 
tell "touched" from "untouched".

My latest fascination has been with capacitive touch sliders, either linear or rotary.
The rotary slider is like what the iPod had for many years: slide your finger
around it like you're spinning a little record. 

How do these work? There's a couple of different ways but the method that I've 
been trying out lately is the "interpolation" technique. This is where you
use two or more interleaved pads and measure the comparative touch amounts 
between them to interpolate a position along them. Imagine splaying your fingers
on each and and interleaving them: as you go from left hand to right hand, it's 
100% your left hand, then 75% your left hand, then 50/50 both hands, then 75% your
right hand, and finally 100% your right hand.

I've got a few projects that have touch pads laid out like this if you'd 
like to play yourself:

- https://github.com/todbot/touchwheels
- https://github.com/todbot/picoslidertoy
- [Tod's Tindie Store](https://www.tindie.com/stores/todbot/)

At the bottom of the "touchwheels" page are some useful links to the
capsense design guidelines I've been heeding like this one: 
[AN2934 - Capacitive Touch Sensor Design Guide (PDF)](https://ww1.microchip.com/downloads/en/Appnotes/Capacitive-Touch-Sensor-Design-Guide-DS00002934-B.pdf)


### Support The Bootloader

If you like what you hear, one of the best things you can do to help the show is tell a friend or write a review.

