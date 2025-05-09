---
date: 2025-03-03
title: "Welcome Brent Rubell"
linkTitle: "Episode 18 - March 3, 2025"
description: "Episode 18"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Tod and Paul welcome guest Brent Rubell of Adafruit Industries.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net).
View the [transcript here](https://www.thebootloader.net/blog/2025/03/03/episode-18-transcript/).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/welcome-brent-rubell/embed/dark"></iframe>

## Show Notes

### WipperSnapper Offline Mode (Brent #1)

Disclaimer, I am biased on this note as I work for Adafruit Industries as an Engineer. To back up and explain this item, WipperSnapper is a firmware that enables people to visually create Internet-connected
electronics projects. What this means is that you can click your way to a fully working project,
there's no programming involved.

My colleague Loren and I work together on this project, WipperSnapper. He handles the Web side of things, specifically
the Adafruit IO MQTT broker and functionality around it. I lead the embedded side. We're two different
engineers working on the same project, which has been fun.

Since WipperSnapper has been out for a while now, and the beta tag is about to get ripped off,
we've spent the last year completely rewriting the API and that involves rewriting the firmware.

One of the fun things we've added  was offline mode. We didn't intend to fully add this feature. I needed
a way to test the API and functionality and Loren was deep in development of a different feature.

We ended up adding a feature that allows you to create a project on Adafruit IO, download the configuration file
(which is a JSON-encoded file) and drag it onto the WipperSnapper device. The device will then read the file and
automatically configure itself to start logging data to a MicroSD card. This runs offline and doesn't require a network connection, which is different from regular
WipperSnapper projects.

It's cool because a) there's nothing like this where you can create a project online and then download it to a device
and b) it's the same firmware! We didn't write a new firmware, the offline mode is a shim that runs
when a configuration file is loaded on the drive. One firmware, two modes!

This should all be released on the Adafruit Learning System in March 2025.


### 200 MHz Clock Support for RP2040 / Pico  (Tod #1)

Good news, everyone! Free speed boost for your Pico!
Raspberry Pi officially supports overclocking the Pico RP2040.
When the RP2040 was originally released, its Pico-SDK library configured the chip to run
at 125 MHz. This was incredibly fast! But still we wanted more. And it turns out the RP2040
was incredibly overclockable. People soon found that even doubling its clock to 250 MHz
worked great with no downsides. Many of my RP2040-based CircuitPython synth projects do
this to let me run at a higher-quality sample rate.

Overclocking is often frowned on by the manufacturer, and in desktop CPUs it can cause permanent damage.
Some venders of RP2040-based products were reluctant to sell something that depended on an overclocked RP2040. So when Raspberry Pi announced that 200 MHz was officially supported and [can be easily configured via a compile-time define](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2040/hardware_regs/include/hardware/platform_defs.h#L65), we all celebrated.

In both CircuitPython and the `arduino-pico` Arduino core for RP2040, changing CPU speed has always been pretty easy.  In CircuitPython, you can dynamically change the CPU speed by setting [`microcontroller.cpu.frequency`](https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html#microcontroller.Processor.frequency).  This can be useful for battery-powered applications, since power usage scales linearly with clock speed.  In Arduino, it's a simple compile-time directive available from the ["Tools"-> "CPU Speed" menu](https://arduino-pico.readthedocs.io/en/latest/ide.html#cpu-speed).

Links with more details:
  - https://github.com/raspberrypi/pico-sdk/releases/tag/2.1.1
  - https://www.hackster.io/news/the-raspberry-pi-rp2040-gets-a-surprise-speed-boost-unlocks-an-official-200mhz-mode-d6c9d267de5a
  - https://bsky.app/profile/thejpster.org.uk/post/3lijrgmptnc2a
  - ["I already use a pretty aggressive overlock to 366MHz"](https://bsky.app/profile/polpo.org/post/3lik2xrznhs2z) - @polpo.org / [PicoGUS](https://picog.us/)


### Microcontrollers as computers (Paul #1)

#### Slimedeck Zero

Microcontrollers are so powerful that we're starting to see almost full fledged computers being built.  A maker named
Abe Haskins has built a small handheld computer called the Slimedeck Zero using Pimoroni's PicoVision as it's brain.
Abe has a [25 minute video up on YouTube](https://www.youtube.com/watch?v=rnwPmoWMGqk) that shows the entire process
and parts used to build this tiny handheld computer that runs MicroPython, has an app launcher / operating system
called `slime_os`, and is extensible with hardware plugins.

It features a keyboard he disassembled from a $9 remote control, a 5" 800x460 screen, and use the PicoVision from
Pimoroni as its brains.  The PicoVision features two rp2040 chips, one acting as the CPU and the other as the GPU.

It also features an expansion port - Abe demos it by plugging in a XIAO microcontroller that's wired to an LED that
the Slimedeck Zero can control.

* [Hackaday coverage](https://hackaday.com/2025/02/22/the-perfect-pi-pico-portable-computer/)
* [Slime_OS on GitHub](https://github.com/abeisgoat/slime_os)

#### Adafruit Fruit Jam

The second handheld is something Adafruit has been teasing for the last few weeks, which they’ve code
named [Fruit Jam](https://www.adafruit.com/product/6200).   LadyAda was inspired from a recent Hackaday hackchat
with Raspberry Pi’s Ebon Upton and built a credit card sized computer using the Rapsberry Pi 2350B chip, the one
with the extra GPIO.

It includes a ton of peripherals such as DVI out, MicroSD, stereo headphone out, USB host with two USB-Type A ports,
switches, Neopixels, and more.

We haven't seen much of the software running on it yet, but I have to guess we'll see CircuitPython running on it,
giving us a full fledged CircuitPython mini-computer.


### Obsidian (Brent #2)

Have we talked about Obsidian on here before? I've used Evernote for years, I have so so so many notes in Evernote.  I've tried Notion, it is way too much for my purposes.

Obsidian is a notes app, which is on the surface kinda boring! But all of
your notes are stored on the device you're writing them on, as a markdown file. You can pop open
each file in your favorite markdown editor, in this age of "cloud"-first, it's great to be able to see
all of my notes as files in a folder on the computer. It just feels "right"!

What I like about Obsidian is how little it does, and how much that can be extended. Instead of Notion's Wiki
system, you can link notes together and that's incredibly powerful. You can create little workflows by combining Obsidian
with other applications.

Like, for example, I use Zotero to organize academic papers and journal articles, and I can link to Zotero
entries in my notes. That's it - the workflow is tiny! Another "workflow" I've started is syncing the folder that Obsidian notes are saved to, to my Google Drive. Free storage and versioning!

- [Obsidian](https://obsidian.md/) - Obsidian Markdown-Based Note Taking App
- [Zotero and Obsidian Workflow](https://medium.com/@alexandraphelan/an-updated-academic-workflow-zotero-obsidian-cffef080addd) - Workflow for Zotero and Obsidian


### ArduinoLibs bot on Mastodon/Bluesky (Tod #2)

We just did a CircuitPython Show episode on the CircuitPython Community Bundle.
In the Arduino world, the closest equivalent is the Arduino Library Manager's list
of libraries.  And one of the my favorite ways to observe updates to that list was the
"@arduinoLibs" Twitter bot that posted whenever libraries were added or updated.

With Twitter gone, thankfully the bot has moved to both Mastodon & Bluesky.
The @arduinoLibs bot appears to be tracking the pull-requests to the
[Arduino library registry github repo](https://github.com/arduino/library-registry)
and it's a great way to get ideas or see what people are doing with Arduino.
The bot is promises no more than six posts per hour so it doesn't overwhelm your feed.
I really like poking around libraries to see what people are building and as a gauge on
the "State of the Arduino community".

Some examples:

- [YAMLDuino](https://github.com/tobozo/YAMLDuino) - YAML file parsing in Arduino
- [Usini Discord WebHook](https://github.com/usini/usini_discord_webhook) - Write Discord bots in Arduino
- [CodeCell](https://github.com/microbotsio/CodeCell) - Wrapper library for a new coin-sized ESP32-C3-based board that has a lipo-charger, 9-axis IMU, and light sensor
- [GoogleFindMyTools](https://github.com/leonboe1/GoogleFindMyTools) - Turn an ESP32 into a "Find My" device

Links:

- [fosstodon.org/@arduinoLibs](https://fosstodon.org/@arduinoLibs)
- [@ArduinoLibs.bsky.social](https://bsky.app/profile/arduinolibs.bsky.social)
- Maintaner: [@tobozo](https://mastodon.social/@tobozo)


### 3D Printed Records (Paul #2)

Paul thought he found the perfect story for this episode, but there's a catch, which he shares at the end.
[Amanda Ghassaei](https://amandaghassaei.com/projects/) used a resin printer to create a 3D printed record.

On her [Instructables page](https://www.instructables.com/3D-Printed-Record/), Amanda shares how a record works and then
walks through how she calculated the sampling rate for a 3D printer including the sampling frequency, revolutions per
second, and inches per revolution to get the max sampling frequency of 12kHz.

She then wrote an Arduino sketch called Processing to take a sine wave and convert it to a series of integers which
could be converted to text, which she could create an STL file from. Amanda then printed 3 test records that played
back sine waves to test the depth of the grooves of the record.

From there, Amanda wrote a Python program to extract the audio data from a WAV file, which could then be imported
into the Processing sketch to create the STL file to be able to print the record.

The catch was that this article was from 2012! There were a few giveaways in the article.  When she compares the
resin printer, she mentions MakerBot and RepRap, which aren't popular printers today.  And her Python program uses
Python 2.5, which is ancient.  The comments ranged from just a few months ago to 12 years ago, and the YouTube videos
are about 6 years old. She was using a commercial Object Connex500 printer, and I'm curious
to know if in the last 10+ years how far resin printers have come to know if you could make an even better sounding
record today.

In more modern news, [The Guardian just published an article on February 25th](https://www.theguardian.com/music/2025/feb/25/vinyl-carver-lathe-cutters-home-cutting-records-craze)
also about creating your own records, but using a custom kit from Ulrich Sourisseau.  It’s a lathe cutting machine
that uses a diamond needle to cut a record one at a time in real time.  People in the UK are using them to create
custom pressings of say 20 to a 100 records that artists or bands can sell who might not be able to afford a regular
vinyl pressing.

The catch here?  Ulrich Sourisseau is a cash only operation, and if you want to buy one, you’ll need about
7000 pounds hand delivered to him in the Black Forest of Germany.
