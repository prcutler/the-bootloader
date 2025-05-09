---
date: 2025-04-07
title: "Welcome Andy Piper"
linkTitle: "Episode 19 - April 7, 2025"
description: "Welcome Andy Piper"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Tod and Paul welcome a special guest, Andy Piper.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/welcome-andy-piper/embed/dark"></iframe>

## Show Notes

### Glance (Andy #1)

Maybe it's just me (and I am a techie, and interested in playing with new things), but it seems to me right now that a lot more people are starting to tinker with running their own home labs - usually clustered and containerised virtual machines for hosting web apps on their own hardware and home network.

I learned Linux "back in the day" 20 years ago by running my own server at home, but over time I migrated most things to the cloud. Now, I'm using Proxmox on a mini PC to run a number of different containerised apps, complemented by various other services running on the odd Raspberry Pi or on my NAS.

My pick isn't a home lab or Proxmox specifically, but it is a really nice piece of software you can self-host, to quickly create a customised dashboard for... well, whatever you want, really. The app is called Glance and you can find it on GitHub at glanceapp. I learned about it within the past few weeks as it got mentioned on sites like Hacker News and Lobste.rs, and got a bunch of new attention.

Glance is a simple web app that you configure via a text file which is in the YAML format. It has a number of built-in and community contributed widgets that enable you to quickly build dashboards containing everything from the weather, news from different sites and RSS feeds, video channels, now playing information, system data like Tailscale or dynamic DNS status, the status of your favorite Minecraft server, and trending links on Mastodon or Bluesky.

It's also fully and easily themeable, and works great on mobile screens as well as on desktop. I know there are some other alternatives to this, but it is working great for me and it has been really nice to see new contributors supporting the project and the author in the past few weeks.

Links:
- [main project](https://github.com/glanceapp/glance)
- [community widgets](https://github.com/glanceapp/community-widgets)
- [setup script for Proxmox VE](https://community-scripts.github.io/ProxmoxVE/scripts?id=glance)
- [note from the maintainer](https://github.com/glanceapp/glance/issues/464)

### SoundFonts, General MIDI and $50 MIDI "ROMpler" (Tod #1)

We all know what MIDI is: a serial data protocol for transmitting musical performance
information.  Basically, digital sheet music. But worse than most sheet music, as MIDI
doesn't contain anyting describing what the notes should *sound* like.
It's just "play a G# on channel 1". A G# on what, a piano? a guitar? a timbale?

So in the 1990s, the [General MIDI](https://en.wikipedia.org/wiki/General_MIDI)
standard was created. Instruments that implementing it would always play a
"electic piano" sound when sent the "Program Change #2" message, an "Acoustic Bass"
sound when sent "Program Change #33", and "Seashore Effect" for Program Change #123.

But now we have another problem. Which electric piano? Which acoustic bass?
What the heck is "seashore effect"?
Different MIDI synths had different recreations for all these.
Some were really good, some sucked!  Around the same time, new PC sound
cards that implemented General MIDI also let you load "SoundFonts".
SoundFonts are sound sets of General MIDI sounds, all in a single file.
And [many many SoundFonts](https://musical-artifacts.com/artifacts?formats=sf2&tags=soundfont)
have been created over the years.  Soundfont sounds are sample-based,
and usable by modern instruments.  Some SoundFonts are special
purpose, like the [Salamander Grand Piano](https://sfzinstruments.github.io/pianos/salamander/),
a huge 1.2 GB multisampled Yamaha Grand Piano sound, under a Creative Commons license.

Okay now to the part I'm really interested in.  There's an open source
software synthesizer for Linux/MacOS/Windows called [FluidSynth](https://www.fluidsynth.org/)
that works really well and uses SoundFonts. It has APIs in C, Python,
Ruby, .Net and other langages.

Recently on the [Floyd Steinberg's Youtube channel](https://www.youtube.com/@mr_floydst)
he demoed a ["$50 Mini ROMpler"](https://www.youtube.com/watch?v=2HWTC6XzUw8)
made from a Rasperry Pi Zero and an Pimoroni I2S DAC Hat,
running a small Python script he wrote that responds to MIDI, talks to FluidSynth,
and provides a UI via the buttons and screen on the Pirate Audio I2S Hat.
The result is a little box smaller than a deck of cards that sounds as good
or better as sample-based synths costing thousands of dollars.

I built one recently and while Floyd's app works, it's early days.
I'm starting to modify it to work more like what I want.
It's a great excuse to exercise my Python skills somewhere other than CircuitPython.

And since SoundFonts are effectively just bundles of WAV file samples, I've been
experimenting with the [`sf2extract`](https://manpages.ubuntu.com/manpages/jammy/man1/sf2extract.1.html)
to pull those WAV files out and use them inside of CircuitPython. I'm not sure
if we can ever get a CircuitPython SoundFont General MIDI player, but we might!

Links:
- [History of MIDI](https://www.musicradar.com/news/tech/30-years-of-midi-a-brief-history-568009)
- [FluidSynth](https://www.fluidsynth.org/)
- [sf2extract commandline tool](https://manpages.ubuntu.com/manpages/jammy/man1/sf2extract.1.html)
- [List of free soundfonts](https://musical-artifacts.com/artifacts?formats=sf2&tags=soundfont)
- [Huge free multisampled grand piano soundfont](https://sfzinstruments.github.io/pianos/salamander/)
- [Floyd Steinberg's video on $50 mini ROMpler](https://www.youtube.com/watch?v=2HWTC6XzUw8)
- [Floyd's app (in Python!)](https://github.com/mrfloydst/midifileplayer/)

### OpenSpool and SpoolEase - NFC Filament Readers (Paul #1)

[OpenSpool](https://github.com/spuder/OpenSpool) and [SpoolEase](https://github.com/yanshay/SpoolEase) are two open source
projects with a similar goal - to provide automatic filament detection for your 3D printer.  Bambu Labs filament, for example, includes an NFC tag that allows Bambu Slicer or OrcaSlicer to get information about the filament that's been loaded, including the color, temperature to print at, brand, and type of filmaent, such as PLA or PETG.  And with OpenSpool, it goes both ways - you can read Bambu filament details for other 3D printers.

Both projects are similar where you'll need to buy some compenents, including an ESP32 for OpenSpool and and ESP32-S3 for SpoolEase, along with an NFC reader and a few other miscellaneous parts.  Both projects have a complete bill of materials for you to bulid the project. You build the NFC tag reader with those parts and 3D print the case  for it. OpenSpool does
[sell a kit on Tindie](https://www.tindie.com/products/spuder/openspool-mini/) with everything you need fully assembled for $66.00.

Once built, you can either create your own NFC tags and program each tag with your filament's settings, or use RFID enabled filament from Creality and Bambu.  Just scan the RFID tag and your filament settings are automatically loaded in Bambu Slicer or OrcaSlicer.

OpenSpool's roadmap has future integration planned with OctoPrint, Prusa Connect, Klipper and Moonraker, and more.

### MNT Pocket Reform (Andy #2)

I'm a big support of Open Source software and Open Source Hardware and I'm looking forward to the Open Source Hardware Association summit happening in Edinburgh next month (by the way, [OSHWA are looking for additional supporters and sponsors](https://2025.oshwa.org/sponsor/), if you're able to help out!).

I've been finding myself using Linux and my Framework 13 laptop more and more lately, although I do have Macs, and also very occasionally use Windows as well.

One company I want to shout-out to is MNT Research, out of Germany. MNT have been making the Reform series of laptops for a number of years. These are completely open systems to the greatest extent possible, even to the whole ethos of the company starting from designing using FreeCAD and KiCAD for the hardware, choosing components with the most open drivers where possible, and pre-installed with Debian Linux for as much Open Source, non-commercial software possible.

They've been using the Crowd Supply platform to crowdfund each model. Oh, and the machines are all hand-assembled and tested by humans in Berlin. As of yesterday, MNT also published a new page on their website that goes into more detail about their philosophy, calling out that they build on and share back to the Open Source community, and have an active community on IRC and in the Fediverse.

My actual pick here is the MNT Pocket Reform laptop, which I've been loving as a smaller (roughly A5 or half-US Letter format footprint) portable device. It is more chunky than the average slim laptop, but it is also completely user serviceable - you can literally unscrew the top panel (the back of the screen) to access the processor board, memory, wifi card and so on, and you can also access the batteries and keyboard and trackball on the bottom half just as easily.

The system controller is a RP2040, which means it is possible to integrate additional sensors (one user added a pair of Adafruit triple axis accelerometers to create a lid closure detection mechanism). There's another RP2040 for the keyboard controller. You can choose from a couple of different CPU modules, and the whole system is modular and upgradable.

MNT Research definitely wants users to buy-in to their ethos and approach, and you pay more for that; but, the [community](https://community.mnt.re/) and company are really really great. I've written a couple of posts about my journey so far with the Pocket Reform, and I recommend others take a look and decide if these devices could be a fit for what they want from their computing experiences.

- [MNT Pocket Reform](https://www.crowdsupply.com/mnt/pocket-reform)
  - [Purchase](https://shop.mntre.com/products/mnt-pocket-reform)
  - [Open Computing Autonomy](https://mntre.com/reform.html)
  - [About MNT](https://mntre.com/about.html)
- Andy's [Pocket Reform first impressions](https://andypiper.co.uk/2024/08/06/mnt-pocket-reform-first-impressions/)
- Andy's [Pocket Reform field test](https://andypiper.co.uk/2024/08/26/mnt-pocket-reform-a-literal-field-test/)
- [Pocket Reform lid detection](https://grimmwa.re/blog/html/00017-pocket-reform-lid-detection.html)

### DIYR Design Lamps and Speaker (Tod #2)

[DIYR (pronounced "dear")](https://diyr.dev/products/) is a website that showcases high-design lamps, speakers, and fans that evoke the trendy minmialism of Scandanavian designs from Ikea. But DIYR is different. The DIYR acryonym stands for "Do It Yourself Revolution" and each product they show has detailed instructions on how to build it. From the STL files needed, which electrical components to buy, which tools you need, and how to solder it and assemble it all together. The instructions are understandable and diagrams are very clear. The results look very professional and highly usable.

I particularly like ["BTN-M"](https://diyr.dev/collections/lights/desk-lights/), a USB-C and battery-powered desk light that has an embedded capacitve touch switch. The designs are highly modular so the "BTN-M" head can be mounted to a
["STR-HNG"](https://diyr.dev/instructions/STR-HNG-L) "structure, hinge" arm or a ["STR-WAL"](https://diyr.dev/instructions/STR-WAL-L) "structure, wall" wall mount.

The lamps they have aren't the many Neopixel-lamps you'll find on Thingiverse and similar. These lamps use high-power LED modules putting out 400 lumens or more with high CRI color rendition. These are real lamps.  Kinda neat we can build them ourselves.

All the designs are [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/), a non-commercial free-to-use share-alike creative commons license that allows transformation, useful in case the particular nice LED modules they specify aren't available.

DIYR.dev is a project from the [Design Friction Lab](https://designfrictionlab.com/).

Links:
- [diyr.dev](https://diyr.dev/)
- [LGT-BTN-M - Light Button Medium](https://diyr.dev/instructions/LGT-BTN-M)
- [STR-HNG-L - Structure Hinge Large](https://diyr.dev/instructions/STR-HNG-L)

### Podcast Later (Paul #2)

You may be familiar with read it later apps like Instapaper or Pocket.  These apps allow you to save an article on
the web to their service and read it later, with the ads and extra stuff you find on a website stripped off.  I've been
using Pocket for years and love it.

Michael Kennedy, a Python Software Fellow and host of the Talk Python to Me podcast, has created a new service called
[Podcast Later](https://podcastlater.com) that does something similar, except it creates a personal podcast for you
of the articles you save on the web. You download one of the open source bookmarklets and when you come across an
article you want to save, you just bookmark it.  Behind the scenes it uses a Text-to-Speech service and to convert it
and you have your choice of a male or female voice to read the article to you.  The service creates a private podcast
feed just for you that you subscribe to - meaning in work in *any* podcast app.  And if your podcast app supports
Apple CarPlay or Android Auto, you can even listen in the car.

Plans start at $6 / month for saving about 100 pages (25 per article) and 4 hours of playback a month.

*Disclaimer*: I am a former student of Michael Kennedy's Talk Python to Me training courses and Michael helped me
by answering some questions when I first was starting out podcasting.  Michael did not alert me to his new offering,
I came across it myself.
