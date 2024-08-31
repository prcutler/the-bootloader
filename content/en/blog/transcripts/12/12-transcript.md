---
date: 2024-09-02
title: "Episode 12 Transcript"
linkTitle: "Episode 12 Transcript"
description: "Episode 12 Transcript - From Arcade to Synth"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
Welcome to The Bootloader. I'm Paul Cutler.

And I'm Tod Kurt. If you want to learn more about this podcast, visit thebootloader.net

for show notes and transcripts, and where you can also find our new newsletter.

Paul, two weeks ago on 16th of August was CircuitPython Day. We were honored to be an

official part of it with a special live video version of our podcast. You can check that

out on YouTube, and we provide a link in the show notes. I just thought we'd like maybe

talk a little bit about the experience of the entire CircuitPython Day in our live show.

But first, I'd like to say thank you so much for organizing all of that.

Oh, it was nothing.

Like not all of CircuitPython Day, but like for our part of it was all organized by you.

I just kind of showed up. So thank you so much.

It was my pleasure.

The format was we first talked about what CircuitPython had been doing for the last

year in terms of like its features and updates and how it's in its relationship to MicroPython.

We each talked about one project that each of us had done. It was really nice to hear

your Song Matrix thing because it straddled so many different technologies because it

was a network project that dealt with MQTT and the Shazam API. I don't do much internet

stuff with my little electronic devices that run CircuitPython. So it was really cool to

see all that and to see like real Python working in concert with CircuitPython.

Yeah that's one of the really neat things about the project. I've got a couple of projects

that do that, but actually writing real Python on a Raspberry Pi and then writing CircuitPython

and having those talk to each other is just, that's what excites me about CircuitPython

is that those physical devices that you can touch and feel. It's just something better

than just seeing code on a screen.

Totally. And it kind of reminds me of the synergy that a lot of web developers got when

we were able to write JavaScript code that ran in the browser and also JavaScript code

that ran on the backend using Node or something. So it's like we're getting that same level

of like, "Oh I don't have to switch gears too much because I'm still writing Python."

Just different flavors of it.

And then my project, I made this like two weeks before CircuitPython Day, I made this

like plan that I'm going to design and build and code a little playing card sized drum

machine and it didn't quite turn out because I made some tiny mistakes. So I've got 10

of these boards and I'm wondering, should I even like fix them up and put them in the

store? But it was a fun experiment. I tried doing a similar thing a couple of years previous

with CircuitPython Day and that worked out pretty well. So this was a good learning experience

for me. And if anybody has seen this little drum machine playing card thing that I made,

if anyone is interested in one, let me know and I'll see if I can send you one.

And I think it's cool that the project didn't actually work out and you talked about it.

So many projects are, "Look, I did this and it just all worked," but that's not how it

is in real life, right? We all have challenges and things break and it's good to actually

show that side of a project.

Yep.

Well, what's your first one this episode for us?

All right. Synthesizers. Have you heard of them? So one of the things that I've been

into is modular synthesis. So it's the kind of mad scientist synthesizers you might see

with all the knobs and lights and all the cables that plug in. And the way this all

works is that each little module does one specific part of the whole synthesis process.

And so you have something that might make a noise and then you have something else that

shapes that noise's loudness and another module that shapes that noise's frequency response,

sort of a tone control. And then things that will produce different pitches that control

the thing that makes noise. And so it can get really expensive really fast. And so people

when I've talked about modular synthesis, they're like, "Oh, that sounds really cool.

I want to get into it." It's like, well, it's really expensive to get into if you're not

building the stuff yourself or if you've just decided to sort of like, "This is my hobby

and I'm going to sink a couple hundred dollars into it every couple of months."

And so if you wanted something else that was modular synthesis but was not as expensive,

what were your options? It's like, well, there are some of these software programs out there

like VCV Rack that will do the sort of virtual on your screen modular synth. And that's actually

a really cool way to get started. But it's a thing on a screen. And one of the whole

points of modular synthesizers and physical synthesizers and physical things in general

is to get yourself away from screens. And there's also the other problem of if you're

trying to build some of this stuff yourself, the things that you will be interacting with,

like the jacks you plug cables into and the knobs you turn, those don't work well on a

breadboard. There's always problems where you're like, as you're turning the knob, the

potentiometer will come out of the breadboard because they're just really not made to be

plugged in like that. And so what's the solution? And I've been seeing some noise about this

thing called MICRORACK from this synth get-together, the synth conference called Super Booth a

few months ago in Germany. And lately I've been inundated by Instagram ads for its Kickstarter

campaign, which I'm like, man, Instagram has me targeted. And so MICRORACK is a collection

of little PCB modules that plug into a breadboard, just like all these other things we might

have that like Adafruit sells, except they are modular synthesis modules. So instead

of being several hundred dollars for each little module, it's a little like each little

module does the same functionality as these synth modules, but they just plug in and you

wire them together, little jumper wires like you do on a breadboard. And so it's really

nice. It's inexpensive. The way you interact with it is very much the way you interact

with stuff on breadboards. So if you're used to doing stuff on breadboards, this is like,

oh, this will fit right in. And they've got a pretty rich set of modules, it looks like.

And they're using the Solaris breadboard mostly as a power distribution and a mounting platform,

which is great. It's like, oh, here's this very common plastic thing with lots of holes.

Let's use it as a mounting board, essentially. I've become a backer of it. I'm going to hopefully

it'll be out. They've been making modules for like six months or a year, and they've

been showing them off for several months now. And so I'm hoping it's a real thing. It looks

pretty real. And if anything, it's going to be a nice way of solving some of these problems

of how do I get the knobs to not move around when I'm prototyping something? Because I

prototype my own little synthesizers on breadboards, and their modules, like some of their modules

are just like little knobs that have outputs. I'm like, that's perfect.

Like you were saying at the beginning, I looked into EuroRack a couple of years ago when I

had some interest, and it was just so overwhelming. I had no idea where to start. And like you

mentioned, the cost quickly went up and up. And I thought about just buying a couple of

modules from just Winterbloom and starting there, but I still found it pretty overwhelming.

But this is something I might check out. Do you remember how much it was roughly on Kickstarter?

I think for like, they've got like a starter kit that's around like 80 bucks or whatever

that contains like a good handful of modules. I think the most expensive thing you can get,

which contains all their possible modules is like 300 or 400, which is the cost of one

modular synth module if you go to a store that sells them. So in terms of I think modules

per dollar, it's one of the highest that's out there. I'm mostly interested in it since

I developed some of my own little music gizmos. I'm mostly interested in using it as little

pieces of potential UI that I will have in my synthesizer. I'll just like use their knobs,

use their jacks, that kind of stuff. There have been other similar, let's make some of

this audio stuff more breadboard friendly little things that have been out there. I'll

put some links to some previous ones in the show notes. One of those famous ones is called

Breadboard Friends by Mutable Instruments, Emily Gillette. It's like two of the main

problems with the synth stuff on when you're prototyping some stuff is how do you do jacks

and knobs? The other one is how do you do power? Because the Eurorack standard is all

the signals are plus minus 10 volts. And your breadboard, like everything you do on a breadboard

is usually like three volts or five volts. So it's like one of the main things it solves

is how do you make that work?

Very cool. So how about you? What's your number one today?

I've been talking about building a standup arcade for probably 20 years from when I first

got a set of ROMs, the actual arcade games you load into an emulator to play. About five

or six years ago, I finally started it. And living here in the Twin Cities, we have a

local company called Paradise Arcade, who has a focus on the community around fighting

sticks, fight stick controllers for fighting games. But they have a wide selection of arcade

parts, including buttons, joysticks, and the hardware to hook them all up to a computer.

I drove down to their shop, which is more of a warehouse and not a retail shop, which

I didn't know at the time. But they were pretty awesome and helped me out. From there, I bought

plans on the internet to actually build the cabinets and then bought the MDF to do it.

But I've never done woodworking. So this has all been in fits and starts over the last

couple of years. I haven't worked on it in a year or two, though I plan to pick it up

again in the next few weeks as I have that itch again.

The point of the story is, if I had to do it all over again, there's a solution that

looks to be a lot easier. Pimoroni is taking pre-orders for the PiCade Max, a bar top arcade,

not a stand up, that sits on top of a desk or a bar, hence the name. It includes everything

you need to build it, just add a Raspberry Pi 5. The kit includes 6mm powder coated MDF,

two player controls, and a 19 inch screen and 5/4 aspect ratio, just like original arcade

monitors.

What's really innovative about the PiCade Max are the add-on boards that come with it.

There's the PiCade Max Power Hat, which powers both the Pi and the screen at 5V and 12V.

The PiCade Max USB controller board supports up to 24 buttons and two 4-way joysticks that

connect via USB-C. This itself is a deal, as the wiring harness I bought for mine was

about $100 just by itself.

And then lastly, there's the PiCade Max USB audio board, which has two screw terminals

for a pair of speakers and is an I2S audio DAC with a 3W amplifier and volume control

via a separate encoder board. What's really innovative is that these last two boards are

powered by the RP2040 and connect via USB-C to the Raspberry Pi 5. Pimoroni mentioned

in an interview with Les Pounder at Tom's Hardware that they'll be selling these two

standalone boards in the future, and I know I want to check out the audio board for sure.

The PiCade Max kit retails for £495, or about $650 with the current exchange rate. That's

really not that much compared to how much it would cost to build it yourself and take

it from me. And it's about 50% lighter and not nearly as heavy as using normal MDF to

build the cabinet. Of course, I don't want to know what shipping would cost across the

pond for that. I'll link to a couple articles from Tom's Hardware with their coverage, as

well as the PiCast show on YouTube, where host Les Pounder had Paul and Phil from Pimoroni

on to talk all about it.

That's really cool. There have been a few retro arcade using a Raspberry Pi things over

the years, but they've always been sort of, "Oh, if you can find these random parts that

I happen to have in my garage, if you can find the exact clones, you can use my plans."

But having something like this PiCade Max could make it really easy just to, "I'm going

to build it this weekend."

Yep. And you do need to set aside time. Paul from Pimoroni joked on the stream that they

did that his speed run of doing a complete installation was like two hours. And that's

someone who knows what they're doing and has probably done it before. So you need to put

a good chunk of time to do it. But then again, it's taking me years and years to work on

mine. So this sounds like it would probably be a lot faster.

No kidding. Yeah. And I'd love to get the link to the place in your area where you actually

got some real arcade hardware. Because I used to be really into that. I used to have a couple

of stand-up arcade machines. They were old Atari Vector things that were always dying

because that was kind of their normal state of things. They were in, once these old games

get past a certain age, they're kind of always failing, it seems like.

Yeah. And it's really neat. They have everything from PCBs for a couple of games to mounting

hardware to they custom make some PCBs. And then they've got the whole fighting stick

stuff. But I'll make sure to link to Paradise Arcade in the show notes too, because they

ship internationally.

Yeah. And the cool thing about the PiCade Max being separate boards is you can take some

of the Pimoroni stuff and use it with an existing sort of arcade platform that you've already

partially built. If you are kind of stuck on the wiring harness problem of how do you

get these joysticks and buttons and speakers hooked up to whatever you want.

And I've been worried about sound because just doing the 3.5 millimeter out from a Raspberry

Pi isn't, you know, it's still a little tinny. But yeah, I'm excited about that because I

really want to check out the audio board. It's got the two pairs of speaker terminals

so you can use a real pair of speakers with it, not just some cheap computer speakers.

Totally. Yeah.

What's your next one for us?

So yeah, well, OK. So at the beginning of August, on August 8th, Raspberry Pi introduced

a new microcontroller board, a successor to their popular RP2040 Pico. It's the Pico 2

and a new chip that powers the RP2350, which is a great chip. It's like they've improved

it in almost every manner. Like it's it's got a like a twice as fast dual core set of

CPUs in it. It's got extra PIO if you're doing that sort of weird protocol stuff. It's got

twice the memory. Just oh, it's a lower power. You know, even though it's twice as fast,

it's lower power. So it's just all around a really good update. And I've been really

excited as I've been slowly getting some of these RP2350 based boards in to test. Since

it's twice as fast and almost all the stuff I do with the chip is in CircuitPython or

synthesizer stuff, both of which are really compute intensive. Having a chip that's twice

as fast means I can do essentially twice as much, twice as many synth voices or something

or twice as fast response time. And as I was testing it out, I learned that the capacitive

touch library in CircuitPython called TouchIO wasn't working with it. And I looked, started

looking into it, found a bug on the CircuitPython GitHub. As I was looking at it with my oscilloscope,

I discovered that there's this errata that was in the data sheet called E9 that is a

problem with the actual hardware, where if you're using a GPIO pin on this chip in a

certain way, mostly as an input, it will latch up and stay at 2.2 volts instead of like high

or low. And so the way the capacitive touch sensing works in CircuitPython and a lot of

other systems is you have a pin and it drives that pin high for like 10 microseconds. And

then it turns that GPIO pin into an input and watches how long it takes for that pin

to go low. And that time that it takes is basically it's discharging the capacitance

of whatever the line is connected to, like a little capacitive pad. And when you human

touch that pad, that changes that capacitance. And so the time it takes to go from high to

low changes. And so with that, you can get a really good sense of like, oh, was something,

has something touched the capacitive pad or not. But because of this pin is sort of like

staying high or not staying high, staying at 2.2 volts, which is kind of not quite high,

but it's definitely not low. It means that touch I/O doesn't work. It also means that

certain kinds of button inputs won't work either that have like certain low or certain

high of resistance pulldown resistors, or if you've configured internal pulldowns in

the chip. And so I'm at this point, I'm not recommending people use the Pico 2 or the

RP 2350 if they're newbies, because it's got this weird input problem where you don't

know is it not working because of my wiring or is it not working because you're tickling

this weird input bug on the chip. And thankfully, Dan Halbert has looked at, Dan Halbert, who's

a core CircuitPython developer, he looked into it in much more detail than I, and he's

created a bunch of really good test cases that he's opened issues up on the Raspberry

Pi GitHub and on the MicroPython GitHub. And so there's a bunch of good data and the relevant

people have been notified. So hopefully there'll be a fix. I don't know if there'll ever be

a software fix. We might have to wait for the next version of the Pico 2 chip to come

out. But if you want to read more about this, Haxter wrote an article about it that talks

a bit, I think they downplay the problem a bit, because I think the problem is actually

more of an issue than some people say, "Oh, it only happens if you have internal pulldowns

enabled, da da da." But no, I think it's a problem any time you're doing any kind of

input with high resistance pulldowns on the output, which if you're doing low power work,

if you're doing certain kind of bit bang protocols like I2C, if you're doing those by hand, would

that require an external pulldown resistor? So yeah, just be warned, there'll be lots

of links in the show notes about all this if you want to look into it more.

Yeah, it's disappointing to hear on such a popular chip, right at the beginning to run

into a showstopper bug like that. Does it occur on all the pins, all the GPIOs?

Yeah.

Oh, okay.

Yeah, yeah, yeah. I mean, I think maybe the ADC pins in some cases, it doesn't affect

them because the analog buffer gets turned on instead of the digital GPIO buffer. But

all the digital pins, definitely. Yeah, pretty frustrating. I think most people won't see

a problem, but I've seen a problem with buttons and I've seen a problem with the cap touch.

Which is one of your favorite things to do.

Yeah. No, it's like, I was like, "Oh, I'm going to just use this as a drop-in replacement

for some of my existing boards on Tindy," and nope.

Just kidding.

Yeah, lol. So yeah, what's your number two this week?

I've mentioned a couple of times on the show that I have a 3D printer from Bambu Lab and

they're back in the news again after Stratasys has sued them for patent infringement. Stratasys

created 3D printing back in the late 80s and through that and their acquisition of MakerBot

just over 10 years ago, hold most of the patents related to 3D printing today. I've linked

to two articles from Ars Technica and Tom's Hardware that have really good coverage in

the show notes that go into far more detail than I will. In question are 10 patents and

two jumped out at me, the heated build platforms in Purge Towers. Both of these are pretty

standard in 3D printers, which raises the question, are their patents still valid or

is there prior art that may invalidate the patents? Phil Torrone of Adafruit asked this

question a few weeks ago when this hit the news. He suggested that someone like the Open

Source Hardware Association should start a database to catalog prior art to see if the

patents could be invalidated. I'm wondering if it actually needs to be a database or could

prior art be tracked in something simpler, similar to an awesome list and simple markdown

on a GitHub page, for example. I'm half tempted to start a list myself, but I don't think

I have the context in the industry to get the list right. This isn't the first time

a prior art search has been done against Stratasys' patents either. Doing some search engine queries

prepping for the show, there were calls just over 10 years ago for prior art to fight some

of these patents, but I couldn't tell if anything ever came out of it. I'll link to the articles

that I mentioned with coverage of the story in a Reddit thread with some speculation about

why Stratasys is going after Bambu Lab and not other companies. Again, it's just speculation.

I'm not going to say they're conspiracy theories, they're just theories. It probably just comes

down to the fact that Bambu Lab has had a large amount of success in a very short amount

of time. They're afraid of losing market share of their large commercial 3D printers to an

upstart consumer 3D printing company. I've heard so many patent issues with Stratasys.

One of the things I think that started the whole consumer 3D printing revolution back

in 2006 or 2007 was that one of the key patents that was about the, "Oh, I'm going to melt

plastic and squirt it out using a CNC-controlled nozzle," that went out of patent in the mid-2000s

or something. Thus, we got RepRap and then we got MakerBot and Prusa and all these others.

Every 3D printer is because of this patent being finally expired. I remember hearing

one of the reasons why a lot of these consumer 3D printers don't have heated build chambers

is because Stratasys still had the patent on heated build chambers, and so everyone

just had heated platforms. Then, people would say, "Well, you know, if you put your heated

platform 3D printer in a small box from Ikea, your prints would be much better."

Right. Stratasys' headquarters is about 15 minutes from my house here in the Twin Cities,

and I'm just half tempted to drive over there, knock on the door and go, "What the hell

are you doing?"

"What?"

But obviously, they look at this as defending their patents and their revenue streams, so

I see both sides of it. It's still very frustrating for things that are very common today to still

have patents against them.

Yeah, super frustrating, especially for things that seem pretty obvious, but this is the

world we have to play inside of, I guess.

And I did look. A number of those patents don't expire until the mid-2030s, so there's

still over 10 years to go on some of them, which is quite a long time.

Yeah. I'm on the crossfingers that we'll find a way.

Well, that's our show. Thank you for listening. Visit TheBootloader.net for detailed show

notes, transcripts, and to sign up for our new newsletter. If you like the podcast, you'll

like the newsletter as we give you some behind-the-scenes and some extra links that we didn't cover

in the show, and we promise there's no spam, no tracking, so check it out. Thanks for listening

and stay positive.
