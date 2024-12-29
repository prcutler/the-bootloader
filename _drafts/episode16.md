---
date: 2025-01-06
title: "Episode 16"
linkTitle: "Episode 16 - January 6, 2025"
description: "Insert Episode Name Here"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Insert intro here.

## Listen to the podcast

Insert iframe from Castopod here.

## Show Notes

### Synthstrom Deluge and its Community Firmware (Tod #1)

The [Synthstrom Deluge](https://synthstrom.com/product/deluge/) is a music making device that falls mostly in the category of "groovebox", if you've heard that term. It's a small device, about the size of a sheet of paper and an inch thick. It's covered with a grid of 144 RGB button pads and a few knobs. It's a MIDI sequencer, a drum machine, a sampler, and a multi-track audio recorder. And it's got a built-in battery so you can use it anywhere. It's also got CV/gate output to control modular synths.  It's what I use as the hub (and often only device) when making music. The Deluge is made by a small team in New Zealand, coded by one guy it seems, but its quality and attention to detail puts it in the realm of professional gear.  I love it.

And then Synthstrom made me love them more. First they introduced an OLED multi-line screen replacement for the 7-segment display the Deluge originally had. And then they announced that not only were they releasing the [Deluge source code on github](https://github.com/SynthstromAudible/DelugeFirmware), but they were releasing it under a true open source license (GPL) and creating a ("Synthstrom Community Fund")[https://www.patreon.com/c/Synthstrom] to financially assist anyone who wanted to work on improving the firmware.

And boy did the community step up!  With a few months, the entire codebase was refactored to make it more usable in a large team. All while keeping the existing functionality.  Within a few months more, the first official "Community Firmware" was released for the Deluge. It added a bunch of UI and usability improvements but also added new features like new audio effects and filters, added new features to the sequencer, and entire new UI views that make it work like Ableton Live.

Every few months, new features are added, and you can try them at any point. Or, like me, wait for the official releases. On December 25 2024, Community Firmware 1.3 was released. It adds DX7 synth emulation, a new "chord library", the ability to export a song as multiple WAVs (very useful for final production), and a whole bunch of other improvements.

It's like getting a new piece of music gear every few months, it's incredible.

### Sunsetting Mu (Paul #1)

Nicholas Tollervey and the developers of the [Mu code editor](https://codewith.mu) recently [shared that they will be sunsetting Mu](https://madewith.mu/mu/users/2024/12/10/retirement-plans.html). Mu has been around for over 9 years and is the first code editor for some people new to programming Python and MicroPython and CircuitPython.

The Mu team will have two releases in 2025. The first will be built with a few bug fixes and is considered a "legacy" release with libraries pinned to older versions so people using older hardware can still use Mu.  Soon after, the final versio of Mu will be released using the latest versions of libraries with the hope that Mu can live a few more years before becoming out of date.

The Mu team expects to have this done by the end of March, 2025.

### Home Assistant Voice (Preview Edition)

The team behind Home Assistant [has announced](https://newsletter.openhomefoundation.org/the-era-of-open-voice/) the [Home Assistant Voice (Preview Edition)](https://www.home-assistant.io/voice-pe/).
