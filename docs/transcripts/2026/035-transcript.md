---
date:
  created: 2026-08-03
title: "Episode 35 Transcript - Thank You For The Music"
---

Tod

Welcome to The Bootloader, I'm Tod Kurt.

Paul

And I'm Paul Cutler. The show works like this. Tod and I have each brought three things to share, and we'll chat about each for about five minutes.

And stick around to the end for a special announcement. Tod, what's your first one for us?

Tod

USB-C and power delivery is confusing. Let's find some tools for that. You know how much I'm into inspecting USB stuff.

When doing any kind of embedded development, I've always always done. have some sort of these little USB tester gadgets in between the computer and the board I'm using. I'm sure you've seen them. They show the voltage being put out by the USB host and the current being used by the device.

Very good when you have like a short by accident. I've been using them for over a decade. They're great. They're cheap.

About 10 bucks. But they're only really for the old USB 2.0 devices. With the advent of USB-C, there's now one connector that can do so many things.

This is especially true in terms of power delivery. It's no longer just five volts and, you know, 2 amps or whatever. There's this new protocol called USB-PD. It's a spec that runs over the USB-C cables where two devices can negotiate for not only who is providing the power, but if the power is anywhere between 5 volts at 3 amps to 20 volts at 5 amps, you know, it's 100 watts.

This is how your laptop can be charged by the wall plug, but also how your laptop can charge the phone, all from the same port. It's kind of incredible. It's amazing when it works.

And then there's the cables. Everything, you know, there's all these USB-C cables, but they're not all created equal. Many are just USB 2.0 cables with USB-C ends on them.

These are usually very cheap. They're usually just charging cables. But some cables are really capable, and you can run Thunderbolt or USB 4 over them.

Oh, and by the way, inside of USBC, there's multiple protocols that can run over them. Two of which of the most common ones are, is USB of the various versions, 432, and Thunderbolts and other things like that. And these Thunderbulk cables or these USB4 cables are really expensive.

But how do you know? You can maybe look on the markings of the cable or the brand of the cable, if neither of those are lies, but not always. The better cables are supposed to have an e-marker chip built into them where the cable itself tells the devices what the cable is capable of, because you don't want to send 100 watts down a little tiny iPod sync cable or something.

But even then, not all cables have, e-marker chips, or maybe the e-marker data has wrong data. So what can you do? Thankfully, there's some tools out there, some hardware, some software that give you insight into what's going on. On the hardware side, there's some fairly cheap gadgets. One of which I like is the RDTC66 USB tester. It looks a lot like the little cheapy USB testers of all, the little thing with plug on one side and a jack on the other, and it shows the voltage and current, but it also as protocol detection to telling you what the cable and charger support.

And that lets you know exactly what power is going into and out of your phone or laptop. It's really handy. A little up from there is the TREDICs USB cable tester.

This is just for cables. You plug both into the cable you're curious about, and it can be just by any cable, USB-C, USB-B, Length Thunderbolt, Lightning. Very exciting.

And the big display has got a huge display, like a 4-inch display. It's like a touch and stuff. It tells you exactly what the cable has, like what.

what pins are connected, first what pins it has, what pins are connected. So if you plug in one of those USB charge-only cables, you know it exactly. But it also tells you what protocols it supports because different cables advertise what protocols they're capable of.

Like, oh, this can be used for Thunderbolt. This can be used for HDMI over USB, over USB-C, or whatever. It also can tell you if it's got an e-marker chip and if the chip matches the spec.

And it also will test the cable to see if it's connected correctly. It's like a really smart version of those really simple continuity USB cable testers you might have seen like 10 years ago that just had little lights for each wire in the cable. But if you don't want to spend any money, there are some apps.

On the Mac, there's a very good app called WhatCable. I think it's the URL, whatcable.co.uk. And it's, oh, no, sorry, just whatcable.com.

John Park actually introduces this to me. It gives you much the same information as some of these tester things as far as what the MacOS sees it as, you know.

It's like you're going through an intermediation layer there, so it's not exactly as accurate as a hardware device. But still, it's really handy to know, hey, I just plug this charger cable in. Am I going to be charging at 100 watts or am I going to be charging at 15 watts?

You know, if you're looking for get a few more percentage of your battery filled up before you go somewhere, it's really important. And on Linux, Linux has a really nice inspectable kernel where you can just kind of poke around in this virtual file system called SISClub. class type C to see a bunch of stuff just with the command line tools like Cat and LS.

But there's also a command line tool called LSU-C-PD that will tell you a bunch of information about the PD capabilities on your computer and what things that are PD-capable are plugged into it. So some of these things hopefully can help people when they're trying to figure out what is going on with the charging of their devices because it's so complicated now.

Paul

I thought it was bad enough six or seven years ago when we were just dealing. with micro USB and you had to ask, is it a data cable or just a power cable? Yeah, totally.

You had just two choices. Now you have multiple choices with all the PD and Thunderbolt 3 versus 4 and now they're introducing 5. It's just crazy.

Tod

This came into a head a couple of weeks ago for me. Someone was talking to me, a friend of mine was talking to me in there. They couldn't figure out why their laptop was charging so slowly because they, but I've got the 100 watt charger.

And I've got, you know, I'm plugging it into the USB C port on my, computer that is supposed to be 100 watt capable. And it's like, oh, it was because the cable they were using was one of these really cheap little $7 cables that can do like 15 watts or something. It's basically a cell phone charger cable trying to charge a laptop.

And it just wasn't doing it. All right, Paul, what's your one for this week?

Paul

I have something a little different. Instead of a thing, I have a person. And that person is Terry Godier.

I hope I'm pronouncing that right. It's spelled G-O-D-I-E-R. He's a software developer living. Wisconsin who has made two video essays worth checking out. The one that grabbed my attention is called A Room You Can't See, where Terry asks, what has changed in how we listen to music, the technology or us? Without spoiling too much, Terry digs into what does it mean when we have an endless supply of music at our fingertips from streaming services for one monthly fee? Where is what he calls the intentionality of what we listen to? He asked himself, when was the last time he really listened to an album or went to a show, sat down and paid attention to an album, not in the background when working or in the kitchen.

He even touches on the music being streamed on Spotify that is AI, and Terry says he's not mad about the music. He's mad that it even works and these songs get millions of listens. Terry challenges you to think about your relationship with music in a video that is about 10 minutes long and really makes you think.

His second video is about design, and it's called Some Decisions Aren't Supposed to Be Optimized. and he asks, when did we hand over design decisions to the machine? He talks about how, for him, design is a feel.

He tells a story about how a designer at Google quit back in 2009 because Google was testing not one, not three, but 41 different shades of blue through A-B testing. He talks about how testing could be answering and asking the wrong questions. It really makes you think into how and why decisions are made in your favorite products.

After watching his videos, I checked out his blog and realized I was using one of the products he created. Earlier this year, and I've been debating about sharing on the show even, Terry released Current, an RSS reader for MacOS, iOS, and iPadOS. I didn't bring it up on the show because I didn't know if it'd be too niche or not, but I really enjoy using Current, and it has a really interesting goal that your RSS feed shouldn't feel like an inbox and show you the unread count.

You should read your RSS feed for the joy of reading and stay in the flow while doing it. I switched to it earlier this year after buying a new box. it for $10 and I've been really happy with it. What a small world it is sometimes. I've linked to Terry's Macedon, Blue Sky, and website in the show notes. I think he's worth checking out.

Tod

This is great. I love RSS. It's what drives podcasts. It's one of the few remaining examples of a decentralized information space that has been around for so long. It's like it was created before podcast. It was created like in the early 2000s or late 90s, I think, maybe in 99. And yet it still is everywhere. And like we used to use feed readers all the time, RSS feed readers. And it's just, it's kind of gone by the wayside. I'm glad to see a resurgence in feed readers again. And current looks great. I think maybe this will start me getting going again. And I really recommend watching his video essays. The fact that they're hosted on YouTube is kind of funny because YouTube encourages creators to change the thumbnail and title of their videos like every hour to see how it performs, you know? And music, music used to be scarce. We used to lord over an album cover and the album no liner notes because we're like, oh, I finally got the album that I've been waiting for for so long.

And like, do we even have scarcity in music anymore? No, we're kind of drowning in music.

Paul

Right. And that's exactly what he's talking about. And I'm with you.

I still use my RSS reader. Even after Google Reader died, I bought a subscription to FeedBin, who's worth checking out. I'm grandfathered in at a ridiculously low price.

I think it's $50 or $80 a year now, I forget. But still, even at $10 a month, they're a little less than that. It's worth it.

And I love the resurgence in that independent web, the indie web that's coming back, and people are adding RSS feeds to their websites again and making it a little more open.

Tod

Yeah. And if you have a iOS device, the checkout current, because it's a beautiful app looks like for iPad or iPhone.

Paul

What's your next one for us?

Tod

So I do CircuitPython. You hear me talk about it a lot. There are some upcoming audio improvements to CircuitPython that are pretty exciting for me as a person who likes doing little audio gizmos.

Some of them are kind of nuts and bolts on the lower level. Some of them are kind of cool fancy features. So this is going to be kind of a little bullet list of cool things that are coming out soon.

Like either they're available right now or they'll be available in like about a month or so. So in sort of the nuts and both side of things, there is a much faster way of talking to SD cards called SDIO. That's the library name that was only available for certain, I think, ESP 32 boards.

It's now available for RP 2040 and RP 2350 boards like the PICO and things like that. If you have a board that supports this kind of SD card wiring, you can get like 10 times faster SD card, which if you're playing samples off of SD cards, this is huge. With a normal SD card setup, you can really only play about one or two samples at a time, like simultaneously off of an SD card.

But with SDIO, I guess it's like 10 or so. Another one is normally the circuit pie drive of circuit Python is either writable by the computer sucked up to or by your code. Dot pi program, not at the same time.

And you have to make that decision as the board's first booting up. Well, now you can change that in real time as your code is running. You can just enable that your code can write to circuit pie, and what it'll do is it'll sort of disconnect and disappear from the computer.

And then your code can scribble on the drive, and then you can reenable CIRCUITPY drive to show back up on the computer, and then the computer will see the changes. So I love having the code right to CircuitPY because it lets you kind of like save config files for whatever settings you have or whatever. But doing the dance of like, oh, I want to talk to via the computer versus I want to like save settings was a real pain. And so that's now something you can do in real time, which is pretty exciting. Another one is if you have something that does USB host, where you can re-plug in like a MIDI keyboard or a mouse or a normal human keyboard into a circuit Python thing, that used to not work very well, even though there's a lot of products that have the USB host jack on it, now the USB host stuff is actually a lot more usable, which is really cool.

And then one of the biggest ones is there is now the ability to, read audio in to circuit Python and then muck about with it and then send it out via the standard i2s protocol i2s is this protocol that lets you do high quality like cd quality audio in and out and circuit python has supported out forever and it's now got audio in and so hey we can make a guitar pedal out of in circuit python now just pretty cool

Paul

So here's my dumb question the episode. So give me it, there's the use case. How does that work? So it's audio in, but how is it processing that?

Tod

So everything that's audio in circuit Python is basically a kind of, I guess, I think, I think it's called audio stream and you hook it up. Like the way you connect the audio things up in circuit Python is kind of like hooking up guitar pedals, really. It's like there are these various modules that have an audio in and audio out. You know, there's a, there's a filter module that has a low-pass filter and it's got an audio and an audio out.

There's an echo module that has an audio and audio out. And you just kind of connect them together. Out of one goes to the audio of the input of the other and so on and so on down the line.

And eventually the final thing that takes an audio input is the thing that will actually produce audio on a speaker. What we've not had forever is something that actually produces audio in real time. Like the producers of audio would be like a wave file or it would be synthio, the little synth engine that's built into Circuit Python.

But we couldn't have, say, really a microphone or like a guitar input or something. But now we can. So now there's all these things that could take an audio input.

And now we have another audio input, a real-time audio input, which is pretty cool. Okay. It's been really kind of frustrating to talk about all these cool audio features inside of CircuitPython.

One of the first things are people ask for like, we'll kind of hook a microphone up to it. And the answer's like, no, not really, not yet. Speaking of cool features, there have long been these three modules, these kind of upper level modules called audio delays, audio filters, and audio free verb that have been enabled on RP 2350, like the PICO 2 and ESP 32, but not on the RP 2040.

But RP 2040 is perfectly capable of doing some of this stuff. So now you can do like echo effects and filter effects and cool. chorus and flanger and reverb on the RP2040.

Also, me and Cooper wrote some speed changer objects. One's called speed changer. One's called resampler.

It lets you, like, in real time, change the speed of a sample. So you can do sort of like scratch effects on a turntable, or you can just like repitch a sample or, like, if you're trying to do beat matching of wave files and stuff. There's also a new granular pitch shift effect so you can do much, like we've already had a pitch shift effect, and that was a granular pitch shift effect. They both have kind of different audio qualities. Sometimes the granular pitch shift will kind of sound more natural at larger shifting of pitches.

And the pitch shift is often used if you want to make, say, make you sound like three voices instead of one voice, you know? So that'll be a fun thing to try out in the coming weeks. They'll be like, oh, can I make myself sound like a multitracked, you know?

And then also sort of the nuts of bolts things, there's a new object called audio file writer, which lets you take a whole audio chain you've created, and instead of outputting it to a speaker where it's ephemeral, you can actually have it right to a file. So it'll basically write a right away file. And that's kind of useful, usually for testing, you know, if you want to see if, like, is my algorithm or is my chain actually doing what it's supposed to do.

But it's also good if you just want to kind of save the effect because you're making weird noises and you want it to, you know, save the file. Yeah, so I'm really excited. Lots of cool things.

It's really neat that like Circa Python has become sort of like the audio toolkit, construction kit.

Paul

Yeah. And it's been exciting watching you and Cooper and others continue to build on that. Because it's been like a two, three year process from when Synthio first came out and seeing all the different layers that have come since then.

Tod

Totally. Yep. Okay. What's your number two?

Paul

Next up, I have the AP 30 Music Boy, which may just be the most adorable retro gadget I've seen in some time. You'll notice that it's called the Music Boy.

And that's definitely on purpose as this MP3 player looks like a Game Boy, from the screen to the buttons, though it's not quite as wide and it's about half as tall. It's pretty small as it sits in the palm of your hand and features a 2.0-inch iPS screen. It's high-res audio certified, and they really push how high quality the music is supposed to sound.

It features a 3.5 millimeter and 4.4 millimeter headphone jacks, as well as Bluetooth 5.3, and you can install a microSD card to store your music. You can stick it in your pocket, hang it on a lanyard, or it comes with a magnetic case to stick on the back of your phone. You can also use it as a USB deck on your computer to punch up the sound quality.

It also includes a Tetris-like game and an e-reader, though it's even smaller than the X4E ink, e-reader we talked about on the show a few months ago. This is a Kickstarter that just launched at the end of July and goes through August 17th. The super early bird aluminum version starts at $93 or the plastic version at $85, though, those might be gone by the time this episode airs. I'm super close to pulling the trigger on this one. I can see using it walking my dog or doing the dishes, but the only thing stopping me is that the vinyl records I buy don't come with MP3 download codes anymore. And I don't see myself buying albums on MP3 again, nor do I want to pirate them.

So in my case, it really would be a nostalgia device as I would have to listen to all the CDs I ripped or MP3s I bought right up until about 15 years ago when it just stops because I started listening to records. But man, this thing is adorable.

Tod

It's really cute. And it totally is hitting at the right time because there are so many like two generations below us, I think. Kids that are just becoming kind of cognizant of music are really wanting to use their parents' iPods and stuff.

But like, you know, old iPods are kind of hard to get working. And so this could be a nice, like this is a smaller lighter than an iPad lasts for longer on a battery. Right.

It stores more songs. But yet gives you that retro. a field because you can plug in where wired headphones into it and get like, you know, eight hours of playing around on a, you sure can.

Paul

All right, what's your last one for us? That's amazing.

Tod

There is this, one of these awesome lists called awesome self-hosted. You've seen all the awesome lists that are out there, usually on GitHub as a markdown file. This one's about free open source alternatives to all the cloud-based subscription services that we're drowning in.

I've been increasingly concerned that we're just becoming tenant farmers of our own information, seemingly barely owning anything we in creator enjoy. Instead, paying increasingly higher monthly fees to just live our lives. And now AI is eating up all of our creative output and regurgitating it back to us for a fee.

I'm a little worried, you know. But hey, the awesome self-hosted list might have some solutions for us. It has links to hundreds of network services and web applications you can install that accomplish most of what we use cloud services for.

Of course, it has links to how to turn, to how to run your own. own Gmail like server or web servers or get repositories, all the standard nerd stuff, but also has links to CMS document systems for small businesses or mapping systems like Google Maps, URL shorteners like Bitly, or backup systems like Backblaze, or even video conferencing tools like Google Meet, all open source, all installable by you. Most of these are bundled up into Docker light containers, so you can run multiple of these services on a single box. You could even run them on a remote virtual machine from digital or Linode. Sure, it's another subscription cloud service, but it's only one instead of many, and you control all the data that's inside of it and it's all security you. Or you can find an old laptop or PC and put Linux and Docker on it and host some of those services. Most of these services don't need much CPU. You know, you're just one or one or a family of people. How much data do you actually need? Or do you actually have? One of the nice things about having your data locally is it will often feel faster when using it.

And if you're interested in tuning an AI, having a local one instead of a remote one that you don't own, that pokes around in your local data is much faster and cheaper and more secure than doing a bunch of remote API calls to a corporation you barely trust. So I run several local servers already for things, but this list has got me thinking about moving more of my life to be directly more under my own control. And it might be fun, you know.

Who knows?

Paul

Yeah, I love the whole HomeLab movement. That's really behind a lot of this. I think it's just fantastic.

Now, the only caveat I would say is you kind of touched on it is when you're maintaining it yourself is to do it securely, right? Read up on it. Make sure that you understand security best practices.

Because some of these software can sometimes be easily hacked via zero day and that kind of fun stuff.

Tod

Yeah, yeah. No, totally. This is where I'm more akin to liking to the done. Docker solution because instead of just, oh, install these random packages on a Linux server, you would do it in sort of these little bundles that are kind of secure by only exposing one port or whatever. But as you were saying.

Paul

But yes, we talked about this in a couple episodes ago.

It's absolutely worth learning Docker. I know the basics of it. I've got a couple of containers running that do some of this stuff. I've got a ebook reader software hosted on a Docker container that it manages all my ebooks for me, for example.

Tod

Oh, yeah, definitely. Yep, yep.

Paul

It's probably on that self-hosted list somewhere.

Tod

Yeah, the list is a little daunting, I must say. There's a lot of stuff.

Paul

But it is absolutely worth putting some time into Learn Docker and doing some of this yourself.

Tod

Yep. And even if you don't use it for Reelsies, just playing around with the concepts is really fun. You know, like I was poking around at one of the mapping examples.

It's like, oh, wow, there are these open source map tile servers or map tile datasets. You can just use, install, and download. And if you want to make it totally local and totally self-contained, it doesn't even need a network connection for all the, if you're doing local maps, you know, it's kind of cool, all the stuff that's out there that we can just play with.

All right, Paul, what's your number three for this month?

Paul

My last two are headphones related. The first has been in the news for a bit, oh, is still new to me. Are you in the Android or Linux ecosystems and never been jealous of the functionality Apple's AirPods have?

Well, thanks to a project called LibrePods, you can now use AirPods-like features on Linux and Android. Android. The developer has used Wireshark to reverse engineer Apple's proprietary protocols. You can use features like Auto Connect, listening mode, battery status, and more.

No more feeling of missing out. If you want to use Apple hardware with your Android phone, now you can. I've linked to the project in the show notes.

And my last one is via Tom's Hardware, which recently covered the Sony Head Tracker project by Nicholas Slattery on GitHub. If you have a high-end pair of Sony's noise-canceling headphones like the Sony WH1000 XM-5s, you're in luck.

These headphones have support for spatial audio, meaning they have sensors including gyroscopes and accelerometers for head tracking. Mr. Slattery has reversed engineered the sensor's firmware to allow you to use head tracking in games on MacOS and Windows. Once you have everything set up, you put your Sony headphones on and the in-game camera will respond to your head movements. For example, look to the left in a driving SIM and your view changes from the front window to the side window, making it that much more immersive.

Check out the article to see the list of headphones that are compatible and for more details on how it works. I've linked to both the article on Tom's hardware and the GitHub repository for the Sony Head Tracker.

Tod

That's cool. Yeah, I'm a huge fan of Apple AirPods. I think it's like one of Apple's best products they've ever made, but I have not even tried to put, try to get them to hook up to any of my Linux devices.

Paul

Yeah, I wouldn't have thought to try it. Once you're in that ecosystem, the stuff just works and it flat out doesn't if you're not in it.

Tod

Yeah, yeah. But it looks like there's a lot of the cool features that beyond just being a basic Bluetooth headphone, which I think they've always been able to be, it sounds like some of the cool features actually kind of can work now on Linux.

Paul

Yeah, it looks that way. Well, that's our show. Our special announcement is that Circuit Python Day will be later this month on Friday, August 21st. Tod and I will be hosting a live edition of The Bootloader all about CircuitPython on the Adafruit YouTube channel. Follow us on social media or join our newsletter, and we'll share what time the show is on as soon as we know. Until next time, stay positive.
