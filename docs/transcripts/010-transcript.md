---
date: 2024-07-01
title: "Episode 10 Transcript"
linkTitle: "Episode 10 Transcript"
description: "Episode 10 Transcript - Four Topics and an Interview"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to The Bootloader. I'm Paul Cutler.

And I'm Tod Kurt. We have a special episode for you today with an interview with Justin

Myers, the author of the CircuitPython Library Connection Manager. Before we get to that,

though, Paul and I each have a couple of things to share with you, each not more than a few

minutes long. What's your first one, Paul?

My first one is how to level up at CircuitPython. Professor John Gallaugher of Boston College

recently released two videos I wanted to share, one for how to migrate from using Mu and

CircuitPython to using PyCharm with Teal and a video on using Circup to install and update

CircuitPython libraries. If you're not familiar with Professor Gallaugher, I talked to him

way back in episode 3 of the CircuitPython Show, which I'll link to in the show notes.

He teaches a class called Introduction to Physical Computing, which uses CircuitPython

along with microcontrollers to teach students computing concepts. He has other YouTube playlists

worth checking out on his YouTube channel, especially if you're newer to CircuitPython.

I'll link to those as well.

But back to his new videos. The first one is how to correctly set up PyCharm on MacOS

to use with CircuitPython. Most of this is applicable to Linux, too, and I learned a

few new things. It's a longer video at about half an hour, but the professor walks you

through how to correctly configure PyCharm, and he's using the free community edition

in the video. Next, he covers using the new and updated CircuitPython setboard so you

have code completion for your microcontroller in PyCharm. That might be brand new to a lot

of people and is definitely worth watching. From there, he covers using Teal, an open

source serial program that is way better than using Screen. It's got auto-reconnect as

its killer feature, and I think it's pretty cool that he included Teal as the serial monitor

in Mu is one of its key features.

Next up is a 15-minute video on using CircUp to install CircuitPython libraries. If you've

used CircuitPython, chances are you've downloaded the Adafruit library or the community library

bundle, and then you have to find the right library out of hundreds. But what if you could

easily use the command line? He walks you through how to use CircUp from the command

line, and then for Mac OS users or for Linux users using the ZSH shell, he shows you how

to add tab completion by updating your ZSH configuration file.

CircUp has also been getting some love over the last few months. Shout out to Tim, aka

Foamy Guy in the Adafruit community. He's been doing some refactoring and adding new

features as well. I know I learned a few things, and if you use CircuitPython and you're looking

to level up your CircuitPython workflow, I highly recommend checking out these videos

from Professor Gallaugher.

I love CircUp. It's sort of like, if you've never heard of it, it's sort of like Pip,

the Python package manager, but for CircuitPython. And it hooks into the two big package repositories

that exist for CircuitPython, the Adafruit one and the community one. It's so good, but

it's a little bit hard to set up if you've never done any sort of Python setup before.

So this video is like super handy because I get people asking me all the time, "How

do you install a CircuitPython library?"

Right.

And I'm like, "The answer is just use CircUp." But then the question becomes, "Well, how

do you install CircUp?"

And I think it's really cool that he actually walks you through on how to update your ZSH

shell for the tab autocompletes, because there's hundreds of libraries, and it makes it just

that much easier to find the library you're looking for.

I really want to follow his steps on how to set up that PyCharm IDE, because I don't really

use IDEs in the normal sense. I just use a text editor with code syntax highlighting.

But there's so many people that have been trying to use the VS Code CircuitPython extension,

and it's been sort of perennially broken.

The people are so frustrated using it. And it looks like PyCharm is really well done.

And there's this nice now intro video on how to actually meld it with CircuitPython, which

is a little weird because most of the times when you're editing Python with an IDE, you're

editing the files sort of in a project, say.

And CircuitPython is a little bit different in that the code lives on a device, and you

edit the device.

And so maybe your actual project is in a GitHub repo that lives on your computer somewhere.

So how do you deal with those two separate views of your code?

And I think PyCharm can help you with that.

It can, but you're still writing directly to the microcontroller in the way that it's

set up in this example.

Because I know I use PyCharm, and I did learn a couple of things, but there's still a lot

of copy-paste.

Yeah, yeah.

Because I commit everything to my GitHub repo, so I'm writing locally, saving it there, and

then copying it over to the drive as soon as I hit save, running the code.

Yeah, that's usually how I work as well.

But I see all these people that try to use Mu, because it's easy to use, but Mu's getting

kind of crusty.

And Thonny, I don't know, Thonny just always seems like it breaks my CircuitPython install

whenever I try to use it.

Sure.

Yeah, it's too bad that Mu's getting a little long in the tooth.

It's an open source project, it needs a little love, but it's nice to see other alternatives

out there that are well documented.

Yeah, no doubt.

Yeah, I mean, the cool thing is that because it's all just a text file, you can use anything

that can edit text files to edit your CircuitPython code.

But it'd be nice to have a really good IDE for those people who need IDEs.

What's your first one?

All right, so kind of related, Professor Gallaugher also does a lot of how to program iOS apps

for Apple devices.

And so those are written in Swift.

Swift is a programming language that Apple has been developing for the last 10 years.

They use it on all their platforms.

It's the officially recommended way for writing apps for iPhones, iPads, Apple Watch, things

like that.

And Swift is a really interesting language.

It's heavily influenced by Haskell and Rust, these sort of academic languages that emphasize

type safety and functional programming, where the compiler itself can catch a lot of bugs

as it compiles your code down, which is kind of foreign to how Python and JavaScript work,

where you just kind of run your code and see if it crashes or not.

And so there's this whole academic effort in computer science that we should be able

to make provably correct programs, or programs that we can prove will not crash for certain

classes of crashes.

That's what Haskell and Rust kind of comes from.

That's where Swift came from as well.

And it's a really interesting language.

It looks a little bit like C, but with all these sort of extra neat things on top of

it.

If you look at Chris Lattner, who developed LLVM and the Clang compiler, which you've

probably seen in various places when you've installed things, it's been the sort of revolution

how to compile C-based or C-like languages.

And so you'll see, I think you'll see LLVM and Clang a lot more going forward.

But Swift uses those two things underneath to do its magic as well.

And the reason why I'm bringing all this up is because Apple just released something they

call Embedded Swift, which is a version of Swift that runs on microcontrollers, which

is amazing.

This is a super high-level language, in many ways higher level than Python or JavaScript.

And we can run it on a microcontroller on things that are even some ways smaller than

what CircuitPython type controllers can do.

And not only did they release here's Embedded Swift, but they also released working demos

for the Raspberry Pi Pico, the ESP32C6, the InterF52-840, which is a Beely chip, and the

STM32 chips.

And they've also released a bunch of examples on how to participate in Matter, a Matter

network, which is the new standard for home automation that Apple's HomeKit API does.

And I think Google's Echo platform also does now.

And so there's a, and it's all on GitHub, you can just go to their Swift Matter examples,

see the smart light example that you can run and control.

You can make a controllable smart light with Siri and about 60 lines of Swift code.

And it's all, it has a lot of the same features of real Swift of the type safety, the functional

programming, that kind of stuff.

And it's just sort of amazing that we're getting this super high-level language running on

tiny chips.

And I've not looked at it too much yet, but in the show notes, there'll be some links

to some other articles describing it and links to the GitHub that has some examples.

So you can actually try some of this stuff out on your Pico or ESP32.

I only know Python, and this has me really intrigued, especially the Matter integration,

right?

We don't have that in CircuitPython yet.

I don't think Arduino has Matter integration that I've seen.

So actually being able to write my own smart home apps on microcontrollers would be a really

cool use case and actually has me thinking of learning a second language.

Yeah, it's like, supposedly there's Matter APIs in the latest ESP IDF, the SDK that you

use when you're writing C code for the ESP32 chips.

And I think that's what these Swift Matter examples are using under the hood.

But do you really want to be mucking around with C code when you could use a high-level

language like Swift?

Yeah.

And so, you know, it'd be nice if we get Matter support in CircuitPython someday.

There's no reason why we can't.

And I think Jeffler might actually be working on that really, really early stages.

Nice.

Yeah, yeah.

I would love to see that.

All right, Paul, what's your number two?

My number two is accessibility matters.

When I first started contributing to open source about 20 years ago, one of the first

projects I contributed to was the GNOME project, the Linux desktop environment.

One of the core pieces of GNOME's culture is accessibility, which includes everything

from the Orca screen reader to how we wrote documentation back then.

You know, the worst disability that I have personally is being extremely colorblind,

but that focus on accessibility has always stuck with me, which is why I'm excited to

see a project like this.

The first is the AccessBit from Dr. John Vidler in the UK.

The Micro:bit Educational Foundation commissioned a report on accessibility, which included

a speculative section on how to improve the Micro:bit platform for those with limited or

different mobility.

If you're not familiar with the Micro:bit, it's a microcontroller primarily made for

education, popular in the UK and Australia, that features two buttons, a 5x5 LED grid,

and connections for alligator clips.

It can run MicroPython, CircuitPython, and MakeCode.

The report included a few sketches and possible solutions for potential 3.5 millimeter audio

jacks, which are the industry de facto standard for accessibility, like what are found on

Microsoft's Xbox Adaptive Controller.

Dr. Vidler decided to design a PCB as a minimum viable product to add five adaptive switches.

He walks through various iterations of his design, landing on a final design that includes

an edge connector to connect to the Micro:bit and room for five 3.5 millimeter jacks.

It's pretty cool the thought that he put into the design, from how the add-on board connects

using the 40 pin Micro:bit controller to the curved design of the board.

He had JLCPCB make a handful of boards and sent them off, and they were shown at the

Blockly Summit in Cambridge earlier in June.

Check out the show notes to the link to his blog post detailing the process, including

photos.

The second product is a new Adafruit product, the TRRS Trinkey.

Adafruit's Trinkey line includes a USB-A port to plug it into a host computer, and a small

board maybe the size of a flash drive, so it's pretty small.

The TRRS Trinkey has a SAMD21 chip, has one 3.5 millimeter jack, and can run CircuitPython

or Arduino.

I think it's great that those who might need it have more options for accessibility, especially

using microcontrollers, which they can program to their needs.

I'm excited to see what people can think up using tech like this, especially if it makes

their lives easier.

These are a great sort of combo, because the Adafruit TRRS Trinkey is purely just a USB device.

It looks like a little USB thumb drive almost, it just has a 3.5 millimeter jack on the back.

But the Micro:bit, it has Bluetooth.

It has USB as well, but it has Bluetooth.

And so you can now make a Bluetooth accessible controller with this little add-on board by

just snicking the Micro:bit into it, and then plugging in some of these accessibility controllers

into that, and then pairing it with your phone with a little bit of code, with make code

or something.

That's incredible.

I think there'll be a lot of fun things being created with this.

I agree.

What's your next one?

So my next one is about CAD query.

So I've been on a journey to move to open source tools for my engineering work.

I've mentioned before I've gone from using Eagle to KiCAD.

I use Fusion 360 for my 3D CAD modeling, and it's pretty good, but I'm always irritated

after using it for a lot of different reasons.

What are the open source alternatives?

If you're going for a gooey 3D experience, there's things like Blender, but I like parametric

modeling.

One of the nice things that Fusion 360 does is you can make everything parametric, where

you just define a set of constraints, and then you create solid bodies from those constraints.

Blender's not really that.

Blender's more of like an artist's tool.

It can do a little bit of it.

So for the longest time, there's been this thing called OpenSCAD, which is a textual

3D parametric modeler.

And it's a gooey app where you've got two panes.

One pane is the text of the OpenSCAD language you write to create cubes and pyramids and

cones and ways to combine them in different ways to make your 3D object.

And then on the right is a render of what that thing looks like.

And so from that, you can, and people have done this to great effect, make enclosures

and other 3D things that can be 3D printed.

Like I think all of the Prusa components in the Prusa 3D printers are all actual SCAD

models that somebody has designed as text files.

And so if you need to make the screw holes a little bigger because you're building it

by hand and you're 3D printing the pieces and you only have M5 screws instead of M3

screws, you can maybe just go into the OpenSCAD file and change one little parameter and change

all the screw hole sizes.

But I've always bristled at OpenSCAD because it's got its own special language.

And I've been looking at other things.

And I just discovered recently this thing that's been around for a long time called

CAD Query, which is like OpenSCAD, but it's all in Python.

It uses standard Python syntax, and it is mostly a library that you can then express

via various ways.

You can just run a main.py and have that output a file, but you can also run this thing called

CQ Editor, which is a GUI editor, kind of like the OpenSCAD editor where you have multiple

windows and you can edit text in one and see a render in the other window.

And I've been using that and it's kind of working.

I don't know, even though I've been using CircuitPython for so many years, I'm still

not a very good Python person.

So this is like kind of diving into more Python.

The reason why I discovered this is Luke Wren, who is one of the ASIC designers, sorry, at

Raspberry Pi.

He's one who has helped us do some of the clever PIO things that we've done with the

Raspberry Pi RP2040 chip, like the cool SynthIO and PWM and touch sensors and stuff is all

kind of because, oh, and most especially the HDMI output from a little $4 microcontroller

is because of some of his hints that he's given us.

But he has a GitHub repo of a bunch of CAD query files.

So if you want to see how CAD query things look, what the Python looks like, you can

just go to his repository and go, oh, look, there's a little vacuum adapter and here's

an air duct plate or whatever.

So there's a nice little library of things for you to kind of browse through and see

what CAD query feels like from a language point of view.

But one of the best things about CAD query is that unlike OpenSCAD and unlike the similar

OpenJS CAD, which is the same thing as OpenSCAD in some ways, but with JavaScript, CAD query

outputs step files, which are object files, not STLs, which are like tessellated, triangulated

shapes.

And I was really frustrated that like OpenSCAD doesn't have a step export feature because

if you have a step file, you can now import that into another CAD program like Fusion

360 and then do additional edits on it.

Whereas it's really hard to do edits on meshes.

The STL format is made for just output, for 3D printing.

It's like the bitmap version of your vector file.

And so having a step is really important to me.

And so, yeah, so I'm going to be playing with CAD query over the next whatever months or

so and see if I do anything with it.

I share your excitement for that.

As I mentioned earlier, Python is the only language I know.

So looking through some of those examples, it's started to click for me.

I've tried to use OpenSCAD and never could figure it out.

I can't use FreeCAD because they don't have a colorblind mode and Fusion 360, I've never

really gotten the hang of.

I've had some luck with Onshape, but actually having the ability to actually program it

is and with the examples that they've got, looks really cool.

Thanks, Tod.

And now we have a special guest, Justin Myers.

Back in episode seven for the CircuitPython 9 release show we did, I mentioned Connection

Manager, but kind of guessed how it worked.

Well, I reached out to the author of the new library, Justin Myers, and asked him about

it.

Here's the interview.

Justin, welcome to the show.

Thanks, Paul.

I'm excited to be here.

To be honest, it's my first time I've been on a podcast, so I'm really excited about

it.

It's great that you're here.

What is the new CircuitPython library Connection Manager and what was your inspiration in creating

it?

Yeah, so basically late 2023, I had decided to spend some of my, let's call it extra time

working on CircuitPython and trying to see how I could help project.

I love the open source community.

And as I was kind of watching the threads, I just saw kind of user after user on Discord

having different connection issues, running out of sockets, different things like that,

memories issues and everything.

And I was like, "Hmm, seems strange.

Should be a better way."

And so as I kind of started digging in, saw like each library kind of managed sockets

differently and really think about and look at the differences between like a microcontroller

and CPython running on a PC is like on CPython, you can open sockets all day long, nothing

really happens.

But then once you get to a microcontroller, it's different.

And kind of once I started digging into that, I was like, "Oh, well, you've got the native

Wi-Fi that does it one way.

You've got like the ESP32 SPI that does it one way.

You've got the WISNET 5K that does it a different way."

And just kind of all this boilerplate and different ways to get the SSL connection and

different things.

And I was like, "This is weird.

Like there should be an easier way to do this."

And so it's kind of what started me going down this road of trying to find out like,

"Is there a better way to do this?"

And what was the better way?

So basically kind of the flow went, I asked the comment on the CircuitPython dev channel

and Discord.

I said, "Hey, I've got this idea."

Basically the requests library had this built-in session manager that kind of managed a bunch

of the sockets.

But oftentimes what users would do is they would just re-init that thing and lose all

the sockets.

And so they were still technically open, just sitting there.

And so kind of that first pass was I basically kind of separated some of that out to a separate

class and kind of shared that with the devs.

And they were like, "Nope, let's create a new library.

Like that's not a good way to do it."

Kind of break up dependencies and everything like that.

And kind of from that, there's literally days spent kind of back and forth on like, "What

should we name this?"

And so ConnectionManager was kind of where that was born and basically just started separating

a bunch of the stuff out of what was in the request library and put it into this new one.

And then building handlers that would take in whatever radio object you passed in and

try to determine, "Oh, what's the right SSL method for this one?"

Reducing imports from five or six all the way down to just the one or two that were

needed.

And that's really the key, isn't it?

If you have a PicoW, it was doing it different than an ESP32 S3.

And now for the user, that setup instantiation is almost the same across the different microcontrollers.

Is that right?

Yeah.

And that was kind of the goal, right?

Because if you think through how CircuitPython started and once connection happened, so the

ESP32 Spy was one of the first ones, developers wrote that library and then they kind of mimicked

it a little bit for the Wiznet 5K.

And then when the new ones came out, like ESP32 S2 and S3 and things, and they started

having this onboard wifi, they changed how they did it again.

And with anything that's open source, they're running forward as fast as they can.

And sometimes it's hard to go backwards to go update everything.

There were depreciation flags and comments, not flags in the code.

And all of these places were like, "Oh, we should get rid of this at some point," but

it was still there like years or months later.

And so a lot of it was like trying to trim some of that down.

What was it like to partner with the core developers on Connection Manager?

I really enjoyed it.

It was really interesting.

It's been a really interesting progress for me.

So a lot of my development started in C, 20 plus years ago when I started doing dev.

And a lot of it was for smaller systems.

And it was at a time where you had to do memory management and really think of your code for

what's going to be the fastest and most efficient ways.

And last 20 years, I've switched over to things like Python and things where...

And JavaScript and everything, where a lot of that stuff's just handled for you and you

forget about it.

And so it's actually been really fun because they'll make comments on PRs and they're like,

"Oh yeah, that's a wasteful way to do something," because there's not a lot of space.

So it's really small and trying to think through it.

But they've been great.

There's been times where a handful of them, we've jumped on calls together to work through

some things and figure it out.

They've been great on the comments and asking questions and whatnot.

And so I think the CircuitPython devs, it's a great team to work with.

Well, that's great to hear.

What's next for you and Connection Manager?

Kind of where I've been going next, I've been opening a handful of PRs to make the radios

again more similar.

So for example, they all had different ways to find out what AP am I connected to?

What's my Mac address?

And different methods of returning everything.

So I've been continuously working to try to get the different radios as close to the same

as possible.

And so really for an idea of...

A typical user probably goes out and they buy a microcontroller that's got whatever

Wi-Fi has on it, and they go run with that project and go.

But oftentimes they see a lot of the questions are someone sees a learn guide and they're

like, "Well, I don't have that stuff that's in the learn guide.

I have this."

But then they really struggle to try to figure out how to get it all to work because these

different methods are different.

So it's really been working to get all those core methods the same.

So you can, for the most part, copy paste other than initializing the radio itself.

And the work I'm doing currently now is I'm actually building out some network test code

that we can run.

And so every time a new version of requests comes out or 9.1 for CircuitPython or 9.2

or 10 or whatnot, we can actually run the same test code across the same different microcontrollers

and actually figure out like, "Oh, is SSL still working?

Can I still connect to MQTT?

Can I run a server?

Can I do requests?"

And ideally with a goal of having a kind of similar to CSS is that this like, "Can I use?"

Like so you could go look and be like, "I have this microcontroller.

I'm using this radio and I want to do this.

Can I do that?"

Well, that's great.

It's been fun and exciting to watch you partner with the core devs as you've built this over

the last few months.

Thank you so much for being on the show.

Thank you very much.

I really appreciate it.

And that's our show.

A special thanks to Justin Myers.

If you enjoy listening to the show, tell a friend or write a review.

It really does help.

For detailed show notes and transcripts, visit thebootloader.net.

Until next time, stay positive.

[Music]

