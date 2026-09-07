---
date:
  created: 2026-09-07
title: "Episode 36 Transcript - CircuitPython Day 2026"
---

Paul

Welcome to The Bootloader, I'm Paul Cutler. This episode is a replay of our live stream on CircuitPython Day 2026.

We do use video and screen sharing so you may want to check out the video on the Adafruit YouTube channel, which I've linked to in the show notes. Welcome to The Bootloader. I'm Paul Cutler.

Tod

And I'm Tod Kurt. If you haven't heard of us, we're the host of the bootloader podcast, but you can find in your favorite podcast player on the first Monday of month or at thebootloader.net. The show works like this.

Paul and I each have brought a few things to share, all about CircuitPython for the last year. And a big thank you to Liz, who's on camera control. Paul, let's break down some of the numbers.

Paul

Yeah, it's crazy that another year has gone by already. Since last CircuitPython Day, CircuitPython 10 was released in October with a ton of improvements. This was the first release to add some audio effects, full Fruit Jam support, including the new CPsaves partition for SD cards, and a bunch of graphics updates, including Better Pico-DVI support, to work on more monitors.

Tod

Okay. It's going to be like 100 degrees today, I think.

Paul

So what was CircuitPython to you last year, Tod?

Tod

So last year, CircuitPython 9 was all about synthio. It was like when synthio really got going and really got good. It kind of existed before, but it was like we had to try to figure out how it worked right.

But with CircuitPython 9, we could make real interesting sense in CircuitPython. This year, it's all about audio effects because a synthio synthesizer voice by itself is just okay. But having audio effects after that, like delay and reverb chorus and like that, like version 9 had echo chorus and reverb created by Mark Gamblor.

Thank you, Mark. But then very soon after that, like right after 9 was released, and right, I think for the 10 betas, Cooper added multi-tap delay, phaser, and distortion. And like both kinds of distortion, like a simple clipping distortion, but also like this sort of soft overdrive distortion.

And then Cooper made some really important changes to how the effects works. We can chain them together. It was kind of hard to do that before.

And so now you can basically plug them together like guitar pedals, which is great because it kind of matches how synthio work, because synthio kind of looks and acts like a semi-modular synth where you kind of connect little cables together to make a synthesizer. So it's like we've got this modular synth on one hand, and then we've got a guitar pedal board on the other. So it's all becoming really interesting.

And then earlier this year, Tim, aka FoamyGuy, added a granular pitch shift to complement the pitch shift effect that Cooper had earlier. they're both relevant. Pitch shift uses less resources.

Granular pitch shift can sound better for larger pitch shifts. And then also the audio mixer module is updated. So it's a level in pan knobs can be modulated with LFOs.

Oh, and did I mention that all these effects have parameters that can be modulatable with SynthiO's? They're like LFOs are like automated knob turning. So you can have things on your synthesizer or now audio effects that can automatically have their pan shifted or their distortion amount change, things like that. And then to bring it home, earlier this year, Tim added the audio I-2S In module, and now the audio duplex module, or I forget what it's called it, but both of them let you do stereo audio into CircuitPython as well as playing audio out via I-2S, so you get high-quality, 16-bit audio. And so now we can truly have CircuitPython-based guitar pedals or effects boxes, which you might have heard a couple of hours ago when Cooper was demonstrating that.

And also, just in the last episode, what are these segments called we're doing on Circuit Python Day?

Paul

Live stream.

Tod

Last live stream, there we go.

Tim demoed how he had hacked the Teenage Engineering Ting handheld effects unit with the entire alternate CircuitPython firmware that lets you do cool real-time effects of your voice. And so it's just like CircuitPython and a commercial product, and it sounds cool, and it's fun to play with.

Paul

It is cool. I can't create music, but it's been really fun watching the different projects that you, Cooper, and Liz have done with the new audio effects.

Tod

Yep.

Paul

So after 10.0, we then saw 10.1 in February and 10.2 this past April. 10.2 included the latest ESPIDF as well as the MicroPython 1.27 merge. So thanks to Dan for keeping up with Upstream.

Tod

Yeah. Thanks. Thank you to MicroPython, which made all the stuff possible. I like that CircuitPython is still merging in updates to MicroPython as time goes on. I think that's pretty hard to do because CircuitPython has deviated a bit. So I think Dan's been the one who's mostly responsible for the merges. So thank you, Dan. Jeez, that must be a really hard task. So, Paul, what's your first one for this show?

Paul

If there was another theme over the last year is that it was the year of the Fruit Jam. This credit card size CircuitPython powered micro PC was a hit. It was first released in July of 2025, but it was hard to find the first few months.

And then in the last Adabox, late last year, Adafruit shipped them to all the subscribers. I'm not going to go into all the hardware specs. You probably know them by now.

But Tod, let's share a few of our favorite Fruit Jam apps from the last year. My favorite is probably Sean Carolan's Pac-Man clone. Originally written for the Wio Terminal, Cooper Dalrymple ported it to the Fruit Jam and upstreamed it to Sean.

Sean vibe-coded Pac-Man in an afternoon, and it's a fantastic port. I had him on a recent episode of the CircuitPython show, and he shared where he got the game resources, how he recreated the sounds of Pac-Man, and more. I'll have to admit to losing a few hours just to playing it.

Tod

Yeah, it's, I find it really fascinating. Oh, I got myself on the wrong screen. I found it really fascinating that we're at this stage where we're able to recreate old hardware in Python running on a chip.

like no OS involved, no super high-powered system. You know, it used to be if you wanted to do emulators, you had to get like a really powerful desktop computer or something. But now it's like, oh, yeah, we can do this on a thing that, you know, fits in your hand.

Paul

What was one of your favorite Fruit Jam things this year?

Tod

So for me, that was the Zork player. So if you're unfamiliar, Zork ran on this thing called Z-machine. It was a virtual machine created in 1979 to run, many of the text adventures created by Infocom.

Infocom, they did Zork, they did Hitchhiker's Guide to the Galaxy, they did a ton of games. Like, in fact, on this webpage, Dan has a picture. And the cool thing about this Z-machine, virtual machine, is it let Infocom get put Zork and all these other games on all the platforms of the 1980s, like the Commodre 64, the Atari ST, the Sinclair ZX81, I think even.

And thanks to that, Dan was able to do the same with a Fruit Jam. His port has that cool retro CRT, 80 by 24, green screen CRT effect. I think for maximumist nostalgia, you should hook your fruit gem up to a CRT, you know.

But Dan wrote this Z code parser in CircuitPython instead of C, which is what most people have been doing for the last, you know, 40 years or whatever. And it works nicely with the Fruit Jam OS, which if you have the CircuitPython-based OS, but writing OS is in CircuitPython, right? But if you run Fruit Jam OS, it works nicely with that.

So it just becomes another app for your free gem. And it's a lot of fun to use this as just Zork and Z machine because it's the first chat system that we normal folks got to have access to. And learning how to use how to play Zork and how to use the language that Zork wants is kind of not that different from the prompt engineering we've had to learn recently of like, how do I phrase this thing so the LLM will spit out something that will work.

And so now you too can be eaten by a grue or get lost in a maze of twisty passages, just like 1980s kids.

Paul

Yeah, I was terrible at Zork. But Dan's been busy.

Tod

Yeah, yeah, yeah. He's been doing a lot, huh?

Paul

In addition to the Z machine, he also released a handful of classic screensavers and another game, Moon Miner.

Tod

Yes, yes, yes.

Paul

It's related to the classic lunar lander game from the 80s. Your mission is to retrieve minerals from the moons around the solar system. It's all physics-based. You try to land your rocket ship based on how much thrust you're giving it and the gravity below. You need to make a safe landing to harvest the minerals, and you can't tip over either. I'm not good at Zork, and I'm not good at physics games either.

Tod

Yeah, this one reminds me a lot of this really old, one of the earlier vector, black and white vector game, coin up arcade games called Lunar Lander. It was totally a physics game as well where you had to navigate your fuel and land on these little platforms on a lunar surface, and I was terrible at it, but it had such good sound.

Paul

What's your next one for us?

Tod

So our host for CircuitPython Day, Liz Clark, built a hardware music visualizer for the Fruit Jam, modeled on the old Atari video music box. She calls it the Fruit Jam video music machine. And let me see if I got a picture up here.

I can show you. So this is kind of what it looks like. The white screen is just a monitor.

The device that she built is this cool kind of 1970s-looking thing with wood grain and these step switches and the cool brushed aluminum knob. So the original Atari video music hardware was released in 1977, and it was the first commercial video music visualizer, as far as I'm aware, The video it output was created just with logic chips, clocked from the video signal and modulated by the audio signal. It looked like a piece of hi-fi gear with four knobs and 12 buttons.

You wouldn't know it was like something for your TV. It looked like something that would just belong in your amp stack. But with those controls, you can get a neat range of effects that reacted to music.

Granted, all these effects were variations of colorful diamonds or lines, some of which that Liz has put up here on her demo. But they were still pretty neat. This is like 977.

So Liz took the designer inspiration from the entire video music. It made this cool Fruit Jam-based thing. And the code that she has for it is pretty cool because it takes the audio from the mic that's, oh, yeah, instead of having to feed a mic into it, it just reads from a built-in microphone.

So it takes audio in from the mic. It gets a spectrogram of that audio using FFT. And it does analysis on that spectrogram to use it as inputs for the various visual effects.

And this kind of process, this loop, is really useful for a lot of audio projects. Anytime you want to do any kind of, I want to look at the audio at a more kind of higher level than just looking at the amplitude. This is the same process.

So if anyone is interested in doing any sort of audio project that actually does audio analysis, look at Liz's code. You can get some cool techniques from it.

Paul

I love audio reactive projects. My first CircuitPython project ever was an audio reactive project with a PDM in mic and an 8x4, so a 32 neopixel feather wing.

Still sits on my desk to this day.

Tod

Oh, cool.

Paul

Yeah, I love audio reactive stuff.

Tod

So what's your next one for the show?

Paul

Where to start with this one? First, let me start this by saying, I'm not a game designer. I don't know anything about designing games.

So if I get some of the details wrong here, I'll just apologize up front. One of the knocks against CircuitPython is that it's not that fast when compared to and that's okay. That wasn't a primary feature for CircuitPython. But that perception may be why CircuitPython doesn't have a lot of homebrew games for it, and that's where picogame comes in.

picogame was created by Vladimir Smitka, and he's created a great write-up of picogame on Chiptron EU. picogame is a small 2D game engine built on top of CircuitPython and requires about 200K of Ram to run, and it can also run on the RP2040 and 2350 family, as well as a number of boards from a expressive. What Smitka, as he goes by in Discord, has created, is a game engine written in C, compiled into CircuitPython. This handles all the graphics, including collisions and other computationally heavy tasks. On top of that is a set of Python libraries to help with USB game pads, keyboards, audio, synthesis, animation, score saving, and more. This lets the programmer focus on what's important, the game design. And the game programming is done in CircuitPython, and we all know that Python is one of the more popular languages, and CircuitPython tries to conform as much as possible with C-Python or desktop Python. Smitka shares his motivation for creating picogame in that he had a PicoPad that you see on the screen here, a checkmate handheld gaming device that uses an RP2040. The Pico pad has a picture of a defender-like game on it, and Smica tried to recreate it, but found displayIO too slow, and so picogame was born, with picogame using a core written in C, performance goes way up, and the article also shares the impressive performance stats.

There's an Adafruit game called Bouncing Balls that runs at about 115 frames per second normally. With picogames compatibility layer, more than double to 250 frames per second. We mentioned Dan Cogliano's moon miner game earlier.

Smitka rewrote that in picogame, and not only was it six times faster, the code was 40% smaller thanks to the engine's native functions. So what can you create and how do you create a game with picogame? Well, it's got a great documentation website.

And just starting at the top, it's got, what is picogame? You can see it in action here. It tells you what it gives you.

And then right here, it shows you what can you build. So not only does it have the example games in there, you can try them right in your browser.

Tod

Yeah, the simulator aspect of picogame is really cool because it lets you kind of work on something wherever you're, at, you don't have to have the particular piece of hardware you're designing for with you at all times.

Paul

Right. And what I love about this with the games is not only can you play them right in your browser, you scroll down, and you can see that this Tetris clone is running in less than 200 lines of CircuitPython.

Tod

Oh, we're not seeing that. We're just seeing your browser.

Paul

Oh, no. I'm not quite sure how to change that, to be honest. So let me drop this in the Discord. But if you hit that link, You'll go right to the playground where you can try the games in the browser and see the code that makes up each game.

Yeah. So the development has all been in the open. Smica has shared progress and asked for feedback in the CircuitPython Development Discord channel.

There was even a recent discussion about if I understood it right, including picogame in the CircuitPython core and not as a library. I think this is an awesome idea. The batteries included nature of having this built right into CircuitPython would make it a great fit. Pair it with something like the Fruit Jam and we'll have to get the word out to the maker and homebrew game communities that there's a new game platform on the block. If you want to see picogame in action, tune into FOMI guys' Game Jam Scream later today at 6 p.m. Eastern.

He'll be building his game and picogame and I'm looking forward to see what he comes up with.

Tod

I think there's a PR currently open in the in the CircuitPython GitHub repo, which means there is a pre-built UF2s, I think, because I think that's what happens with the PR is you get kind of pre-built versions, which means you can try out picogame in CircuitPython right now without having to do any sort of compiling, which is very nice.

Paul

Oh, that's awesome. I didn't even realize that you could just install one of the UF2s off the PR. That's genius.

Tod

Yeah, I think that's the way it's all set up. But yeah, it sounds like Scott's been working with Smica to help get it into CircuitPython, because this is like some pretty low-level changes to how the display stuff works. And so I'm really looking forward to it.

Paul

Yeah, I'm excited. What's your next one for us?

Tod

So another neat project outside of the Adafruit community that I saw recently. It's building a autonomous Lego train with CircuitPython and LIDAR. This is from Lorraine from Element 14.

She also posts a nice YouTube video describing the design hurdles and how it all comes together. And you can actually see the final effect in action. But her project immediately taught me two things that I should have known.

Like, wait, you can get a Bluetooth-controlled Lego train. Like when did this happen? I'm going to have to get, yeah, I might have to get one of those.

The other is there are serial, controllable, 360-degree lighter scanner modules. They're like 70 bucks. I'll put a couple of links in the show notes for like later.

If you're listening to this on a podcast, clearly I'm not as good at hackers. I thought I was that I missed that these two things existed. I thought lighter scanner is like a hugely expensive, like multi-thousand-dollar things.

You can only put on top of your smart car or whatever, but now you can get them. and they're about the size of a deck of playing cards. So her project is really funny.

It uses CircuitPython on a Seeed Xiao NRF 52840 to talk BLE to the train and then talk serial to the LIDAR scanner and control neopixels along the way. And let's see if there's a, I forget if there's actual picture. This is kind of the picture of the final result.

And this is a perfect use for CircuitPython because, you know, CircuitPython BLE on the NRF chips is really great. And doing cereal and Neopixels is so easy. The only real complexity was the data coming off the LIDAR is just kind of this raw data that you need some math, some algorithms to actually parse and it's something useful.

But fortunately, she found some Python code for the Raspberry Pi written in normal Python and was able to quickly port this to CircuitPython because this is one of the great things about CircuitPython is it's almost like real Python. And so if you find algorithms, there's a good chance it'll work for, you can get it to work for CircuitPython. And so the result is that she's got this autonomous light-up train that moves along a track on her wall up near her ceiling and it knows where it's going.

So it doesn't run into the ends or if there's something on the track, it knows to stop. Yeah, and it's like, yeah, sure. You know, she notes that you could have done this with maybe just a couple of ultrasonic distance sensors.

But that's not nearly as fun as using the LIDAR scanner.

Paul

Right.

Tod

So this is cool. Watch the video. She shows in the video, I don't know how well this will play, but getting data off the lighter scanner.

And because it basically gives you a sort of 360 donut around it showing you how far things are. And this is her hand playing around with the lighter scanner and just getting the raw data out at certain arcs of the view that it has. But it's really cool.

I highly recommend checking out this article and watching the video.

Paul

Yeah, watch the video for sure. And like you mentioned, I love the fact that she was able to take Python code and port it to CircuitPython. Like I mentioned earlier, right? CircuitPython tries to conform as much to see Python as it can. And that's just one of the benefits is that portability, which is just so cool.

Tod

So what's your, I guess, maybe final one? Is this, are we almost done?

Paul

Yeah. Time flies when we're live. Yeah.

By now, I'm guessing most folks have heard that our favorite CircuitPython code editor, Mu was sunset back in December of 2024. We've seen a couple of really strong online editors since then, and now we have a spiritual successor to Mu called RV Circuit Studio. Created by Armstrong Subero, RV. Circuit Studio is a full-featured CircuitPython IDE.

It's written in Python. It has so many nice touches, I'll probably forget a few. But the first time you started up, it asks you, where do you want to back up your code.py file, which is so nice. Just pick a local directory on your PC, And it will also save it there when you update your code.py on your microcontroller.

And then when you plug it in a board, it will detect whether it's running the latest version of CircuitPython or not and open the download page to your board to help you if you're running an older version to make it easy to download. So here's RV Circuit Studio in action. The first thing that you might want to do is hit the settings button and make the text size a little bigger than it is.

It's a little small when you start. And I've got it blown up for the live stream today. but everything that you need is right along in the menu bar.

So you can see you can open files here. There's a play button for the REPL to start and stop. One thing to note is that Control C and Control D does not work down here.

You actually have to use the button to start and stop your code. I've got a nice pink feather RP2040 with a very old DPS 310.

Tod

Oh, limited edition pink feather.

Paul

That's right. Very proud of that. And this is a temperature and barometric pressure sensor, and I'm just printing the temperature in Celsius to the REPL.

So one of the other nice things it does is it makes Toddbot's cereal plotter obsolete. It has its own serial platter built in. So you can see it plotting along the temperature.

You can see when I grabbed it and it actually changed the temperature. But here's where my favorite feature might be. In the left-hand sidebar here are a ton of code snippets, organized by type. I don't know about you, but I learn a lot by cobbling together different bits of code.

And here it puts a ton of examples right at your fingertips. From to bouncing, there's an example for that, to PWM, to battery voltage monitoring. It's all built in.

Like I mentioned, it's a Python app available on Windows, MacOS, and Linux, but it's not a native app, so you'll need to use the built-in menu bar, like I mentioned earlier up here. Everything in the UI has a toggle so you can hide or show the project explorer, the snippets, and more. It has a debugger built in, and you can step through functions like you would find in most modern IDs.

You can also reformat your code using the black linter, and it will also prompt you to install it the first time when you try to run it. And lastly, one of my favorite features is the library manager. What it does is it shows you all the libraries that you have installed in a list, and they're color coded if the library needs to be updated, And there's just one button to click update and it will update all your libraries for you right in the ID, which is great.

And then it's got another button right next to it called Browse the Bundle, where if you click that, you can look for any library that you need in the official bundle. I wasn't able to get the community bundle up and running within it. I'm sure I'm probably just missing something.

Tod

No, I actually opened an issue on this. And it's an official response that he will not support the community bundle.

Paul

Oh, bummer. Okay.

Tod

Yeah, it's a bummer.

Paul

But either way, my hat's off to Armstrong. You know, thanks for creating RV Circuit Studio. When someone asked me for an editor recommendation, this is now my go-to for CircuitPython.

It runs locally, has install packages for MacOS, Windows, and Linux. It does all the major things you would expect. And there are so many nice touches from the code backup to the snippets, to the library manager, to using black for code formatting.

I could go on. I'm a big fan.

Tod

Yeah. And it's also written in Python itself, like desktop Python. So if you want to learn, like if you're pretty good at CircuitPython, I want to learn more, like, quote, quote, quote, real Python, you can totally peruse his app here and kind of see how things work.

But because I think it is written in Python, some of these other aspects we might expect from an application, like be able to do Control C in the Ripple or use the native file edit view menu, doesn't really exist. So just beware. It's kind of its own little self-contained world.

Paul

Yep, it sure is. What's your next one for us?

Tod

This is another retro-inspired project from Liz Clark. Thank you, Liz. This is the chip tune player.

It's a inside this cool little arcade-looking box is a feather, an I-2-S audio DAC, and a touchscreen display that has a SD card little holder at the top. And it lets you load up an SD card with retro chip tunes and play them. And you think, oh, that's just like a MP3 player or a wave player, but no, it's so much cooler because Liz made a CircuitPython library that uses synthio to emulate the A.Y. 8912 sound chip. This is a chip that's been in many coin-out video games from the 1980s. All those bloops and bloops you might think of old video games are probably sounds generated from the A.Y.8912.

Unlike today's modern fancy game sound generation hardware, back in the 80s, you had to use one of these special chips to make noise, and they had very specific limitations. For the A1-8992, you got three whole channels of sound, and each channel could either play a square wave or white noise, and you could adjust the pitch and the volume, but that was it. If you wanted to do any sort of envelope generation, there was one envelope generator for the whole chip.

It affected all the voices. There was no filters. There was nothing.

But with that, a clever game designer could make a whole video game soundtrack with game sound effects. And so some of my favorite arcade games from that time period that use this chip are Frogger, Tron, and Spy Hunter. I love Spy Hunter.

So these chips are very beloved, so much so that there's a whole special file format called VGM. Dot VGM files for video game music that stores the various chip instructions on how to make sounds at certain times. And there's entire fan websites out there that will, let me see if I can show you it real quick here.

It's called VGA Rips. Here we go. So these are VGM files for various games or other things.

And you can just download these and stick them on the SD card and play them in Liz's thing. Because her CircuitPython library parses these VGM files and then runs that through the AI8912 emulator. And the library is pretty cool because it's a great demonstration of how Synthio does.

stuff and how you had to use it for something actually useful. Because like, A, doing three squareways and some noise with a simple envelope, that's something that Synthi O can totally do. And being able to like have that as a, here's a thing that accomplishes a specific goal is very cool.

I've been for the last year or so trying to do an SN 76489, I think, a sound effects chip emulator. This was a chip that you could buy from Radio Shack back in the 70s and 80s. It's about the same complexity as this chip that Liz emulated. So thank you, Liz.

I might be stealing some of your work.

Paul

Got to love open source.

Tod

Yeah.

Paul

And like you, I was a big spy hunter fan, but I think I loved the Tron video game even more.

Tod

Yeah, it was good.

Paul

All right. Well, I think we have time for one more. And Tod, I'll let you share it as it's one of the most innovative uses of CircuitPython I've seen in the last year.

Tod

Yeah, and I forgot to bring up a screen for this. Here we go. I think maybe this.

He has a really nice website for it. It's called PICOTTI. There's actually a really good story about this as well.

So CNX Software Embedded System News is a really old embedded software blog. Very handy to look at. But so what is PicoTTY?

Imagine this. You've got a whole cluster of servers and you need to manage them remotely. What do you do?

So PICOTTY helps you manage that server cluster with a collection of PICO's running CircuitPython and then a Raspberry Pi 2W as a manager. It's a real niche tool for system administrators to manage groups of machines, but it shows how useful CircuitPython can be even in these demandion environments. The problem with servers is that they're headless.

They've got no screens, no keyboards, but you still need to be able to remotely type on their keyboards and see their console messages, especially when they boot. Normally it means you have to buy some expensive remote management KVM hardware, but security researcher ChironGV, created a low-cost system for network serial console for a networked server console with keyboard injection using Raspberry Pi Picos. They're in CircuitPython using the USB serial and USB Hid modules that are built in CircuitPython.

The CircuitPython Picos feed keystrokes to the server to type commands on their keyboard because it looks like a keyboard to the server. And then it receives console messages over USB serial. This does require that the server is configured to actually output console messages via server.

which is something that like Linux can do, but Windows can't do, I think. And then the reason why there's a PICO is that you've got, sorry, the reason why there's a Raspberry Pi 2W in there is it's a hub. It receives all the messages from the PICOS unless you control the various PICOs.

Via a nice web interface, you can see different server messages from all the different servers in real time. You can send keystrokes. You can even do OTA updates of the PICOs if you want to update like the version of Circa Python or whatever without having to touch anything.

As long as you can access the Raspberry Pi 2W, you can access all the servers and all these little picos controlling the servers. So this is kind of the architecture diagram of what he's got set up. Here's the, here's the Raspberry Pi 2, here's the various picos, and then these are the various servers down at the bottom here.

And if you wanted to, you can even make a little 3D printed enclosure that includes four of these modules for these picos and a Raspberry Pi. It's something that I wish I needed. I needed this like 20 years ago back when I was a system in.

Don't need it now. But I've got a home lab with like maybe four servers that I could perhaps benefit from this. But so cool.

And it's kind of neat to see the ghost of my past job kind of pop up.

Paul

What a great use of CircuitPython. For so often we think of makers or maybe people new to programming or coming to CircuitPython. But here it is in a commercial production environment being used with real world servers, which is just so cool to me.

Yeah. Well, that's our show. Thanks for hanging out with us and to learn more about The Bootloader, visit thebootloader.net or find us in your favorite podcast app. Stay tuned for JPs Workshop at the top of the hour, and thanks to Adafruit for having us. And until next time, stay positive.
