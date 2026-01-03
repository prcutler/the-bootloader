---
date: 2025-02-03
title: "Episode 17 Transcript"
linkTitle: "Episode 17 Transcript"
description: "Episode 17 Transcript - Bamboozled"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to The Bootloader. I'm Paul Cutler.

And I'm Tod Kurt. If you want to learn more about this podcast, visit thebootloader.net

for show notes and transcripts, and we can also find our newsletter. Paul, what's the

first thing we're going to talk about today?

We're going to talk about drama in the world of 3D printing, because there's just been

a little of that lately.

Just a little.

And some of the drama includes Printables pulling the 3D Benchy models. The 3D Benchy

model is a small boat that's used to diagnose issues with your 3D printer.

It was originally created by Creative Tools, who was recently acquired by another company

called NTI Group, and it was originally licensed under a CC BY no derivatives license.

The non-derivatives license means you can't use the model and remix it into other shapes.

And if you're in the 3D printing community, you probably know that there are dozens of

remixes.

And remixes are kind of a thing one does in the 3D printing community.

always like sticking some random head on some other random part of a 3D print.

Well, it turns out that Printables is doing this on their own. That they saw

the license and they're just shutting it down. The original copyright holders

don't have a problem with it, even though they haven't changed their license. But

I'll leave the links to that in the show notes. That's not the real drama going on

these last few weeks in the world of 3D printing. Let's talk about Bambu Labs,

who's going to add a new authorization control system, they call it, to their 3D printing software.

So we've talked about Bambu Labs many times in the podcast going all the way back to episode one.

Back in episode one, I had shared it as my best friend had bought one. Six months later,

I bought a P1P. I've been a big fan of Bambu. I know they're not open source, but I was willing

to put that aside for the benefits of speed and quality that came with it. Well, the community is

up in arms. To oversimplify, Bambu claims that this is a security enhancement, but hasn't exactly

said why it's needed. So let's just break it down because I'll oversimplify a couple of different

things. First up is there's one Reddit user who is the main developer behind a project called

OpenSpool who hypothesizes that their project might have contributed to this problem.

With OpenSpool, you attach an NFC sticker to your filament and then you build an ESP32 NFC reader

and place it next to your printer.

Touching the filament to the reader

automatically updates your filament settings

on your Bambu printer.

They say it's almost as seamless as

using the Bambu filament with an AMS.

Maybe Bambu saw that as a threat to

their filament business and wants to shut that down.

The other one that's really affected is OrcaSlicer.

This is the slicer I personally use instead of BambuSlicer.

I like OrcaSlicer because one, it's open source,

and I use it primarily for some of its calibration features,

and they tend to release features a bit faster than Bambu does.

Bambu did release a short video showing how it adds one extra step to OrcaSlicer

by using their new Bambu Connect app.

Anyway, Bambu shared a blog post where they tried to clarify that this isn't about third-party software integration,

but it's hard to not think that it is,

especially when it's not clear what they're trying to secure.

Yeah.

So what can you do?

Bambu claims that the firmware update will be optional,

but even that raises questions.

If you don't update, you'll probably miss out on future features and better improvements.

You can also jailbreak your Bambu X1 Carbon.

There's the X1 Plus firmware, which we covered back in episode 13 last October.

And someone is also working on a Clipper conversion for Bambu printers as well.

I have lots of links in the show notes with more information and details for those who want them.

Suffice to say that Reddit is up in arms.

There's hundreds of posts, and I've tried to break them down into just a couple that give you

information about it. The moderators of one of the Bambu subreddits tended to

be Bambu employees, so now there's a new subreddit up for Bambu customers to use.

And it's just crazy how much up in arms the community is. It's debatable whether

it's in shitification or not. I can understand their concerns. There was a

security engineer who did post on Reddit and said this isn't actually a bad thing

and here's kind of why.

But at the same time, like I've mentioned earlier,

they haven't really said why they need these security

enhancements or what they're trying to protect from

other than people in the community going, well, my

project is going to be affected and here's how and

why. Yeah, it's super frustrating because like Bambu

has been so good in their communication, both their

technical design, but also the design of like the

documentation and the software that controls the

printer. It's just like they know how to run a company.

you know, much more than a lot of these other open source 3D printer companies that turned popular

and then had to like backtrack on their open source sort of promises. But Bambu has always

been very professional and this seems kind of an unprofessional response from them. So it's

unclear what's truly going on. One of the hypotheses I heard that I, like the more

charitable hypothesis, is that Bambu has seen a lot more use in institutional settings like schools

and companies that have small 3D printer farms.

Because of the current setup, you can on your phone just start a print when you're not on

the premises, which is a terrible, not a security problem, but just a terrible access control

problem for the printer.

What could cause the printer to mess up at three in the morning if some person randomly

butt prints off their phone?

You bring up a good point.

that print farms might be one of the leading causes of this as well.

Yeah, and so you often see systems having to be redesigned a bit to work in a multi-user

environment with like potentially less skilled users that don't have true ownership of the

device. And so I can see like that's like kind of the more charitable reading. Unfortunately,

I'm a victim of both the MakerBot problem where they went from being a very community-driven thing

to being owned by Stratasys and you know, kind of crapping it all up.

And also a big Prusa convert who promised 100% open source forever and their recent

printers have been just going less and less open source.

And so it's just like, I'm just kind of sighing and shrugging with the Bambu.

It's like, well, you know, it's still a really good printer.

I was on the verge of buying one before the beginning of the year wildfires happened in

here.

And I would probably still recommend them.

To me, a lot of this is overblown.

Yes, it's a step backwards in some ways, but it could be a step forwards in others.

From a user experience, the average user, if you're using the Bambu slicer, you're

not going to notice anything different.

Nothing changes.

It's only for those advanced users, probably the vocal minority, who are doing things with

things like OrcaSlicer or with other firmware.

So to the average person, this isn't going to affect the way that they're 3D printing

at all.

all for them being fully closed down, but I want to be able to use the printer on my

LAN without having to go to the internet.

Using a slicer that I can run on my own.

It's like I don't want to be beholden to their slicer and I don't want to be beholden to

some cloud service that might get turned off in the future.

Because that way the product becomes evergreen.

We can always use the slicer with it.

I can always talk to it on my local internet.

Sorry, on my local net.

But yeah, if it's tied to something else like, you know, a service or a piece of software

that's not controllable by any of us, then yeah, I'm not there for it.

And I should have mentioned that they will have a LAN only mode they've promised.

So we'll see if they follow through on that.

Yeah.

Yeah.

I think we just got to keep pushing them to make sure that they register that it's an

important aspect.

Yeah.

And a couple of users out there have already hacked one of their apps to get the security

settings out to show them that they're not the most secure company.

of trying to add this might not be the smartest thing in the world.

So we'll have to see what happens.

Yeah, that was that was one of the other other readings I heard was that like, they rolled

out the main Bambu Studio app that's basically I think, like an electron web app that has

like the slicer executables hidden there somewhere.

And it was just sort of all clumped together with security not really thought about.

Then they're like, Oh, wait, we should probably secure this up a little bit and did it in

of like 1.0 sophomore CS level of way of doing it.

Yeah, there's no question they could have handled that a little bit better as well.

No kidding.

What's your first one for us this episode?

All right, so I would like to talk about oscilloscope music.

So two things there.

What the heck is an oscilloscope?

If you're unaware, oscilloscopes are tools that we electrical engineers use.

They look sort of like a piece of graph paper on a screen.

They're used to graph a signal over time.

And so like the X axis is time,

the Y axis is the value of that signal over time.

And we normally use them to plot repeating signals,

you know, like sine waves

or the output of your little waveform generator

or something.

Most oscilloscopes are at least two channel.

So you can have two different signals you can plot

to compare each other over time.

But these oscilloscopes can also be put into XY mode,

where instead of the two channels being graphed over time,

One channel is like the X position of the dot on the screen

and the other channel is the Y position

on the dot on the screen.

And then as you change those signals,

you can draw anything on the screen.

It's like, it's almost like a, like an Etch-A-Sketch.

This is also called a vectorscope mode.

You might've seen these round green screens

that sort of draw curvy spirograph like shapes.

That's sort of a stereotypical vectorscope sort of look.

And that's what was the inspiration

for the 2023 Hackaday Supercon badge,

which was a little RP2040 Pico driving around LCD.

And it made it look like an old-timey green oscilloscope.

It was really cool.

So you can use this X, Y mode to draw pictures.

And one of the earliest video games, in fact,

was a 1958 Tennis for Two

that used an oscilloscope in vectorscope mode,

but using an analog computer,

'cause they didn't really have digital computers yet.

And so this is fascinating.

I've got a link to the Wikipedia article about that

if you've never heard of this.

It's really great reading.

To keep drawing the picture on the screen,

you can't just draw it once

because the way the oscilloscopes work

is the signal kind of fades.

So you have to keep drawing the signal

over and over and over again.

And that kind of gives you the sense

of like maybe a frame rate or an animation.

But then if you're repeating the signal over and over again,

well, why don't you just pipe the output

of those two signals to speakers

and hear what it sounds like?

And it turns out people have done this

and you can make music.

You have one signal, one pair of signals,

like a left and a right, that's doing both

creating an image but also making sound

just by virtue of how it works.

And so that's what oscilloscope music is.

Been around for quite a while,

and there's a website called oscilloscopemusic.com

that is a composition of many of these pieces.

From their website, oscilloscope music

is audiovisual music where the visuals

are drawn with the sound.

In order to get the closest possible correlation

between image and sound, the exact same signal

connected to the left and right speakers is also connected to an analog oscilloscopes X&Y inputs

producing complex LisaJu images. And there's a link in the notes all about this. There's also

some tutorials if you want to make some of this stuff yourself. You don't have to use an analog

oscilloscope. You can use kind of any little scale oscilloscope you have. You can even use

oscilloscope-like programs on your computer. But on this oscilloscope.com website, they've created

in an album called InSpheres that is just crazy.

They're able to draw these evolving, recognizable shapes and images that are also kind of like

glitchy dance music.

It's really fascinating.

So go check that out.

I found it a lot of fun.

Also a bonus video.

I've been really into Justice's song Never Ender and their official lyric video is a

XY mode oscilloscope set of visuals that kind of play the lyrics along with the song

So I've included a link to that in the show notes as well. So for the oscilloscope music, what does it sound like?

Some of it sounds like

Kind of like early 80s synth pop like, you know kind of glitchy

Sort of synthetic drum sounds with like little weird

siren II bits on top

But it's it's got a lot of I say it's got a lot of glitchiness to it because of how

It eventually has to kind of like reset to redraw the next part of the screen or something

So it's a little hard to listen to over time because it just there's a lot of high frequency kind of

Going on but it's really fascinating. Sometimes it's really aesthetic and beautiful. Sometimes it's kind of harsh and

And hard to listen to but but interesting all in all cases

Hey Paul, so what's your second thing for this week?

I have a nice palate cleanser after all the drama and 3d printing land. Let me take you back to the 90s

Do you remember Tamagotchi's which were these small handheld electronic digital pets?

You do I can tell you're laughing

There were 90 million sold since the mid 90s and this next item reminded me of them

This brings me to the micro critter which is spelled with a you the micro symbol crit air a IR

Ah, air, like a--

Which will make sense in a minute.

The MicroCritter is a small handheld device

that's both a game and an air quality sensor.

Its primary purpose is as an air quality sensor,

and it includes USB-C charging, Wi-Fi, Bluetooth,

a microSD card for data logging, a battery, a speaker,

and both an e-ink and touchscreen LCD screen.

The e-ink display is meant to be used, for example,

sitting on your desk monitoring the air quality,

and the LCD screen is for gaming.

The game is a virtual pet called the microcritter,

who is healthiest when the air quality around you

is the best.

The microcritter continuously samples

the air quality around and gives your microcritter animal

in the game, the simulated experience of the air

you are personally breathing.

Yeah, it's a little crazy.

It also includes-

- That's really adorable.

- It also includes some fast-paced arcade games

earn coins that you can spend in the vending machine.

You can then purchase upgrades for your microcritter from the vending machine with things like

baseballs, furniture, and more.

What's really interesting is that it's open source certified with Oshawa, and the firmware

and hardware is open source and available on GitHub.

It looks to be built on top of Zephyr, but they haven't shared the price yet and it's

not available for purchase.

And even more interesting is they're local to me, headquartered here in St. Paul, Minnesota.

Oh neat. Yeah, this is really, really, as someone who has fully fallen down the rabbit hole of air sensors because of the fires,

I've got like four different ones now and have been comparing their numbers to make sure that they kind of correlate to each other.

But they're all very boring and they just sit on a shelf. This is much more entertaining.

Yeah, and I think that's the goal. So, pretty cool project. I like that it's all open source.

Plus, I mean, it looks kind of like a little Game Boy.

So it's like, even if you're not, and it's all open source,

means you could just like write games for it, or somebody might

have written games for it, so you just play it also in addition

to switching it back over to micro critter error mode.

Micro crit error.

It's hard to say that because it's mu capital C R I T capital A I R.

Mu crit error.

Micro critter.

That's all you need to remember.

Micro critter.

What's your next one for us, Tod?

All right.

To continue on the synth thing, although I mean, I guess not the synth thing, but the

music thing.

Over the last weekend on January 25th, there was this event called Buchla and Friends.

It was a synth get together.

It was held during the NAMM conference, N-A-M-M, which is the big CES for music conference

that happens every year.

And that conference is crazy.

It's as large as CES, it seems, but it's like for people who sell guitars and drums and

PA systems and laser displays for your concert venue and also synthesizers.

And so it's just too much.

I've been a couple times and it's just way too much.

Stimulus overload.

And in comparison, Buchel and Friends was at this interesting little studio in Echo

Park.

was two stories. Both stories were filled with synth people. And the cool thing is,

is that all the synth company, like some of the synth companies that were there were also

at NAMM. So they're the big international companies. But some of them are these little

small best spoke companies of like, there's this really adorable three person company

from Iceland that made a synthesizer that had in cheeks that were made with Icelandic

volcanic rock. I mean, and the synth sounded great. And, and like, and there's this one

One guy that's making this thing called the Qord, which is this little, I don't know,

foot-long synthesizer thing that is just a drone synth.

There's no keys on it.

It just continuously makes noise and has knobs and sliders to let you sculpt that noise.

Both John Park and I went, because it was just like 20 minutes from where either of

us live, and had a great afternoon.

It was interesting to see some of these really cutting-edge new synthesizer things that are

coming out, but also seeing some new versions of stuff that has been around since the 80s.

And so it's like this evolution of some of the synth ideas that had happened way back

when are still happening and evolving, but still recognizable from that time.

Did you get a chance to play with any of the synths, or are they just there for display?

Oh no, no.

It's all playable.

And one of the nice things about this unlike NAMM is that this was a headphone only event

So, you know picture this large large room full of all these people and synthesizers and you don't hear any

Cacophony of the synthesizers. It's all just people chatting and so you can actually have a conversation and if you want to actually play something

There's like a huge amount of headphones on the tables

You just picked a set of headphones up and start playing around and you could still then talk to the person

About their device about their their their cool instrument and that was that was really cool

Because one of the really bad things about these conferences you go to them and they're just like so noisy

You can't hear what's interesting about this new instrument. So yeah, you could play with it all. It was great

There's a link in the show notes of me and JP. They're playing synthesizers

And some other links about like other people who have done walkthroughs of the event and the preview of this cord

Thing that I was talking about very cool. All right, Paul. What's your next one?

the last one for us this episode is

Inventory management for makers. I don't know about you, but I have parts for all my projects in different places

I've got three bins behind me in a closet full of parts that aren't sorted or organized in any way shape or form

I found a project on github just called inventory

It's an open source project for managing small parts inventory

It had its 1.0 release just a few weeks ago in January with the best release name.

It's finally 1.0 after five years.

It describes itself as a flexible parts database which keeps all relevant information,

as well as data sheets, prices, and a visual representation of where you stored the parts.

The idea is that the system may tell you in which compartment of which box,

in what area of your workshop you have to search for to find the part you currently need.

It's been optimized to store information for electronics parts and other small hardware

like screws, nuts, and bolts.

It's a Python app, written using the Django framework, and uses poetry for dependency

management and Postgres as the database.

It has installation instructions to walk you through all of that.

You'll probably need a little Python knowledge, but it also has a standalone Docker container

which might be easier to stand up for some.

You can change the currency, add and manage multiple users, and then start adding your

parts.

One of the neat things is that it has what it calls a box view that is a container full

of parts.

You customize each box for the number of compartments, number of items, and how it's laid out all

in the admin backend.

From there, you can add a part and add tags to help manage them as well as which distributor

from where you got the parts from, the price, links to it, when you last ordered it, and

then you can also attach a data sheet for storing it as well.

Check out the GitHub repo in the show notes for installation instructions and screenshots

of its features to see if it's something that you might want to use.

I think for makers who are building projects for resale, this could be a handy tool.

Yeah, this is this is really, really interesting.

I've I've had to store all my stuff in clear plastic totes

because, you know, when they were in opaque things, I could never find anything.

And even still, I know that I have this real voltage regulator somewhere.

Where is it?

Because because one of the problems of someone who sells occasionally on Tindy

is that I've got the parts storage for this run of a product,

and then I've got my general parts storage

for doing development and stuff.

And sometimes those overlap, and sometimes they don't,

so it's really hard to know what's going on.

I really like this box view idea,

because with electronic things,

you often have many different parts

that are disparate in one container.

So having something that understands that,

I used to try to keep track of this in an Excel spreadsheet,

And it just was like way too, just did not work.

I can't imagine building projects for resale like that and having to have all those parts on hand and not having a system to kind of manage that.

So this might be that tool.

Totally.

Yeah.

And Hey, it's a, it's a real Python project.

You're using like a real database and that kind of stuff.

So that's a, that's interesting.

I've, uh, as someone who has done a lot of circuit Python, but not real Python, this might be a fun thing to kind of crib from.

Well, that's our show.

Visit our show notes to follow us on Mastodon or Blue Sky or to sign up for our newsletter.

And until next time, stay positive.

(bright music)

