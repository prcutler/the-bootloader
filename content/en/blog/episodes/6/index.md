---
date: 2022-12-05
title: "Episode 6: Supersized for Supercon"
linkTitle: "Episode 6"
description: "Supersized for Supercon"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
## Welcome
Welcome to The Bootloader!  This week we are doing something a little different.  Tod recently attended Supercon and shares some of his favorite talks and presentations. Paul and Tod also share one interesting thing.

[Full transcript available here](https://thebootloader.net/blog/2022/12/05/episode-6-transcript/).

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/supersized-for-supercon-jvu55/embed/dark"></iframe>

# Show Notes

### Hackaday Supercon

* What is [Hackaday Supercon](https://hackaday.com/2022/10/11/2022-supercon-more-talks-more-speakers/)?
  * Annual get together in Pasadena of talks & workshops on stuff you'd see in [Hackaday.com](https://hackaday.com/)
  * A way for me to see friends I've only really talk to online
  * It's held at the [Supplyframe DesignLab](https://supplyframe.com/designlab/)
     and at [Los Angeles College of Music](https://lacm.edu/) next door
  * In between is an alley where there's hardware hacking and snacks
  * The workshops are held at [Supplyframe HQ](https://supplyframe.com/), up the street a few blocks
  * One of my favorite conferences, before pandemic
  * This Supercon was first in-person since 2019
  * It was so nice seeing everyone, but wow I am out of practice being amongst people

* The [SuperCon Badge](https://hackaday.io/project/188025-2022-hackaday-supercon-6-badge-guide)
  * Hacker conferences have these "badges" that don't really function as IDs any more
  * Instead, they're a playground for electronics experimentation
  * This year, the badge was a microcontroller-based board that acted like an old switches-and-lights computer from the 1970s.
  * Designed by [Voja Antonic](https://en.wikipedia.org/wiki/Voja_Antoni%C4%87), a Serbian inventor,
     created the "Galaksija" build-your-own-computer in 1983, inspiring thousands to learn computers
  * Check out the [Video badge walkthrough by Voja](https://www.youtube.com/watch?v=ix__enrtYF4)
  * You program it the way computers used to be programed: hand keying in bits one-by-one, and clicking the "load" switch to enter a single machine code instruction, one at a time
![Todbot's Supercon Badge](todbot-supercon-badge.jpg)

* Some of the talks I liked
  * [Nick’s DIY Vacuum tubes](https://www.youtube.com/watch?v=39-5WgcvaHk)
  * [Adrian’s Soviet chips](https://www.youtube.com/watch?v=i1gZR1U2cF4)
  * [Chris Comb](https://chriscombs.net/artwork/all/)'s "How to Hang and Sell Your Blinky Goodness as Art"
      (on the DesignLab stage, so recorded but not streamed)
  * Also, [Bradley's talk](https://www.youtube.com/watch?v=Z1IbAKz1qUY) about 'showing up' and making a difference, disguised as a talk on hacking electric scooters
  * Lastly, [Samy's "random walk" exploration](https://www.youtube.com/watch?v=B6a25Smokkk) that resulted in a flexible wearable tesla coil to light up his breathe in a glass ampule

### Python in the Browser (Paul #1)
* [MicroPython in the browser](https://www.anaconda.com/blog/pyscript-updates-bytecode-alliance-pyodide-and-micropython)
  * Builds on Pyscript, announced this past PyCon by the founder of Anaconda, Peter Wang
  * Great [podcast at Talkpython.fm](https://talkpython.fm/episodes/show/391/pyscript-powered-by-micropython) sharing more, including the technical details
    * Included Brett Cannon, Fabio Pliger, and Nicholas Tollervey
  * Pyscript can use the MicroPython as a runtime
    * Reduces the size of Python in Pyscript from 11MB to 300k using MicroPython
    * Pyscript is a framework the developers see building on top of
    * [PyScript Runtimes - MicroPython Technical Preview](https://pyscript.net/tech-preview/micropython/about.html)

### PicoStepSeq in The MagPi Magazine! (Tod #1)
* [My PicoStepSeq project made it as an article in The MagPi](https://magpi.raspberrypi.com/articles/picostepseq-rp2040-music-maker)
* Also in the print version (and [the PDF](https://magpi.raspberrypi.com/issues/124/pdf))! (and it's a slightly different, longer article.)
* [PicoStepSeq](https://github.com/todbot/picostepseq/) is a tiny 1980s-style MIDI sequencer, using these lever switches with embedded LEDs (called ["step switches" by Adafruit](https://www.adafruit.com/product/5519))
* It was desgined, coded, and built [in the two weeks](https://twitter.com/todbot/status/1560676715424141313?ref_src=twsrc%5Etfw) leading up to [CircuitPython Day 2022](https://blog.adafruit.com/2022/08/08/circuitpython-day-2022-schedule-circuitpythonday2022-circuitpython-python/)
* It has both a CircuitPython-firmware and an Arduino-based firmware
* See it in action in [John Park's Workshop from November 30](https://www.youtube.com/watch?v=GvbF1Mo4WMw)
* I've slowly been considering a 16-step version, but it's complicated for various reasons

### Support Sponsor The Bootloader

If you like what you hear, one of the best things you can do to help the show is tell a friend or write a review.

Consider supporting the show financially - your support helps with the cost of hosting, recording and transcripts.  Thank you for your support!

[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/prcutler)
