---
date: 2025-05-05
title: "Episode 20 Transcript"
linkTitle: "Episode 20 Transcript"
description: "Episode 20 Transcript - I'm Afraid it's TRMNL"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Tod Kurt
- Welcome to The Bootloader, I'm Tod Kurt.

Paul Cutler
- And I'm Paul Cutler. The show works like this. Tod and I have each brought three things to share and we'll discuss them for about five minutes each. What's your first one for us, Tod?

Tod Kurt
- I have aspirations for making things out of wood. I've taken a few classes at the local wood shop but I've never really made anything. I don't have the tools at home and you need so many tools. And most of the things I want are pretty basic like benches or boxes. I don't think I really need the nice tools. But I think I need some sort of built-in skill that I don't have, which I just can't get from watching all the woodworking YouTube videos that I watch. And so I just recently learned of this website called Hyperwood. Hyperwood is a way of making furniture using standardized materials and minimal tools. With a handsaw and fasteners of your choice, screws, nails, glue, you can make benches, plant pots, chairs, and more. Think of it as Lego for furniture. The core material of Hyperwood designs are wood slats, which you can get more per tree than any other type of wood product. And these slats are pretty cheap and they come in some nice wood types. And the way that the HyperWood design works is that it's a description of how to attach these slats together. And for each of the HyperWood designs, the furniture designs, the HyperWood author provides GitHub repos for each one with a text-based data interchange format called the HyperWood Exchange Format, HEF, And command line tools let you customize the design based on the particulars of what you want, the materials you have. Like if your slats are slightly different dimensions, or if you want the bench to be taller, shorter, or wider. So it's a really interesting approach to making furniture that I'd not really considered. The end result looks a little bit like the Ikea Ivar stuff. You've ever seen that? The sort of like blonde wood, but you could use darker wood or stain it and make it look a little bit different. but it does look kind of like a Lego piece of furniture. (laughs) That's kind of interesting. And thanks to our previous guest, Andy Piper, for pointing this out to me like a week or so ago.

Paul Cutler
- Yeah, it's pretty neat. Like you, I don't have any woodworking skills. My father-in-law is actually a master woodworker and passed all those skills down to my wife. So if I ever need something done, she's on top of it and I've never had to learn them. So this is pretty interesting.

Tod Kurt
- Oh, that's great. You got that in the house though. (laughs)

Paul Cutler
- Yes. There's a question of who's really built my arcade, her or me at this point. - Well, you know, she did the wood, you did all the non-wood electronics.

Tod Kurt
- Exactly. - So what's your first one for this week?

Paul Cutler
- I generally try and keep the stories I pick positive, but sometimes the company I love does something so dumb, I just have to rant about it. I'm lucky that I've had a few network-attached storage devices over the years, and two of my last three have been from Synology. I've also recommended them to a number of folks, but no longer as in shitification raises its ugly head once again. Now, NAS devices aren't for everyone, but I have a large media collection which I've ripped. I have all my podcast backups and my live over the air TV service has a DVR that runs on my NAS. So what did Synology do? They recently announced that to use one of their plus series NASs, it would also require a Synology branded hard drive to unlock all of the features. And these just are optional features you might not care about. These are core features including hard drive health reports, lifespan analysis, and automatic firmware updates. Synology doesn't make their own hard drives, they're rebadged enterprise drives from the likes of Toshiba and Seagate. And you pay extra for what those drives would normally cost, and I would assume that's due to Synology doing all kinds of product testing to make sure they're compatible. And they also add a little DRM chip so they can unlock these extra features. But now it feels like you're having to pay for that privilege twice, once in the cost of the NAS and in the hard drives. And when you're buying four 6/8 hard drives for a large NAS, that cost adds up quick. Synology's made some vague promises that third-party drives might be certified sometime in the future, but claim that Synology-branded drives paired with Synology systems are at less risk of drive failure. But now you're going to pay a premium for that and not be able to buy some of the best hard drives on the market that you might want to buy.

Tod Kurt

Yeah, I've heard about this too and I've been on the verge of getting a Synology NAS. I had an older no-name brand NAS many years ago and I hadn't had one for the longest time relying on a really old Apple time capsule as my main backup solution. But recently I got a Ubiquiti U-NAS Pro, which is a rack mount, seven drive thing, which is really nice. But like with the Synology, you have this problem of which drives do I put in it? I had to spend all this time researching drives. And one of the things I liked about that Synology did for so long is they had these hard drive reports of which drives are good for our products. And it was really which drives are good as NAS drives. So like using any other NAS, you could rely on the Synology report. And so on the one hand, I'm like, well, I could have saved myself a lot of time if I just would have bought a NAS with drives in it. You know, it's like, don't even think about the drives thing that's separate from the NAS, which is kind of one way you could think about the new Synology move. It's like, oh you just buy the 20 terabyte NAS and it happens to have four drives in it or whatever. So it's like, well yeah okay, and how often do you upgrade drives? It's like this is a problem I'm now going to be wondering now that I've got a NAS. How often have you swapped the drives out on your Synologies? So I put

Paul Cutler
my Synology, my last one in when we built the house. So that was probably eight, nine years ago. In that time, I've had one of my eight hard drives go bad. So I've only had to swap out one. And I got to tell you, it's one of my worst fears is when that thing dies. I've got so much stuff on it. And I know I can, you can

Tod Kurt

reclaim it using another Synology NAS. But still, I don't want to go through data loss at all. When I had a normal job, that was one of the things we'd do every once in a while, was to pull out one of the drives in the NAS to make sure it would still work. You know, it's just like, it's like, okay. So I don't, yeah, I don't, I don't know, like how much more expensive are these Synology rebadged drives? Because if they're about the same price as the Enterprise drives, you know, I'd maybe be okay with just buying the Synology drives.

Paul Cutler

You know, I've linked to articles from Hackaday and, or not Hackaday, ours is Technica and Tom's Hardware with coverage out of them. And they've got some prices in there. I wanna say that on about a roughly $300 drive, there's about a 10% Synology charge. So you're paying about 10 % more. So to your point, yeah, that peace of mind might be worth it for some folks, but for some folks who are doing all that kinds of research and know, hey, these drives are compatible, these drives last longer than this brand.

Tod Kurt

It's kind of frustrating not having that flexibility that you've had for years and years with this brand. - Totally, yeah, 'cause if you don't agree with Synology's choice, like if they're using Seagate drives and you're a real Western Digital person, you know, maybe you've got a contract with Western Digital even, so you get like a thousand drives from them or something. (laughs) - Yep. - Yeah, that's tough, that's tough. I don't like what they're doing. I hope they will change that, but we'll see. - What's your next one for us? - Okay, so I'm gonna talk about the Terminal, TRMNL, battery-powered Wi-Fi e-paper wall display. So there's lots of these things that are out there. This one's got a twist, and that twist is open source. So these things, they're these ambient displays. You put them on your wall and they display your calendar or weather or like stock prices or whatever. They're totally standalone. They don't require a computer, but they do require an internet connection. And most of the other ones that are out there in the world require a persistent subscription to the server that it talks to. And if you stop paying, your device that hangs on your wall, that gives all this information, turns into a brick. Where Terminal, T-R-M-N-L, is not that. Terminal has a website that you log into, you configure the device, selecting which plugins of information you want to display and wear out on the device. But unlike the other devices, Terminal's website lets you easily create your own plugins with an open API. And you can make those plugins public on the Terminal's site for other people to use. So if you make something that's really cool, like a-- I don't know, for some Steam game that you use, it has an API, you want to reflect your stats of that game to the world, well, you could set that up and then let other people put in their data so they could see their stats for the game. Not only is Terminal's protocol open, but it's open in its entirety. The folks behind Terminal recognize that their box is just an ESP32 with an ink display. So they provide a set of docs that you create your functionally identical DIY terminal out of a WaveShare e-paper display and ESP32 dev board or whatever other parts you have laying around. Because the terminal firmware is totally open-source. It's up on GitHub, you can poke around and look at it. I highly recommend anyone do that because just the read me for the firmware repo is a really good explanation as to what it takes to make a long-lived Internet-connected device. This thing has a battery and you can charge it up via USB-C, but it will last for half a year on its battery because it's really smart about how it pulls the data off the Internet, which is a problem that we've all had. If you ever use the Adafruit MagTag, which is a very similar device to USB 32 with a little E-ink display, it's hard to make that thing last for a month because most people aren't used to writing low-power code. The README and the firmware itself has a good explanation as to how to do some of that stuff. I've had a terminal for a few weeks now, and it was super easy to set up. Even though my company thing was an early proponent of what we now call Internet of Things, I don't really have many IoT devices in our house, because most are just e-waste waiting to happen. But terminal will keep on working long after the company servers go away, because you could just go to their repo that has the server functionality and open it up, start it up, start up your own server. You could even set up, I think, the server on your own LAN, so the traffic for it never leaves your local network, it could just be on your home network. Yeah, there's links to this in the show notes. It's really cool. You get to see how a productized thing gets made as well, because it started out just as an ESP32 Dev Board and an E-Ink display module, and they turned it into a full product, which you can just buy. >> I love companies that

Paul Cutler

get open source. They're doing it from beginning to end. You know, it's the firmware, the server. It's just so great to see so many times these companies go belly up and then they open source the server components at the last minute so people can do this. But here, you know, the community can give back and add new features like you were saying, or new stock tickers or, you know, whatever, whatever they want to

Tod Kurt

write. Yeah, it's been it's been I've been I've been chomping to dive more deeply into it and actually write some my own little plugins for like things in the house, like, oh, if the cat door is unlocked or something. (laughs)

Paul Cutler

- Well, you have to keep us in the loop and further episodes about how those adventures go. - Oh, definitely. So what's your next one, Paul? - Hackaday recently covered the Rockbox 4.0 release and it took me for a trip down memory lane. Rockbox is an open source project that replaces the firmware on an MP3 player from many different manufacturers. And if you know me, you know I love music and I know I'm dating myself as I fondly remember having a slew of MP3 players before smartphones and streaming took over. Looking at the Rockbox list of support for MP3 players, such as the early Arcos, iRiver, and SantaSansa, those were all MP3 players I owned and probably put Rockbox on back in the day. Rockbox was also known for its iPod support, though I never personally owned an iPod. Rockbox adds a number of features to MP3 players, such as support for other music formats like AugVorbis or Flac, Gapless playback, Last.fm support, and the list goes on. Rockbox was started in 2001 with its first release in June of 2022. It's pretty cool to see a project that's still going strong with major releases after over 20 years.

Tod Kurt

That's really great. I think I remember looking at this website because I had an old, one of those old early MP3 players before the iPod and was really frustrated with the really bad UI it had.

Paul Cutler

Oh, they were terrible back in the day. You know, those companies were just slapping the cheapest thing they could put together and shipping it out. Their primary focus at all.

Tod Kurt

I love I love that the rockbox.org website still even looks like it comes from the from the mid

Paul Cutler

If it works why change it no exactly this is my philosophy All right, what's your number three for us?

Tod Kurt

All right, little shameless plug incoming for the last few months I've been working off and on on a circuit Python synth. I owe tutorial website For those unaware, synthio is a CircuitPython core library for musical synthesis. It pretty much lets you turn your CircuitPython board into a modular synthesizer. Back two years ago when the synthio library first came out, I made a CircuitPython synthio tricks page. It was sort of a quick tips guide for fun things to do, kind of like my CircuitPython tricks page. But over time, synthio has evolved thanks to Jeff Epler, the original synthio author, and Dalrymple and Mark Comis to make Synthio even better. And also Mark and Cooper were key to making these new guitar inspired audio effects libraries, which we chatted about in the CircuitPython show in a panel a couple weeks ago. But I've only had really cursory experience with. So given all these changes, I felt like I'd be well served to come at Synthio fresh and reteach it to myself from the ground up. And since I learn best when I document as I go, I figured this would be a great excuse to create something more structured than a tricks document, and instead have a set of goal posts and then a final destination. This tutorial is the result. It's about two-thirds done. It's broken up into sections, starting from you just have a bunch of parts on your desk, and it's heading toward a fully featured synthesizer. Along the way, you learn some synthesis techniques like filter envelopes and wave tables and how to deal with controls like MIDI. For each of the examples at each stage, it was important to me that the code blocks in the guide do something musically kind of cool, and that they be fully functioning, although they might use like some modules from past sections, and there'd be a small accompanying video for each code block showing what the code does and how you interact with it. So eventually there'll be over 50 small programs with videos. It's been fun to try to learn how to record those and document them, that's both clear and short. So if anyone's interested in making a CircuitPython synthesizer, See if this tutorial guide is useful. To get started, all you need is a Raspberry Pi Pico, a cheap I2S DAC, and a couple of potentiometer knobs. Please let me know if you have any suggestions on these things, on things that I missed, and ways to make it better. Links to it are in the show notes.

Paul Cutler

- I was lucky enough that you gave me a preview of it a couple weeks ago, and like you mentioned, I think it's really important to call out because it's really neat that you did it. You start with the hardware and the circuits, and then you teach a little bit about what synthesis is, and then all those code samples just continue on each other, and to your point, they actually play a little bit of music in an interesting way

Tod Kurt

for every sample. So you've done a hell of a job on it. Oh, thank you. Yeah, it's a, I'm like, one of my problems is I get, I will make a little thing that does a little random, random melody, and I'll just let it play for a while because I kind of zone out and like, Ooh, that sounds kind of neat. So hopefully someone else will, will have that fun as well. Okay, Paul, what's our final one for today? Lastly, there is Moby Gratis.

Paul Cutler

Do you remember the artist Moby? You may know him from such hits as Go and Southside. He's just released 500 different songs for free and they come with only two restrictions. You cannot use Moby Gratis songs to promote meat, dairy, or other animal products. Moby's a vegan and it's one of his rules. You cannot use Moby Gratis songs to promote right wing causes, which is something I can get right behind. Other than that, Moby encourages any creators, whether that's filmmakers, musicians, students, remixers, and the list goes on to grab those songs. There's 500 songs total. These are songs, not just fragments. You can filter by genre or by mood and the list shows you the song name, a description such as energetic, uplifting, or happy, and the beats per minute. You can just click to play right in your browser or you can favorite it or download it as well if you create an account. So if you have a music or a film project or maybe even a synthio project in CircuitPython and want some samples, check out

Tod Kurt

mobygratis.com. This is really nice. As a big fan of the various Creative Commons song libraries that are out there, because it's like sometimes it's hard to find a good piece of background music for some piece of video content you're creating and just be able to find something that's nice that you know is legally clear. Right. It's really handy. But I've always kind of wished that there was an extra add-on for the Creative Commons licensing that was sort of like the no jerks clause, you know, which he kind of has.

Paul Cutler

Yep, some kind of morals clause. I'm right there with you. Totally.

Tod Kurt

So that's awesome. I totally want to dig into this and see like the fact that it's all is free for remixing as well, which some of the licenses don't let you do means you can like take out the real some really cool bits of sound that he might have in some of the songs and use them as basses for your own weird little sounds you want to make, which is something that I like to do.

Paul Cutler

Yeah, you can download WAV, MP3, or Multitrack. And I don't know if Multitrack is the actual stems or not.

Tod Kurt

I think that might be the stems. Oh yeah, that's cool that he gives you his Multitrack. Fun. All right, I'm digging into this. This is cool.

Paul Cutler

Well, now we know what Tod's going to be up to until our next show. And that is our show. For detailed show notes and transcripts, visit www.thebootloader.net. Until next time, stay positive.
