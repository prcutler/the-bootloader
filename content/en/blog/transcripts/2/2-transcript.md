---
date: 2022-10-10
title: "Episode 2 Transcript"
linkTitle: "Episode 2 Transcript"
description: "Episode 2 Transcript - M is for Makers, Music, and Machine Learning"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---

[Episode 2 Show Notes](https://thebootloader.net/blog/2022/10/10/episode-2/)

## Episode 2 Transcript

Paul Cutler  0:02  
Welcome to The Bootloader. I'm Paul Cutler.

Tod Kurt  0:04  
And I'm Tod Kurt, and this is episode two. The show works like this, Paul and I each have brought three things to share with you. We'll spend a few minutes talking about each but no more than five. If you want to learn more, we have detailed show notes available at the bootloader dotnet. And give us a follow on Twitter at the bootloader.

Paul Cutler  0:20  
So I wanted to follow up from last week, Todd, you had shared the full control XYZ, and they released a new STL last week for a phone holder in the funnel. There's pretty cool in and of itself that it lets you use it vertically or horizontally. But when you go to the STL there's a challenge to printed at double speed. Cool. Now I've got an Ender three V two. And I took the challenge and it printed out parallely I've never printed out something out this fast on mine. And love it. Those guys are doing a great job

Tod Kurt  0:52  
over there. That's amazing. What filament did you use? Just standard PLA?

Paul Cutler  0:56  
Yep, just standard black PLA. I think it was Eyrone. So it was pretty cheap stuff.

Tod Kurt  1:01  
Oh, that's cool. Yeah, I love I love that, that there are different ways you can use that phone holder. It's like this weird sort of organic C shape of the phone goes in multiple different directions. It's pretty, pretty awesome.

Paul Cutler  1:11  
I'll make sure to include some of those in the show notes as well. Before we get started this week, I did want to give a shout out to everyone who listened. Thank you. Thank you, thank you, you made our launch such a success. I also should mention that I was inspired by the Python bytes podcast Hosted By Brian Aachen and Michael Kennedy for the bootloader. You'll notice that the format is slightly similar. And I also have an interview podcast like Michael Kennedy. And both of them have been so kind and gracious as I've launched both of these podcasts in 2022 that I just wanted to give them a shout out and thank them for all their help. Yeah. Thanks, guys. Todd, why don't you get us started this week. All right.

Tod Kurt  1:45  
So first thing I want to talk about is an LED color pattern language. So if you've followed the maker verse on Twitter, you may have seen projects by Geek Mom projects, aka Deborah Ansell, or Deborah Ansell, aka deep bond projects. And in her co led project, she often uses these pixelblaze LED controllers. And they're pretty interesting, their ESP 32 based you so you connect to them via Wi Fi via your phone or computer or whatever, you configure LEDs. And then you can select a bunch of different patterns that are built in. And there's a huge online library of existing patterns of different color patterns, you can just kind of click on and click run, and they show up on your LEDs. But what's what's really interesting is these patterns are algorithmically defined. There's a little built in editor that runs in the browser. So on your phone or on your on your computer where you edit these patterns. So like anything you download, you can look at you can change if you don't want to like exactly how they work. And then you can run and you do do the standard sort of edit test run. But instead of a computer language, it's this kind of special JavaScript D colored language for just LEDs, LEDs. And it actually is the the pixelblaze. DSL domain specific language, actually is a ACMA script derived sort of mini version of a JavaScript like language. And it's got a bunch of built in LED and math functions. So your scripts can be really small like if you wanted a simple sort of spinning rainbow animation like the spinning beach ball on Mac OS that's like five lines because there's like cue functions and you know get led index on kind of stuff. So that's one cool thing the pixelblaze controllers and you can buy them on tindy or on on Ben hex Ben Hanks pinkies site. They're the they're great. separately. There's the fees, really beautiful Fibonacci LED displays. It's a circular LED display where instead of being arranged like in a grid, or in a sort of radial arrangement, they're arranged in a Fibonacci spiral like like a seashell. They're beautiful. They're created by Jason Kuhn, available on tindy any bank, he makes a bunch of different sizes them. But the 40 millimeter one, the size of like a large coin is perfect for like maybe making a wearable pendant. And so the three of these people got together and created a luxe lavalier lavalier. I don't know how to quite say that word. But it's a wearable led pendant, usually when these Philips 50 millimeter sorry, 40 millimeter Fibonacci spirals and it's got a pixelblaze on the back. And then it's got a really cool magnetic clasp. That's also a battery holder, designed by Geek Mom. And so it's the three of them work together to like create this sort of easy to assemble kit or might be fully assembled. But it's like the perfect kind of perfect storm of these three makers coming together and making a really cool object. And one of the reasons why even though this is kind of old, like the Fibonacci display is the bear of a couple of years pixelblaze It's been around for like three or four years. Geek Mom has led stuff forever. The website that they've created just for the light Lux level Lear has one of the best intros to the pixelblaze pattern language that I've seen. And so you can check that out at Lux lovelier.com/patterns. We'll have a link to that in the show notes. But it's super awesome.

Paul Cutler  4:47  
I love all of their projects. I don't know any JavaScript, but it sounds like it's that hard to pick up if it's just a subset of the language.

Tod Kurt  4:55  
Yeah, it's like it's like super minimal. So like all the craziness, like like a lot of these languages. As they get complicated, fast and sort of the same way that circuit Python is a smaller, simpler version of Python than normal Python. This is an even simpler version of JavaScript than you've ever ever seen. And so it's really approachable. You don't even have to really understand coding you just go Oh, I see. It's, they're multiplying this number by five. Well, if I multiply it by six, oh, look, the color spin faster, or something.

Paul Cutler  5:24  
And you said that the battery is actually in the necklace.

Tod Kurt  5:27  
Geek Mom was getting really good at designing 3d printable structures to hold batteries and stuff and play with magnets. And it's a thing that holds one of these 18 650 magnets, that's like a sorry, 18 650 batteries, and then with embedded magnets on the sides, and so just kind of clips around. Battery hangs up behind your neck and in the pendants around your chest. Yeah, that's pretty awful. Alright, so what do you got for us?

Paul Cutler  5:50  
My first one is a project called whisper from the open AI group open AI earlier this year released Dolly, which I think you are a big fan of dough. Yes. So Dolly, if you don't remember is you feed a text, it generates the pictures based on the text that you give it. They've taken what they've learned in that machine learning model, the next level, and whisper is transcription and translation service. So they've released some blog post a formal paper and even released a Google colab with a Jupyter Notebook. So you can see the code running, but it's a Python library, you do a pip install, and then the Git repo for whisper, and it installs it now the catches for, for some folks, they might need to install rust, and FFmpeg as well. And I think rust can be a little tricky at times, based on some of the forum posts that I saw. But I got it installed, no problems. And it's this easy to make a transcription, you type whisper the name of the audio file that's in your current directory. And it goes, it just works. And it outputs a text file. And a VTT file, which I use for subtitles. I originally saw this on Hackaday. It was built with Python 3.9 point nine and pytorch. One point 10.1. So they're both, you know, fairly recent versions. I'm glad to see that pytorch has been transferred from beta to the Linux Foundation, it gives me a little more confidence to actually use pytorch. Totally. And they've trained it with 680,000 hours. And they created five models have that from small to very large. The smaller the model, the faster it runs. And you can pass a command line arguments to tell it which model to run. Now, when you start to think about this, if it's really as easy as typing the command, whisper audio file name, almost anyone may be able to use it. I've played around with a lot of transcriptions, because of the podcast accessibility is very important. And I'll come back to that in a sec. But I you know, the irony was this was released just days after I had finished a personal Python project using assembly AI to create transcripts for the podcast. And I had spent dozens of hours trying to do that because my pythons not very good. And then here comes this that's like, Hey, you can do this with one command. Now there are a couple of catches, but I'll get back to that. So when you think about it, the accessibility part is huge. If you're deaf, you now have the ability to take an audio file and transcript it for free. Most of the services that are out there are paid services, and it doesn't excellent job. need subtitles for your YouTube videos. And I'll put a VTT file for you. It's not SRT. So that's a catch, but it's good enough. And then the thing that most people really haven't been talking about in a lot of the articles I read was The translation aspect, you just pass it a command line argument. And it will do automatically detect which language is being used no matter what. But then once you pass it the command line argument, it'll take Japanese and translate it to English. There's almost 75 different languages supported with varying degrees of support. And you'll see it on their GitHub page. They have a nice chart that lays it out. But it's it looks pretty neat. The license at MIT so it's open source already created a forum for show and tell people are already building on this. It's been out for two weeks. I was going to share that. One of the things that uh, doesn't do is speaker diarization Or so I can't tell the difference between you and me talking. It's just going to transcribe all of the text from this podcast, for example. Yeah, I was going to call it I was a gotcha. Nope. One hour ago, someone actually posted that they built diarization On top of whisper. I need to check that out. Someone built a twitter bot that extracts a video, translates it and then replies with the translated video on Twitter. Yeah, someone built a command line utility to transcribe or translate audio from live streams in real time. And someone has built a tool that automatically add subtitles to DaVinci Resolve when you're editing videos, which is incredible as well. Pretty amazing. Using write the downsides, I was gonna say no speaker tagging, but it looks like someone might be there might be third party support for that. And then the only catch that I really saw is it's slow if you're not on a GPU, so it's it's about real time if you're not on a GPU, which a it's free.

Tod Kurt  10:16  
Yeah, that's, that's incredible. It's just gonna get better too. It's like, it's like the whole I remember, you know, in Star Trek, one of the many things that seemed a little implausible to me. One was the universal translator. And, you know, granted, this requires a lot of trained backlog of audio, but we're getting close to this real time translation of audio that like we just have in our pockets or something or is on our wrists. It's just kind of incredible that we can do that. It's something that seems not really real, like it's a thing of sci fi, not not something that we'd actually have in our lives in our lifetimes.

Paul Cutler  10:48  
I agree. And in fact, someone actually built a project that transcribes the audio from your speakers live as you play it, which is almost exactly that use case that you talk about. So it's common, probably gonna come sooner rather than later. What's your next project?

Tod Kurt  11:03  
Kind of related eventually? And I'll show you, I'll show you why. So, so I want to talk about music generation and live coding, but in the browser, so what I mean by this, so So how do so how does one create music? So the standard way is you write it down, either with a pen and paper or the computer sequencer, it's kind of kind of the way I do it. But there's another way, what if you had a code window or multiple code windows, and in the code window, there was a, there was a code block, and a code block had one part of the music of the music piece you're creating, described in some sort of algorithm, maybe there's multiple code blocks. And each code block describes different parts of the music you're creating, maybe they talk to each other. I mean, we have different windows that have different pieces that are sort of interacting with each other. And that seems kind of strange. It's like I'm reading real time software. I mean, sorry, I am in real time writing software. It's also real time software, to generate music. And so there's been this thing for a while that's been around called Title cycles. And it is a live coding Environment for Music basically just presents a window and you start writing functions and the functions will start playing a melody and this function will generate a beat and this functional generative baseline, say, and and they all will are synced together, perhaps so they're all playing with each other. This underneath what what title cycles is, is it's a Haskell, which is a functional language that's really good at concurrency shell on top of supercollider, which is a audio programming language, it's been around since the 90s. A bunch of artists that you might have heard of had been using supercollider over the years to make weird sounds, it used to be kind of a kind of a compiled thing where you would give it a piece of code and it would generate a sound like a dot wav file, you'd listen to it, you edit the file and you know, do the sort of edit compile test thing that you know do with neural code, but the output would be audio instead of a functioning program. But now it's all in real time. And so you have supercollider kind of running in real time, Haskell sits on top of it, and directs it to create audio in various ways. And then that's pretty cool. There. But it's hard to install someone who created a thing called Sonic Pi, that's also open source. All this is all this is open source. By the way, Sonic Pi is a sort of one click install app that lets you kind of that lets you run something kind of like title cycles on your computer. But it's still an app that runs on, you know, in its own little window. But what if you could do this kind of stuff in a browser. And it turns out, you can there is a library called tone.js. That is a library that sits on top of the Web Audio framework that's part of browsers now. And it's not just playing mp3 or waves, but it's actually doing audio synthesis. And so you can create live music generation. Here's a little sample there's a thing called strudel that sort of like a mini version of this title cycles. And here's a quick little audio piece that's just one line of code. It's it's smooth, it's small, two sets of arpeggios playing against each other. And I'm going to edit

this just in a browser window on my laptop over here, it's pretty amazing. So even though toned up Jas, and and similar thing and strudel have been around for a while, it was kind of new to me that like this was able to be done in real time, sort of doing title cycles type stuff in the browser. So that was very cool. But there's more, more. If you don't tend to making what to make music yourself, you can go to pi songs.com, a site created by Kenton Becker. And he has used tone.js to make a bunch of little mini sites that algorithmically generate music based on the numbers of pi. So you can create music that no one's ever heard before. And he's got he's got a couple different styles. I just started one up here. It's sort of like finding the random digit of pi I just chose and then starting up as playing, and this is sort of an ambient soundscape generator

Paul Cutler  15:00  
Nice thing about this being unique is that we're not going to get a YouTube strike against us by playing

Tod Kurt  15:05  
that. Yeah, that is exactly what I'm thinking. Is it like I could have this play for hours, no one would care. So there's this this one, and it's very nice. It's very kind of milage to have in the background. While you're writing software, there's also a techno one. These are the same techniques. This is a different digital pie. But it will start playing techno. Let's see if it starts up here a code to Yeah, exactly. And then, you know, if you if you really want to go to a rave, there's also acid hit, which will generate random acid techno baselines?

I think that was was that the 1,600,665,893 606,930? If digit of pi is where that started, I think

Paul Cutler  16:08  
amazing. You export any of this audio to import into a Das? I

Tod Kurt  16:14  
don't think so I've been I've been playing around with using these various audio loopback gizmos that you can hook up to like kind of capture the audio of one app, one app and send it to a file. But yeah, it's it's and this is all in the browser. This is just kind of freakin amazing that like this all just lives in the browser. You can do full audio synthesis and music synthesis and song synthesis using pie. I don't even know what's going on. It's amazing. Alright, so anyway, so what's yours next thing,

Paul Cutler  16:41  
I love mechanical keyboards, I have been using a mechanical keyboard for about 20 years, probably going back to a local company that made clones of the original IBM x t like that 20 pound keyboard. I just love them. But I've never built the keyboard. But that might be changing. Oh, Thomas Pol, who goes by th Paul to on Twitter has a coffee page. And we'll link to all of this. But he's built a split keyboard. That's RP 2040. powered. What's magical about it is every key has an OLED screen. So they're all customizable. Wow. Exactly. And he's walking through the build process on his coffee page, which is, which is his blog, which is great. So he shares there's a matrix of which key caps and key switches may or may not work, because you've got to insert those little OLED screens, and they have a little ribbon cable that needs to come out of them. So if this works, I would be so excited to see something like that not just on a keyboard. But more importantly, on a macro pad. That's where I could see a lot of use for it. Yeah, one of the really neat things that he goes through on his blog is all the competitors that have tried to come out over the last five or six years. And none of them have really stuck around. Most of them like Elgato, that with their stream deck. It's one RGB screen, but they just segment off the little, the little parts. Yep, those those keys aren't individual screens. Yeah. So you know, some of the use cases for that are pretty cool, whether it's different languages, or whether it's a macro pad, and you have different shortcuts for different apps. But it's it's really neat that he's walking through that whole build process with and comparing it to other keyboards out there. And comparing the key switches and the key caps and everything that you're going to need to actually go with it. So that's something that it's not finished yet. He's actively working on it. He wants to make a kid it sounds like of it. It's definitely something I'm going to be keeping my eye on. Because once a maker can do it, you know, some of those other companies might step in, it'll be it'll be interesting to see if that's something that will ever be mass produced.

Tod Kurt  18:52  
Yeah, that's I'm really interested in this. There's a long ago, there was a keyboard created by someone in Eastern Europe. Like it was it was it was a design agency. It was called like the Optimus or something I forget the name, but it was it was it promised a display per key. And when they finally did release something, I think it wasn't display per key. It was maybe display per key for the function keys and it costs $1,000. And it just was like they kept having to sort of roll back their promises as they found out that it was really hard. And and then the thing the other thing I've seen is somebody a couple people have tried making little OLED as keyboard keys, macro pads, where they just take these little cheap, tiny o LEDs that are I squared C based and sticking them on top of a tax switch. And then kind of having like letting enough there's enough flex in that in that connection system that you could flex the OLED and push the tax switch underneath it. But the problem with that is that you're flexing this circuit board that's not made to be flexed. You're pushing on a OLED piece of glass. It's not made to be pushed on. And yes, of course everyone when they build these after like a month or two was like oh, it's starting to flake out it's not working. Whereas this project, it seems like he's taking In Karis actually running the flexible circuitry cable from the OLED, instead of using the, you know, fixed PCB connectors, he's putting the OLED underneath the plastic keycaps rather than just having them having to be glass on the top. So it seems like he's actually thinking about the problem in a in a durable way rather than just like, oh, let's hack it together.

Paul Cutler  20:20  
Exactly. And it's RP 2040 powered. And I think I think you mentioned kmk at some point as well.

Tod Kurt  20:26  
So yes, that'd be the thing to do. And

Paul Cutler  20:29  
it's yeah, it's it's amazing. I'm really excited about that. And if it ever gets to that kit stage, I'll have to give it serious consideration. I have a feeling it won't be cheap.

Tod Kurt  20:39  
No doubt. Yeah. Yeah, each of those little LEDs Yeah, a couple of bucks each right, at least,

Paul Cutler  20:44  
it adds up quick. That's why I'm kind of hoping for a macro pad. My macro pad is one of my two favorites circuit Python powered devices, it's probably the one that gets the most used. I actually maintain an awesome list for the Adafruit macro pad. I love it so much. So if I can get oil up on that, because then I don't have to look at the screen all the time. Yeah, it would just be wonderful. I would I would be over the moon.

Tod Kurt  21:06  
Yeah, I did get end up getting some of those key caps that have the removable plastic bit with a little piece of paper, you can stick inside. So So I think I can then label it. So you okay, this key is for launching this app. And this key is for doing that thing. Yeah. It's like, oh, it'd be much better if I could just like tell it to update the keys themselves, because they're all displays. Right?

Paul Cutler  21:26  
What do you have for us next?

Tod Kurt  21:27  
All right. So let's see here to continue the audio trend and the machine learning trend. There's this new thing created by FX twin who's a artists techno ambient artist has been around for about 30 years or so. And David Griffis it's called Sample brain. And so if X twin is his real name is Richard D. James, he has been creating some weird, fun, sometimes disturbing music. It's it's very challenging. It's very interesting and very challenging. Listen to some of the stuff. But he's been a supercollider user kind of since supercollider came out. And some of his albums I think have been mostly like almost exclusively supercollider, you could do things that you just wasn't possible with synthesizers and effects in the early 2000s. But you could write a program to do it. And there's this really good engineer named named David Griffis that he has essentially worked with to create this thing that takes a target sample. And using a collection of other wav files, tried to recreate that sample using those wav files. And it uses some machine learning techniques to do this. It mostly just sounds terrible and awesome at the same time. And so here's a quick little little sample of it.

Paul Cutler  22:46  
That is definitely terrible and awesome. At the same time. This is

Tod Kurt  22:50  
this is the chip shortage song from Adafruit.

So it's trying. It's trying hard to recreate it. And like a lot of these machine learning things. It depends on the library of information it has at its disposal. And I've not given it very much, which is why it's kind of janky but with the jank Enos it's still interesting sonically. And so you could take that take these raw sounds and then like, you know, do something further with them. It's free to download, you just go to the website and download it will be linked in the show notes. It's pretty weird. But it's been a lot of it's been a fun thing to play with here. Now down the unasked, like, can I make you know, can I throw these samples at it? And does it change what I'm getting out from the audio?

Paul Cutler  23:34  
So we have dolly and stable diffusion for images. And now we have this for music. Yeah. I welcome our AI overlords, right.

Tod Kurt  23:44  
All right, what's your final thing

Paul Cutler  23:48  
I wanted to highlight of maker Kevin McAleer. He has an amazing YouTube channel. He's got 40 different playlists with multiple videos in each playlist. And he's got a focus on building robots with micro Python. The project that caught my eye recently, though, was he built what he called the PyCon to take a Nikon with the Raspberry Pi high quality camera. Oh, and what's really cool. Yeah, what's really cool about Kevin is he does an hour long live stream where he goes deep. And so you're making a bit of a time commitment, but you can scrub through it. I would rather have a long video than leaving stuff out where if I tried to build it, I might get stuck or for example, but for when he's building the video, he takes you through the camera itself. He teaches you about lenses. I picked up a couple of things that I didn't know he talks about computer vision and why this will work and why computer vision isn't important for this project. And he takes you through how he 3d printed and designed it and then assembled it and it is just cool to see this 3d printed high quality camera and action. I'm looking

Tod Kurt  24:57  
at the list of the videos he's got graded and like, Oh, here's an air quality sensor. Here's here's a robot. Here's some hackable hackable glasses, it's, there's a lot of really cool stuff here.

Paul Cutler  25:08  
He's got a series on building your own personal. Yeah, this

Tod Kurt  25:11  
is great. And, you know, props for him for doing live stream builds, I have really hard time having people watch me create stuff. And the fact that he's able to do that, and it's usable. It's usable to other people. That's wonderful.

Paul Cutler  25:27  
Every every Sunday, and I actually reached out to him to to have him on the circuit Python show. He's done so much stuff with microcontrollers. He'd be a perfect guest. So definitely looks like we might be able to do that in a couple months. I'm pretty excited. Cool. So Todd, when you're not doing the podcast, what projects have you been working on lately,

Tod Kurt  25:43  
as you might have known, I've done Eurorack modular synthesizer projects in the past. And one of the one of the youtubers slash bloggers that I've been really inspired by is this person named huggy, Whoa, he's a Japanese, his his YouTube channel, and blog are wonderful resources if you want to build really inexpensive Eurorack modules, which is great, because your ex stuff can get pretty expensive. But one of the things he's created, I think, a couple years ago is this. He calls the additive VCO and uses an Arduino Nano and a handful of passive parts and a single op amp to create this beautiful, like interesting sine wave summation thing. Here's a little audio sample of it

so it's it's really simple. I all of his stuff he does by hand soldering on perfboard. I decided to this this last week, I've decided to lay it out on a PCB and maybe get the PCBs made using all through hole components so that maybe anyone could make one of these in like an afternoon because doing stuff by hand on perfboard requires a bit of skill. He's very good at it. I can do it. I'd much rather have a PCB it's much easier.

Paul Cutler  26:57  
But I can't do it. I want to learn so but I just can't my soldering skills are not there.

Tod Kurt  27:04  
No, it's It's a Yeah, it's like PCB is the way to go. And this project is a really good example of how to use the mozzie audio library. It's this audio synthesis library for Arduino that I've used a bunch. And the whole code for it is just like maybe like 30 or 40 lines. It's like super simple, pretty understandable. So I think it's a good sort of thing to explore further, like, hey, I can make this cheap little Arduino Nano based Eurorack module. That's what I've been working on this week. Very cool. And what have you been up to?

Paul Cutler  27:35  
I took the circuit Python show on the road recently and traveled two hours east to Wisconsin for a very special Halloween episode that's going to be coming out in just a couple of weeks. Oh, that's

Tod Kurt  27:44  
incredible. This isn't spooky.

Paul Cutler  27:48  
It involves a couple of trolls. And we'll just leave and we're not talking internet trolls. That's awesome. But other than that, I had Braden Lane recently on the show who's circuit Python projects, including he's got a macro pad called the joypad. And then he's got some led projects called the Loomis ring in the Luma stick that I think are just super cool. It was great having him on the show. Yeah, the Luma stick is cool. Yeah. And coming up as Jim Musa read from the micro Python project. Oh, interesting. Yes, a lot of people might think that micro Python and circuit Python, you know, being a Ford might not get along and it couldn't be farther from the truth. We had a wonderful conversation so

Tod Kurt  28:23  
there's no fight. I want to see a fight.

Paul Cutler  28:26  
No fighting. Lots of hugs. Oh. Well, that's all we have for you this week. Thank you for listening to the bootloader. For show notes and transcripts, visit the bootloader dotnet or follow us on Twitter at the bootloader until next time, bye

Transcribed by https://otter.ai
