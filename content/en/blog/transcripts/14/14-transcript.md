---
date: 2024-11-04
title: "Episode 14 Transcript"
linkTitle: "Episode 14 Transcript"
description: "Episode 14 Transcript - Welcome Kevin Santo Cappuccio"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to The Bootloader. I'm Paul Cutler. And I'm Tod Kurt. We have a special episode

today as we welcome guest Kevin Cappuccio, creator of the Jumperless breadboard. Kevin,

welcome to the show. Nice to be here. Thanks for having me on. We each have brought two

things to share. We'll chat about each one for a couple of minutes, but no more than

five. If you want to learn more, visit the detailed show notes and transcripts at thebootloader.net.

Kevin, before we start, let's talk a little bit about this Jumperless V5 that the crowdfunding

campaign is going on for. I made the original Jumperless about almost exactly a year ago.

And I hacked in this probe thing. So what makes the Jumperless V5 so much cooler is

I added a probe that lets you just poke out connections. And it was like, once I did that,

I was like, oh my God, this is the way to use this thing. It's so much nicer. So I just

started over, you know, like used all the cross point switching matrix to make all the

breadboard connections in the back, kept that. And then, yeah, so V5 is just making it really

like intuitive, a nice UI to do whatever. It looks so cool. Like, especially with all

the LEDs behind each breadboard point. So like as you touch the probe, they light up.

It's just, that's great. Did you use these 446, I lost the chip now, the analog crossbar

switch that's like 128 switches in this little chip. Did you use that on the previous Jumperless

as well?

Yeah. So like early prototypes, I was using an old Mitel 8816, MT8816. And so it turns

out, but they're like big PLCC packages. They're like huge, like ceramic heavy chips. So I

couldn't fit more. And so I went looking, turns out the CH446Q is kind of a clone, but

they like made it a lot better. Like it's kind of cool to see companies doing that where

they're like, they take the same thing and then they're like, we need a serial addressing

mode. So like you don't have to send a bunch of parallel data and run a bunch of wires.

You can just, so yeah. So I use those. They're great. I use them way on spec too.

Yeah. I'm a big fan of these analog multiplexer chips to like basically let you turn one analog

input into eight or something. And to see this cool, it's got 16 lines on this side

and eight lines on this side. And you just connect any one to any of them and even have

multiple ones connected. It's just, it's kind of blew my mind. It's like, ah, why don't

play with this chip for something? I don't know what yet.

Yeah, they're great. They also make a five by 24 version, like if you want to like really

fan out, I don't know if I'll be used for them, but I want to.

So the other, the other difference in the jumperless V5 is it's got the new RP 2350

chip. Have you liked that chip? Cause this is one of the first designs I've seen actually

use it.

Yeah. So they make it in a bigger package so you can get that extra GPIO was so clutch.

Like it, I had a GPIO expander on there. It was like driving the chips and it's like,

it's so nice to be able to take that out and just, you know, instead of sending an I squared

C message to it or something like you can.

It was a lot simpler.

The, the beta test units that are out right now, like those were handed to me as samples

at Defcon, like cause they launched it at Defcon. I was like, no way I have to do this.

And like, yeah, just spent all of Defcon reading the data sheet like a couple of times over.

Yeah. I was wondering where you got the 2350 because no one else has them. And I was so

shocked to see a new product with them.

Yeah. I, I was one short for them and I bought a Pimoroni like a board with it on and just

de-soldered it and put it on there. Yeah.

Yeah. Cause I think, I think Pimoroni is the only place you can get those, the bigger version

of the RP 2350 I think. Yeah.

Yeah. It adds some like it's, there's like, you know, more pins, more ADCs and stuff,

but like really it's just cool. Like I just did it cause I was like, ah, this is going

to be awesome to have the newest, newest chip on there.

Totally. Well, I mean it's, it's a good marketing move, you know, even if you don't need the

extra CPU power and stuff, it's just to say, Hey, I'm using this new shiny new chip that

everyone's all agog about.

Yeah. I mean, and it just gives us, eventually we'll probably need that room cause keep getting

all these app ideas in the discord. Like we should have a Python REPL on it. Like, sure,

why not throw that in there? Like we got so much room.

Do protocol decoding or something.

We do that. That was actually this entire week we were doing protocol.

Oh really?

Serial pass throughs. So now I can like, there was an update that just got sent out on CrowdSupply,

but yeah, we were like screwing with it for like this last week straight of getting serial

pass through so you can route UART lines or any like, or I squared C or something. And

then anything that comes in through the second USB endpoint, we'll just get like bi-directionally

pass straight through. So you can put like an AT tiny on there and you can just flash

it as if it was plugged in by itself. It's kind of cool.

Oh man, that's cool. Yeah. Cause normally you got to pay like a bunch of extra money

on your, on your scope to get protocol debugging. And if this is like, this is part of your

breadboard.

It's not as good as a scope. Very set expectations right there. It does a lot of things. It does

not do any one thing really, really super duper well.

Once the, the, the probe thing came out and you're touching stuff and lighten things up,

I'm like, okay, this has got to be a synthesizer or a synthesizer interface device or something.

Cause it looks like something out of a sci-fi 1970s rack mount synthesizer thing.

I was going to sell a second synthesizer version, which is exactly the same thing, but twice

the cost.

Hey, now for those at home that might be curious, how much is the jumper list? V five?

It's 350 bucks while crowdfunding is going. And then as soon as that's over, which by

the time you hear this, it will be, then there'll be three 79. Okay. Well, I'll make sure that

we'd link to that in the show notes too. So people can check that out. Totally. Yeah,

this is very cool.

What's the first thing you brought us this week, Kevin?

So I brought the Uno plus plus looks kind of like a regular Arduino Uno, but every pin

has an led on it and it tells you the state of each of those pins. So like if it's, you

know, pins high, that actual row is lit up and how he does it with the actual like plastic

header is it's a clear plastic bit and it acts as a light pipe. So like it's not just

an led next to the header that's lighting up. It's the whole part of the header lights

up.

That's pretty cool.

Yeah. Something like this. Okay. If I had just seen it and I didn't see the schematic,

I would not trust it in a million years. Like the easy way to do this would be put another

microcontroller on it and then just read all those inputs and then send it to some addressable

LEDs. But John talked to him, he can't program. So he instead did it the cool way and did

it with comparators. And so it's a ton of, you know, quad LM three, three, nine comparators.

They've been around forever. And so like that, I would trust, like if I see if that's on,

there's really not much that could go wrong. That would tell me the wrong state.

Yeah. And it buffers it. So it doesn't impact your use of the GPI.

Yeah, exactly. And he even like set the comparators, right. So like with the hysteresis, like,

you know, they won't go over 1.8 volts what they're supposed to. Yeah. It's cool.

That's awesome. Did he get like custom headers made instead of the black plastic, they're

clear light pipes or?

Yeah. So I was, I was just talking to him and what he was doing was doing a clear 3d

printed, transparent, like resin, and then having a second 3d print that slots into it,

like really thin little blades that keep the light separated from one to the next. So it's

got a really tiny channel, but JLC now, I was just, just looking on JLC the other day

and they do like full color resin, like clear resin, and then you can put color inside it.

So now it can be one part. Yeah.

That's pretty neat.

Yeah.

Wow. So is this a thing you can buy or like, is it, does he, does he have also a crowdfunding

campaign going?

No. So he's, he's close. He's getting there.

Ah, cool.

I don't even think the Hackaday IO project that I linked, I don't think that has all

the newest things. I think he's now using full color PCB, but no, it's, it's coming

up soon and it's, it's going to be rad.

That's awesome.

Hopefully I can convince them to make a Arduino Nano version. That's going to be so much harder.

Oh, because then that will plug into the jumperless board.

Yeah, yeah, exactly. I mean, like it sounds like a little beginner learning tool, but

like, you know, like 99% of my debugging is, is this pin actually doing the thing I want

it to like, is it the, is it the pin or is it the code or something, you know?

Like 90% of the times when I'm helping people with coding projects, I just tell them, put

print statements like in between every line so you can see what's going on. And they're

like, Oh, and it, but like, you can't do that because it'll slow down your code or, or it's

just like unfeasible having LEDs, like physical representation of what's your, what your circuit's

doing is like so much more clear.

Yeah. It's funny walking people through debugging stuff and you're like, no, no, check again,

check, check that that's up. You know, like, no, the code says digital, right? Hi. And

you're like, no, dude.

Not really. You didn't set the pin to an output or something. Very cool. I can't wait to see

more of this. Uno plus plus and it's spelled P L U S plus sign. Yeah. It's hard to search

for if you don't know that.

I actually genuinely thought I was going to lose the Hackaday prize last year to that.

Like that was the project I was like, that's cooler than jump for this. Like I would, I

would vote for that over my own.

I don't know. They're pretty, they're both pretty cool. All right, Paul, what's your

one for this week? Mine is the Manyfold app by James Smith. Manyfold is an app that's

been around since 2021, but it's been in the news recently because it just added activity

pub integration, which I'll come back to in just a minute. It's a self-hosted app built

to manage and organize your files related to 3d printing. It's open source released

under the permissive MIT license and written in Ruby on rails.

Imagine printables or thingiverse, but self-hosted. You're not locked into another walled garden

and it has some really, really neat features. You can run it as single user or multi-user.

So if you're running it in single user, you're just keeping a track of all the files that

you have multi-user. You can invite other folks to join your server, almost like pixel

fed does for sharing photos. I mentioned earlier that it's integrated with activity pub. That

means it's on the Fediverse. Imagine being able to follow a creator or a model directly

from your mastodon account, which I think is really, really cool. So every time that

that model is updated, you'll get a notification. I believe I need to double check that.

And then one of the other cool things about it is it doesn't just handle the 3d printing

file formats like you would expect, such as step files, STL files, and 3mf files. It handles

everything related to 3d printing. Every image format is supported from JPEGs to pings to

GIFs to SVGs. Video files are supported if you want to show a render of the 3d printing

model that's going to be printed. And it can keep track of all the text files that go with

it. So if you have installation instructions, for example, it'll have all of that built

in like you would expect it to. If you want to learn more about it, I've linked to an

interview with James and the Floss Weekly crew on their podcast. You can check it out

at manyfold.app and there's a demo server at try.manyfold.app to see it in action. It's

really, really neat. I highly recommend it.

That's cool. I love seeing more things that we think have to be monoliths being added

to the Fediverse in some way. Because like, why not? Especially for something like Thingiverse

and printables, you know, fundamentally it's not that hard. It could be an FTP server.

It could be. But, you know, if you're running one of the servers, one of the things you

might need to think about is copyright violations, right? What if you have a file that's copyrighted?

Or I think James mentioned in his podcast that he buys or subscribes to Patreon creators

who if you subscribe to them will give you files. Well, you're going to want to make

those private, for example. You don't want to make those public because those were for

sale and all that functionality is built right into Manyfold.

And just seeing updates. Like, you know, sometimes you get a file that someone made and then

you forget that like maybe they tweaked it, made it better. I don't know.

Exactly. I think that's one of the coolest things about it being on the Fediverse like

that.

Yeah. And back in the heyday of Thingiverse, one of the things I really liked about some

of the models is the discussion that was going on on a model. People were like, oh, you know,

what's the right way to print this? And there'd be like discussions on like, you know, different

filaments or different orientations of the part or whatever.

And like if it's kind of part of your Macedon experience, that that conversation can happen

pretty seamlessly, I would imagine.

Yeah, I don't know if that's enabled, but it's definitely something to check out.

Yeah.

All right, Tod, what's your first one for us this episode?

All right. So some of you might have already seen this, but to me, it was just like kind

of a little bit mind blowing. Like we've all seen the Doom game ported to insert tiny electronics

like the watch or the little Arduino or something, but...

Or the jump.

Yeah. Oh, is it going to have Doom?

And that's great. You know, it's like a really complicated game engine compared to like things

like Pong, but it's not true 3D. It's more like a 2.5D where the enemies are just sprites

and the level geometry is just perturbations on a 2D plane. But the game Quake, which is

the game that came after from id, was full 3D, fully polygonal monsters and objects in

the world, fully polygonal game world. And I figured Quake would never be part of these

little tiny embedded things. But I saw a couple of days ago that people at nexthack.com got

Quake running on a SparkFun Thing Plus Matterboard, which is a feather format board, you know,

9 inches by 2 inches. And it's only got... It's a 39 megahertz little board that's got

256K of RAM and 1.5 megs of flash. And this is the same specs as the RP2350 pretty much.

So, you know, are we going to see Quake on the jumper list or on an Adafruit feather

soon? So first they started with a SparkFun board and made a little sort of prototype

that you can build yourself. They've included all the source. But then they created their

own gamepad PCB that houses an Arduino Nano matter. Like this uses the same chip, this

MGM240 module that has a Silicon Labs EFR32MG24. And it's some Bluetooth matter chip that's

pretty cool. And they got this whole complete package that has a screen, has the Arduino

Nano on it, buttons, sound output, and it runs at 35 frames per second at 320 by 240.

Oh, and also you can do BLE based multiplayer with someone else with the same board.

Oh, that's amazing.

Yeah. And so like, like as someone, as someone who sort of, sort of got into PC gaming by

buying the 486 with the 4 megs of RAM minimum and like having that be such a stretch back

in whenever it was. And now to see that, oh wait, they could have done it in 256K of RAM.

It's pretty amazing. In the show notes, we'll have links to their multiple posts they have

on this, a write up from the Silicon Labs tech blogs. They really liked it. Links to

the design files if you want to build your own of these boards. It seems pretty doable.

I love this project. Quake always has a special place in my heart. I was a big gamer in the

mid nineties or starting in the mid nineties. And I had a 3DFX Voodoo card. And I, one of

the top five gaming memories I still have is the first time I had that card in my machine.

And then Quake, you walk up to the puddle and you see a reflection of the character

in the puddle in full 3D. Something else still never forget, because it was just mind blowing.

We didn't have graphics like that until that card and that game came out. So it's, it's

pretty neat to see how far that's come in the last almost 30 years.

Yeah, yeah. For me, one of my one of my memories that comes back unbidden to me is being able

to bounce the Quake grenade gun grenades around the corner to kill monsters and the noises

that it make of the "dunk, dunk, dunk" because it bounced around. It's just like, it's like,

oh, you can like kind of think strategically in this first person shooter game.

Like what if someone came back in time and told you that like that chip is a smart light

bulb or something. Yeah, it's easier to just put that whole thing, something more powerful.

Yeah, yeah. It's like, it's like I saw seed just came out with a Xiao format, like a cutie

pie format board with the same chip for like $7. And, you know, like you're not going to

be driving a really like high res screen with that, but, but hey, maybe it could run Quake.

All right, Kevin, what's your number two for this week?

Yeah. So this one's not really, it's not a project. Like I'm, I'm bending your rules

a bit, I think. But it's, it's a field. So like the field of evolvable hardware, it's

literally as old as I am. So the first project with evolvable hardware was University of

Sussex, Adrian Thompson. What he was doing was, oh, in 1990. So, so what he was doing

was like getting an FPGA. So I think he was using a Xilinx XC6200 and basically giving

it a fitness function. So I think the first, the like the seminal thing that he did was

a tone discriminator. So being able to tell the difference between one kilohertz and 10

kilohertz on, I think there's a hundred gates, it's like a 10 by 10 FPGA. And yeah, and so

he would just say, is it okay at that? And then it would give it a random bit stream,

just random arrangement of a bunch of logic gates. And then, you know, at first it's probably

just kind of up in the air of none of them are doing the right thing, you know, but then

over time, you know, he's doing like an evolutionary thing where he's like the two most fit ways

of getting, you know, making this pin go high at 10 kilohertz and low at one kilohertz.

Do that again, you know, and then put some randomness in it. And he ran it for a while

and it worked. Like it just found, and it's like, if you look at the, you know, the arrangement

of gates, it's complete nonsense. Like there's parts that are not even connected to anything,

but are necessary for it to work. Like it's using kind of just like the weirdness of like

signals going, like, you know, there's no constraints. We don't have to like, you don't

have to abstract anything. So it's just like, yeah, it's using, and it probably wouldn't

work on another one. Like if you put that exact same setup, it wouldn't work on a different

chip because it's just, but yeah. And so running circuits like that would be, I don't know,

I just think it's the coolest thing ever. But yeah. So what happened though, was why

I feel like it's kind of relevant now is they stopped using it. Like they discontinued the

Xilinx XC6200 and now all the FPGA bit streams are like encrypted. They're like all, you

know, they're very proprietary and what you need to get this to work is kind of just a,

I know one-to-one of, if I say top left corner logic gate, be that, it'll be that. But what's

cool now is I hope that there's a resurgence in this because the, have you heard of a project

Ice Storm? I have not. They're kind of, they're like, they're reverse engineering the bit

stream of a lattice FPGA, like a modern one. Okay. And so like we had 30 something years

of like, basically this whole field is kind of dead. Like there's just wasn't like hardware

for it. And then, and only now, like we can pick up again and people can screw around

with trying to get, you know, is it the best way to do something? I don't know. Well, I

have to imagine too, it's a lot cheaper now to do it than it was back in 1990. Oh yeah.

Yeah. Yeah. There's a little, there's a little ice 40 FPGAs are pretty cheap. I see them

pop up on various Arduino looking boards and stuff. So, and if, and if it's just, you know,

set it up and let it run and call me, call me when you figure it out. That's pretty great.

Yeah. I think there was some, there was some interest from like space stuff. Cause if you

broke your FPGA, like physically broke it in half, you might be able to get one that

runs on just the rest of it. You know, that's yeah. Yeah. It's like, how do you make, how

do you make resilient circuits? Like right now we design things very sort of cathedral

where like every bit has its own important part to play. And if one bit is missing, the

whole thing doesn't work. But if we can make something that can recover, that'd be pretty

great. And fun fact, uh, in the book, 2001, a space odyssey, that's how Hal was programmed

was like, he described some process just like that, where they, Oh wow. So jumperless, like

the first idea of it came after me going on this rabbit hole for like a really long time

about evolvable hardware. And it's, it was kind of frustrating cause it does it like,

you know, there's a lot of work on it and then it kind of just fizzles out, you know,

cause they discontinued the chip and it was like other universities weren't able to screw

around with it as much. And yeah. And so that was kind of part of my thinking of like something

you could do with this whole analog cross point switch away array is you could like,

it's not going to be a feature, like you would just be able to run it and it would try to

fight a circuit, but as a thing to screw around with, it's that's pretty cool. Good for that.

Plus on the jumper list, it could look cool because you could have the LEDs represent

the connectivity that's, that's evolving over time or something. Yeah. All right. So, uh,

Paul, what's your second one for this week? Uh, my next one is a current Kickstarter project

that's going on for a few more weeks for the FlexiPi. It's a new Raspberry Pi Pico format

board, but it's wafer thin and it's flexible. Hence the name FlexiPi. It's got a few upgrades

from a normal Raspberry Pi Pico. It uses USB-C. It's got a Neo pixel built in. Otherwise

the pinouts stay exactly the same. The Kickstarter campaign runs through November 24th and it

includes three digital books that come with it. Getting started with the Raspberry Pi

Pico, a micro Python book and a circuit Python book. They've already reached their funding

goal that their goal was $500 and they're over $7,000 already. But if you do back it,

remember it's a Kickstarter, so nothing's ever guaranteed, but it's really neat to see

how flexible that really is. And I don't understand how they got it so thin, but it's something

that I want to keep an eye on going forward. Yeah. Flex circuits are pretty cool. I it's

like, this is, this is really impressive. I don't know exactly how I would use it. I

mean, I don't really do much flex stuff, so wearables are the first thing that came to

mind for me. Ah, yeah, definitely. Definitely that. Yeah. Yeah. Someone actually dropped

that on my discord just a couple of days ago and it, yeah, it's funny cause I can't think

of what to use it for, but it's really fun to think of situations that it would be useful.

Yeah. There's so many, like what weird problem you're having really like, Oh, I need to just

wish this Pico could bend. Exactly. And I should mention it's, it's $20. So it's, it's

not cheap compared to a normal Pico, but that's what you get for having something that's that

so thin and flexible. Yeah. Yeah. And just having a little bit of give on something that

you wear could be all the difference. Like it doesn't have to bend much, but maybe just

a couple of degrees could make it not be like, Oh look, he's got a piece of technology embedded

inside of his hat or something. Right. All right, Tod, wrap it up for us. All right.

So my second thing is the EMMG MIDI synth and is created by a hacker in our sort of

larger community. It's got a name Jonathan Bisson or B. John J. It's a board he created

as a teaching tool for a workshop he gave on MIDI and music synthesis at the pumping

station one hacker space in Chicago. In the show notes are links to the presentation and

other, other aspects of the project. The, the workshop taught what MIDI is down from

the signaling level to how it's used by performers. Each student of the workshop got, got one

of these custom design boards. The board has eight pots, 12 cap touch pads and OLED display

and stereo out all driven by a Pico clone. That's a USB-C 16 megabyte version. The workshop

also talks about how the GPIOs work on the Pico, how CapSense works. It was like, it

was pretty fun. And the board has a secret mode by default. It comes up as just a MIDI

controller, but you powered up one of the switches held down. It also is a full synth

using this interesting Prof32U synth engine for Pico that he found. And he was able to,

it's like an, it's like an Arduino chunk of code. But it's really cool. It's got like

four, it's like it's a paraphonic polyphonic four voices with built-in chorus and delay

effects. Really, really cool filter. It sounds pretty good. Selfishly, one of the reasons

why Bright bring this up is because I have one. He sent one to me. I was literally just

about to ask you that. Yeah. He, he based the design of this board on a couple of my

previous projects, most notably the Pico test synth, the Pico slider toy, and this sort

of unreleased thing I have called 8x, which is a sort of eight pots to one analog pot,

sort of expander board for, for microcontrollers. And his board, by having eight pots instead

of two solves one of the biggest problems I've been struggling with, with my little

Pico test synth as I try to write code for it for people. And that's having only two

pots when you need to control a whole slew of values is a real pain in the butt because

you have to keep saving the state of where the pots are currently when you switch which

parameters you're changing. And so, and then you have to like deal with the fact that like

when you come back to that parameter, the current location of the pot is not where the

pot physically is. And so you have to like deal with like knob what's called knob pickup

and stuff. It's just a real kind of pain in the butt. So with eight pots, you can like

have immediate control, a bunch of parameters without having to do a bunch of page switching

and stuff. I think if I were to redo the Pico test synth thing, I would have either more

pots or use rotary encoders, which is why you see a lot of rotary encoders on things

because they're incremental. You just show the state immediately and just any turn of

the knob will just increment or decrement the state. All of the designs for the board

and for the workshop notes and presentations are up on GitHub and I'll put links in the

show notes. He also has a really great sort of blog post that describes his whole design

process including like the DFM of like how do you make this thing actually buildable

and also the open SCAD CAD files for the custom knobs he made for the board. It is pretty

nice to get some sort of like free stuff back for all the random little circuit boards I've

made over the years.

That's pretty cool. And you said it runs Arduino?

Yeah, his like the main code he has is Arduino. He also he's also got some experimental stuff

for CircuitPython, but he started down CircuitPython route but wanted to have something that was

like was easily able to switch between these two modes and he wanted this with the synth

engine that was based on Arduino.

I love the idea of making a board for a workshop. Like because now like the person giving the

workshop knows exactly how that board was made. You'll never run into a question of

like, oh, why is it like this? And they're like, I don't know.

Yeah, I wish there was video for it because I kind of wanted to know like how did he have

everyone hook up the boards like were they all controlling like a synthesizer in the

room or something? I'll have this in the slides and I haven't asked him about it.

Just probably like a loud mess in that room.

I know.

Each person doing their own.

Well that's our show. Special thank you to Kevin for joining us this episode.

Thank you so much for having me. That was fun.

For detailed show notes, transcripts and to join our newsletter, visit thebootletter.net

and until next time, stay positive.


