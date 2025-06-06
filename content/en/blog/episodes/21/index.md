---
date: 2025-06-02
title: "Rated PG for Language"
linkTitle: "Episode 21 - June 2, 2025"
description: "Rated PG for Language"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

In this episode Paul and Tod discuss tariffs, desoldering tricks, a classic arcade game, and more.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net). Follow Paul on [Mastodon](https://www.hachyderm.io/@prcutler/) or [Bluesky](https://bsky.app/profile/paulcutler.org). Follow Tod on [Mastodon](https://www.mastodon.social/@todbot/) or [Bluesky](https://bsky.app/profile/todbot.com).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/rated-pg-for-language/embed/dark"></iframe>

## Show Notes

### Tariffs are Bullshit (.com) - Paul #1
Thanks to Jason Coon of Evil Genius Labs, and inspired by an idea Carrie Sundra of Alpenglow had, Jason has launched a new website at [tariffsarebullshit.com](https://tariffsarebullshit.com).  The site is an opportunity to share emails, videos, and social media posts from manufacturers and suppliers explaining how tariffs are affecting their business.

If you have a story to news item to share, open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models) or [start a discussion](https://github.com/jasoncoon/tariffsarebullshit/discussions) in GitHub!


### Desoldering Tricks - Tod #1

If you've ever soldered together electronic circuit boards, you've probably wanted to *un*solder
components at times. Unsoldering parts from PCBs is a pain and, for some parts,
it's almost impossible. Better to just start again on a fresh board.
That's not the most cost-effective solution, especially now with the uncertainties in part
supplies thanks to the ever-shifting tariff landscape.

And it may become cost effective to desolder parts from existing boards in order to
repurpose them.  I know a few small manufacturers who did this during the Covid chip shortage.
So, I'm always on the look-out for techniques that are quicker or cheaper
than what I normally do.  And I recently came across two videos that do that.

The first, from Youtube channel [Tinkering Daily](https://www.youtube.com/@tinkeringdaily),
[shows a really clever and low-cost technique](https://www.youtube.com/watch?v=2E7y5i1DkGo)
for removing surface mount (aka "SMT") components.
To start, get a soda can. No really! And using tin snips, cut out a piece of the can
a few inches long and about as wide as your finger. Trim down one end to a
tapered rounded tip less than a centimeter across. Then using sandpaper,
sand down that tip to reduce its thickness to about 0.08 mm.
This is now a thin desoldering shim!
That thickness means it can slip *under* soldered down parts.
The process to desolder becomes: slide in the shim, heat up one side of the part,
wiggle the shim under that, then heat up the other side of the part.
Part is now desoldered.
Since this drink-can shim is made of alumimum, solder doesn't stick to it. And in the video,
they show some rather huge and difficult parts being removed like SD card sockets,
audio jacks, and large flash storage chips.  Last week I got a soda can and tried
this myself.  It works! I'm not very good yet, but it's totally going in my toolkit of techniques.

Later in the video, they also show a way to make unsoldering through-hole components
with a solder sucker better, but if you *really* need to desolder a lot of through-hole parts
and you have $200, check out the [recent video from Jeff Geerling](https://www.youtube.com/watch?v=PRW5WBmOCBQ) about the [Hakko FR-301](https://amzn.to/3Sk25aF).

The Hakko FR-301 is billed as a "portable desoldering tool": it's a motorized solder sucker.
It solves the two main problems I've experienced using solder suckers.
There's always a small gap in space and time when you're heating the solder joint vs
when you're trying to suck up the solder. In that gap, the solder cools.  And if you manage
it, the solder sucker quickly clogs, requiring you to stop to clean it. The FR-301
has one tip that's both the heater and the sucker. And when it sucks up the solder, it
stores it in a little chamber that's separate from the nozzle. It looks incredibly well designed
and if I need to do a lot of through-hole rework, I'm getting one of these.


### Philips Fixables - Paul #2
Philips, the company that makes everything from lightbulbs to electric toothbrushes or razors, has announced a new program they call Fixables. The Fixables program will make plans available for 3D printing select Philips replacement parts.

Parts are being [published on Printables](https://www.printables.com/@Philips) and the first part is a 3mm comb for the Norelco OneBlade. Philips has partnered with Prusa Research LePub to help with local maker adoption starting in the Czech Republic.  (Via [Tom's Hardware](https://www.tomshardware.com/3d-printing/philips-debuts-3d-printable-components-to-repair-products))

### Resurrecting Sinistar: A Cyber-Archaeology Documentary - Tod #2
[Resurrecting Sinistar](https://www.youtube.com/watch?v=lCuoUSDBVac) is a documentary
by nom-de-plume musician "Synamax" about the revolutionary (and scary as heck to me as a kid)
coin-op video game Sinistar.  Sinistar was created by Williams Electronics,
makers of other famous games like Defender, Robotron, and Joust.  It was the first
game to feature real-time sampled voice audio (*play Sinistar sample here*),
had a 49-way! joystick, and blistering fast gameplay. If you've never seen it,
gameplay is vaguely Asteroids-like, but you shoot the rocks to "mine" bombs used
against the growing sentient planet of Sinistar.

This documentary is quite long, at over two hours, but it goes the history
of the team that created these games, the challenges of making games in the 1980s,
some of the assembly language tricks needed for certain game features,
and the technical hurdles that made Sinistar unique.  It also discusses the
challenges of reconstructing a modern working build of the game from 40-year old source code.

This is because a couple of years ago, the [source code for several Williams' video
games](https://arcadeheroes.com/2021/04/14/source-code-for-several-williams-midway-arcade-titles-pop-up-online/) appeared anonymously online.

Along the way, the documentary has exclusive interviews with members of the Williams
game team: project lead and software engineer Noah Falstein, sound engineer Mike Metz,
and game designer John Newcomer.

You can track his work on [his public github repo](https://github.com/synamaxmusic/sinistar).

### Kiwix - Paul #3
[Kiwix](https://kiwix.org/en/) is a non-proit dedicated to providing offline access to free content.  It’s free and open source and allows you to make compressed compies of entire websites, like Wikipedia or Project Gutenberg.

Their home page mentions 50% of the world doesn’t have access to reliable internet and this is one way to bring the world’s content to those areas without good internet.

Kiwix supports the whole stack - they have a Kiwix server you can run on a Raspberry Pi or any other major OS, like Windows, Mac, or Linux.  But if you use a Raspberry Pi, you can also use it a wireless hotspot to serve these local websites to anyone connecting.  Almost any model of Raspberry Pi will work from the model 3B on up, except the Zero 2W.  Or, you will soon be able to buy a Pi Hotspot right from Kiwix, that comes with an SSD, Pi5, real time clock and more.

So what does Kiwix do?  It allows you to download entire websites and serve them offline.  You can have Wikipedia, which is only 57GBs for the English version, and host it locally.  You can visit [library.kiwix.org](https://library.kiwix.org/#lang=eng)  to see the websites they make available for offline use, and it includes about a 1000 books as they call it.  They have tons of documentation available, from Linux distro docs to Python documentation to all of FreeCodeCamp to teach you how to code.  They use the Zim file format, which is an open document format, with excellent compression.


### Euroknob - Tod #3
It's a knob! It's a jack! It's a knob! It's a jack!
It's [Euroknob](https://www.youtube.com/watch?v=dLw2QQdOLaM)!

The talent hacker "Mitxela", perhaps most famous for his
self-proclaimed "smallest and worst" MIDI synths that fit on a
[USB-A](https://mitxela.com/projects/silly_synth) or
[USB-C](https://mitxela.com/projects/smsc) jack,
[recently posted this really clever hack](https://mitxela.com/projects/euroknob)
that allows you to plug a knob into a headphone jack and turn it to adjust things.

So imagine: you've got this Euorack modular synth setup, with wires going all over.
Some of the wires carry these control voltages, maybe from a slow oscillator module
(a low-frequency oscillator or "LFO") that alters the behavior of another module
like a filter. Thus this wire is what's making the sound rhythmically go
*bwoowwooowooowoowow*. But now you can just unplug that wire, plug in a knob and turn
the knob to change that filter directly!

What is this magic?!

He calls it ["Euroknob"](https://mitxela.com/projects/euroknob) and it solves
a common problem in modular synths like Eurorack systems.
Some of these synth modules have inputs with no corresponding knob on their front panel,
making those input difficult to quickly adjust without running wires.

The way his hack works is a special PCB that contains both the jack and a magnetic
position encoder below it. When you plug a cable it, the jack acts like any old jack.
But the shaft of his special knob is a plug with a small embedded magnet. Turn the knob,
the jack shaft rotates, which spins the magnet, which is picked up by the magnetic
position encoders.

These magnetic encoders are incredibly precise. The [cheap AS5600 ones](https://amzn.to/4mB1dwf)
he uses provides 12-bit position accuracy and are effectively noiseless (unlike the ADCs of
most microcontrollers we hook up our pots to)  I’ve been wanting to do something with
those AS5600 magnetic position encoders for a while (as used in mitxela’s euroknob).
The only thing stopping me has been trying to figure out a decent assembly
that “just works” to act as a knob replacement. It may be that something like
what Mitxela has done is the approach.  Even without using the jack as a jack,
I'd find this useful!

Mitxela's write up is great and he's posted the PCB design, software and CAD files
on the [github repo for the project](https://github.com/mitxela/euroknob).
