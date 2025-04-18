---
date: 2024-09-02
title: "From Arcade to Synth"
linkTitle: "Episode 12 - September 2, 2024"
description: "From Arcade to Synth"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Welcome to a new episode!  Paul and Tod recap the recent CircuitPython Day, chat about a new synth Kickstarter, arcades, a bug in the Raspberry Pi 2350, and Bambu Lab gets sued.

## Join our new newsletter

We've started a new newsletter.  Get behind the scenes info about the podcast, links we liked but didn't make it into the show, and learn what we're up to.  [Sign up](https://buttondown.com/thebootloader) or [view the archives](https://buttondown.com/thebootloader/archive/) and subscribe via RSS.  Each newsletter is spam and tracking free and is emailed out a couple days after a new episode.

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/from-arcade-to-synth/embed/dark"></iframe>

### Small CircuitPythonDay2024 recap

Thank you to everyone who listened to our first live episode on CircuitPython Day. You can stream it on the [Adafruit YouTube channel](https://www.youtube.com/live/uTl1KA2MPxI). Paul and Tod recap the live episode including a look back at the last year and some of the projects they worked on.


## Show Notes

### 3:00 MICRORACK: solderless breadboard modular synth parts (Tod #1)

I recall seeing some noise about [MICRORACK during Superbooth](https://www.youtube.com/watch?v=Ixls7PbfC88)
a few months ago, and lately I've been inundated by Instagram ads for its
Kickstarter campaign.

["MICRORACK"](https://www.kickstarter.com/projects/microrack/microrack-affordable-and-compact-modular-synthesizer) is a collection of fully-assembled PCB modules that plug into a solderless breadboard. These modules comprise the same parts in modular synth setups: oscillators, filters, envelope generators, LFOs, sequencers, etc., but Microrack modules are small, cheap, and hackable. They're just exposed PCBs, using the solderless breadboard as a mounting plate and for power distribution.

While I'm a big fan of Eurorack modular synths, I have a hard time recommending it to newcomers because it's so expensive to get even a basic sound. This could bridge that gap. Microrack looks to be compatible with Eurorack and by its nature, it's compatible with the kind of random breadboard-based music hacking I do in Arduino and CircuitPython.

And you don't need Microrack to do modular synth stuff on a breadboard. I do it all the time, but it's kind of annoying: interfacing to other gear is flaky, jacks & knobs aren't breadboard-friendly, input & output level conversion is tricky, etc. Over the years there have been various attempts to make this easier. I've linked a few in the show notes.

Microrack links:
* [MICRORACK Kickstarter](https://www.kickstarter.com/projects/microrack/microrack-affordable-and-compact-modular-synthesizer)
* [MICRORACK demo videos](https://www.youtube.com/watch?v=ivEz-3fFn0E&list=PLLej0pNV9kNhAPo4oWYCVr5jbwbFUBKQZ)
* [Sonicstate interview w/ MICRORACK at Superbooth](https://www.youtube.com/watch?v=Ixls7PbfC88)

Similar past projects:
* [Breadboard Friends by Mutable Instrument's Émilie Gillet](https://pichenettes.github.io/mutable-instruments-diy-archive/bbf/)
* [EricaSynths EDU DIY LABOR](https://www.ericasynths.lv/shop/diy-kits-1/edu-diy-labor/)
* [Korg littleBits Synth Kit](https://www.soundonsound.com/reviews/korg-littlebits)


### 8:16 Pimoroni's Picade Max Arcade (Paul #1)
Paul has been talking about building a standup arcade for years.  Pimoroni just launched the [Picade Max](https://shop.pimoroni.com/products/picade-max?variant=42007494623315), a bar top arcade you assemble yourself for £495 or about $650.  It works with the Raspberry Pi and includes a 4:3 19" screen with HDMI driver board.  It includes everything you need to get started, minus the Pi, such as joysticks, buttons, and speakers.  The Picade Max Control Board is the interface to the Raspberry Pi 5 and is itself powered by an rp2040 and works just like a normal gamepad / keyboard.  The sound is also powered by an rp2040, the Picade Max Audio Board, that acts as a USB soundcard with 3 watts of power and a rotary encoder on the rear to control the volume.  It's powered by the Power HAT for the Raspberry Pi.

 * [Paradise Arcade Shop](https://paradisearcadeshop.com/)
 * [Picade Max at Pimoroni](https://shop.pimoroni.com/products/picade-max?variant=42007494623315)
 * [Tom's Hardware coverage](https://www.tomshardware.com/raspberry-pi/raspberry-pi-powered-picade-max-brings-two-player-retro-gaming-to-pimoronis-picade-family) and [review](https://www.tomshardware.com/raspberry-pi/picade-max-review)
 * [Tom's Hardware Pi Cast](https://www.youtube.com/live/VddDblPom6c?si=f5A54m1Vxkfj_HJF) with guests Paul Beech and Phil Howard of Pimoroni


 ### 13:17 Pico2 / RP2350 GPIO Input issue (Tod #2)

To start: I would not recommend using the Pico2 or other RP2350-based boards for new users. There's some weirdness going on in the silicon of the new RP2350 chip that makes inputs sometimes not return the correct logic value. Instead, an input may get stuck HIGH with no easy way to recover.

I found this out because the way `touchio` works in CircuitPython: it takes a GPIO pin, turns it to an output and sets it HIGH, then it turns that pin to an input and waits for it to go LOW.  The time that takes is an indication of if that pin was touched.  I filed a CircuitPython bug, discovered there was an "RP2350-E9" errata in the chip that seemed to only cover the case when using the internal pull-down resistors, but which also seemed to be affecting us. I couldn't find a way around it after hacking a few hours in the CircuitPython internals for `digitalio`.  Then [Dan Halbert looked into it](https://github.com/orgs/micropython/discussions/15621#discussioncomment-10446747) and filed a bug both with Micropython and with Raspbery Pi. This then was confirmed by Philip Howard at Pimoroni and Ian at Dangerous Prototypes (maker of Bus Pirate).

Thankfully [Hackster wrote up an article](https://www.hackster.io/news/a-surprise-hardware-bug-in-raspberry-pi-s-rp2350-leads-to-unexpected-pull-down-behavior-76b51ec22ede) about it, but I think it downplays the issue a little.  I don't see how this can be fixed in software and will limit the kinds of circuits we can use the RP2350 with.

From what I can tell the following uses will not work:
- Certain ways of wiring button inputs
- Capacitive touch sensing
- Bit-banging open-collector protocols like I2C

Links:
* [My original `touchio` CircuitPython issue](https://github.com/adafruit/circuitpython/issues/9541)
* [MicroPython issue filed by DanH](https://github.com/micropython/micropython/issues/15718)
* [pico-feedback issue filed by DanH](https://github.com/raspberrypi/pico-feedback/issues/401)
* [Bus Pirate Mastodon post referencing it](https://mastodon.social/@buspirate/112932355552638918)
* [Hackster article about RP2350 GPIO issue](https://www.hackster.io/news/a-surprise-hardware-bug-in-raspberry-pi-s-rp2350-leads-to-unexpected-pull-down-behavior-76b51ec22ede)

### 18:36 Stratasys sues Bambu Lab over 3D printing patents. (Paul #2)
Stratasys, an early pioneer in 3D printing who also acquired MakerBot in 2013, has [sued Bambu Lab](https://arstechnica.com/gadgets/2024/08/stratasys-sues-bambu-lab-over-patents-used-widely-by-consumer-3d-printers/). The lawsuit focuses on PEI-coated build plates, purge towers, and automatic bed leveling.  These features are common across multiple 3D printer brands, so why sue Bambu Lab?
* [Tom's Hardware - Is Bambu being targeted for being successful?](https://www.tomshardware.com/3d-printing/weve-always-respected-intellectual-property-bambu-lab-responds-to-3d-printer-patent-lawsuit)
* [Adafruit coverage including suggesting a prior art database](https://blog.adafruit.com/2024/08/13/is-stratasys-a-3d-printing-patent-troll-stratasys-v-bambu-lab/)
