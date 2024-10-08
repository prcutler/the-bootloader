---
date: 2024-08-05
title: "Teardown 2024 with Debra Ansell"
linkTitle: "Episode 11 - August 5, 2024"
description: "Teardown 2024 with Debra Ansell"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/teardown-2024-with-debra-ansell/embed/dark"></iframe>

## Welcome to the show

### 00:28 Teardown 2024 recap with Debra Ansell aka geekmomprojects

Debra attended Teardown 2024 hosted by Crowd Supply in Portland, Oregon, June 21 - 23, 2024.  Debra shares highlights from the conference and what made it special.
* Find Debra on [Mastodon](https://mastodon.social/@geekmomprojects) and [Instagram](https://www.instagram.com/geekmomprojects/).
* [Building Up Excitement for Teardown 2024](https://makezine.com/article/maker-news/building-up-excitement-for-teardown-2024/)
* [Teardown 2024](https://www.crowdsupply.com/teardown/portland-2024)
* Makers mentioned by Debra:
    * [Jason Coon](https://www.evilgeniuslabs.org/)
    * [Charlyn Gonda](https://dev.to/charlyn)
    * [Ben Hencke](https://www.bhencke.com/)
    * [Joey Castillo](https://www.oddlyspecificobjects.com/)
    * [Carrie Sundra](https://www.alpenglowindustries.com/)

![Debra's LED Jacket installation at Teardown 2024](geekmomprojects-led-jackets.jpg)
Pictured: Debra Ansell (left) and Alie Gonzalez (right) display Debra's LED jacket installation at Teardown 2024.

### 14:17 Tulip Creative Computer and Amy synth library (Tod #1)

Okay another DIY synth thing. I'm a big fan of synth libraries for microcontrollers. My favorites
are [Mozzi for Arduino](https://github.com/todbot/mozzi_experiments) and [CircuitPython's `synthio`](https://github.com/todbot/circuitpython-synthio-tricks),
but I've also use [Teensy Audio Library](https://www.pjrc.com/teensy/td_libs_Audio.html), [Daisy](https://github.com/electro-smith/DaisyWiki/wiki), and others.
All have the startup issue of "how do I get things wired up to make sound?" and then they require a good amount of programming & synthesis knowledge too.

The Tulip Creative Computer project tries to solve these problems, and many others. I've been following Tulip and it's gotten really interesting. Tulip is an ESP32-based device you can buy right now for $60, which includes a 7" touchscreen, high-quality audio DAC, MIDI I/O, and a battery.
It runs a custom version of MicroPython and is made to have a USB keyboard plugged right into it so you can code on it directly, no computer needed!

As you code it in MicroPython, it can be like a live-coding music environment,
sort of like [SonicPi](https://sonic-pi.net/), but without the hassle of getting a Rasperry Pi running. Tulip boots up instantly.

Oh and did I say it's a device? It's also a fully-open source project you can build
yourself from an ESP32-S3 and touchscreen and the Tulip designers provide multiple guides depending on what hardware you have.

And to get back to synth libraries, Tulip uses the AMY synth library,
which has bindings to both Arduino and Python. It's a fascinating take on a synth library, going in a more high-level direction than Mozzi and synthio and is extremely cross-platform.

I have a Tulip coming my way in the next week.

* [Tulip homepage](https://github.com/shorepine/tulipcc)
* [Build your own Tulip](https://github.com/shorepine/tulipcc/blob/main/docs/tulip_build.md)
* [Floyd Steinberg's video on Tulip](https://www.youtube.com/watch?v=1lYFjQp7Xrw)
* [AMY - Additive Music librarY](https://github.com/shorepine/amy)


### 18:27 More new IDEs - ViperIDE and Zed (Paul #1)

#### ViperIDE

Continuing my review of various IDEs, [ViperIDE](https://viper-ide.org/) is a brand new IDE in a web browser focused on MicroPython, with CircuitPython support created by Volodymyr Shymanskyy.  You can connect a board in a variety of ways including USB, Bluetooth, and you can use `WebREPL` to connect over the local network or even the internet.  It's a true IDE in a web browser with advanced features including syntax highlighting, auto expanding and minify of JSON, a terminal, and MicroPython package support.  It also features a full [MicroPython emulator](https://viper-ide.org/?vm=1) with an example and it uses MicroPython compiled to Web Assembly.
* [ViperIDE](https://viper-ide.org/?vm=1)
* [Zed GitHub repository](https://github.com/vshymanskyy/ViperIDE)
* [Review from Les Pounder](https://www.tomshardware.com/raspberry-pi/raspberry-pi-pico/how-to-write-code-for-your-raspberry-pi-pico-in-your-web-browser-with-viperide) at Tom's Hardware
* [Live demo with Volodymyr Shymanskyy](https://www.tomshardware.com/raspberry-pi/raspberry-pi-pico/how-to-write-code-for-your-raspberry-pi-pico-in-your-web-browser-with-viperide) on Tom's Hardware Pi Cast

#### Zed

Zed is a fairly new code editor and IDE for macOS and Linux users who might miss Atom or Sublime Text.  It's open source, released under the Apache and GPL 3.0 licenses, and focused on speed and collaboration.

* [Zed homepage](https://zed.dev/)
* [GitHub repository](https://github.com/zed-industries/zed)
* [pyright static type checker for Python](https://github.com/microsoft/pyright)


### 23:03 CeraMetal: 3D Printing Metal with Bronze Clay (Tod #2)

I was happy to see my friend Leah Buechley mentioned on Hackaday recently.
Leah is a professor at University New Mexico and for the last few years has
been applying CNC and advanced mathematical techniques to ceramics and clay, creating shapes with overhangs and angles that I wouldn't think possible
in clay, let alone 3d printer plastic.
They use commercially-available clay 3d printers with some special tricks.

(If her name is familar, she is also creator of the Lilypad Arduino sewable electronics system about 15 years ago, the echos of which we see in the CircuitPlayground Express boards from Adafruit)

Her team's newest project is called "CeraMetal", a way of 3d printing metal on the desktop using a custom metal clay. Once it's printed, it's fired in a kiln and sintered into a solid metal part.  The custom metal clay is made from metal powder, xanthum gum and a few other ingredients, mixed together.

To slice the model to be printed, standard slicers like Cura can't be used.
Once the CeraMetal clay starts extrusion, it just keeps coming out.
Normal slicers stop extrusion and do travel moves. So they had to write their own slicer to support this continuous extrusion aspect of the material.

The print resolution is close to standard PLA printing: 0.6mm nozzle, 0.3mm layer height.  The costs are around $2k, for printer and kiln, compared to the $50k-$130k for a Selective Laser Sintering (SLS) machine.

And as an aside, they mention the algorithm used to get equal area spacing in their slicer is Fermat Spirals. These are space-filling curves that have the property that the area between its lines are equal. Perfect for 3d printing. I love spiral algorithms and so I've been looking into these. Links in the show notes of a few Fermat Spiral toys.

* [CeraMetal: A New Approach to Low-Cost Metal 3D Printing with Bronze Clay" -- Leah Buechley, Jaime Gould, Fiona Bell](https://handandmachine.org/index.php/2023/10/30/cerametal-metal-3d-printing/)
* [CeraMetal talk on ACM SIGCHI](https://www.youtube.com/watch?v=0FEgQUjrrwg)
* [Hackaday blog post on CeraMetal](https://hackaday.com/2024/07/21/cerametal-lets-you-print-metal-cheaply-and-easily/)
* [Fermat's Natural Spirals](https://www.sciencenews.org/article/fermats-natural-spirals)
* ["Fermat Spirals for Layered 3D Printing" on Two Minute Papers](https://www.youtube.com/watch?v=6rNcAVr-U4s)
* [Fun Fermat Spiral toy in Processing](https://flyingpudding.com/projects/florets/applet)


### 27:08 CircuitMatter (Paul #2)

Matter is an open source standard managed by the Connectivity Standards Alliance for IoT devices. It requires a Matter controller such as some Google Nest devices, Apple Homepod or AppleTV, or some Amazon Echo devices.  For example, you can buy a Matter-supported smart bulb and set it up with Apple HomeKit, Google Assistant, or Amazon Alexa—without having to worry about compatibility.

Scott Shawcroft, CircuitPython's lead developer, [shared he is working](https://www.adafruitdaily.com/2024/07/22/python-on-microcontrollers-newsletter-python-was-at-risk-rp2040-chiplets-being-sold-and-much-more-circuitpython-python-MicroPython-thepsf-raspberry_pi/) on `CircuitMatter`, a pure Python implementation of some of the Matter specification that will be compatible with CircuitPython and potentially MicroPython.

* [What is Matter?](https://www.wired.com/story/what-is-matter/) - Wired Magazine
* [Matter and Home Assistant](https://www.home-assistant.io/blog/2024/01/25/matter-livestream-blog/)
* [Sparkfun Thing Plus Matter](https://www.sparkfun.com/products/20270) dev board

### 29:47 Special Announcement about CircuitPython Day 2024
Tune in to the [Adafruit YouTube channel](https://www.youtube.com/adafruit/live) on CircuitPython Day, August 16th for a special live stream of The Bootloader with Paul and Tod. Keep an eye on the [Adafruit Blog](https://blog.adafruit.com) for the schedule and see you there!
