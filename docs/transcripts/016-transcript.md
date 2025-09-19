---
date: 2025-01-06
title: "Episode 16 Transcript"
linkTitle: "Episode 16 Transcript"
description: "Episode 16 Transcript - Sunsets, Synths, and Pinball!"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to the bootloader. I'm Paul Cutler. And I'm Tod Kurt. Each podcast, we bring you news, project updates, product talk from the tech and maker scenes. In this episode, we'll be talking about three things and chat about them for a few minutes each. Paul, what do you have us this week for your first one? My first one is sun setting Mu. The Mu code editor is coming to an end. Nicholas Tollervey and the Mu maintainers released a blog post in mid-December sharing that they will be retiring and sun setting Mu.

What started off almost 10 years ago with feedback from the Raspberry Pi Foundation turned into an editor thousands and thousands of people used.

If you got started with CircuitPython, this was the editor that was recommended, and it also worked with MicroPython and CPython.

It included Python built in so you didn't have to install it, which is what made it so easy to use.

And one of the other cool features is it also included a serial monitor and plotter, things that you don't find in most IDEs.

One of the reasons it was so successful is Mu had four key design features.

Less is more, remove all unnecessary distractions, keep it simple.

So Mu is easy to understand, walk the path of least resistance.

Mu should be easy and have fun.

Learning should be a positive experience.

I would say they hit all of their goals and had a good run.

The blog post kicks off with this decision has been coming for a while.

And if you followed Mu at all, it hasn't had a release for over two years.

What I think is so cool is that they communicated that Mu is coming to an end, but what to expect from them going forward. So there will be two more releases before the end of March. The first will be a legacy version based on the current main branch with all the bug fixes that they can do.

Oh, great.

Yep. It's hoped that this version will still work for a while for schools and other educators using Mu.

The second and last version of Mu will be updated to use all the newest version of libraries included in Mu.

And I think one of the big challenges they had was how they integrated Qt and PyQt and the different versions in between.

So I think they're going to try and upgrade that so it'll help with life on the Raspberry Pi as long as it can.

Yeah, that's a shame. I really like Mu because it was the most like the Arduino IDE for CircuitPython.

and that it was a pretty usable editor.

It talked to the hardware, and it had a serial monitor and a serial plotter, which are like the three things that you need when you're doing Arduino stuff.

And like, oh, if you're coming from an Arduino environment, which I was, here's something that acts kind of like it.

And people crap on the Arduino IDE a lot, but it's actually really good.

But there's a lot of choices, like the various things that you're talking about, about what Mu focused on, is the same things in many ways that Arduino people focus on.

It's like make it simple make it you know so you can have fun don't get bogged down in configuring JSON files or adding plugins You know it's like like there still isn't a good replacement in circuit Python that will replace mu I think yet. I would agree. There's nothing that has the the serial and the plotter for example Yeah, I mean we're seeing we're seeing some of the online IDEs have the serial Which is a must-have I think when working with these microcontrollers, but there's still a ways to go for I think for the online I'd ease to catch up a little bit. So thank you, Mu. It was my thing that I always recommended to people when they're first getting started. Now I'm at a loss as to what to recommend. Well, hopefully we'll have a couple more years before that we have to transition away from it completely. What do you have for us next? So my first one is something I've been wanting to talk about for a long time because it's something I've been really excited about for many years and it just keeps getting better and better. So I goof around with music. You've heard me talk about synth stuff and one of the gizmos I use the most is most is called the SynthStrom Deluge. It's a device that's about the size of maybe a sheet of paper, it's about maybe an inch and a half thick. It's in the groove box category, if you know what that is.

Groove boxes are these things that kind of came around in the 90s mostly, that were little self-contained music making devices that had drum machine plus the ability to make some sort of synthesizer noises and a sequencer to sort of tile together maybe some other things. That's kind of the basis This is what a groove box was. So the Deluge is kind of in that category, but it's a lot more.

It's kind of like a digital audio workstation that is about the size of a book. You can put it in your book bag and take it around. It's got a grid of 144 RGB buttons in a matrix and a couple knobs at the top. And it can do all the stuff. It's a MIDI sequencer, sampler, drum machine, multi-track audio recorder. It's got a built-in battery and a built-in speaker. So you don't even need to really have any other infrastructure to goof around. It's also got CV gate outputs.

So you can hook it up to modular synthesizers. That's what your thing is. And so it's kind of the hub of my music making world It's the thing sometimes I compose entirely on it. Sometimes it's just the controller for things that exist outside of it But it's just like this amazing little box that seems like a really premium piece of gear and it's made by a small team in New Zealand it's like it's mostly like one guy was the coder and another guy was the salesperson or whatever but they've got a small team now, but like for many years it was just, I think, the two of them.

And so the only way to buy it used to be was to order from their website New Zealand. And it was, so it was like a real, real best spoke piece of gear. And it felt like a really quality bit of kit. And every year they would improve the deluge. They would like release new firmware that would add new features, like not just fix bugs, but entirely new features, like the ability to record audio or to act as a looper, to have wave table synthesis. And then a couple years ago, they offered a new version of the Deluge that had an OLED screen, but they also made it so that if you wanted to send in your old Deluge and get the OLED screen upgraded for your device. It's like, what?

Hardware makers never offer upgrades to their gizmos. It's very rare. But then on top of that, Two years ago, I think, they released the Deluge source code on GitHub.

And instead of just having it be like some, what some companies do, they just like release it and it's like, okay, do whatever you want with it, but the licensing is either unclear or not very permissive, so you can't really use it for anything, they made a GPL.

So it's like truly fully open source.

And they created a Synthstrom community fund to help financially assist anyone who wants to work on the firmware.

So the community really stepped up within a few months, the entire code base was refactored, like just totally reorganized.

Because it was a product of kind of one person, the code is kind of in just a couple of files, a couple of big files.

And so the team pieced it all out.

These people working globally on just on GitHub, they piece it all out to make it more usable by a team.

And so that first version came out and it was had all the same functionality as the normal version, but now it was all like refactored.

And then a few months after that, they came out with official version of the community firmware.

Now this is a parallel track from the official firmware from Synstrom, but it had a couple improvements. It had like a couple new UI modes, it had some new features like audio effects and filters, some new sequencer modes, and it was just like it was better in so many ways. Like it had a new reverb algorithm that just had a much better sounding built-in reverb, was one of the coolest new things that came out of the first version I think.

and every few months new features are added. At any point you can just go to GitHub and download the latest build to see what crazy new thing they added. Like on December 25th of 2024, just a few days ago, they released the 1.3 version of the Community Firmware and it adds a DX7 FM synth emulation. So like in addition to all the other ways you can make noises with this box, it now can recreate the sort of pinnacle music synthesizer from the 1980s, the Yamaha DX7. And it also has some other cool like useful abilities for me like the ability to export stems. So like you create this multi-track composition and currently if you want to record that you kind of just have to record the stereo out. Now you can essentially export each track individually as a multi-track folder of waves and then use that pull out into your computer if you want to do some post-production.

And it's just like it's ever since I've bought this thing like six seven years ago every year It's like getting a new bit of gear because it gets improved over and over again first by since from originally and now by the community Of people who are hacking on it every day So this isn't some deluge if you're looking for music piece of gear, this is not sponsored, but I love this thing That's awesome. It's so cool to see open source and action like that So many times like you were talking about a company will come to an end-of-life product and throw the source code over the fence and say have at it, but we're not going to support you at all. So to see it on an active product with an active community making all of those kinds of changes to it is pretty darn cool.

I'm a big believer that open source can work as part of your business model and Synthrim just showed like here's a way of doing it, you know, and it's just it's really nice. So yeah, so that's my first one for this week.

Paul, what's your second one for this week? My next one up is Home Assistant Voice Preview Edition. I'm fascinated by Home Assistant, the home automation software platform that people usually run on a Raspberry Pi. I have an instance running with just a couple of things hooked up, and it's one thing I wish I would spend more time with. But I also know that home automation can be quite the rabbit hole once you go down it, especially the effect on your wallet.

Back in 2023, the Home Assistant team dubbed it the Year of the Voice and started to lay the groundwork for building a voice assistant into Home Assistant. It had to align with their goals, especially around privacy.

All of that work over the last two years has culminated with the Home Assistant Voice, a small square device that listens for your wake word. It features a big button in the middle to activate it, a speaker, and a built-in microphone.

It's 59 bucks, so it's more than a Google Home or an Amazon Alexa, but it's fully private. You can use a large language model locally if your hardware is beefy enough, like a Raspberry Pi 4 or 5, I believe. Or you can use OpenAI, Google, Anthropic, and more in the cloud if you choose to. Since it's open source, they crowdsource a number of languages, and it supports more languages out of the box than most of its competitors, with over 25 languages supported already. And that's just the preview edition. And again, like we were talking in the last one, it'll be interesting to see how the open source community rallies around that and how many more languages grow over just the 25. I don't have any Amazon Alexas or Google Homes in my house. Siri on my iPhone is about the only voice assistant that I use. This I'm actually tempted to dip my toes into. That whole idea of privacy, like we've talked about in past episodes really appeals to me.

Yeah, me too. I've been an avid spectator of the home assistant scene for so long because I want to play with these home automation thingies, but I don't want the privacy invading gizmos that are the Google and Amazon things. But yet, one of the problems with getting a home built system working is getting just audio input reliably into a Raspberry Pi. And so this kind of solves that "last mile problem" for you in a really kind of aesthetic way. You know, it looks pretty good for a little $300 gizmo.

And presumably you could have multiple of them one per room in your house or whatever if you wanted to do that.

Exactly. And then yeah, and you just run the actual beefy guts on an old PC you have that you have as a server or maybe a Raspberry Pi somewhere in your basement or whatever.

And that does the actual like large language model I think, right? Exactly. That's exactly how it works.

So you can choose to run it locally or in the cloud and I think it's Raspberry Pi 4 is the minimum for the beefy that you need, but plenty of people have an old computer lying around.

typically too that you could run that on. Yeah, so I'm really intrigued and I actually think I might get this just because, hey, we can finally do some open-source home assistant type stuff now without needing... Exactly, I'm just afraid once I open Pandora's box it's a rabbit hole I'm gonna go down and not be able to climb out of. Oh yeah, yeah, I know I've heard some people have been hooking up their garages and their cars and stuff to Home Assistant. What do you have for us next. Okay, so to continue the synthesizer theme that I had in the first one, right before Christmas, a few days before, I attended a workshop hosted by the Hackaday Supply Frame Design Lab. It was called The Sound of Logic, Klangorium, and it was taught by Richard Hogben. He's the guy who does the really great interstitial music at Hackaday Supercons. If you've watched any of the live streams of Supercons on YouTube, all the music that happens before and after the talks are his compositions. And he taught the workshop and the workshop is about this little kind of synthesizer board called the Clangorium that was made by Elliot Williams who's the I think the head editor now at Hackaday.

And he's been working on this board since 2015 which is now 10 years. He's documented a whole bunch of it via a series of Hackaday articles. We'll have a link to those in the show notes. But unlike most modular synthesis boards you might have heard this board is not expensive it's like just a bunch of logic circuits because it turns out if you're a clever hacker you can turn some of these really boring old 80s era logic chips like a hex inverter into a six voice oscillator you can turn a shift register into a sequencer and because it's just square waves you can just use a diode or as a mixer it's kind of just nuts that you can do a bunch of this stuff that sounds like a lot of the components you would have in a modular synthesizer setup, but it's just a couple of little logic chips that are like 50 cents each. And this board is, you know, it's about maybe five inches by eight inches, and it has little sections that are different parts of what you might have in a synthesizer like oscillator, mixer, filter, that kind of stuff. And it's got little pin headers like you would have on an an Arduino or a breadboard where you just connect wires between them to patch your synthesizer sound.

And so the workshop was soldering up part of that board. It's a pretty big board so you couldn't do all of it.

We did about maybe a third of it. And getting the oscillator section working and the little drum voice, because there's a little drum voice on there that was easy to solder up, and then the output section.

It was a lot of fun. And I love that it's been this work of love by Elliot for the last 10 years, is that every so often he comes back to it, he teaches like maybe a workshop at a Supercon, or he writes another article on the blog, and we get to learn more about this crazy, let's use logic circuits to make synthesizers stuff.

This reminds me of the Charles Lortok from Supercons that we had in our last episode.

Totally.

Microcontrollers are just radios in disguise, where he's using a microcontroller to do something that it was not intended to be.

Yep.

And that's what comes to mind when I hear about this project.

Yeah, it's so nuts. It's like normally, so the way these, this circuit works is you have an inverter, which normally it takes the input that's high and turns into low and vice versa. And you feed it back from the output and back to the input. And normally feedback like that is bad. But if you insert a little resistor capacitor in that whole loop, you've now delayed the signal a little bit. And the amount of delay is kind of how fast the oscillation happens as the chip goes, Oh, I should be high. Oh, no, wait, I should be low. Oh, I should be high. Oh, I should be low. Oh, I should be high. Oh low. That's an oscillator and change that resistor and they can change the pitch of the oscillation.

It's just kind of funny that like two things that we're taught as engineers not to do. It's like don't do positive feedback like this and don't do you know don't do analog stuff with digital circuits and and here we are doing it and it sounds pretty neat. Okay what's your next one Paul?

I'm going to call this segment fun with 3D printing. There's been so much 3D printing news in the last month you may have missed it if you blinked. First up is a four axis 3D printer By 4-axis, Joshua Bird has created a 3D printer where not only does it have the normal X, Y, and Z planes, but on this printer the nozzle can rotate as well.

You almost have to see it to believe it, but it allows you to have greater than 90 degree overhangs.

It's open source and I've linked to the YouTube video in the project source.

Then there's Mobiprint, which looks like a 3D printer on a robot vacuum, which it literally is.

You have it map your room using its built-in LiDAR, and then you select the objects you want to print and where in the room you want it printed and it prints right on the floor.

[laughter]

This sounds dangerous.

I'm not sure how well that works when I know how clean I need to keep my 3D print bed and I can't imagine what a dirty floor is like. Next up is a video by Stephen Hawes on how he used the UV light in a resin printer to print onto a fiberglass copper block and make a working PCB. It's about 15 minutes long but it's an interesting process and he goes over the challenges he ran into.

And it's not for the faint of heart. Some of the chemicals he used, you actually need to talk to your municipality and how to dispose of them.

But it was pretty cool that in the end, he was able to make a working PCB.

The Lemontron 3D printer debuted. This is a small, mobile 3D printer that prints inverted, upside down.

It's only $400 to build yourself, so it's relatively affordable.

And they say that gravity really doesn't affect it because the filament cools so fast that you don't get any stretching when you print it upside down.

Back when like the first wave of open source 3d printers were happening at Maker Faires, there would always be a couple of people who would have the 3d printer in a backpack and some of them would have them mounted upside down because yeah if you do it if you have the settings just right or have the fans blow fast enough that it cools before it can droop. Yep. Next up there's a new add-on kit for your 3d printer mostly Creality type stuff it looks like that straps an inkjet toner to your 3D printer and allows you to add some color to your 3D prints. The beta unit kits retail for about $200 but are currently sold out. It launches later this month in January for $250, I believe. So an interesting way that if you don't want to do MMU, you know, multi-material prints, this just basically is spray painting it right on. That's interesting. Much better than the attach the sharpie to the edge of the filament that I've seen. Exactly. And then lastly, there PET Fusion 2.0. This is a Kickstarter where you buy the STLs and bill of materials to create a device that recycles plastic bottles and turns them into 3D printer filament. It's pretty unique and it was fully funded in just three hours.

You build in a motor that cuts the bottles into two strips, then you feed those strips back in, and it's extruded as 1.75mm 3D printer filament, and then you can add a dye to it as well to color it.

It looked pretty neat, and it was relatively cheap. The STLs, I want to say, started at $40, and only went up to about $120 for commercial versions if you wanted to resell them. So, interesting product.

Wow, that's really amazing. Yeah, I would love to see more home recycling of the various plastics we have. I know it's like a really hard problem, but this is pretty interesting.

My challenge would be is I don't really buy soda bottles because I don't want that kind of plastic in the environment.

Same, yeah.

What do you have for us last?

Pinball. All right, I love pinball. I grew up with mall arcades with pinball machines. The machines were usually kind of broken.

and we're definitely old timey compared to the video games or like all the cool new thing.

But when I got to college, whoever ran the laundry room in the dorm basement was really smart.

And he had room for a couple of coin-op video games and one pinball machine.

And that pinball machine was always in good shape.

And if you're a college kid like me with some leftover quarters waiting for his laundry to dry, what are you going to do?

You're going to play some pinball.

Yeah.

I got really good at that pinball machine.

So from then on, whenever I'd come across a pinball game, I'd play it.

But pinball is kind of like, they're like little puzzles.

You spend more time with them and you unlock more fun.

That takes a lot of time, can get expensive.

So I mostly didn't play very much.

Then, I don't know, maybe 10 years ago or 15 years ago, a company called Zen Studios came along with a really solid pinball physics simulation engine and licenses to many of the classic Williams pinball games like Theater of Magic, Attack from Mars, and my laundry room game, High Speed.

They have apps on mobile and tablet and Xbox and console, PC, everything.

And so I've been playing these games for many years virtually, and I've gotten really good at a few of them because now that I have it on my phone, if I got a couple of minutes, I'll just play a little pinball, you know?

And so this is all background for what I did during my Christmas vacation.

While visiting family up in the Bay Area, I was fortunate enough to visit the Pacific Pinball Museum in Alameda.

And it's a nonprofit and it takes this nonprofit charter pretty seriously.

It has, it has events, but it also has wall text for every one of the hundred plus machines they have.

That explain why this particular machine is important.

In addition to like all the old games they have from like 1800s or early 1900s, where like, you know, flippers hadn't been really considered yet.

So it was just like mostly a game of chance where the ball went from the top to the bottom and hitting pins, you know, but they have like a, also a bunch of the modern games or, you know, from the nineties and two thousands games, um, including classics, like the ones that I'm really good at, High Speed and Theater of Magic, and I got to play both.

- Nice. - It was really great.

It was so good.

And I sucked at both of them. (laughs) - The real world's a little different than the virtual world, is that what you're saying?

- Yeah, see it turns out that the Zen Studios Simulator games they present this perfect machine to you.

It's a machine that's just come off the factory floor, doesn't have wear spots on the table, or a flipper that's kind of weak on the second hit.

You know, it's like just, it's just perfect.

But in real life, every pinball machine is kind of unique and ever-changing.

It's got to kind of get to know the machine and know that it can't do certain things or you have to like do different actions to get what you want.

So I'd forgotten that. (laughs) The distance between when I really played a lot of pinball and playing a lot of pinball on computers was like pretty vast.

So I decided to visit more real pinball places.

And it turns out there's a really good arcade that's a few miles from me in Pasadena called Neon Retro Arcade.

You know, I got some gift certificates and I'm going to go and visit them in a couple weeks I think.

And I just looked on pinballmap.com, which is a great website, you should go visit it.

That in Minneapolis, there is a place called Lit Pinball Bar that has 47 pinball machines.

So Paul, if you want to go.

I will have to check that out.

There's also, I think, an app version of the pinballmap.com website that I have on my phone.

So if you want to check in real time, "Hey, I'm in this random location.

Are there any pinball machines within two miles of me?" Oh, crazy.

So yeah, go play pinball, people.

It's fun.

Before we end the episode, I'd like to give a shout out to RadioFreeFedi, who I covered last June in episode nine.

Turning off the lights on the online music streams later this month, and I'm grateful to have been part of the community.

really did rock. And that's our episode. Thanks for listening. For show notes and transcripts, visit thebootloader.net. Until next time, stay positive.

