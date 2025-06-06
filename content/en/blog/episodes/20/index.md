---
date: 2025-05-05
title: "I'm Afraid it's TRMNL"
linkTitle: "Episode 20 - May 5, 2025"
description: "I'm Afraid it's TRMNL"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

In this episode, Tod and Paul chat about woodworking with open source furniture, MP3 players, a CircuitPython `synthio` tutorial, and more.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/im-afraid-its-trmnl/embed/dark"></iframe>

## Show Notes

### Hyperwood - Open Source Furniture (Tod #1)

I have aspirations of making things out of wood. I've taken a few classes at the
local woodshop but I've never made anything really. I don't have the tools at
home (and you need so many tools) and most of the things I want to make are pretty
basic like benches and boxes. I don't think I really need the nice tools.
But I think I need some sort of "built-in" skill that I can't just get from
all the woodworker Youtube videos I watch.

[Hyperwood](https://hyperwood.org/) is a way of making furniture using standardized materials
and minimal tools. With a hand saw and fasteners (screws, nails, glue), you can make benches,
plant pots, chairs and more. Think of it as Lego for furniture.

The core material of Hyperwood designs are wood slats, which you get more of per
tree than any other type of wood product. And thus they're pretty cheap. And come in some
nice wood types.

The Hyperwood author provides github repos for each design, a text-based data interchange format
called  Hyperwood Exchange Format (HEF), and command-line tools to customize each design
based on the particulars of what you want and what materials you have.

Thanks to previous guest [Andy Piper for pointing me](https://macaw.social/@andypiper/114392576041698951)
towards this.


### Synology Shoots Themselves in the Foot (Paul #1)
I'm lucky that I've had a few network attached storage devices over the years and two of my last three have been from Synology. I've also recommended them to a number of folks, but no longer as enshittification raises its ugly head once again.

Synology recently announced that to use one of their Plus series NASes it would also required a Synology branded hard drive to unlock all of the features.  And these just aren't optional features you might not care about, these are core features including hard drive health reports, lifespan analysis, and automatic firmware updates.

Synology doesn't make their own hard drives, they're rebadged Enterprise drives from the likes of Toshiba and Seagate.  And you pay extra for what those drives would normally cost, and I would assume that's due to Synology doing all kinds of product testing to make sure they're comapitible.  But now it feels like you're having to pay for that privilege twice, once in the cost of the NAS, and in the hard drives.  And when you're buying 8 hard drives for a large NAS, that cost adds up.

Synology has made some vague promises that 3rd party drives might be certified some time in the future, but claim that Synology branded drives paired with Synology systems are at less risk of drive failure.  But now you're going to pay a premium for that and not be able to buy some of the best drives on the market.

* [Ars Technica coverage](https://arstechnica.com/gadgets/2025/04/synology-confirms-need-for-synology-branded-drives-in-newer-plus-series-nas/)
* [Tom's Hardware coverage](https://www.tomshardware.com/pc-components/nas/synology-requires-self-branded-drives-for-some-consumer-nas-systems-drops-full-functionality-and-support-for-third-party-hdds)

### TRMNL WiFi ePaper display (Tod #2)
[TRMNL](https://usetrmnl.com) is a battery-powered WiFi ePaper display wall display.
But with a twist. And that twist is open source.

There are several gizmos out there that put information you're interested in,
like your calendar or weather, onto a stand-alone display. Almost all of these require
a persistent subscription to keep the device working.  Keep paying or your device turns into a brick.
TRMNL ("T.R.M.N.L.") is not that.  Yes, TRMNL has a website to let you configure the device,
selecting which "plugins" of information you want to display and where on the device to display them.
But unlike these other devices, TRML's website lets you easily create your own plugins
with an open API. And you can make those plugins public on TRML's site for others to use.

But wait, not only is it open in its protocol, but in its entirety. The folks behind TRML
recognize that their box is "just" an ESP32 with an eInk display, so they provide a [
set of docs](https://docs.usetrmnl.com/go/diy/introduction) to let you create
your own functionally-identical DIY TRML out of a Waveshare ePaper display ESP32 dev board,
or whatever parts you have laying around, because the
[TRMNL firmware](https://github.com/usetrmnl/firmware) is open-source and on github to explore.

Just the README for the firmware repo is a good dive into what it takes to make a long-lived internet-connected device.

I've had a TRMNL for a few weeks now and it was incredibly easy to set up.
Even though my company ThingM was an early proponent of what we now call
the Internet-of-Things, I don't actually have many IoT devices in my home because
most are eWaste waiting to happen. TRMNL will be able to keep working long after
its company servers go away.

Links:
- TRML - https://usetrmnl.com
- TRML firmware repo - https://github.com/usetrmnl/firmware
- TRML DIY docs - https://docs.usetrmnl.com/go/diy/introduction

### Rockbox releases 4.0 (Paul #2)
Hackaday recently covered the Rockbox 4.0 release and it took me for a turn down nostalgia lane.  Rockbox is an open source project that replaces the firmware on MP3 players from a number of different manufacturers.  If you know me, you know I love music. I'm dating myself as I fondly remember having a slew of MP3 players before smart phones and streaming took over.

Looking at the support for MP3 players such as the early Archos, IRiver, and Sandisk Sansa were all MP3 players I owned and probably put Rockbox on back in the day.  Rockbox was also known for its iPod support, though I never personally owned an iPod.

It added a number of features to MP3 players, such as support for other music formats like Ogg Vorbis or FLAC, gapless playback, Last.fm support, and the list goes on.

Rockbox started in 2001 with its first release was in June of 2022.  It's pretty cool to see a project still going strong with major releases after over 20 years.

* [Hackaday coverage](https://hackaday.com/2025/04/19/rockbox-4-0-released/)
* [Rockbox home page](https://www.rockbox.org)

*Correction notice*: Paul accidentally said Rockbox's first release was in 2022 when he meant 2002.  We regret the error.

### CircuitPython Synthio Tutorial (Tod #3)

Shameless plug incoming! For the last few months, I've been working off-and-on
on a [CircuitPython Synthio Tutorial](https://todbot.github.io/CircuitPython_Synthio_Tutorial/) site.
For those unaware, `synthio` is a CircuitPython core library for musical synthesis.
It's pretty much let's you turn a CircuitPython board into a modular synthesizer.

Back two years ago when `synthio` first came out, I made a
["CircuitPython Synthio Tricks"](https://github.com/todbot/circuitpython-synthio-tricks) page
that was a "quick tips" guide for fun things to do, kinda like my [CircuitPython Tricks](https://github.com/todbot/circuitpython-tricks) page.

Over time `synthio` has evolved, thanks to Jeff Epler ("jepler"), the
original synthio author, and with some critical improvements by
Cooper Dalrymple ("relic-se") and Mark Komus ("gamblor21").
Also by Mark & Cooper were these new guitar-inspired audio effects,
which [we chatted about on The CircuitPython Show in a panel](https://www.circuitpythonshow.com/@circuitpythonshow/episodes/audio-effects-panel-discussion).
And which I only had very cursory experience with.

Given all these changes, it felt like I would be well-served to come at `synthio`
fresh and "re-teach" it to myself from the ground up.  And since I learn best when
I document as I go, I figured this would be a great excuse to create something more
structured than a "tricks" document and instead have a set of goal posts and a destination.

This tutorial guide is the result. I am maybe two-thirds done with it. It's broken
up into sections, starting from you "just have a bunch of parts on your desk" and
it's heading towards creating a fully-featured synthesizer.
Along the way you learn some synthesis techniques like filter envelopes and wavetables
and how to deal with controls like MIDI.

It was important to me that each code block in the guide do something musically
kinda cool, be fully-functioning (albeit it does use modules created in past sections),,
and that there be a small accompanying video showing what the code does and how
you interact with it.  Eventually there will be over 50 small programs with videos.

So if anyone is interested in making a synthesizer in CircuitPython, see
if this tutorial guide is useful. To get started, all you need is a Raspberry Pi Pico,
a [cheapie I2S DAC](https://todbot.com/blog/2023/05/16/cheap-stereo-line-out-i2s-dac-for-circuitpython-arduino-synths/),
and a couple of potentiometers. And please let me know if you have suggestions
on things I missed and ways to make it better!

Links:
- [CircuitPython Synthio Tutorial](https://todbot.github.io/CircuitPython_Synthio_Tutorial/)
- [Adafruit Show-N-Tell 4/23/25 where I show it a bit](https://www.youtube.com/live/PUzCYALKXqY?si=P_EpC3gucNgY6SRE&t=1187)
- [CircuitPython Synthio Tricks](https://github.com/todbot/circuitpython-synthio-tricks) (kinda outdated)

### mobygratis (Paul #3)
Lastly, there is [mobygratis](https://mobygratis.com).  Do you remember the artist Moby?  You may know him from such hits as Go and South Side.  He's just released about 500 different songs for free and they come with only two restrictions:
* You cannot use mobygratis songs to promote meat, dairy, or other animal products
* You cannot use mobygratis songs to promote right wing causes

Other than that, Moby encourages any creators, whether that's filmmakers, musicans, students, remixers and the list goes on.  There are about 500 songs total, and these are songs, not just fragments.  You can filter by genre or or mood and the list shows you the song name, a description such as *energetic uplifting* and the beats per minute.  You can just click play to hear it right in your browser or favorite it or download it as well.

So if you have a music or film project or maybe even a synthio project in CircuitPython and want some samples, check out [mobygratis.com](https://mobygratis.com)
