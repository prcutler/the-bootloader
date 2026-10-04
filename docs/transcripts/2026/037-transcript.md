---
date:
  created: 2026-10-05
title: "Episode 37 Transcript - The Spirit of Radio"
---

Tod

Welcome to The Bootloader. I'm Tod Kurt.

Paul

And I'm Paul Cutler. The show works like this. Tod and I have each brought three things to share, and we'll chat about each one for about five minutes.

Before we start, I have an ask, and that's to help keep the show free of ads. Join our supporter tier and get early access to episodes, exclusive content, and more for only five bucks a month. Visit thebootloader.net slash support to learn more.

With that out of the way, Tod, what's your first topic for us?

Tod

all right so if you're in the CircuitPython universe you might have heard a bunch of news and posts about CircuitPython turbo what is that so this is i'm going to talk about CircuitPython turbo if you've done python programming you quickly learn to just not do certain things in python because it's too slow python is great but it's not a raw speed demon if you need to do a lot of math in python use various native packages like numpy pytorch tensorflow things like that but what about on microcontrollers? Well, on MicroPython and CircuitPython have had a secret for several years to speed up your code, and recent work has made it easier in CircuitPython. Adafruit has labeled this CircuitPython Turbo.

So what is Turbo? Well, if you're familiar with the MicroPython Viper Code Emitter, it's just that. But there's been some added work behind the scenes to make the lives of library authors easier.

But first, on microcontrollers running MicroPython or CircuitPython, what can we do to make our code faster? We've had a mini version of NumPy for a long time. And if the code you want to speed up is an algorithm expressible as an array operation, you can get C-like speed, which is great.

But what then? Well, in MicroPython, you can decorate your code with the @Micropython.native or @Micropython.viper function decorators. Add one of these to your function and the MicroPython parser on the chip will take it and compile it into native code.

And it'll store that compiled function in RAM. This can get you a 2x to 10x speed boost. It's a pretty amazing trick that MicroPython has had kind of since its inception.

There's a blog post that Damien George, the creator of MicroPython, wrote back in like 2013, I think, outlining how this stuff works. If you want to read about it more, it's in the links. But it's not a cure-all.

Just sprinkling these decorators on your functions won't do you much good. Because in microcontroller programs, there's I-O slowdowns, SD card writes, Wi-Fi transactions, display updates, I2C sensor reads. We're usually waiting for something in the actual code.

And none of these actions will be sped up by these decorators. They really only work for pure logic operations. Think like math algorithms that are trickier than a simple array operation that NumPy could do.

So things like image processing, audio processing, game engines, like the physics in a game engine. So that's where this MicroPython native or Viper decorator can work. And instead of doing it on the chip, you can choose to do it on your computer by compiling your code.

If you could see my fingers, they're making quotes now. Compiling your code ahead of time with the mpy cross tool. This results in a.mpy file that contains a tokenized version of your code.

This is what we normally use. We want to make our code kind of smaller and faster anyway. But it can also contain any native code functions that you've decorated.

But the problem with mpy files currently is that they hold native code. if they have native code, they hold native code for a single chip architecture. So if you need to make a library for multiple boards, you have to have multiple MPY files, and that's like a real hassle.

And in CircuitPython, the on-device native compilation is disabled by default. You'll get a syntax error invalid MicroPython decorator if you try. But as of CircuitPython 10.3.1, I think, native code loading in MPY files has been fully turned on for many chips.

You can use the CircuitPython mpy cross to make an mpy file of your.py file with a MicroPython.viper decorator in it, and it'll work great. But like with MicroPython, if you're making a library for others, you have to keep track of the many different mpy files for the different chips. And so this is part of what CircuitPython Turbo is.

It's a tool for bundling up a library and compiling the different mpy files for the different architectures. And then in CircuitPython itself, there's a slightly different loader that knows how to load from the CircuitPy drive the right version for the right chip architecture. And you can imagine this is an important thing for Adafruit because one of the nice things that Adafruit does for the CircuitPython community is periodically publish two bundles of CircuitPython libraries in MPY form.

The Adafruit library bundle, which is this huge library of drivers for all the boards that they make, but are also used by everybody else. And the community library bundle, which has fun functions and other drivers for things that Adafruit doesn't make. This is super handy.

We get nice, small, tokenized versions of all the libraries that are easily installable with tools like Circa or the VS Code extension. But you can imagine the headache Adafruit would have if they want to offer libraries with native code in them. Suddenly, every library explodes into like, you know, six or ten different files because you have to support all the different chips that CircuitPython runs on.

And so this part of Turbo is critical for them, I think. So what is CircuitPython Turbo finally? It's kind of three things.

First, enabling native code loading in.MPY files in CircuitPython. Second, a tool for helping libraries with native code manage multiple chip architectures. And then finally, a light rebranding of the existing MicroPython native code decorators.

And it's not required. I've been using the just at MicroPython.Viper decorator and the MPY cross, and it works just fine. There's no turbo in any of my code.

So if the turbo thing kind of bugs you, you can just go ahead and just use kind of the standard process that we've all been using with MicroPython for many years. And so if you have any CircuitPython code that is compute bound and you think could really benefit from this, try out these decorators. Links in the notes for how to get started.

There's a really great post that PT did on the Adafruit Learn Guide that goes through extensive detail and some examples. Or send me a message on the Discord and I can help you get going.

Paul

Yeah, I've been following this since they announced it a couple weeks ago. along with the CircuitPython 11 alpha that seems to be fully turbo enabled. So I had no idea until now that this has been around for years and years in MicroPython, which is just amazing to me that it took this long for someone to actually enable that in CircuitPython. It's pretty cool.

Tod

Yeah, I'm definitely going to go through some of my libraries because some of my libraries are very compute heavy. Like I've got a Perlin noise library that is useful for making like smooth sort of semi-random textures and stuff. And that it can definitely benefit from a turboification. So,

Paul

well, you have to report back on how well it works after the fact.

Tod

Oh, definitely. All right, Paul, what's your first one for this time?

Paul

If you follow me on Mastodon or you're one of the seven people who read my blog, you can probably guess at my first topic. And that's an open source project called Hyper HDR. Late last year, Liz Clark at Adafruit wrote a Adafruit Learn guide on how to install HyperHDR to control ambient lighting behind your TV.

Now, I have white LEDs behind my TV giving off ambient lighting, but HyperHDR takes us to the next level. Using a USB video capture card and a Mac, PC, or Raspberry Pi, you install HyperHDR, and it uses the video capture device to match the colors of the LEDs to what's on the television. So imagine you have a string of LEDs going around all four edges of your TV, and you're looking at a grassy hill with a bright blue sky and white clouds in the air.

Along the bottom edge of your TV, it would be green matching the grass, and the top would be blue or white depending on where the clouds are in the sky. So that's HyperHDR. When Liz first published the guide last year, I starred the project on GitHub and filed it away in the, that's a really cool project but way too expensive folder.

But then Hyper HDR version 22 was just released and that got me thinking. And then I decided to do it anyway after getting a surprise bonus at work. So when I said it was expensive, it ended up somewhere around $400.

Living in the Midwest in the US, I have a large basement. So of course I have a large TV. So I needed over just over five meters of LEDs.

And of course they come in five meter packs. So that was almost a hundred bucks right there because I needed two spools. The recommended USB capture card is a Ugreen model that's another $100.

You'll need a Raspberry Pi 5, so there's another $100, and that's about 75% of the cost. You'll also need some random parts like a power supply for the LEDs, one for the Pi, some HDMI cables, and an HDMI splitter. So, it all adds up pretty quick.

At the heart of Hyper HDR is a PC or Mac with a USB capture card hooked up to it, and a microcontroller to control the LEDs. A handful of RP2040 boards that also have a built-in level shifter are recommended, including Adafruit's RP2040 Scorpio board, which is what I went with, along with a Raspberry Pi 5. I also went with SK6812 lights, not NeoPixels.

The SK6812s are RGBW with an extra white channel, and these are the cool white. HyperHDR is made by GitHub user AwawaDev, and she also has created special firmware for these RP2040 boards. just flash the uf2 wire the data and the ground lines to the leds and power supply plug it into the pie and you're ready to go this is kind of where i differed from liz's learn guide she used an led trinkie with neopixels but i wanted that extra white channel which is what was recommended the hardest part of the project for me was learning how to power the leds and soldering them together i watched so many youtube videos and did so much research for that this is the first time that I've really done a major soldering project, especially with LEDs.

And of course, the first time my wife and I tried to install the LEDs to the clips on the back of the TV, I broke one of the solder joints. So I had to redo that. Let's just say I was pretty surprised when I got to the end and the LEDs all lit up.

Tod

Oh, yay.

Paul

Yeah, exactly. It also took me two HDMI splitters to find one that could bypass content protection and display HDR content. Otherwise, this wouldn't work with a 4K Blu-ray player or most streaming apps like Netflix.

If you're curious about the hardware that I went with, I have a link to my blog post in the show notes. But after you split the HDMI signal, one to the TV and one to the capture card, you flash the Hyper HDR Raspberry Pi image and boot it up. Everything is then configured via a webpage hosted on the Pi or the mini PC or whatever you're using.

You'll need to know how many LEDs you used, where the first LED starts, and in what direction the lights go. Of course, when I answered everything in, nothing lit up. It took me a good 10 or 15 minutes to figure it out.

And one cool feature of Hyper HDR is that you can preview what the capture card sees. I wasn't getting a signal. And sure enough, I just hadn't pushed in one of the HDMI cables all the way.

Tod

Doh.

Paul

Uh-huh. As soon as I did and updated the config, the lights came on. And I haven't really even touched on some of the features and the infinite color engine a Wawa created to match the colors to.

But anyway, it's pretty neat and it's really immersive. I've included a link to a 30 second demo on YouTube that's worth watching to get the full effect. This is a silly and expensive project, but I'm really happy with how it turned out.

So thanks, Liz, for writing that up last year and introducing me to Hyper HDR. Check out the show notes for a link to that video, the project on GitHub and links to my blog posts.

Tod

Yeah, well done. Soldering to the surface mount solder pads on LED strips are a pretty advanced level of soldering.

Paul

Okay, good. Yeah, and I had to do it twice because I had to inject power halfway through. So trying to line that all up and have the wires the right length behind the television, it was like playing Jenga behind the TV.

Tod

Yeah, totally. Yeah, I mean, the nice thing about these LED strips is that you can cut them every LED, which I've had the problem a few times where I wired up and I do something wrong and I blow out that first LED, so I cut it, re-solder to the next LED, try again.

Paul

I might have done that once or twice, not going to lie.

Tod

Yeah, I remember trying something similar to this. It was in HyperHDR with some other random Linux program back like 10, 12 years ago when the WS2012s first came out. And like, oh, addressable LEDs are a possible thing now.

But it looked so bad, partly because it was doing like really simple detection of the video and it was like a little laggy and like the colors didn't match very well. But like all the videos I've seen on HyperHDR looks so good. It's like there's clearly a lot of work to be more subtle and to match the colors well.

And you're using the four-channel color, the four-channel LEDs, so you get that extra white level that is so important with some of the bright scenes and stuff.

Paul

Yeah, and it's really neat how much work she's gone to because she has custom microcontroller builds for ESP32s, for SPI devices, for Adafruit devices, and then other RP2040 devices. And then with this infinite color engine she's developed, those two things in tandem with microcontrollers being so powerful now, being able to control those LEDs, it's just really cool how it all works together.

Tod

Yeah, yeah, very cool. And just being able to have this sort of like backlit screen, it must look so cool.

Paul

It does. I need to take a video and probably post that on YouTube too.

Tod

Yes, please.

Paul

All right, what's your next one for us?

Tod

I don't normally talk about the various hacking tools that are out there, even though so many of the boards I talk about support it. But things like the Flipper Zero and things like that, just because I'm not in network security and I don't really have a daily use for them. And also, these tools are often targeted at younger people who really need to learn the legality of these tools before they use them.

So it seems like advertising cigarettes to kids almost. But having said that, there's an interesting firmware out for the M5 stack Cardputer ADV called Evil M5. And it can be useful for us, for those of us even who don't consider ourselves hacksores.

You may remember me talking about the Cardputer back in 2024 on episode 9 of the bootloader. The Cardputer is a little pocketable ESP32-S3 Wi-Fi device. It's got a built-in screen, a QWERTY keyboard, speaker, SD card slot, battery, it's microphone.

It's even got like Lego stud receptacles on the back, I think. But since then, M5 has released the Cardputer ADV, which is the same size as the original. It's still $29, but it has a headphone line out port, which is really important for me who likes to do musicy things with little tiny computer gizmos.

But it also has a GPIO port on the back. And M5 has made a bunch of snap-on modules that are useful to hackers, like a $30 LoRa modules with optional GPS. so you can turn it into a mesh-tastic node, or a $30 NFC and sub-1 GHz RF scanner for $30 to turn it into a flipper zero, basically.

And so this is what makes it a next-level wireless protocol exploration tool. With the EVIL M5 firmware installed, you can do the normal Wi-Fi BLE hacking stuff that people do with ESP32s for years, like Wi-Fi sniffing or BLE jamming. Since it's an ESP32, it can also do USB hacking, like bad USB or mouse jiggling, or just act as a thumb drive.

It has all this built into its firmware. It's got like, you know, 30 different options. But it also has tools that would be useful if you find yourself not trusting of established networks, like a Wi-Fi dead drop server.

So you can share files without having to set up a Wi-Fi system or an ESPNow mesh IRC-like chat client. So you can all chat to each other without having to join Wi-Fi. It also has several anti-surveillance tools, like a CCTV toolkit for finding IP cameras and a way to discover if you're being tracked by AirTags.

It's kind of like every conceivable kind of thing you can do with Wi-Fi stuff, you can do with this firmware. And then if you have the NFC module for the cardputer, you also have a bunch of NFC tools available to you in Evil M5 that can do RF scanning and NFC scanning. This makes it about as powerful as a Flipper Zero, but much cheaper.

And to me with more features because it's got Wi-Fi and Bluetooth, which the Flipper Zero does not have. But I'm bummed I can't use my original Carputer that I got back in 2024 with this because the original Carputer doesn't have that GPIO port and the EVIL M5 project doesn't support the older Carputer. But maybe I'll get one of these Carputer ADV modules for music stuff because, you know, they're $29.

And I definitely get this over a flipper zero.

Paul

I was amused looking at the project and they've got all the warnings everywhere, right? This is for educational purposes only. But then you name the project Evil M5. It's like, yes, I understand that these things can be used for good or evil. When you're promoting the good side of it, maybe don't name the project evil.

Tod

No, it's so funny because the bad USB concept is basically it's a macro player. It looks like a keyboard and mouse to your computer. And then it's got a macro language that you give it a script to run.

So when you plug it into a computer, it runs this script. And that script could be, you know, it knows to click on the start button of a Windows computer and open up Internet Explorer and then go to this URL to download a nefarious malware package. Or it could just be like, oh, I'm going to open up the shell and type ha ha ha and make my friends giggle or whatever.

But, you know, it's called bad USB. And like so many kids on Reddit and stuff be like, hey, help me get bad USB going because I want to like tease my sister or something. It's like, oh, you don't understand what you're doing, kid.

Paul

Right.

Tod

It's called bad USB. Maybe that should be a clue, but I mean, you know, kids, I used to be a kid. I think the bad USB term would be very attractive to me. All right, so what's your next one for this day?

Paul

Tom Nardi at Hackaday had a great article a couple weeks ago breaking down the impact of FCC regulations on the 900 megahertz industrial scientific and medical band or ISM and what it might mean for the Meshtastic and Mesh Core projects. We've talked about MeshTastic before on the show in one of our Supercon episodes. I'm oversimplifying, but MeshTastic and Mesh Core are both wireless networks that use LoRa radios on the 900 MHz band to send short text messages over short hops.

You can pick up a $20 microcontroller with LoRa and get started for next to nothing. As Tom shares, it turns out that the default radio configurations may be in violation of the FCC regulations that have been around since the 80s. But it turns out it's not just a technical challenge to meet the requirements. It sounds like that part can be done fairly easily.

Mesh Core operates at 62.5 kHz and MeshTastic uses 250 kHz, and the FCC says they both need to be at 500 kHz or higher. But fixing it breaks all the existing networks that are out there, and it sounds like there's a lot of worry about fragmentation. The article goes on to share that the Philly Mesh in Philadelphia did some testing this summer utilizing the 500 kHz band.

Turns out there were a number of bugs, and even after they fixed some of the hardware they tested, they were unable to work correctly when switched into 500 kHz mode. The bigger issue, as it turned out, is that in a dense urban environment, it adds a ton of interference, and the 500 kHz band was especially susceptible to the electromagnetic interference. With all that said, Philly Mesh announced they were switching to Mesh Core because of these issues.

It means that users running old MeshTastic radios will be unable to communicate with the newer radios running at 500 kHz. Lastly, Tom shares that it's too early to tell what will happen in the Philly Mesh communities, but as he says, it's a painful transition. And speaking of MeshTastic, if you're a CircuitPython user, CircuitPython community member Feta2 just released a MeshTastic library for CircuitPython that was written in Rust. i've linked to it in the show notes

Tod

yeah i i really need to read up on this whole issue because like so mesh tastic operates in this 900 megahertz ism band uh it's one of the one of the free bands that we get like there's the there's one at 2.4 gigahertz which is what we use for wi-fi and microwave ovens and stuff and and just like in the wi-fi case where there's channels within that 2.4 gigahertz area there's channels within the 900 megahertz and this is what they're talking about about the 250 kilohertz or 500 kilohertz. So basically how big is the channel? How wide is that channel?

And I don't understand why saying that 250 kilohertz is too small. Like it seems like having a bigger channel would be worse, but they're saying, no, no, you have to have the bigger channel. And I'm like, why can't MeshTastic just use 250 kilohertz channel width, but just space them every 500 kilohertz?

Yeah, so I need to read up on like why they feel they need to go. So, I mean, I've been on the fence about MeshTastic versus Mesh Core for a long time because, like, I've heard that, like, oh, MeshTastic is great if you just want to, like, kind of all get started and you all just want to start talking to each other really quickly without having to do much setup. But it kind of doesn't scale very well, whereas Mesh Core takes a little more setup, but it can scale, like, globally much easier than – so it's like MeshTastic for an emergency maybe, but maybe Mesh Core is what we use kind of day to day.

is kind of how I've been thinking about it.

Paul

Interesting.

Tod

Yeah, but yeah, I really want to learn more about this. I know hardly anything about RF.

Paul

Yeah, that makes two of us.

Tod

Everything would be good and new for me.

Paul

What's your last one for us?

Tod

All right, this whole section, it's kind of two parts. It's called Broke Beats, cheap music hardware. So as you know, I love inexpensive music gadgets.

I make them, buy them, please. But there's two groups of people going much harder on the cheap music scene than I ever could. Cardputer hackers, which I've already mentioned Cardputer, and Chinese guitar pedal makers.

The first group are various hackers making audio apps for the M5 stack Cardputer ADV or regular. The last two years since I spoke about the Cardputer, a whole app ecology has built up around it and similar boards. And it's now so easy to try out so many of the projects.

Point your browser at the M5 launcher project and install its grub-like bootloader. And then you can choose from that same web page from literally hundreds of different apps for the cardputer. I think it was something like 680 right now.

You just search for it. You type in a keyword or two, click it, upload it. And then in about 20 seconds, the cardputer becomes a whole new project.

And it's all done in the browser via web serial. So on Chrome-based browsers, Firefox, et cetera. And one of the most amazing things in that launcher catalog is the, I think it's called, I think it's pronounced Baklava, but it's the BKLVA Pocket DAW app.

So Baklava or BKLVA is a full four track digital audio workstation on a teeny tiny screen. It's got a sampler, a drum machine, a six voice synth, a sequencer with a ranger and song mode. And then it's got a mixer with audio effects with like delay and reverb and a couple others.

And this is all free, and it all runs on this $30 handheld gadget. And the Cardputer ADV has that headphone out, right, or line out, so you can actually run it to, like, a real thing to, like, save your work or just to, like, listen to it without bugging other people. And because it's an embedded gadget, not running OS, it just comes up immediately.

There's no waiting for it to boot. And similar, you can just turn it off without any issue. Just turn it off, put it back in your pocket, and then later bring it out, and you can sketch music ideas anywhere.

or, you know, erase it. Go back to the M5 launcher page and install the Mini Acid app, a TR-808 and TR-303 emulator, sort of like the Propeller Heads Rebirth app from the 90s. I don't know if you remember that, but it was super, super cool. Or maybe instead install a web radio MP3 player.

It only takes a few seconds. There's like many different web players on there. I found this.

I'm a big fan of Soma FM and there's a Soma FM player for it. Just like, bip, bip, bip. And suddenly I'm listening to Groove Salad.

So the Cardputer ADV plus Baklava DA recommended now the other group of people making cheap chinese sorry making cheap gizmos are the china-based usually sold on aliexpress companies they're producing these little synths and guitar pedals and one of the one i just found out about a few days ago that i really like is the livtra nano core it's this handheld tiny guitar effects box it's got a big color screen two knobs battery powered, USB-C and Bluetooth. And it does, over USB-C, it does at least USB MIDI. It might also do USB audio.

I haven't checked that out. But like a pedal, it's got mono input and output, and it can do eight simultaneous effects that you chain them together internally when you're setting it up. And the effects are everything a guitarist usually needs. It's got amp simulators, compressor, drive and distortion, overdrive, delay, chorus, flanger, tremolo, reverb, EQ, everything.

It might even have an octaver effect. Anyway, and each of these effects parameters are adjustable, as you expect, you know, like every pedal has a not has knobs on it, this pedal, each each sub pedal inside this thing has knobs on it too. And then an entire effects chain with its settings can be saved as a preset.

And this thing is going for about $50 on AliExpress. It's just like, oh my god. And it sounds pretty good. Apparently, I've not got one yet.

But maybe because the UI looks pretty usable, I'm thinking maybe I'll get myself one of these for Christmas. So both the Baklava DAW app and the NanoCore gadget, I learned from the Broke Beat series that's on sonicstate.com. I'll include links to them, a link to the articles for both of these.

It's one of the better gear music websites out there and highly recommended. They've also got a YouTube channel.

Paul

I love that you had a follow-up to a topic from two years ago. No, I think that's great. And I had no idea that such a huge community had grown up around this $30 device. It makes me want to pick one up for $30.

Tod

Yeah, it's like between that, between the cardputer and the CYD, the cheap yellow display ESP32 box, which is essentially a touchscreen on the front and ESP32 on the back, which also that M5 launcher page also supports. So if you want to search for a bunch of apps for your CYD that's sitting in a drawer somewhere, go do that.

Paul

That's awesome.

Tod

All right, Paul, play us out. What's the last one for this time?

Paul

My last one is just fun and silly and makes me smile. I used to play the Elder Scrolls games back in the day and say one thing for games by Bethesda, but they do make a great job of making the games moddable. So imagine my surprise when Ikea, of all companies, announced a mod for Skyrim, which is a 15-year-old game at this point.

Ikea brought its iconic Kallax shelves to the game. Everyone knows I'm a vinyl record collector, and I have too many Kallax shelves to count. Ikea released a one-minute gameplay video showing the Kallax shelves, which are four high by two wide, following a round of fighter through the world and storing his equipment on the shelves.

But the funniest part to me is that they gave the shelves a voice and that voice is actor Matt Barry. Most people will know him as Laszlo on the TV show, What Do We Do in the Shadows? But he'll always be the incompetent boss Douglas on the IT crowd to me.

He was also the voice of the Oscars this past year and his voice is instantly recognizable. You either love him or you hate him. I've linked to the video and the article on Tom's hardware in the show notes.

It almost makes me want to go see if I still have my Skyrim disc somewhere.

Tod

Oh, that's great. Yeah, my wife just played Skyrim a couple years ago just because it came out on the Switch or something. And she's like, oh, what's this?

You know, she likes RPGs. And I'm like, oh, Skyrim. You got to play Skyrim.

Paul

It's a classic.

Tod

Oh, that's amazing. And Matt Berry. Oh, my God.

Yeah, he was also in the recent Fallout show as the voice of one of the robots, I think. I mean, he's also the voice of like an actor, like an actor that sells his voice to become one of the robot voices. Okay.

But, you know, one of the best voices out there currently, I think.

Paul

Yes, he is. And that's our show. Thanks for listening. And you can find detailed show notes and transcript at thebootloader.net. Until next time, stay positive. 

(laughter)
