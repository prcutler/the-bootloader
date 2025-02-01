---
date: 2025-02-03
title: "Bamboozled"
linkTitle: "Episode 17 - February 3, 2025"
description: "Bamboozled"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show
Paul and Tod discuss drama in the world of 3D printing, oscilloscope music, inventory management for makers, and more.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net) and sign up for ad-free, spam-free, tracking-free [monthly newsletter](https://buttondown.com/thebootloader).

View the [transcript here(https://www.thebootloader.net/blog/2025/02/03/episode-17-transcript/).

## Listen to the podcast

Insert iframe from Castopod here.

## Show Notes

bamboozle:  *To deceive or dupe; hoodwink. synonym: deceive.*

### Paul #1: Drama in 3D Printing

#### Printables pulls Benchy models

The 3DBenchy is a 3D model that is used to calibrate 3D printers.  It's a small boat and is used to diagnose issues with your 3D printer.  It was originally created by Creative Tools, who was recently acquired by NTI Group, and licensed under a CC-BY-ND license.  The non-derivatives license means you can't use the model and remix it into other shapes - and if you're in the 3D printing community, you probably know that there are dozens of remixes.

At first, people thought that the new owner, NTI Group, was sending takedown notices, but they released a statement that they weren't doing that.  It turns out that Printables, the 3D model website owned by Prusa, took it upon themselves to enforce the license for unknown reasons.

* [3D Benchy shutting down remixes](https://www.redditmedia.com/r/BambuLab/comments/1hwqe8e/fyi_3dbenchycom_is_sending_lawyers_to_kill_the_fun/)
* [more history on Reddit](https://www.reddit.com/r/3Dprinting/comments/1hx2xbp/about_3dbenchy_someone_else_owns_the_rights_now/)
* [Creative Tools history](https://www.linkedin.com/posts/danielnoree_a-piece-of-3dprinting-history-just-faded-activity-7282680313879683072-FCET/)
* [Hackaday](https://hackaday.com/2025/01/09/3dbenchy-starts-enforcing-its-no-derivatives-license/) or [is it](https://all3dp.com/4/no-3dbenchy-remixes-arent-being-dmcad/)?

#### Bambu to add a new authorization control system

Bambu Labs, who we've covered multiple times in the podcast, has announced that they’re adding a proprietary authentication mechanism that locks out 3rd party tools from controlling your printer.  To oversimplify, Bambu claims that this is  a security enhancement, but hasn’t exactly said *why* it’s needed.

* [New Bambu firmware](https://blog.bambulab.com/firmware-update-introducing-new-authorization-control-system-2/) that shuts out 3rd party slicers and [Orca benefits](https://www.reddit.com/r/BambuLab/comments/1i3gyn5/tell_me_why_orcaslicer_is_better_than_bambu_studio/) and [Hackaday coverage](https://hackaday.com/2025/01/17/new-bambu-lab-firmware-update-adds-mandatory-authorization-control-system/) and [key cracked](https://hastebin.skyra.pw/pufugimoye.js)
  * [The Verge coverage](https://www.theverge.com/2025/1/21/24349031/bambu-3d-printer-update-authentication-filament-subscription-lock-answers)
 * [Reddit thread on why it might have happened](https://www.reddit.com/r/3Dprinting/comments/1i4gotq/my_product_is_the_reason_bambu_blocked_the_api/)
 * [Bambu Klipper conversion](https://github.com/ChazLayyd/Bambu-Lab-Klipper-Conversion)
 * [Bambu's official blog post](https://blog.bambulab.com/updates-and-third-party-integration-with-bambu-connect/)
 * [X1Plus follow-up](https://www.crowdsupply.com/accelerated-tech/x1plus-expander/updates/bambu-labs-security-updates)

### Tod #1: Oscilloscope Music

My first one is about "oscilloscope music"

For the unaware, oscilloscopes are a key tool for electronics engineers.
Generally they're used to graph a signal over time.  They have a screen that looks
like graph paper, where the X-axis is time and the Y-axis is the signal's value at that time.
Normally we use them to plot repeating signals. Most all oscilloscopes are two-channel,
so you can see two different signals plotted against each other over time.

But oscilloscopes can also be put into ["XY-mode"](https://www.tmatlantic.com/encyclopedia/index.php?ELEMENT_ID=9524) or "vectorsscope" mode.
In this mode, the two channels control the X- and Y-position of the dot on the screen.
This means you can draw any shape on the screen!
And this was the inspiration for the [2023 Hackaday Supercon badge](https://hackaday.com/2023/10/18/2023-hackaday-supercon-badge-welcome-to-the-vectorscope/).

Many people have used this XY-mode to draw pictures. In fact, one of the earliest video games
was in 1958 ["Tennis for Two"](https://en.wikipedia.org/wiki/Tennis_for_Two) on an analog computer
and an oscilloscope.

To keep the picture on the screen, the signals you're feeding into an XY-mode oscilloscope have to repeat.  If you make this repetition happen at audio rates and feed the output to a speaker,
you're now also making sound as well as a picture.  There have been many people who have done this over the years, but the best I've seen is by Jerobeam Fenderson and Hansi3D who have created a whole album of audio-visual compositions.

Thus: [Oscilloscope Music](https://oscilloscopemusic.com/watch/n-spheres)

"Oscilloscope Music is audiovisual music, where the visuals are drawn by the sound. In order to get the closest possible correlation between image and sound, the exact same signal that is connected to the left and right speakers is also connected to an analog oscilloscope's X and Y inputs, producing complex lissajous images."

More about it, with tutorials and how-to links: https://oscilloscopemusic.com/info/about/

One really nice piece from the album: [Intersect from N-SPHERES](https://www.youtube.com/watch?v=R9jOWIhZZCE) (really gets good around 2:15 onward)

Bonus video: [Justice's "Neverender" official lyric video](https://www.youtube.com/watch?v=47YNsf-7Y7c) with XY-mode oscilloscope visuals

### Paul #2: μCritter

[uCritAir, or microcritter](https://www.ucritter.com) is a small handheld device that is both a game and an air quality sensor. It's primary purpose is as an air quality sensor, and includes USB-C charging, WiFi and Bluetooth, a microSD card for data logging, a battery, a speaker, and both an eInk and touchscreen LCD screens.  The eInk dispaly is meant to be used, for example, sitting on your desk monitoring the air quality and the LCD screen is for gaming.

The game is a virtual pet called the μCritter, who is healthiest when the air quality around you is the best. The μCritAir continuously samples the air quality around you give your μCritter the simulated experience of the air you're breathing.

It also includes some fast paced arcade games where you can earn coins that you spend in their Vending Machine. You can "purchase" upgrades for your μCritter from the Vending Machine, with things like baseballs, furniture, and more.

It's also [open source certified with OSHWA](https://certification.oshwa.org/us002714.html) and the firmware and hardware is [available on GitHub](https://github.com/ucritair).  It looks to be built on top of Zephyr.

### Tod #2: Buchla & Friends synth get-together

[Buchla & Friends](https://www.reddit.com/r/synthesizers/comments/1i5yteb/this_weekend_buchla_friends_2025_the_two_day/) was an annual two-day event on the weekend of 25 Jan 2025. It was during the big [NAMM conference](https://www.namm.org/), think CES-for-music, so lots of synth makers from all over the world were already in Los Angeles.  But unlike NAMM, the Buchla & Friends event had many small synth makers that I think are the lifeblood of the industry.  John Park & I went and it was a lot of fun.

One really nice aspect was that it was a "headphone-only" event.
So even though it was full of synths and people playing them, you could still chat with people
(which is not true at NAMM)

One of the best instruments we saw was this thing called ["Quord"](https://soundwork.shop), a 100%-analog 4-voice drone synth with a very playable interface. I've built a few drone synths ([in circuitpython](https://gist.github.com/todbot/532e069845c2cc4c1bc39c9162a34bfe), [in arduino](https://github.com/todbot/macropadsynthplug/blob/main/arduino/dronesynth/dronesynth.ino)) and the Quord has inspired me to revisit this idea in CircuitPython to see if I can get something as fun and playable.

Some videos of the event:
- [Tod & JP at Buchla & Friends](https://bsky.app/profile/todbot.bsky.social/post/3lgmaoneeuk2e)
- [Quord preview](https://www.youtube.com/watch?v=MRkyQq8vd7U)
- [Rain City Modular, Under the Big Tree (playlist)](https://youtu.be/WaRUUxJo5Z0?si=ycqipL4V6pFDd6so&t=62)
- [Walkthrough by Sonic State](https://www.youtube.com/watch?v=DJxKEjer_AE)
- [Piqued FM reacts](https://www.youtube.com/watch?v=By-shXpcjSg)

![Tod at Buchla & Friends playing a synth](todbot-buchla.jpg)

### Paul #3: Inventory Management for Makers

"Inventory" is an [open source project](https://github.com/dunkelstern/inventory) for managing small parts inventory. It had it's 1.0 release in January with the best release name: "It's finally 1.0 after 5 years"

It describes itself as a *flexible parts database which keeps all relevant information as well as datasheets, prices and a visual representation where you stored the part. The idea is that the system may tell you in which compartment of which box in what area of your workshop you have to search for to find the part you currently need. It has been optimized to store information for electronics parts and small other hardware like screws, nuts and bolts.*

It is a Python app written using the Django web framework and Poetry for dependency management.

Features include:
* Currency
* Add or manage multiple users
* "Box view", which is a container full of parts that you customize to show number of compartments and number of items in each.
* Inventory management including adding tags, pricing, order information and you can attach a datasheet.
