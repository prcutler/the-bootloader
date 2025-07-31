---
date: 2025-08-04
title: "Episode 23 Transcript"
linkTitle: "Episode 23 Transcript"
description: "Episode 23 Transcript - Drop the beat with John Park"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Tod Kurt

Welcome to the Bootloader, I'm Tod Kurt.

Paul Cutler

And I'm Paul Cutler. We're happy to welcome special guest John Park to the show. But first, two housekeeping items. Last episode, I incorrectly said that Andrew Clark was the creator of Supriya, the Python API for SuperCollider. I received a kind note and link to Joséphine Wolf Oberholtzer and her GitHub profile. She has been developing Supriya solo since 2014. I apologize and regret the error. Second, Tod and I will be hosting a special live edition of the bootloader for CircuitPython Day on Friday, August 15th. We'll be chatting about and sharing some of our favorite CircuitPython projects and features from the last year. Check out the Adafruit blog and socials for more details, and we hope to see you there. With that out of the way, John, welcome to the show. Thank you so much for having me.

John Park

I'm a big fan of the show and it's exciting to be here. Oh, thanks.

Paul Cutler

And what did you bring for us to share this episode?

John Park

All right. I have a couple of things. start with this first one, which is floppy disk MIDI boom boxes. I became aware of these, I think, through a more modern DIY version, which I'll talk about in a second, but that led me to do a little bit of research and looking around, and it turns out in the 90s, a couple of companies, notably Roland and Yamaha, and to some degree Casio, but the big ones being Roland and Yamaha, created these music players that used floppy disks and had MIDI files on disks that you could buy and then later you could kind of put together your own floppies. And so they would have these pretty small MIDI files which contain all the information for playing a song on multiple channels of audio. And then inside of the Roland one, for example, they had a synthesizer, a little PCM synthesizer, similar to some of their, kind of based on some of the principles of some of their bigger synths, like the D-50, which was then sort of reduced down into a little desktop synth called the MT-32. And then they said, okay, let's take this idea of being able to play MIDI on a little synth inside of a box and feed it from a floppy disk. Initially, I think the idea being for music students and music teachers to be able to play a little arrangement of a song, change the tempo, transpose the key, remove or bring in different instruments. If you were practicing piano, you could drop out the piano track on the original and just have the drums and the bass or whatever. So they were kind of a little slightly cheesy because they're these, you know, somewhat of the era synthesizers that who knows what the quality of the MIDI track you have going into it is going to do. But then at some point in the more modern era, people realized, well, We love listening to songs, particularly video game soundtracks, using sound fonts, which I know Tod has talked about on the show before, which are these sort of pre-compiled blobs of a whole bunch of instruments sampled. So you have a couple of different drum kits, maybe, and eight different choices of bass to play, or maybe just one of these things, maybe a grand piano that's been sampled, or maybe synths that have been sampled, or other weird processed stuff. The idea of being able to pop in a floppy disk with a MIDI soundtrack from a video game and then play it back on maybe an accurate rip of a game console's sound font, or maybe not, maybe it's some weird thing that it shouldn't have been played on, is just super, super fun. So I became aware of, like I said initially, this project called the MIDI Blaster, which was made by someone who goes by the name Luke the Maker. And there's going to be I think links in the show notes, but I saw it first on Instagram, they've put together a Patreon where you can go download all the files necessary to build this sort of modern recreation of that type of old MIDI player that uses a Raspberry Pi, it uses fluid synth to be sort of the the MIDI player that can access all these different sound fonts. And Luke the Maker has put together an image that you can put on an SD card to play on your or to run on your Raspberry Pi that contains a whole slew of great sound fonts. And I think there are some maybe some sample songs, but he's also put together floppy disks that you can download the files, make your own floppies. And so I've got a collection of them I've been putting together here, including the four disc set of Final Fantasy VII soundtrack. I've got, in fact, I probably can't play these in set up to play those. I have okay computer the full album by Radiohead, which is just really fun to play back using like the Glover 64 sound font, which is just goofy and weird or pick some, you know, old synth, a Casio VL one that someone has has put together a sound font for that actually, I think Luke also offers some for sale if you don't want to build one, but I built one including all the three printing files are included and a nice bomb of the parts that you'll get for a little audio amp and a little matrix display. I have resisted the urge to go and buy an old vintage MT-80. I came close on one that looked rusty and busted, and I threw a lowball offer there that didn't work out. But those actually didn't have the conveniences of picking different sound fonts, because it was just kind of one synth engine built into the box. They didn't have these nice displays with the name of the song and the name of the sound font or synth settings. So I think kind of the modern one actually does one better than the old ones as cool as those might be. So that's the thing I've been playing around with and really enjoying. It runs with a little USB floppy. So I bought, I don't know, a $17 USB floppy drive on Amazon to shove in the thing. And it's worked out surprisingly well. I love that it uses real floppy disk.

Tod Kurt

That's so cool.

John Park

It is. I think I love nostalgic old stuff that doesn't work. This does work well, but you've got that moment when you pop the disk in and it clicks and whirs and you wonder, is it going to, right now it says no MIDI files on my display. It's spinning up, it's searching the thing, it takes 10 seconds, 15 seconds to see, and I'm like, "Oh my gosh, it found a song." Then I can go hit play and now I'll start up with whatever sound font I've got picked.

Tod Kurt

floppy experience.

John Park

It is a real floppy experience. And I know that they've, Luke the Maker has got some updates coming. Some other people have reached out to help with some coding so that you'll be able to right now it just plays one song, and then it's done and then you forward to the next song. So they're going to add a you know, be able to play through the full album, which will be a really nice convenience, and some other things with with an upcoming version on their Patreon.

Paul Cutler

I did watch the video that you shared. It's about 10 minutes long. I think it's on the Roland. And I thought it did a of explaining why you might want one, because I didn't quite get it at first from a tutoring perspective, even though it's called the music tutor. Yeah. But the one thing that grabbed me was speaking of discs, he showed or demoed a bunch of 90s pop music in MIDI format that you could buy on MIDI discs during the 90s.

John Park
Isn't that wild?

Paul Cutler
Yeah, it was crazy. And I needed, I should have paused it to actually wrote down some of the album names and some of the songs, but I was like, that was on MIDI? I was just laughing.

John Park

So strange. Yeah. I've looked around on eBay just a little bit, and they just might not be that prolific. So it's up to you, make your own. And you, of course, can print your own labels. And Luke, the maker, puts out nicely designed labels that mimic the album art, even though a floppy of it may have never existed.

Tod Kurt

Very cool. - This Roland MT-80 is amazing. It looks kind of like a boom box, but it's got a floppy drive instead of like a cassette or a CD hole. And I'm a big fan of the MT-32, which is the MP-80 is like a boombox version of MT-32. MT-32 was my second synthesizer.

John Park

And it was amazing

Tod Kurt

'cause it could play multiple different sounds at once. And it had decent-ish drum sounds and piano sounds. And so, yeah, anything that's MT-32 descended is got a soft spot for me.

John Park

'Cause it's like, "Oh, this little box,

Tod Kurt

"it can do so much."

John Park

Oh, that's great. Yeah, and I was reading also that they, went one further and put a reduced set of it onto a sound card. So instead of like a Sound Blaster, you could get this Roland SC-55. And I believe there are some pretty popular, well-known video games of the era that were made with those sound cards and then recorded if it was CD audio. So you could be playing a game that had the audio going through this whole pipeline of this Roland MT-32 derived synth engine, which is interesting. That's cool. - That's a great pick. Tod, what's your first one for us?

Tod Kurt

All right, so my new favorite live music genre is Algorave. Well, it's a term that's been around since at least 2011, according to Wikipedia. I just recently came across it. Basically, it's live coding dance music in a live club audience. But wait, you may think watching nerds twiddling on laptops isn't quite live music. I need to be right. In the mid 2000s, I went to a few clubs where people were playing on monomes, those light-up, gridded mini controllers that controlled sensor laptops. But they were on music stands angled towards the audience, so you could see the monome button lights change with the performer's actions. Made it much more engaging than just watching a laptop user bop on their head. Seeing computers unashamedly used as live musical instruments was new too for me. With the monome, you could see the performer playing, see the device respond. It brought the audience in, showing them a little bit how the performance worked. Later we got performances like Median's Pop Culture, Sean Wasabi's Marble Soda, on the Launchpad or Midi Fighter devices. These grid devices had become displays unto themselves, yet they were still distance with the audience. You couldn't see what these button presses were really triggering. There's a laptop maybe off screen or kind of hidden from view, and you couldn't even see what programs they were playing. Then there's live coding in Algorave. Instead of hiding the laptop screen, brought to the front. Live algorave performers project their laptop screens on club walls. And it's not boring. These live coding apps look more like something out of a Hollywood executive's idea of hacking rather than standard GUIs we're all familiar with. Picture a screen of text. Seemingly random sections of it flash in time with the beat. You see the performer's cursor move and position over some text. It changes. The screen flashes. The beat drops. Under and above the text are visual representations of notes, the drums, the audio waveforms being played, making it difficult sometimes to make out the text. This code that is somehow also music performance. And then it scrolls again, changes, and the beat goes on. It's really hypnotic. Now you can see both the performer and instrument they're playing, but the instrument is code. That's Algorave and live coding more generally. If you'd like to try out live coding in your hand at Algorave, there are many apps to try. I'll include links in the show notes. Most are free and open source. Several I mentioned back in bootloader episode 2 back in October 2022 The one I've been using a lot these last several weeks is called strudel It runs in the browser and that's a lot of fun any any time you ever you have access to a browser You can do a little live coding session an artist who's working primarily in strudel now goes by the handle DJ Dave And I think I've posted both links links to both both Paul and John Park bugging them about DJ Dave I remember DJ Dave using Sonic Pi a few years ago, another live coding environment, but now she's all Strudel. Her Strudel live sets project the Strudel live coding ruffle screen on multiple walls, embedding you in the music code. She's mostly active on Instagram, and you can learn some cool Strudel tricks from watching her Instagram reels. So I've included some links in the show that's about that. So go ahead and check out some Strudel videos on Instagram or YouTube. You can see the musical composition, the music compositional thinking happen in real time as the person writes their strudel code. It's a lot of fun.

Paul Cutler

I'm so impressed by the people that know coding and have enough knowledge of music theory and music composition to do both at the same time.

John Park

It's crazy. Under pressure.

Paul Cutler
Exactly. Yeah, it's so cool.

John Park
You were sending, you sent me a link to it, not only performances by DJ Dave, but also a little web snippet that you texted me. And one of the things I really love about it is the sort of active highlighting of elements of the code that are currently doing something. At least that's my understanding of it, is you can more than just seeing a block of code and listening, you're a little more active in following what thing in the code is doing a step at that moment.

Tod Kurt

Yeah, it's a great debugging tool for both you, it's a debugging tool for you, the writer of the stuff, but also it helps the viewer kind of see what the song is doing.

John Park

Mm-hmm. Yeah, I wonder if you can rent out the Madison Square Garden Sphere in Vegas to do a live coding conversion.

Tod Kurt

You know, I think she might be performing in Vegas soon. Oh my gosh.

John Park

We could sneak into the one they have here in Burbank, the little trial space that they built.

Tod Kurt

Oh, yeah, totally.

John Park

Perfect their acts and try to do some strudel. Why is it called that? Any idea where the name came from?

Tod Kurt

I have no idea. I think it's part of the Tidal project, which is another live coding thing that's been around. So I think it might just be like S to T. Yeah, it's kind of like Tidal, but with an S. I don't know. Makes me hungry. All right, Paul, what's your first one for this week?

Paul Cutler

Every year there's a joke in the Linux community that this year will be the year of Linux on the desktop. And it never happens. But I think 2025 might be something different, the year of the microcontroller as a mini-computer. This is because when Raspberry Pi released the 2350 chip, they released a 2350B version which contains 48 GPIO instead of the normal 30, allowing for a lot more peripherals to connect to the microcontroller. Adafruit's been teasing us for months about their mini-computer, the Fruit Jam, which they've been developing in the open and even have a product page up for it. It features the RP-2350B, 16 megs of flash plus 8 megs of PSRAM, with the PSRAM helping for emulation, a microSD card, DVI output, headphone output, 2-port USB-A host for keyboards, mice or gamepads, 3 switches, and even more. And if you've been following their development, they're up to a Rev-D version that I think features a Wi-Fi coprocessor, though I don't see that on the product page yet. But now a company named Olimex has beat them to the punch with a product and description that doesn't leave a lot to the imagination, calling it the RP2350 PC. It too features the 2350B, 16 megs of flash and eight megs of PS RAM, but has four USB-A ports for USB host, DVI and HDMI output, micro SD card, stereo out and in. It's only 25 euros, which seems really reasonable. It comes with a custom UF2 that looks to be running MicroPython, and they market the Reload emulator to run Apple II games and software on it as well. There's a short manual that mentions their uext connector of which they've developed some plug and play modules that use this universal extension connector. They've also made the schematic and KiCad files available on GitHub, which is a nice touch. I looked at picking one up, but it was 23 euro to ship it. And that's before any tariff. So almost double the price. I'm really excited for these. If you can't tell, it takes me back to being a kid and plugging a computer into a TV and programming basic, except this time it could be circuit

Tod Kurt

Python or micro Python like I mean I think one of the reasons why the all of X 1 is is much cuz gonna be much Cheaper than the Adafruit one is because it doesn't have Wi-Fi Right, I think that's that's I think I think more as as they were developing the fruit jam I mean like JP might be able to speak to more of this But it seemed like it's like well if we're designing something sort of a game console slash tiny computer Shouldn't it also be on the internet? So it's like how do you make it be on the internet?

Paul Cutler

you have to add the Wi-Fi. And I don't mean to put John on the spot and share any trade secrets.
I'm just excited about these. No, not at all. I don't think there are any secrets. But yeah,

John Park

so I have the Rev-A is the only one that I have here at my workshop, which did not have the Wi-Fi and otherwise it's very similar other than some spacing of some things. And I agree with you, it's exciting in a 1983 Apple IIe in JP's basement kind of way, because It's so direct. The project that I've started working on along with Tim, Foamy Guy at Eddiefruit right now is a little sort of video text generator to just composite on top of other stuff. And so I wouldn't do that with a Raspberry Pi because it would be so cumbersome, but this having no OS to speak of and just booting instantly and allowing me to do display IO things to pop text in front of something with a green screen background, it's got the HDMI out and it's got a keyboard and mouse in. So it does feel like an instant on super simple computer. So I'm excited about it too for those reasons. And the idea of it in general, I think not just this Adafruit one, but the OLIMX one looks really interesting. And just that general idea of we are hitting a spot where it's not quite as pulling teeth to do computer like things on a little microcontroller board.

Tod Kurt

Right. Yeah, and these and these things have the great like both both the fruit jam and the This all the next thing and anything else that is like a micro controller based thing has the really nice Feature of it just like old computers They turn on instantly like nowadays we have to wait 30 seconds or whatever it is to take for computer to boot and that's cool You know when you're learning about computers, but but it it definitely is the oh I just want to goof around for a little bit like that with the buddies used to always do with my little Apple 2 was I'd turn it on I type a few lines of basic and Make something goofy appear on the screen and that would be like my 10 minutes of Playing with the computer for that afternoon and now these these things had that we just turn them on and they're running All right, John. What's your next one for us? All right, so my next one is a

John Park

Modular RC toy microcontroller sort of combination product called cyber brick and And this comes from the Bamboo Lab people who make the 3D printers. And I have one of their 3D printers and love it. I think it's really well done. And the ecosystem around it is excellent as far as support and documentation and updates and things. So I was excited to find out in their little maker supply area of their store where they sell LEDs and things that they encourage you to couple with some of their pre-made 3D models. I'd missed the launch of this, that they have launched essentially a modern version of a Lego Mindstorm type of idea, which is modular electronics that are fairly plug and play with some motors and some servos and some LEDs and some buttons that communicate with each other and communicate with your phone or your computer to code them in a graphical environment. Digging a little deeper, what these are, I ended up getting a set of some of just the basic bricks, But what they're really targeting and some of their kits that you can get right out the gate are meant for printing little RC cars and trucks and forklifts and things that they've got available for free up on their maker world, I think it's called. Get their models, 3D print them, and then couple them with these modular electronics and motors and things. And now you can build little toys that you can control, which is pretty interesting. I haven't printed any of those cars and things. I just wanted to get the microcontrollers and their little peripherals and start playing with them. So what it looks like is a little ESP32, I think C3 on these sort of general purpose controller boards that you can code over USB-C and MicroPython if you want, or just using their Bluetooth firmware, you can code with this graphical environment. And then they have a little carrier board or a shield they plug into, which they call a transmitter and a receiver shield. As far as I can tell, they are not transmitters or receivers. The shields, I think that's all handled on the little controllers, which I believe are using ESP-NOW. So they're a really smart use of ESP-NOW to do this kind of remote control to gizmo. The little carrier boards deal with things like power boosting and motor driver and servo control. and they have a bunch of little JST, different sizes of JST connectors for hooking up NeoPixels, hooking up motors, hooking up buttons and switches. So really interesting. It kind of straddles a line between straight up DIY, hey, I wanna go to SparkFun or Adafruit or buy an Arduino, versus a more closed system like Mindstorm, which Lego is never sure if they wanna be selling that or not. So I think they're currently in a dark age of Mindstorm as far as I can tell. But this thing is really interesting. I think it's Tod and I, in fact, we're talking about maybe trying to get CircuitPython onto it. It seems like it could be a neat just bit of hardware to hack around with. I don't think they're entirely open source. It's a little unclear which parts of what they're doing are open versus closed. But I think it's exciting. They have a pretty big audience and I think it puts some neat microcontroller DIY stuff out into the world for people to play around with.

Tod Kurt

And you're becoming an expert in ESP now on CircuitPython too, so you can maybe learn some of what it's doing underneath.

John Park

I'm hoping to become good at it. I would not use the word expert. I'm very at the beginning of my using ESP-NOW, but I'm digging it. If you're not, by the way, for people who aren't familiar, ESP-NOW is a really neat little peer-to-peer protocol that uses the radio that's built onto these ESP32 chips, but does not use the whole cumbersome Wi-Fi stack. It instead can do either one-to-many, many-to-many, one-to-one communications that are meant to be simple, small, I think 250 bytes is the package size, communication among things. So a nice, simple alternative to try and do things with like BLE or IR or other radios. So that seems to be in a lot of light bulbs and home automation products. And now I'm becoming more aware of it as something that we can program in CircuitPython or Arduino on our little microcontrollers.

Paul Cutler

I'm so glad you brought the Cyber Bricks to share. I too missed the launch on this. I remember seeing a year, year and a half ago that Maker World had a kit you could buy to make a little turntable. And of course me being a big into records, I looked at it and it wasn't the cheapest thing, but they had the little servo or the motor that would turn the record and then you 3D print it apart. So it looks like they've really taken that idea and run with it at a hundred miles per hour.

John Park

Yeah, yeah. You know, I should also mention one other, since what you just mentioned is outside of the RC car thing, another one that they have available as a kit, I think it's not available right now just 'cause they've probably sold through, is a time-lapse camera module. And it meant for probably your printer, which a lot of printers have that built in. But so they at least are aware, this could be extended out to way more stuff than just RC cars and trains and cranes and things. And if you go, actually, if you go to the Maker World or Bamboo Studio and look for search for models, you will see a lot of stuff that users are making too, including of course, there's an R2D2 kit on there, there's a robot arm kit, bumper cars. So people are making their own models and then presumably their own profiles to upload to the firmware on the board so they do what you want to do.

Paul Cutler

Well, that was a great pick.Tod, what's your next one for us?

Tod Kurt

All right, so did you know that you can use KiCad from the command line? Until recently, like the last 20 years, I used Eagle to design circuit boards. It was pretty great. It was made better back in 2011 when the community, including Adafruit's Limor and PT, convinced them to change their proprietary binary file format to a text-based one. This made integration with version control systems like Git much easier and a stable of tools to process Eagle files blossomed, making our lives easier. When I moved to KiCad last year, I was pleased to see it also had a well-defined text-based file format, script-based processing of KiCad designs, both in the app and outside with standard practice. This has enabled wonderful tools like various image importers and exporters, Stargirl's web-based KiCad viewer for the web, organic round trace generators, you can have those cool curvy traces from the '60s, a manufacturer part number to KiCad footprint generators, you can just put in a part number and it'll generate a whole KiCad schematic symbol and footprint for you, and exporters for popular PCB fabs. So it's really easy to get your board made. But editing these KiCad files can be tricky, especially if they're currently open by KiCad the program. So I was really intrigued to learn about KiCad CLI, a command line tool that ships with KiCad. Using this tool, you can do the obvious things like export Gerber files and drill files for PCB production. You can also use it to import and export schematic symbols and PCB footprints, but you can also have it run ERC, electrical rules check and DRC design rules check on your schematic and PCB from the command line. This is like a syntax and linter for your code, but for circuit design, it means you could add these to a GitHub action to ensure you never check in a bad schematic. This is pretty cool. It's because as someone who has checked in a bad schematic and then built a board from that and then realized, "Oh, I ran the DRC, but I forgot to run the DRC after I made the edit." And this would have helped me in a couple of places. The reason why I started looking at this whole KiCad CLI is I wanted to do a visual Git diff of a PCB design. The normal Git diff will show you how your text is changed for code. But for a vector art design like a PCB, it's not really helpful. And the tools that I found to do this were either some part of a for-pay monthly service, or I had huge dependencies and written for old versions of KiCads. I wasn't sure they'd work. I kind of want to invest in a whole node type script install or a whole Rust-- get Rust installed to make this one program work. So using some tips from a KiCad forum post, I made a very simple visual diff shell script that only depends on having KiCad and having a working web browser. It works by calling KiCad CLI twice to render two different versions of the PCB to SVG images, and then some quick HTML CSS magic to animate a crossfade between those images. It's about 90% of what I want. And with some changes to my Git config, I can now do a Git diff for PCBs visually. It's not a tool I'm gonna use every day, but when I do need it, it's really handy.

John Park

Yeah, Tod, that sounds really cool. It's interesting, you showed that to me and the ability to do a little cross wipe, cross fade between them is a great reminder of you can have all the tools in the world trying to find differences, but just you looking at it and seeing a thing move or a trace not be correct is really powerful. In fact, it reminds me of when I worked in animation at Disney, there were some similar scripts up at Pixar in the rigging-- I worked in character rigging-- in the rigging group. Just every night, automatically, all of the character rigs would be animated through a little set of standardized walk cycles and things. A script would just diff them visually. So if you just diff two animations on top of each other, you can notice like, wow, I think, you know, the elbow deformer or something changed in the code somewhere in this huge pipeline, because there were some pixels that showed up. Like if you diff two images, they should just be black, one on top of the other.

Tod Kurt

So they had a really clever way of saying,

John Park

hey, just flag me if you notice anything visually different between these without, it's not computer vision or anything. It's just literally, is there a pixel that isn't just black on these two sandwiched images. - Totally. - So that reminds me of that, being able to just swipe between your two PCBs, you're gonna catch stuff. - Yep. All right, Paul, what's your second one for this time?

Paul Cutler

Growing up as an '80s kid, it seemed to me that there were two camps of those who had an early computer. You either had an Apple II, like John mentioned earlier, or you had a Commodore 64. Personally, I was lucky enough to have an Apple IIc, but a number of my friends had the C64, and now the Commodore 64 is back. YouTuber Perry Fractic, who runs an all things retro YouTube channel, has announced via a video on his channel that after seven months of negotiations, he has a deal in place to buy the Commodore 64 brand for seven figures. He's created a public benefit corporation for Commodore 64, which means that while it's not a non-profit, it has been founded to preserve and promote retrocomputing. And with that comes news that they're selling a Commodore 64 Ultimate that you can pre-order now and is supposed to ship before the end of the year, starting at $300. They claim it's the first new Commodore in over 30 years, And that's because it's not doing software emulation. They're using an FPGA to recreate the actual Commodore hardware. There's three models to choose from, the basic beige edition, a starlight edition that adds a translucent case with sound reactive LEDs, and the ultimate founders edition, of which there are only 6,400 made for $500 and comes with gold plated badges, gold keys, and more. - Lasers, does it have lasers? Each model does have an HDMI port, built-in Wi-Fi and USB to bring it into the modern era. They're able to play any of the original Commodore 64 games and applications, and the description even claims that you'll be able to plug in old cartridges, CRT TVs, or even disc drives. I hope they pull it off. That's a lot of $300 retro computers to sell to get a return on investment on that seven figures. - Wow. - This is really cool, though.

Tod Kurt

I'm always amazed at how, what you can get an FPGA to do.

Paul Cutler

Yeah, it's interesting. When you look at the actual back of it, it's got the original ports that it had. So on the far right side of the computer is where they've added the USB and some of the newer stuff. And then the back, where the FPGA is, motherboard is, it's set up to be just like the original Commodore 64. It's pretty interesting.

John Park

Wow. Do you think it's time to finally take that trip into Commodore 64 land as a former Apple guy?

Paul Cutler

You know, I went through a phase where I bought my first two computers. My father actually gave me my first Timex Sinclair that we had as a kid, and then I went out and bought an Apple IIc. During the pandemic, I ended up putting them both up on eBay. I tried the retro computing thing, and it's just not for me. The first time I heard the Apple IIc boot up with that classic sound, I was instantly a 10 year old again. It was amazing how it took me back. - And then bored five minutes later, right? - Kind of, yeah, to be honest with you.

John Park

That's how a lot of these go.

Paul Cutler

Well, that's our show. Thanks to John Park for joining us and check out his weekly show, John Park's Workshop on the Adafruit YouTube channel. And don't forget that on August 15th, Tod and I will be hosting a live edition of the Bootloader. Check the Adafruit blog and socials for the time and we hope to see you there. Until next time, stay positive. (gentle music)
