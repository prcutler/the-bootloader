---
date: 2025-01-06
title: "Sunsets, Synths, and Pinball!"
linkTitle: "Episode 16 - January 6, 2025"
description: "Sunsets, Synths, and Pinball!"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Happy New Year! Tod and Paul are back, each with three things to share.  They discuss sunsetting a popular IDE, Tod's favorite synth (which does so much more), 3D printing, pinball, and more.

We're now on Bluesky!  [Follow us on Bluesky](https://bsky.app/profile/thebootloader.net) or [subscribe to our newsletter](https://buttondown.com/thebootloader).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/sunsets-synths-and-pinball/embed/dark"></iframe>

## Show Notes

### Sunsetting Mu (Paul #1)

Nicholas Tollervey and the developers of the [Mu code editor](https://codewith.mu) recently [shared that they will be sunsetting Mu](https://madewith.mu/mu/users/2024/12/10/retirement-plans.html). Mu has been around for over 9 years and is the first code editor for some people new to programming Python and MicroPython and CircuitPython.

The Mu team will have two releases in 2025. The first will be built with a few bug fixes and is considered a "legacy" release with libraries pinned to older versions so people using older hardware can still use Mu.  Soon after, the final versio of Mu will be released using the latest versions of libraries with the hope that Mu can live a few more years before becoming out of date.

The Mu team expects to have this done by the end of March, 2025.

### Synthstrom Deluge and its Community Firmware (Tod #1)

The [Synthstrom Deluge](https://synthstrom.com/product/deluge/) is a music making device mostly in the ["groovebox"](https://en.wikipedia.org/wiki/Groovebox) category, if you've heard that term. It's a small device, about the size of a sheet of paper and an inch thick. It's covered with a grid of 144 RGB button pads and a few knobs. It's a MIDI sequencer, a drum machine, a sampler, and a multi-track audio recorder. And it's got a built-in battery so you can use it anywhere. It's also got CV/gate output to control modular synths.  It's what I use as the hub (and often only device) when making music. The Deluge is made by a small team in New Zealand, coded by one guy it seems, but its quality and attention to detail puts it in the realm of professional gear.  I love it.

And then Synthstrom made me love them more. First, each year they'd release new Deluge firmware that added entirely new features, then they introduced an [OLED screen replacement upgrade](https://cdm.link/synthstrom-deluge-oled/) for the 7-segment display the Deluge originally had. And then they announced they released the [Deluge source code on github](https://github.com/SynthstromAudible/DelugeFirmware). And releasing it under a true open source license (GPL). AND creating a ["Synthstrom Community Fund"](https://www.patreon.com/c/Synthstrom) to financially assist anyone working on improving the firmware.

And boy did the community step up!  With a few months, the entire codebase was refactored, making it more usable in a large team. All while keeping the existing functionality. Within a few months more, the first official "Community Firmware" was released for the Deluge. It added UI and usability improvements but also added new features like new audio effects & filters, new sequencer modes, and entire new UI views that make it work like Ableton Live.

Now, every few months, new features are added, and you can try them at any point. It's all on github. Or, like me, wait for the official releases. Just a few days ago on December 25 2024, Community Firmware 1.3 was released. It adds DX7 synth emulation, a new "chord library", the ability to export a song as multiple WAVs (very useful for final production), and a whole bunch of other improvements.

It's like getting a new piece of music gear every few months, it's incredible.

### Home Assistant Voice (Preview Edition)

The team behind Home Assistant [has announced](https://newsletter.openhomefoundation.org/the-era-of-open-voice/) the [Home Assistant Voice (Preview Edition)](https://www.home-assistant.io/voice-pe/).
* [Blog post](https://www.home-assistant.io/blog/2024/12/19/voice-chapter-8-assist-in-the-home/#language-support)

* Home Assistant Voice supports over 25 languages
* LLM support both local and in the cloud with Google, OpenAI, Anthropic, and more
* Wake word support (Hey Nabu, Hey Jarvis, Hey Mycroft)
* $59

### Elliot William's Klangorium: Logic chips as synths (Tod #2)

A few days before Christmas 2024, I attended a workshop hosted by the Hackaday Supplyframe DesignLab called
[The Sound of Logic: Klangorium](https://hackaday.io/project/196424-the-sound-of-logic-klangorium).
Taught by Richard Hogben (who does the music for the Hackaday Supercons), the workshop was about the "Klangorium" board that [Elliot Williams has been working on since 2015](https://github.com/hexagon5un/klangorium/) and has been the topic of a [series of Hackaday articles](https://hackaday.com/tag/logic-noise/).

This board is a kind of modular synth, but where the modules are various CMOS logic chips configured in weird ways: a 40106 hex inverter becomes a 6-voice oscillator, a 4051 shift register becomes a sequencer, and so on. Because everything is square waves, a "mixer" can an OR-gate.  The board has header pins on the various sections, so you "patch" the synth together with jumper wires as if you're breadboarding a circuit.

links:
- [original klangorium github project](https://github.com/hexagon5un/klangorium)
- [updated repo used in the workshop](https://github.com/wero1414/klangorium)
- [hackaday.io project](https://hackaday.io/project/6540-logic-noise-klangorium)
- [matrixsynth article with deep dive](https://www.matrixsynth.com/2019/06/logic-noise-klangorium-diy-glitch-synth.html)

### Fun with 3D Printing (Paul #3)

A few short stories that might you might have missed:

* A [4D axis printer](https://www.youtube.com/watch?v=VEgwnhLHy3g), where the nozzle can rotate.
* MobiPrint, a mobile 3D printer, without a bed.  [Hackaday](https://hackaday.com/2024/12/10/3d-printer-eliminates-the-printer-bed/) [YouTube](https://www.youtube.com/watch?v=SknW-Oygh3w)
* Make a [working PCB](https://www.youtube.com/watch?v=lX7dRaOLtZk) using a SLA printer's UV light.
* The Lemontron 3D printer costs just over $400 to make yourself and is small enough to transport in an empty filament box. [Hackaday](https://hackaday.com/2024/12/26/open-source-lemontron-3d-printer-is-ready-to-build/) and [Tom's Hardware])https://www.tomshardware.com/3d-printing/lemontron-an-open-source-fully-portable-3d-printer-has-arrived-can-be-transported-in-an-empty-filament-box)
* [PolyDye](https://www.level9000.co.za/index.html) adds an ink jet toner cartridge to your 3D printer to allow printing in color. [https://hackaday.com/2024/12/28/full-color-3d-printing-with-polydye-and-existing-inkjet-cartridges/](Hackaday)
* [PETFusion 2.0](https://www.tomshardware.com/3d-printing/all-in-one-machine-recycles-plastic-bottles-into-3d-printer-filament-petfusion-2-0-launches-on-kickstarter) launched a [Kickstarter](https://www.tomshardware.com/3d-printing/all-in-one-machine-recycles-plastic-bottles-into-3d-printer-filament-petfusion-2-0-launches-on-kickstarter) that fully funded in 3 hours to create a bottle recycler and custom 3D printer filament maker. It includes the STL files and bill of materials you need to build your own.  STLs start at $39 up to $109 for a commercial license version.

### Pinball!!! (Tod #3)

I love [pinball](https://pinside.com/pinball/top-100). I grew up with mall arcades with pinball machines. They usually were kinda broken and were definitely old-timey compared to video games. But in college, whoever ran the laundry room in the dorm basement was smart and had room for a couple of coin-op video games and one pinball. This pinball machine was always in good shape. And if you're a college kid with some leftover quarters and waiting on his laundry, what are you doing to do?

I got so good at that pinball machine.

From then on, whenever I'd come across a pinball game, I'd play it. But these games are like puzzles: spending more time with them unlocks more fun. That takes time and gets expensive. So I mostly didn't play much. And then [ZenStudios](https://zenstudios.com/games/) came along with a really solid pinball physics simulation engine and licenses to many classic Williams games like ["Theatre of Magic"](https://pinside.com/pinball/machine/theatre-of-magic/gallery), ["Attack from Mars"](https://pinside.com/pinball/machine/attack-from-mars/gallery), and my laundry room game [High Speed](https://pinside.com/pinball/machine/high-speed/gallery). They have apps for mobile & tablet, so I play them a lot. I have gotten really good at a few of them.

This is all background for "what I did during Christmas vacation": While visiting family up in the Bay Area, I was fortunate enough to visit the [Pacific Pinball Museum in Alameda](https://www.pacificpinball.org/). It takes its non-profit charter seriously, having wall text explaining why each of its 100+ machines they have on display is important, and keeping the machines in great shape. And they have the classics! Including High Speed and Theatre of Magic. I got to play both. And I sucked at them. The Zen simulator games present a "perfect" machine for you: everything works as if it was brand new. There's no slight wear on this part of the table, that flipper isn't a little weak on the second hit, etc. In pinball, each machine is unique and ever-changing, and I'd forgotten that.  So I've decided to visit more real pinball places.

In Pasadena not too far from me there's [Neon Retro Arcade](http://www.neonretroarcade.com/)
And according to [PinballMap.com](https://pinballmap.com/), in Minneapolis there's 47 pinball machines at [Litt Pinball Bar](https://littpinballbar.com/)!  (btw, pinballmap.com is great)

[Find machines near you with Pinballmap.com](https://pinballmap.com/)
