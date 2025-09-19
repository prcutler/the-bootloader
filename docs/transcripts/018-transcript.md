---
date: 2025-03-03
title: "Episode 18 Transcript"
linkTitle: "Episode 18 Transcript"
description: "Episode 18 Transcript - Welcome Brent Rubell"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to The Bootloader. I'm Tod Kurt.

And I'm Paul Cutler. We're excited to welcome a special guest today, Brent Rubell of Adafruit Industries.

The show works like this. We've each brought two things to share, which we'll talk about, but for no longer than five minutes each.

We have detailed show notes and transcripts available at the bootloader.net.

Brent, welcome to the show.

Hello. Happy to be here.

What's the first one that you brought for us this episode?

Okay, for my first one, we have Wippersnapper.

is offline mode. So I'm biased on this note. I work for Adafruit as an engineer.

Back up and explain this site, I'm Wippersnapper' as firmware I work on. It enables people to

visually create internet-connected electronics project. It means you can click your way into a

functioning prototype. No programming involved. It's really good for scientists, artists, and

non-technical people to get projects off the ground that they want to get going. And my colleague,

Loren and I work on Wippersnapper. He's like the website of things. I'm the embedded side of things.

And we also have other people work in this project,

but we're the main two leads.

It's been pretty fun.

It's been out for a while now.

I think we were talking about that Paul.

It's like the original guide's like 2020.

And it was an alpha, then beta.

Now the beta tag's about to be ripped off.

So we spent the last year re-doing the API,

that involves rewriting the firmware.

And then like one of the more fun things I think that we've added is offline mode.

So like we didn't intend to add this feature at all.

I needed a way of testing the API and functionality.

And Loren was like, he's busy as something.

else right now as far as development.

And usually we work in tandem, like, he'll implement things, and then I'll come in on

the embedded site and I'll implement things, and then we'll just, like, work like that.

But right now, it's like I was stuck.

So we added this feature that allows you to create a project on Adafruit I.O.

Download a file, which is like a JSON encoded file, and then you just drag it onto the device.

Then the device reads back this file and, like, automatically configure it to itself.

So there's logging data out to an SD card.

So there's like no network connection, but the grand idea of like creating a device by clicking some buttons on a website still exists.

It's cool.

There's like nothing like this where you can just create a project and download it and starts logging data.

And it's also sitting, it's like doing a magic trick where it sits on the same firmware.

So if you insert an SD card and add this like special file, then it will switch into offline mode.

And if you don't do that, it will switch into online mode and start logging out to Adafird iOS.

So, like, this is a totally weird little side project that I'm working on that I think is going to be really useful for mostly, like, people working on environmental sensing projects because it's like the existing ways of getting these up and running do involve programming.

Or they do involve buying this, like, NCD makes these like $3 to $400 versions of this, which are like kind of expensive for like a nonprofit.

So like the board I used in the guide is like the.

Adalogger, which is like really cheap, and then like a BME sensor, which is also like,

so the whole thing comes in under $50, which is a big difference from $400.

Totally.

And this is kind of amazing because like, I mean, first there's just the Wippersnapper thing

itself, which totally solved sort of the last conceptual mile problem for me of like,

okay, I've got a thing that can send MQTT messages and maybe I set up a broker somewhere,

but then how do I actually configure what all the messages mean?

And how do I ensure that there's no sort of decay between the sender and the receiver?

And like Wippersnapper and Adafruit Io kind of made all that just not be a problem.

It just kind of you configure it and it updates the device.

And now you can do that for data logging, which is, I don't know, it seems like a totally separate thing than Wippersnapper to me.

A huge thing.

It's almost to have its own separate name to me.

But I like that it's under the umbrella of Wippersnapper.

So it's all the same configuration, all the same UI that you use to configure it.

Yeah, I mean, the name's immutable.

I haven't changed it yet.

I haven't done anything.

I'm just like, well, it logs offline and it also sends the online.

But I haven't, if you have a name, Tod, like, let me know.

I have no idea.

I mean, that's the thing is that I think drafting off the Wippersnapper concept is really handy

because people know that, like, oh, I can use Wippersnapper to quickly configure a device.

Like, I want to hook up this sensor to this pin and this other sensor to this other pin.

And that, you don't have to write any code to do that.

You just drag and drop in things.

If that is what Wippersnapper is, then the output mode could either be MQTT or it can be an SD card text file, I guess.

Yeah.

And I got to believe there's a subset of people out there who don't want to connect to AtaFruid I.O.

Or don't want it network connected.

So this is a great tool for those kind of people who want to keep their devices offline or off the IoT networks or whatever they're doing.

I think that's growing too.

You're seeing like home assistant and more project that popular because it's like people don't want to put their.

data on like commercial servers or like a different server is pretty great as far as like

maintaining your like privacy rights but like the bigger like AWS and Google and also like

wherever my robot vacuum sends the server image like the image of my house that's like later

later mapped I don't know where it's going but like an SD card that I can like pop out a device

that's pretty rad yeah I mean also just for just for longevity like the internet between your

device and the server recording the information, there are so many points of failure there.

And with the SD card, it's just the device.

There's like so few places it can go wrong.

I'm glad we have that alternative now.

Awesome.

Thanks.

All right, Tod, what did you bring us this episode?

Okay, so a couple weeks ago, maybe two weeks, one week, there is now 200 megahertz clock

support for the RP 2040.

Good news, everyone.

What does this mean?

It's a free speed boost for your pico.

Raspberry Pi officially supports overclocking the PICO RP2040.

When the RP2040 chip that's in the PICO was first announced,

the PICO SDK library that you use with it ran the chip at 125 meghertz,

even though the data sheet for the chip says it's 133 meghertz parts.

So it's already a little bit of like, hey, why is it underclocked?

Sometimes that means that the manufacturer is a little bit conservative with their design,

so they kind of run it slower than what their specs were, just in case there's problems.

But it turned out the RP2040 has been incredibly overclockable.

People have been doubling its speed to 250 megahertz with no downsides as far as pretty much I've known that you can do this.

Many of my RP20-based CircuitPython synth projects run at that 250 megahertz because you can get a higher quality sample rate for your audio stuff.

And normally overclocking on CPUs is frowned upon by the manufacturer.

You can actually burn up a desktop CPU when you overclock it.

So Intel is usually like, no, you know.

But of course, there's all these cool gamer overclocking rigs that have been liquid cooled and stuff

to make it until you like double the speed.

So some of the vendors who have made RP20-based things have been reluctant to sell something

that depended upon an overclockerty-2040 because of this sort of historical fear.

But then last week, Raspberry Pi officially announced that the PICO SDK will default to 200 megahertz.

That's almost twice the speed.

It's like 60% faster or 70% is half faster.

and that speed can be configured via compile time to find.

In CircuitPython and in the Arduino Pico Arduino Core for the RP2040,

changing the CPU speed has always been pretty easy.

In CircuitPython, you can do it in real time, in the REPL even,

by just setting the microcontroller.computer.

One of the things you can use that for is you can underclock the CPU

to make the chip draw less power when it's on a battery.

Because one of the cool things about microcontrollers is their power usage scales

pretty linearly with clock speed.

So if you half the speed of the microcontroller,

it's going to draw half the power, almost exactly.

And in Arduino, you can do it with a compile time directive

that's just in the tool CPU speed menu in the Arduino IDE.

It's been pretty cool that we've been able to do this

without any seeming repercussions.

Like there's this one guy who makes a project called Pico Gus, GUS.

It's a sound card, like an old IBM sound.

sound card, Gravis Ultrasound, I think was the name of the sound card, that is emulated with a

RP2040 chip. And he runs that at 366 megahertz. So clearly, clearly the Raspberry Pi team

who've designed this chip did a pretty good job because it's so overclockable. And now Raspberry

Pi officially supports it. It seemed like it just came out of nowhere after having the RP 2040

around for three, four years for them just to support it. Sure, people like you were doing it,

But all of a sudden they just dropped that news and everyone's like, oh, my goodness, this is so cool.

Yeah, yeah, it makes me almost wonder if they're like, hmm, well, everybody's been doing it and there haven't been any reported problems.

So let's just make it official.

Are there any heat issues?

You know, I don't, I've not detected any.

Just from the very gross determination of putting my finger on the chip, like normally when chips or my controlers running hot, you can just kind of feel it.

Go, okay, that doesn't feel right.

There's really no obvious observable problems as far as far as I've seen.

Yeah, so yay for us.

So hey, Paul, what's your first one this week?

I'm going to come back to something that we've touched on before,

but that's microcontrollers as mini computers.

Microcontrollers are so powerful that we're starting to see almost full-fledged mini-computers being built,

which we have talked about in a past episode.

We're getting closer every day,

and a maker named Abe Haskins has built a small handheld computer called the Slime Deck Zero

using Pimoroni's Pico Vision as its brain.

Abe has a great 25-minute video up on YouTube,

It might sound like it's a little long, but it's engaging as all heck,

and I highly recommend checking it out.

He shows the entire process and all the parts used to build this tiny handheld computer

that runs MicroPython, has an app launcher and operating system called Slime OS,

and even has an expansion slot to add additional hardware peripherals.

It features a keyboard he disassembled from a $9 remote control,

a 5-inch 800-by-460 screen, and uses the Pico Vision from Pimoroni as its brains.

The PicoVision features two RP2040 chips,

one acting as the CPU and the other is the GPU.

He created a custom PCB for the keyboard

to talk to the PicoVision over I-2C using a quick StemmaQT port.

One of the neatest features of the Slime Deck Zero

is that Abe added this expansion port.

Abe demos it by plugging a XIAO microcontroller

in that's wired to an LED that the slime deck zero could control.

It's running MicroPython,

and Abe has created a custom app launcher for it.

It's also aware when something is plugged into the expansion port and can display an app if applicable for the hardware plugged into the port.

The second one is the new Adafruit Fruit Jam.

This handheld is something Adafruits been teasing for the last few weeks, which they've codenamed Fruit Jam.

I don't think it'll be the final name.

Lady Ada was inspired from a recent Hackaday hackchat with Raspberry Pi's Eben Upton and built a credit card-sized computer using a Raspberry Pi 2350B chip, the one with the

extra GPIO. The number of peripherals built in on the fruit jam is crazy. It includes 16 mega flash and

8 megs of RAM, a microSD card, DVI output using the new HSTX port, I2S stereo headphone and a

mono speaker, not one, but two USB type A ports for USB host for things like keyboards, mice,

or game controllers, StemmaQT, and Stemma Classic, I spy for TFT displays, five neopixels, and

and three switches.

So this is literally almost a motherboard for a handheld mini computer.

Scott Shawcroft, CircuitPython's lead developer,

has been sharing progress on it during his Friday deep dive streams.

I can't wait to get my hands on one of these.

As soon as they put it up for pre-order it,

I'm like, notify me, notify me and put my email with this in right away.

Yeah, it's just begging to be made into a little tiny video game console-looking box

because it's got the two USB ports on the front,

like what I'm considering the front,

and then it's got the video and power port out the back.

I can see a little Nintendo-style box for it

coming out pretty quickly for it.

And there are these little $10-NES-like USB controllers

you can get to plug in.

And the Fruit Jam also has a row of, I think,

maybe 20 or 10 GPIO pins located right behind the USB

ports, and that's on, I'm thinking, oh, that's a cartridge slot.

Oh.

I mean, the board already has so much memory on it.

You don't need to add more memory with a cartridge, but maybe the cartridge is basically

just a wiring diagram that kind of enables different programs that are already on the

fruit gem itself to load.

But it'd be fun to actually plug the cartridge in and then play the video game.

Absolutely.

We want the slime deck.

I'm really interested in the fact that it has the expansion port.

I've been seeing more expansion ports on devices, like the framework, lap,

top super popular and it has this expansion port and people love it.

And they're like, oh, it could be a USB port, could be a SD card reader.

Like, I feel that's getting more popular as far as like things that people want there.

And the flipper zero has the same thing too.

It's like, how can I expand this hardware that already has some level of functionality?

And I don't know.

It's interesting to like, see people.

So like, I built this little computer and it's like, what else can I do?

Oh, maybe I should be able to plug in something.

But then it comes back to like, what do I plug in?

Right.

Yeah.

Yeah.

And with the slime deck, I think it's interesting that he plugged in a full-blown microcontroller.

It's not like he just plugged in a humidity sensor or something to see a whole Cidzia board attached to it being controlled from the Picovision device, from that brain, was pretty neat.

Yeah, and the build looks pretty good.

I'm just kind of amazed that we have microcontrollers that can spit out essentially HTML and also do Wi-Fi and Bluetooth.

And it's just like, it's a $5 microcontroller.

Right.

All right, Brent, what's your second one for us?

Yeah, a second one.

Did you guys talk about Obsidian before?

We have not.

All right.

I've used like this Evernote program for years.

I think John Park uses it too.

I have so many notes and EFernote.

I tried Notion.

Everybody in the software field loves the notion.

And it's too advanced.

They don't need an entire Wikipedia like system for just my notes.

So Obsidian's a Notes app.

It's kind of boring, but it's good because it's boring.

So all of your notes are stored on the vice you're writing them.

I guess the theme today is from my brain is offline storage.

Everything stored is a markdown file.

And you can pop each file open in your editor.

So in the age of cloud first, it's like great.

You can see all your folders.

You can see all your files in a folder.

It just feels right.

It's like I'm writing this file.

This file is located here.

It's not I'm writing this file.

It's going to a server somewhere and I don't have this file anymore.

What I like is how little it does and how much it can be extended based on how little it does.

So like instead of Notions, wiki system, you can actually link each Markdown note together.

which is really powerful.

And if you want to do wiki stuff, you can create your own.

And then you can create like little workflows by combining obsidian and another application.

So it's not all like notion like sitting in one.

So like I use Zotero to organize academic papers, journal articles.

Then I can link Zotero entries in my notes.

And that's it.

Like that's the whole workflow.

Another one I have is like Obsidian has a paid plan which lets you sink.

But I don't necessarily need the other things under plan.

So I can just, these are files, right, like to sit on my device.

So, like, I have a Google Drive folder.

I move my Obsidian Storage right into that folder.

And there, it's, like, syncing.

And these are marked down files, so each of them will show versioning through Google Drive.

So there's, like, three storage and free versioning, which is really great.

And, yeah, it's definitely like a program I've been using a lot for every type of note taking.

Yeah, I used to be a big Evernote user and stopped when they started down the road of incitification.

And I tried Obsidian and was a little overwhelmed by it at the time.

And switched to an app called Bear, which is a MacOS note taking very similar where it's marked down only.

But it's got syncing.

But it was also a third the price of Obsidian from a yearly perspective.

And I'm cheap.

But one of the really neat things I think about Obsidian is there's over 2,200 different plugins for it that you can add extra functionality.

It's just a, if there's something you want to display in a note in a different way,

they probably have a plugin that'll do it for you.

I only have one plugin and it's command where I just command it and I just type like date time and it puts like the current time stamp on it.

And that's all I need.

Like I need a way of just inlining dates into my notes.

I think I tried Obsidian many years ago like when it first came out.

And I think I wasn't so steeped in Markdown that I just was kind of like, meh.

But like now that I live and breathe Markdown every day, I think I think it's time to revisit Obsidian.

because I'm already trying to take notes in Markdown in the Mac Notes app

and getting frustrated that doesn't do it like I think it should.

I didn't even know it does it.

Yeah, that's awesome.

Yeah, I think.

And also, Obsidian has an iOS app, which is nice, looks like.

Yeah, they support all the different platforms.

If you want to sync your data, it's Android, iOS, Mac, Windows, Linux.

I know a lot of Linux users who use Obsidian.

Yeah.

Yeah, thanks, Brent.

I think I'm going to try this out.

I'm always looking for a good note system.

Trying it again.

Totally.

All right, Tod, what's your second one for us?

Paul and I and Cedar Grove Studios, aka Jan,

just did a CircuitPython show

about the CircuitPython Community Bundle.

In the Arduino world, the closest equivalent

is the Arduino Library Manager's list of libraries.

One of my favorite ways to observe updates to that list

was the Arduino Libs Twitter bot

that posted whenever libraries were added or updated.

With Twitter gone,

And thankfully, the bot has moved on to both Macedon and Blue Sky.

And I've always wondered how it got that information.

And I looked into it.

And I think it's just looking at the pull requests from the Arduino Library Registry GitHub,

which I've done in the past.

I've just looked through their PRs and seen what people have been adding to it.

But it's one of the few ways that the GitHub interface is actually kind of poor to see those changes.

So with this bot, you get to see it all in a nice little social media post size.

with a link to the actual repo.

The bot itself promises no more than six posts per hour,

so it doesn't overwhelm your feed,

which I've had to unsubscribe to some other bots that I've liked

because they just kind of flooded my timeline.

And I really like poking around the libraries that people have been writing

to see kind of what people are thinking about,

what kind of tasks they're trying to solve,

and get as a gauge on the state of the Arduino community.

A couple examples that just came out.

As I was thinking about this,

this was like maybe yesterday the day before,

There's a library called YAMLDuino that lets you do YAML file parsing and writing in Arduino, which is pretty awesome because YAML has been infecting my life more and more.

I'll be using whatever the successor is to Obsidian is that's all in YAML instead of Markdown.

There's a library for writing Discord bots called Ucini Discord Webhook.

And we'll have links to all these in the show notes, of course.

There is a library called CodeCell that's essentially,

a sort of board

abstraction library

for this tiny coin-sized

ESP32C3-based board

that has a lipo charger,

9-axis IMU, and a light sensor

all on something about the size of a quarter.

Here's an example of where the library shows you

new hardware. Just looking

at this library feed shows you new hardware.

So that's pretty interesting.

I don't have, I don't do wearables, but this is like a really

cool board for doing wearable stuff.

And another one is a library called Google Find My Tools that works not just for Arduino,

but also for like Zephyr-based embedded devices, but it turns an ESP32 into a Find My device

on the Google Find My network.

So if you wanted to make little tokens that like joined that so you could like track something,

I've been wanting to put an air tag on my cat to see where he goes, where he gets up to.

I'll have links, but Arduino Libs on Fostodon, on Mastodon, and Arduino,

libs.bsky.com

The maintainer is someone named Toboso.

So if you do like Arduino Libs, give him a shout or give them a shout out because I love this thing.

Okay, Paul, what's your second and final thing for this week`?

I recently came across a story that I was so excited to share because it combines two of my passions,

vinyl records and 3D printings.

But there's a catch, which I'll come to at the end of this.

So just bear with me for a minute.

But Amanda Ghassaei has one of the most in-depth tutorials and project recaps of

ever seen. She was able to use a resin 3D printer to recreate a 3D printed record that can play

on a normal record player with a normal stylus. On her Instructibles page, she first shares how a record

works as the needle spins along the grooves of a record and vibrates and produces audio signals.

She then walks through how she calculated the sampling rate for a 3D printer and all the math

that goes along with it, which I'm not going to get into here, but trust me when I say it's detailed.

She calculates the sampling frequency, revolutions per second, and inches per revolution to get a max sampling frequency of 12 kilohertz.

She then prepared some test files to print to understand what might be possible with the printer and to optimize the size of the grooves in the record.

She tested a few different amplitudes, depths, and groove widths, and printed three test prints to figure out what was possible.

To do that, she used an Arduino sketch called processing to create sine waves, convert those to an SDL file that could be.

be printed. After the third test was complete, she had the groove depth, the width,

and the frequency range figured out. She then wrote a Python program to convert a wave file to an

array of integers and be converted into a text file. She can import that text file into the processing

sketch to convert it into an STL. Her instructables page contains examples using the song DeBaser

from the Pixies and New Order's Blue Monday. You can clearly understand the songs, though with

the distortion, it sounds worse than an AM radio station, but it's impressive for having done it herself.

The catch was this article was from 2012.

There were a few giveaways in the article.

When she compared 3D printers, she was talking about her resin printer, she compared it to a maker bot and a reprap.

And right there, my radar went off that, oh, you know, people aren't really using those 3D printers anymore.

And her Python program uses Python 2.5, which is ancient.

Wow.

Exactly.

I didn't really catch it until I started reading the comments

and one of the oldest comments is from 12 years ago,

but newer comments are from just a few months ago,

so other people like me are just discovering it.

The YouTube videos that she posted are about six years old.

Now, she was using a commercial object Connect's 500 printer,

and I'm curious to know in the last 10 to 12 years

how far resin printers have come

to know if you can make an even better sounding record today.

In more modern news, The Guardian just published an article on February 25th also about creating your own records,

but using a custom kit from Ulrich Sorosso.

It's a lathe cutting machine that uses a diamond needle to cut a record one at a time in real time.

People in the UK are using them to create custom pressings of, say, 20 to maybe 100 records that artists or bands can sell,

who might not be able to afford a regular vinyl pressing.

The catch with this one is Ulrich Sorosso is a cash-only.

operation. And if you want to buy one, you'll need about 7,000 pounds, hand delivered to him in the Black Forest of Germany.

What?

So we'll have links to both of those in the show notes.

That doesn't sound sketchy at all.

No, not at all.

They talked to a number of makers who are making records that have done that.

They've gone over, paid them the money in cash.

It's cash only, and came home with the lathe.

That's really cool.

Wasn't there in like the 40s or 50s, like a record cutting thing you could go and get your photo taken at a event, a little coin operator photo thing?

There was a similar thing where you could go and put a quarter in and record a little message onto a tiny record that would engrave it in real time?

And I think they're still around.

I want to say that Jack White of the White Stripes has he has a couple record stores, one in Nashville, one in the UK.

And I know that the one in Nashville, I want to say that he's got a machine that does that.

I don't know if you can personally record,

but he has artists in there and they press the records

as soon as the mini concert is over.

I've got a couple of them.

It's pretty cool.

That's amazing.

I'm glad the records are still being made.

That makes two of us.

Yeah, I'm getting more popular.

This project's incredible.

Amanda's work is totally incredible.

You're making a record from nothing.

3D printing is always cool because it's like additive manufacturing.

The Guardian one's really cool too because then it's like,

okay, let's like make these

but like sound good.

And I wonder people have done this

with like laser cutting like as far as

Oh yeah. Actually

she did an if you visit her homepage

she's got a list of all of her projects.

In 2012 she did this project

and then in 2013 she revisited

it using a laser cutter.

So she's been all over it.

Her website is incredible. It's got so many

amazing projects all across the

space. I recommend

anyone go to her website to see

some amazing projects.

Well, that's our show.

For detailed show notes and transcripts,

visit the bootloader.net.

Thanks, Brent, for joining us.

And until next time, stay positive.



