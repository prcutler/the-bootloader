---
date: 2025-11-03
title: "Episode 26 Transcript"
linkTitle: "Episode 26 Transcript"
description: "Episode 26 Transcript - Super Smooth - with Liz Clark"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Paul Cutler

- Welcome to The Bootloader. I'm Paul Cutler. -

Tod Kurt

- And I'm Tod Kurt. The show works like this. In each episode, we bring about six things that we're excited to share, chatting about each for about five minutes. For detailed show notes and transcripts, visit thebootloader.net.

Paul Cutler

- We now have stickers. If you're interested in getting a two inch by two inch sticker, visit thebootloader.net and click news and the link to the form is there. fill it out and I'll send you a free sticker. With that out of the way, Liz Clark has joined us today for a second time. Liz, there used to be a podcast I listened to and whenever a guest would come on for the second or third time, they officially become a friend of the show. So you're our first official friend of the show.

Liz Clark

- I'm honored, thank you so much. Thanks for having me again.

Paul Cutler

- Thank you, Liz. - What's the first one that you brought for us?

Liz Clark

- So my first pick is something I've been using a lot lately from my work of Adafruit, and it's Raspberry Pi Connect. And what it is is it's a new service, or at least it was new to me, that comes with the new distributions of Raspberry Pi OS. So if you've been using the newest Trixie or even Bookworm before that, and you saw this little circle icon up at the top next to the status, that's what that is. And what it lets you do is when you log in, you're able to manage all of your Raspberry Pi devices. And it's not software dependent, it's actually hardware tied. So even if you do a new install of the OS, your devices still appear registered, which is nice. And what you can do then is, in a browser, you can log into your Raspberry Pi either with a remote shell session or a windowed session. So that means you can have it just powered on headless, but have a full browser view with your keyboard, your mouse, and you can use it right at your computer, which for me, I don't have a lot of space in my desk, so that just is wonderful. I don't have to have another keyboard and mouse. I don't have to capture it with my capture card. Don't do any of that. But the best part, I think, is you can also copy and paste to the Pi. So if you're doing development and you're trying to do, oh, I don't know, E Ink in its, for example, and you're trying to find different things on a data sheet, you can copy and paste really easily. and it makes it really nice. And then also it means I don't have to log into GitHub on a Pi. I can copy it out and do a PR on my home machine. That has been a lifesaver recently. And even recently, I did a project for Halloween for Adafruit, which used a Raspberry Pi. And it used a camera. And for the demo, I wanted to do a screen recording to show it happening in real time. And in the past, it would have been like a mess of cables all over my apartment trying to get the capture card and everything. But for this, I was able to just set up the Pi in my usual filming spot, film, and then I was just doing a regular screen grab of my computer of the Raspberry Pi Connect window, and it was just beautiful. So if you're doing a lot of Raspberry Pi stuff, highly recommend setting up Raspberry Pi Connect. Really easy, and it just makes the workflow a lot simpler.

Paul Cutler

- How is performance, especially in a windowed mode, when you're connecting remotely? Is it jerky at all? Is it smooth?

Liz Clark

- No, it's super smooth. 'Cause sometimes I've even forgotten that I'm in Raspberry Pi Connect if I maybe started with OBS and I grab the keyboard and mouse that's actually connected to it, and I'm using it in the browser window now, so then I remember, oh wait, I can just use my regular keyboard and mouse, I don't have to use the thing in my lab. So it's really smooth, which is surprising.

Tod Kurt

- So for Raspberry Pi Connect, I've got some Raspberry Pi servers that I connect to via usually SSH, but sometimes VNC, but the VNC stuff's a little janky, and so this is kind of interesting, but does the Raspberry Pi Connect stuff work for non-GUI mode, do you know? It seems like it's a GUI mode thing.

Liz Clark

- That I haven't checked. It might be GUI only. I haven't checked that.

Tod Kurt

- Yeah.

Liz Clark

- So that would be something I keep in mind.

Tod Kurt

- Yeah, this is definitely cool if you don't have, like my servers are right over here, I can touch them with my hand, but if you're in a different state, perhaps, different country, you can still have access to your computers. That's pretty cool. So Paul, what's your first one this time?

Paul Cutler

- My first one is the OpenBook Touch. Joey Castillo has announced the OpenBook Touch, an open source e-reader coming soon on CrowdSupply. I interviewed Joey back about three years ago in episode 22 of the CircuitPython show. Joey's the creator of the SensorWatch and the SensorWatch Pro among other things. And these were PCBs that allowed you to upgrade Casio's iconic F91W watch by swapping it out with a new PCB that adds an LED and infrared light sensor and more. He ran two successful crowd supply campaigns for the SensorWatch and the SensorWatch Pro. So I have a lot of confidence in his latest campaign for the OpenBook Touch. He's been working on it for a while and it's exciting to see it coming soon on crowd supply where it's described as a long standing effort to build an affordable, open source, hackable, DIYable ebook reader. It features everything you would expect in an e-reader And here's just a few of the stats. It's got an ESP32 S3 microcontroller with support for Wi-Fi and Bluetooth, a 60 megs of program memory, eight megs of RAM, a 4.26 inch 480 by 800 display with warm and cool front lights. The touchscreen is capacitive and it's got a micro SD card so you can store all your eBooks on it. And the battery, it's got a LiPo battery with 1800 milliamps with integrated charging and monitoring USB-C Type-C connection, all in about a package that's 77 by 118 by less than 10 millimeters thick and only weighs three ounces. Everything will be open source, including the software, documentation, KiCad schematics, board files, and the enclosure. By using the ESP32-S3 processor, it's got plenty of horsepower for EPUB documents, and with the S3's low-power RISC-V coprocessor, it should achieve days to weeks of reading time and months of standby time with its user-replaceable LiPo battery. Under the hood, it's using the ESP-IDF framework and FreeRTOS, so no more Arduino workflows like earlier prototypes had, though it has been tested with both Arduino and CircuitPython. The project is coming soon on crowd supply, and I'm excited to see an open-source e-reader that's not tied to an online bookstore full of DRO. Yeah, I was just looking at like I've been trying to get back into to reading more more frequently and e-readers are the obvious solution Doing it on the phone or the tablet seems very distracting. But like the big Behemoth out there is the Kindle which is amazing, but it's tied into the whole Amazon thing hasn't Joey been working on the open book project for like years like it seems like I've seen like Yes, every time I see like he posts on socials. There's like a new better version that's come out This looks like the best one but so far

Liz Clark

- I love Joey's work. I'm sure I'd be curious to chat with him about it. I'm curious if he had situ issues with sourcing the actual E Ink display because often the Manufacturers like they'll stop with no warning with the chip set. So I'm curious if that's what's part of the delay, but It's really cool. That's a 800 by 480. Like those are really nice and I just his work is great. His documentation is great So really cool. See you come out

Tod Kurt

- Yeah, and he he knows low power design like all that work. He did on his watch Replacement where you saw him sweating the micro amps to get it down because it's a watch it has to last for a long time So I'm sure he's do been doing the same thing for this this e-reader Which you don't really think of as being the thing you have to plug in very often We're recording this on Thursday, October 30th and Tod. Are you going to? Supercon this weekend because if you are Joey, you'll be there and you might be able to see it in person. Oh And on Halloween and I'm going and it'd be wonderful if I see him He's he's always he's always very very pleasant whenever I run into him. So yeah, it'll be nice Check it out and give us a book report when it won't for the next episode book report

Liz Clark

- I saw he also has simple add-ons. He's doing two that are like an homage to the open book. It's like these little mini illuminated That's cool. Yeah, did their screens with the book covers? So you might have some of those (laughing)

Paul Cutler

- All right, Tod, what's your first one for us?

Tod Kurt

- All right, so you can now design circuit boards with code, well, sort of. So let's say you want to design a circuit board. This is a little bit of a refresher on how circuit board design works. As you are both aware, but maybe not some in our audience, usually that begins with a schematic, a flowchart-like drawing that describes the logical connections between the parts of your circuit. From the schematic, you then create the PC board layout. This is the physical layout of exactly which components you'll be using and exactly where they'll be on the circuit board. In your schematic, you might just have noted a 500-ohm resistor, but it's during the PCB layout where you choose exactly which of the thousands of 500-ohm resistors that your circuit needs. At the end of this design process, you'll have two drawings, the schematic for logical design and the PCB for the physical layout. But what if instead of starting with the schematic drawing, you started with code, and that code then gets turned into the PCB layout? This is what the Atopile project is attempting to do. That's A-T-O-P-I-L-E. Atopile is a few things. First, it's a Python-inspired domain-specific language for specifying components and connectivity between them. Like the way you would assign variables and properties to variables and stuff, you do the same thing, but now you're assigning properties and connectivity to components. Like code, you design little sub chunks of functionality like LED status light, keyboard matrix, voltage regulator, or even RP2040 microcontroller. And each of these subcircuits then become a reusable function in AdaPile. And so AdaPile is also a package repository, sort of like NPMJS or PyPI, but the modules it knows about are these subcircuits. And like in other languages, you can install them and then import them into the top of your code and use them in your code, I mean, circuit. (laughs) More importantly, these Adapah modules contain KiCad PCB layout chunks. So when you import the RP2040 package, it contains the entire KiCad PCB layout for an RP2040 microcontroller circuit like what's on the Raspberry Pi Pico. So the somewhat tricky power trace routing, the correct crystal oscillator and capacitors critical for the chip's function are all specified here and laid out properly according to the guidelines in the data sheet. having those tiny but important details bundled up is really nice. Like normally you'll be copying and pasting those from previous known working circuits. And so now you just say, import RP2040 at the top of your out of file file and you get all that. And so out of pile is also a compiler. Once you have your out of pile code written using these modules and some of your own, the out of pile compiler generates the PCB. When you open the board in KiCad, you'll see the sub modules that are fully routed, but the connections between them are not. so you maybe just move them around and then quickly hand route the connections between and you're bored to be finished. From code to finished PCB, how amazing is that? Well, that's the dream. (laughs) And it's not even the end goal for the devs. By moving the logical design, the schematic side of things, into this hierarchical code-like way of specifying it, the AdaPile devs are hoping to leverage LLMs to help design circuits. To do this, they have a first-party VS Code extension and uses cursor AI to help with writing the Adopile code. Apparently it's pretty good at writing Adopile code. I mean, you know, me as someone who's only been playing with it for about a week, it writes a better Adopile code than me. I've been playing with it, it's interesting. I'm a bit skeptical. There's a bunch of gaps in the package manager, sort of like, you know, how useful is Python without all the cool libraries that exist out there? It's hard, if you're having to reinvent everything, it's kind of tough. It's the same thing in KiCad. It's like, KiCad is much easier because of all the available components already there. You don't have to draw every component. You can import the libraries and stuff. Also in regular circuit design, there is this back and forth that usually happens between the schematic design and the PCB design. It's called forward and backward annotation. You know, you'll be laying out the PCB and you'll wanna make some small changes. And so you make those changes and then you have that update the schematic. And this sort of back and forth happens a lot. AutoPilot doesn't support this concept. its flow is very much one way from code to PCB layout. It breaks the way that you think of your design if you're used to that way of thinking, but it's very similar to how code works. You don't take your machine code and make changes and then push that back up to your source code. Related to me, this got me looking into KiCad and KiCad supports design blocks in a schematic view. These are reusable schematic functional modules that you can just plop down, sort of similar to the reusable module of Adopile, but KiCad doesn't yet have the corresponding PCB layout side of that, which is the part that for Adopile is really attractive to me. 'Cause layout of this is really kind, like layout of some of these subcircuits, these complex subcircuits that are high frequency or have weird capacitance, like RF circuits is a real tricky thing. So having that already done for you and done once is nice. And also I miss schematics. The code view of AdaPal is nice, but like well-structured code, a lot of the implementation of a circuit is hidden behind the sub-modules, but these sub-circuits. And when you're trying to figure out a problem with your circuit, it's often useful to get a holistic view of how the whole thing works, which you can get with one schematic page, but it's hard to do that with these sort of well-structured code that AdaPal encourages. So I'm gonna keep playing with AdaPal. Seems really interesting. We used to design FPGAs and ASIC chips all with schematics, now they're almost always done in the VHDL or VLog languages. So there's precedent for moving circuits from a schematic to a full code-based workflow. But yeah, and I'm not even touching the LLM side of things, because that's like a whole other can of worms I don't want to look into yet. But yeah, it's interesting. And I think if you're more a code-thinking person, Adapile might be an interesting way for you to get into circuit design. So is Adapile to PCBs like OpenSCAD is to CAD design? I think a little bit, yeah. Yeah, yeah. That's a good way to think about it. Also similarly one way, where it's like your source code and it gets compiled down into the solid model. I did think it was interesting. I was flipping through some of their documentation and you're right, they recommend using cursor as your IDE. And in the docs, they specifically call out that LLMs have gotten good at writing ATO code, which is what Adapile uses. I kind of did a double take when I read that because new to me, but it's great that it had something to train on. Yeah, it's kind of, it's an interesting, it seems like their thought process was, "Hey, we want to use chat.gpt to write KiCad boards. Oh, well, the file format that KiCad uses isn't really usable by LLMs. Well, what if we had a language?" [laughter] And here we are. And here we are.

Liz Clark

- I'd be curious if it could be leveraged with GitHub CI,

Tod Kurt

- so that if you needed to maybe swap a part,

Liz Clark

- and it could maybe do a check to see if it's still meeting the parameters set in the code.

Tod Kurt

- Yeah, that's interesting, because they do have a whole test framework that I've not looked into at all. But you can specify various attributes of components. and I wonder if you specify then attributes on the sub-circuits that use those components, if then you're testing, you can do like, oh wait, you're blowing your power budget or something, right?

Paul Cutler

- You know? (laughs)

Tod Kurt

- Yeah. - Like, I'd be interested to see what kind of tests they have, because they do have some sort of a CI set up as well, so as you check in, it'll do some tests.

Liz Clark

- Yeah, that would be really cool.

Tod Kurt

- Yeah. Okay, so Liz, what's your next one for this time?

Liz Clark

- My next one is the MIDI Baby Gen 4, and it's this utility pedal made by Disaster Area Designs. They make a lot of music utility pedals aimed at guitarists, and it's operated by Matthew Farrow, who also runs Alexander Pedals. The MIDI Baby has been around for a bit. I actually did a teardown of the original one when it came out on my, let's say, YouTube channel. That's how I met Matthew. that. He's a really nice guy. He then offered to do a teardown of one of his Alexander pedals with me on the channel where he actually walked through the circuit. And the original Mini Baby used a SAMD21, but this new one uses an RP2040. And the reason why I bring it to the show today is that it also can run CircuitPython. And he has ported it to CircuitPython. It does have a USB MIDI host port, it has a NeoPixel. So there's definitely, I think, some interesting community hacking that could happen with it. And I think he's also hoping for that. There's so much awesome MIDI support in CircuitPython that I think with this little tiny little square pedal,

Tod Kurt

- there could be some cool stuff there. Yeah, that's pretty cool. It's like, I love the proliferation of these "guitar pedals" that have no like guitar-ness inherent to them. This is just a MIDI controller, you know, and a MIDI router that is in guitar pedal format.

Liz Clark

- It's the only way I think that guitarists can really understand MIDI is if you give it to them as a pedal, then they're like, "Oh, okay, I get it now."

Tod Kurt

- Yeah, so this is pretty great. And I love how you can configure it all via the little WebUSB webpage thing, so you can do all these crazy stuff. Like, like one jack can be transmit or receive of MIDI, or it can be other stuff. It's just like, what?

Liz Clark

- Yeah, it's really wild how it all works. And then if they do a new firmware release that isn't CircuitPython that's written in the Pico tool, then you can also do it via the web GUI, which is really nice.

Paul Cutler

- Oh, that's nice, yeah.

Tod Kurt

- All right, Paul, what's your next one for this time?

Paul Cutler

- Next up is an open source gaming console called the Game Tank, which you can learn more at gametank.zone. It's marketed as an open source 8-bit retro console that you can build and build games for. It compares itself to fantasy consoles like Pico 8 or TIC-80, but sets itself apart because it's a physical hardware device first, followed by an emulator second. And yes, there's an emulator also to make development easier. The emulator runs on Linux, Mac OS, and Windows. And when they say it's open source, everything is open source. You can get the PCB schematics in Eagle or KiCad right from their GitHub repository, so you can order your own. It also includes the files for 3D printing, so you can print your own shell or even print your own controller. For the hardware, it features a 3.5 MHz CPU with a double 128x128 framebuffer with 200 colors. It also features a dedicated audio coprocessor. The homepage at gametake.zone features a one-minute teaser YouTube video that you have to see the motherboard with all the chips built in. It looks like it's right out of the 80s. One of the things that sets it apart, though, is that it's an actual hardware console that uses actual cartridges to load the games. For developers, there's a GameTake cartridge programmer that connects via USB-C to flash ROM files onto compatible cartridges. For creating the games themselves, there's a C SDK and a Rust SDK. Say that three times fast. On the CrowdSupply page, it mentions because it's open source, that's how the Rust SDK, the Rust emulator and the Rust Cartridge Flasher program, which has overtaken the C++ version and features, all came to be. The Game Take originally sold for $300 in their store, so we'll have to see how much it will be once the crowd supply campaign kicks off. It's a pretty neat project in that everything from the console to the software SDKs to the emulator are all open source. - That's really cool. And I must say, the fact that it has those DB9 connectors for the joysticks is a super, super retro triggering for me. - Yeah. - Yeah, and when you actually open the shell and look at the motherboard, for lack of a better word, it takes me right back to looking at like an Apple II with all the different chips laid out in order. - Totally, yeah, this looks, it's got a very retro look. Like a lot of these modern console retro game platforms are basically like, here's the one big FPGA or the one big microcontroller that does everything. But this one looks like it's from the 80s or 90s on the inside.

Liz Clark
- I love that there's this renaissance happening right now, like kind of retro computing, but rethought with a modern spin on it. It's really cool to see all these different projects coming out.

Paul Cutler
- Yep. There's some Pico 8 games that you can play right now in a browser.

Liz Clark
- And I think even their emulator works in a browser.

Paul Cutler
- So it just makes it so much more accessible.

Liz Clark
- Yeah. I like that the emulator they've got on Linux, Mac OS and Windows. That's cool. Confidence usually one or one, yeah.

Paul Cutler
- All right, Tod, why don't you wrap it up for us?

Tod Kurt
- Okay, so you know, Quick StemmaQT, the cabling standard by SparkFun and Adafruit? It enables hundreds of different I2C devices to connect in a consistent way, make it easier for new people to get going, and generally making prototyping ideas a lot faster. But using that makes your project bulky fast if you get a couple of different StemmaQT modules. What if there was a micro-sized similar standard? There may be, it's called Tiles from BergZone Labs, and tiles are only four millimeters on a side. While tiles are sort of like a micro version of StemmaQT or Qwiic, they're targeting a more production level market. As mentioned, each tile is only four millimeters on a side, and it has 10 connections that consist of power, I2C, and SPI. And so these little four millimeter things are meant to be soldered down on easily fabbed carrier boards. You can even have the carrier board be a flex circuit. So four millimeters, how big is that? So if you look on your various circuit boards, you might see a NeoPixel LED. The standard ones of those are five millimeters. So each of these tiles is smaller than that. And a tile module can be a full BLE microcontroller or a six axis IMU or a LiPo battery management circuit or a haptic driver, a heart rate sensor. There's 26 tiles under active development. And they all connect together sort of like the way a StemmaQT sort of bundle of things would. The carrier PCB can be small enough to be production ready 'cause it's, you know, the four millimeters, right? It's taking the design blocks approach I mentioned before with like KiCad or Autopile and making them physical. And the nice thing about the tiles is that the modules will be pre-verified and certified. So you can just use them as if you use a component and all the drivers are open source, just kind of the same way that Adafruit open sources all their drivers for all their StemmaQT boards. It looks really interesting. As someone who has pretenses of making production-level things, this is a really cool way of almost going to production with things that are kind of like StemmaQT. The tiles were created by a friend, an associate, Jonathan Fine, from the Max Planck Institute for Intelligent Systems. He created the BergZone Labs in Germany to encourage the use of tiles. BergZone is also working on an online design studio app to help with the creation of project using tiles. And they've also created some carrier boards with ZIF sockets, so that you try out different tile modules without soldering. I got to play with tiles a little bit a few weeks ago, and it's really hard to describe how small they are. They're smaller than your fingernail, you know, and each one is like a full computer or a full sensor or something. It's still very early days, but I love this modular approach of tried and true circuits. I love not having to reinvent the wheels. one of these I really love about systemic UT boards. And I can see new products, like Kickstarter type products, being composed entirely from tiles for an initial production run. And there'll be links to this in the show notes so you can see kind of like what they look like. There's a few reference designs that he has created. Like there's a ring, a smart ring, and there's I think a stylus, some other ones he's working on. But I hope this goes somewhere. I hope this gets picked up by a big manufacturer like, like earlier, a distributor, like a DigiKey or something, because it'd be kind of cool to order a whole bunch of these and build a thing.

Liz Clark

- Yeah, definitely.

Paul Cutler

- Small enough where you could just order a whole reel for all practical purposes. I know, right?

Liz Clark

- I like that. It seems like it's, like you said, it's like you have your kind of STEMMAQT kind of family of sensors, but then like this would be almost kind of like the next step if you were kind of doing more of a bigger production run. And yeah, I like that.

Paul Cutler

- Well, that's our show. Big thanks to Liz for joining us this episode. For detailed show notes and transcripts, visit thebootloader.net and click on news if you want to get a free sticker. Until next time, stay positive. (chiming)
