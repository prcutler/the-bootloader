---
date: 2022-10-07
title: "Welcome Liz Clark"
linkTitle: "Episode 13 - October 7, 2024"
description: "Welcome Liz Clark"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

Welcome to our first guest, Liz Clark aka BlitzCityDIY.  Liz, Paul, and Tod chat about a new iOS app from Adafruit, the new Raspberry Pi AI camera, maker skill trees, and more.

Join our newsletter!  Keep up with the show and what Paul and Tod are up to.  Visit [The Bootloader's newsletter page](https://buttondown.com/thebootloader) to browse the archives or subscribe.

You can [read the entire transcript](https://thebootloader.net/blog/2024/10/07/episode-13-transcript) here.

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/welcome-liz-clark/embed/dark"></iframe>

## Show Notes

### 00:25 Adafruit itsaSNAP iOS App (Liz #1)
I have to say I'm a little biased with this pick because I contract with Adafruit, but I'm mildly obsessed with the new itsaSNAP app. This is the latest iOS app from Adafruit by our iOS developer Trevor. It acts as a bridge between your iOS device and your Adafruit IO feeds. There is support for Apple Shortcuts, which means that you can log health data, home data, any data that's on your iOS device. You can also read feeds from the device and have Adafruit IO affect tasks on your phone. I've worked on two guides with it so far. The first uses a Qualia board with a round display to show photos from my photos app. I'm able to encode the photo in a Shortcut, send it to an IO feed and then decode it with CircuitPython. I've also worked with using Matter devices in Apple HomeKit with itsaSNAP to log sensor data and also to control an RGB light strip. I'm really excited about all of the functionality and I'm looking forward to seeing what people do with it.

  - [itsaSNAP Intro Learn Guide](https://learn.adafruit.com/it-s-a-snap-by-adafruit/overview)
  - [Qualia S3 Photo Frame](https://learn.adafruit.com/qualia-s3-ios-photo-display-with-itsasnap)
  - [Health Status Board](https://learn.adafruit.com/itssnap-apple-fitness-status-board)

### 5:09 Raspberry Pi AI Camera Module (Tod #1)
There is a new camera module from Raspberry Pi. It's an "AI" camera.  What does that mean?
It appears as a regular camera to the Pi, plugs into the CSI camera port.
The "AI" part is that it has an RP2040 and 16MB of flash to store a pre-trained AI model you upload to it.

This is the kind of Machine learning (oh I mean "AI") I prefer: on the edge, at the device, rather than in the cloud.
The ML models live in the camera module. Results are delivered frame-synced alongside regular camera data over I2C.

You upload models via I2C too. It takes several minutes to upload an 8MB model.
And like all these AI models are static, they don't learn: their categorization is baked-in.
This is expected but I think means you can't use newer techniques with models that learn.

There's really good docs so far. Easy-to-use command-line tools and a nice Python library.

More on-device ML devices please.

  - [Raspberry Pi blog post](https://www.raspberrypi.com/news/raspberry-pi-ai-camera-on-sale-now/)
  - [Hackster hands-on article]( https://www.hackster.io/news/raspberry-pi-s-ai-eye-hands-on-with-the-raspberry-pi-ai-camera-module-383fb34afcf7)
  - [Getting started](https://www.raspberrypi.com/documentation/accessories/ai-camera.html)
  - [Picamera2 repo](https://github.com/raspberrypi/picamera2)
  - demo videos: [Pose estimation](https://www.youtube.com/watch?v=rloJNA_VuSA), [Object detection](https://www.youtube.com/watch?v=D-foRupzOiY)

  Also see:

  - [Person sensor by UsefulSensors $10](https://www.sparkfun.com/products/21231)
  - [We talk about in Bootloader Episode #3](https://thebootloader.net/blog/2022/10/24/episode-3-the-middle-is-a-pumpkin/#person-sensor-by-useful-sensorshttpswwwsparkfuncomproducts21231-tod-2-935)
  - [Twitter thread with my eye that follows you](https://x.com/todbot/status/1584662808691896320)


### 10:05 The Bumpin' Sticker by Guy Dupont (Paul #1)
Guy Dupont creates his take on the "Keep Honkin' I'm Listening to..." bumper stickers.  Using a Raspberry Pi Zero 2W, a screen from Ali Express, a Particle IoT board, and his Last.fm account, the screen dsiplays a bumper sticker with what Guy is currently listening to.
* Guy Dupont on [The CircuitPython Show](https://www.circuitpythonshow.com/@circuitpythonshow/episodes/guy-dupont)
* Guy Dupont [MakerChat on CircuitPython Day 2024](https://www.youtube.com/watch?v=cJ2dCxfGfyk)
* [The Bumpin' Sticker](https://www.youtube.com/watch?v=mWRPRW6pHIY) YouTube video
* [GitHub Repository](https://github.com/dupontgu/now-playing-bumper-sticker)

### 13:40 Nothing To See/Hear : Wireless Fuzz Pedal (Liz #2)
I follow quite a few guitar pedal folks on instagram and saw the newest post from @different.noises last week. It's a "wireless fuzz" that completes the circuit by transmitting it via an infrared LED. The circuit converts the signal from the guitar to headphone audio level and then again into light that is sent out the infrared transmitter to an infrared LED. He includes the schematic in the post as well as an explainer and a few demo videos to prove that the signal is in fact transmitting via infrared.
  - [Nothing To See/Hear : Wireless Fuzz Pedal Post](https://www.instagram.com/p/DAb1d48TZ7N/?igsh=bjBtaDZtaWl5YWs0&img_index=1)
  - [different.noises on Instagram](https://www.instagram.com/different.noises/)

### 16:10 X1Plus alternative open source Bambu X1 firmware (Tod #2)

I've been thinking of getting a new 3d printer. My Prusa mk2.5s has seen better days.
And I'm wowed at the literal 2x speed improvement I could get out of a Prusa mk4s or a Bambulab X1.
So when I discovered this X1Plus alternative firmware for the X1, I was intrigued.

The X1Plus firmware runs on the "application processor" (AP) board of the X1,
(sort of like what Octoprint does for me currently). It doesn't touch the motion control system.
And seems like all does to the the AP firmware is patch the bootloader to also look for a firmware file on the SD card, and use that if present.
So you can always go back to stock firmware quickly.

And the team behind it have started a CrowdSupply campaign for an expansion board X1Plus can use for
extra features light lights and cameras.  I don't think I'd want this, but I'm glad they're finding a funding path for the keep them going.

  - [X1Plus](https://github.com/X1Plus/X1Plus/wiki)
  - [X1Plus expansion board crowdfunding](https://www.crowdsupply.com/accelerated-tech/x1plus-expansion-board)
  - [Hackster article](https://www.crowdsupply.com/accelerated-tech/x1plus-expansion-board)

Also to consider: [Craftcloud 3D printing service](https://craftcloud3d.com/)

I've done a few runs using Craftcloud and the results are pretty good. Like renting a Bambu.
Craftcloud is a service front-end for a bunch of additive manufacturing companies across the US.
Some offer metal as a material.  Their quoting system is pretty easy just to get an idea of the cost.
As an idea of costs: it costs about $4 per piece (inc shipping) for a typical synth enclosure.

### 22:31 Maker (and more) Skill Trees (Paul #2)
Steph Piper aka Maker Queen has created [Maker Skill Trees](https://www.makerqueen.com.au/skill-trees-1) as a way to track your progress across a range of skills.  These include things like PCB Design, 3D Printing and Modeling, and Dev Boards to crafting skills like Crochet, Knitting and more.  There are almost sixty different skill treens to pick from.  Each skill tree has 73 skills or experience hexagon tiles, with basic skills at the bottom to more advanced skills at the top.

There's a [web app to create your own skill tree apps](https://schme16.github.io/MakerSkillTree-Generator/) designed by [Shane Gadsby](https://github.com/schme16).

There's also a book in development with an even more expansive range of skill trees, tools to track your progress and calculate your life score across all areas.
