---
date: 2022-09-09
title: "Episode 1 Transcript"
linkTitle: "Episode 1 Transcript"
description: "Episode 1 Transcript"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---

[Episode 1 Show Notes](https://thebootloader.net/blog/2022/09/26/episode-1/)

## Episode 1 Transcript

Tod Kurt  0:02  
Welcome to the bootloader. I'm Todd Kurt.

Paul Cutler  0:05  
And I'm Paul Cutler, and this is episode one. The show works like this: Tod and I each have brought three things to share with you. We'll spend a few minutes talking about each but no more than five. If you want to learn more, we have detailed show notes available at [thebootloader.net](https://thebootloader.net). And give us a follow on Twitter at [@thebootloader](https://twitter.com/thebootloader). Todd, why don't you get us started?

Tod Kurt  0:23  
Okay, we all know how 3d printers normally work. You got a 3d model on your computer, you run it through a slicer program that chops it up vertically like a deli slicer. And then that creates and then it creates instructions to draw in plastic. Each of those slices. Those instructions g-code are sent to the 3d printers one file. So 3d printers more like a 2d printer that stacks a bunch of 2d printed layers on top of each other. In fact, there was a 3d printer that use printer paper, a CNC knife and glue to make 3d prints like 10 years ago or so. The benefit of this the benefit of this approach is that any 3d object can be sliced up without knowing how the object is built. The downside is you can't have graceful curves that move in three dimensions. But a 3d printer can move in all three dimensions at once. The 3d metal the 3d printer nozzle could move up and down while moving around in a plane creating 3d structures that are impossible with traditional slicing approaches. There have been various research projects showing this but the most approachable I just came across is the full control design library. Go to [fullcontrol.xyz](https://fulcontrol.xyz) to check it out. It's a web based demonstration of an upcoming open source Python library. The 3d model has a beautiful and well cyberpunk aesthetic with purples and blues and 3d wireframes. The site currently has a collection of handpicked gender 3d designs, you pick one you modifies design parameters, you click Generate, and you get g-code directly downloaded from your browser. No slicer needed. I started playing with this and it's really fun. I can't wait to play with the library itself.

Paul Cutler  1:51  
I've been looking at some of those overhang challenges they have and wondering if my printer could actually keep up with some of those models that they show.

Tod Kurt  1:58  
Yeah, yeah, it's nuts. I don't I don't even know how how. Like normally there's all these extra g-code settings for your printer. So so I'm, I've been seeing a couple through my printer and it's a single work so I'm really curious to see what the library looks like.

Paul Cutler  2:11  
I'm gonna have to give that a try. Definitely. The first thing I wanted to share is about an open source project called tio, T I O. Martin Lund is the developer and I have a cool story about him too at the end. tio just released version 2.0 On September 11. I've been using CircuitPython for a year or two. And I didn't know about to until John Park featured in late July on his show the CircuitPython Parsec. tio is a modern day replacement for the old Linux tool screen. If you go to tio's GitHub page, Martin shares the motivation for tio: to make a simpler serial device tool for talking with serial TTY devices. With less focus on classic terminal modem features and more focus on the needs of embedded developers and hackers. It's that last sentence that's key. Up until July like most users I use mu to see any serial output or errors with my CircuitPython devices. Even the Adafruit advanced serial guide for Mac and Linux has you use screen, the old Linux tool. I've been using a Unix like operating system for too many years. And this is perfect for someone like me who was comfortable dropping down into a terminal. I can also run to in my IDE's terminal. It's got a lot of cool features, but it has one killer feature which is auto reconnect. If I unplug my microcontroller and plug it back in to automatically reconnect, I don't have to look up what serial device it was, or type the command to connect. It's just there and running. Just like my CircuitPython code is when I plug it on a board. That's not the only cool part. The Monday after the episode aired. Martin Lund joined the Adafruit Discord after he heard about the episode, he answered some questions and asked for feedback. It's cool to see open source collaboration like that in the open. And when 2.0 came out, Martin popped in a difference discord to let folks know the new release, couple of users shared a few bugs, especially on Windows and he fixed them right away. He didn't have to do any of that. But what a way to go above and beyond. It's so cool to see open source collaboration happening in real time. If you're looking to level up your CircuitPython skills and move on from the Mu code editor checkout to Tod, what do you have for us next?

Tod Kurt  4:14  
Oh, so just real quick, I super love to reconnect is great. I had been using screen a lot. I'm big terminal guy. And so So tio was right up my alley. Because of how a CircuitPython sort of functions whenever you're doing updates, the whole reconnect thing kind of happens a lot, at least the way I use things. So yeah, big thumbs up. So speaking of serial stuff, with Python, the thing I'm gonna talk about next is called Belay B ELAY. Belay is a desktop Python library that remotely controls your CircuitPython or MicroPython device. Like if you are first coming to MicroPython CircuitPython, and you're an expert, Python person you might be in for a rude awakening In the restrictions and limitations that these little embedded systems have, you're used to like having gigabytes of memory, and you don't really have that. And so if you don't need a standalone device, if you don't need the CircuitPython MicroPython device running by itself on a battery not connects to a computer. And really what you want is more of a smart peripheral that you can poke at from your computer. And what Belay does is it lets you kind of treat the sort of virtual serial port going from your computer to your CircuitPython device, as this little tunnel that you can send Python code to. And so you just write in normal desktop Python. And you just use a special decorator to say, hey, basically send this code to the device. And so you're going along in your normal big python program have a little function and it goes boop, out to the CircuitPython device or MicroPython device comes back with the result. And you can control pins, you can read read inputs, you can do NeoPixels basically just do anything you can do in CircuitPython, you can have it written in your desktop Python. And and that's, that's really cool. If this sounds a little bit like fermata, if you're an Arduino person fermata is this custom protocol and sketch that runs on an Arduino kind of takes over the Arduino and turns it into a is a remote sort of GPIO device for your computer. And so Belay is a little bit like that. But because Python is Python, it's much more because you can just run arbitrary code. And that's much more interesting than just you know, the sort of fixed protocol that fermata supports. Believe is available on pi pi and on GitHub.

Paul Cutler  6:36  
The developer of Belay has been working on this nonstop it just came out a month or two ago. And it's already 0.8. Nice first had MicroPython support, and then later added CircuitPython support and he's just keeps going at it as in, it's great watching that come along. I'm big into music. And this next one is a little fun. For me. This is from the Department of rockstars can be developers too: Rivers Cuomo, the lead singer of the band Weezer, whom you may know from such hits as Buddy Holly, Beverly Hills, and Pork and Beans was recently spotted on GitHub. It turns out, he's an open source developer when not writing songs, he submitted a PR to another open source project. And he also has his own project on GitHub. He's written a Python app and released it under the GPL. Here's the description from his GitHub repository: a Python script to update a Spotify playlist every day with all the songs from any significant new albums. It shouldn't include single only releases anything other than a month, it should be deleted. Interesting. And Mr. Cuomo goes on to share even more detail about it in the about section. This project is for me to experiment with open source collaboration. So please feel free to chime in and participate. I've been learning programming since 2015. But I've been mostly working on my own. So my GitHub collaboration skills are weak. I'd like to learn more about collaboration. So I can accomplish more as a programmer through teamwork. He goes on to say, his project will be a first low risk foray into the field of open source collaboration. If things go well here, maybe I can start to open up some of my other repositories, it could sure use some help. And I love the thought that some of my programs could be useful to others. My first goal here is to understand how different developers can work on a codebase together. So that's pretty cool. Now, I don't have a Spotify account to test it out. But you'll need a Spotify client ID and secret and then you can customize the program to even exclude certain genres of music that you might not like. But if you do have a Spotify account, and know a little Python, check it out and maybe even submit a pull request.

Tod Kurt  8:44  
That's great. I love it when we hear of famous people that are secretly nerds.

Paul Cutler  8:48  
Exactly. I don't mean to go all TMZ on the show, but you know, once I saw that it saw my two worlds colliding, I had to put that in the show. What do you have for us next?

Tod Kurt  8:57  
All right, so another CircuitPython thing. Did you know that CircuitPython has camera support? Like this is something that's pretty new, seems amazing that it can even function that like we could have like little microcontrollers with cameras? I mean, I know that's kind of like what cell phones are but the class of processors that that are in my in the article dev boards are like way below within a cell phone. So so this hacker named Ashish he used a Raspberry Pi pico running CircuitPython on these little cheap camera boards, and some clever machine learning stuff to do. Machine learning recognition of handwritten digits with the cameras, the cameras looking at a piece of paper, you write a digit down and it says, Oh, you wrote a two and and this is just like, like, two things I think that I didn't think would ever come a CircuitPython like machine learning and envision, like here's one example of it's this both and the way it works is so on the PC he has the actual training of the of the model and that of course takes, you know, a lot of memory and a lot of a lot of memory. And a lot of time. He used a, there's a standardized data set for handwritten digits. And he ran that through a classification system called support vector machines, which is a sort of simpler kind of machine learning that was all the rage, like a decade or so ago, it basically tries to find hyperplanes that cut through the data to sort of separate out the data. So if you've got a multi dimensional set of data, like, like an image is basically a bunch of multi dimensional set of data. Like images for multiple handwritten digits is a big multi dimensional set of data, you can use the support vector machine math to kind of cut through the data to create these little nodules that are oh, this is what a four looks like, this is what a seven looks like. And the nice thing about it is that once you've trained the model, the model itself is pretty small enough that it can run on a microcontroller. And normally, I've seen this on like, you know, C based things never something is as a kind of easy to use as Python, and so CircuitPython. And so um, so once you trained it, he then minimize the resulting Python file. And that's like maybe 10s of 10s or 20 of K, on the flash. And, and so now you can have vision system CircuitPython, machine learning. And she has all blog posts on how to do this, and a GitHub, it has all the code. So you can just use his train model off the bat, if you want to try that. I got a camera board just a few days ago, and I'm gonna try this out this weekend. So let's see if it works.

Paul Cutler  11:36  
That'll be a fun project. And we'll make sure to link to all of his work in the show notes too.

Tod Kurt  11:43  
All right, so what's the last one?

Paul Cutler  11:45  
We're gonna come back to 3d printing. So what kind of 3d printer Do you have?

Tod Kurt  11:50  
I have a couple but the one I'm used the most as a Prusa. Mark 2.5.

Paul Cutler  11:55  
Okay, so I'm going to talk about the Bambu Labs, which started the Kickstarter earlier this summer. Now there's a rule in the 3d printer community to never buy a printer on Kickstarter, for a number of different reasons, I'm not gonna go into here. Bambu knew that because before the Kickstarter went live, they sent out a ton of review units to YouTube posts and other influencers. They all came back glowing about it. And a couple even follow even said they'd be spending their own money to buy one it was that good. The Kickstarter launched and they raised about 10 times what they were looking for. What's so cool about it is the next one is generational. This printer sets the bar for the next generation of printers. It has built in LIDAR for auto bed leveling, as well as some other bells and whistles. Like if you buy the step up, it's got the built in webcam and can do time lapses, among other things. But the key selling feature here is how fast it is, it's up to four times faster than an Ender three or a Prusa. Wow, the quality is excellent. I had a chance to help set up my best friend's ex one carbon, carbon, and the hype is real. The OtterBox experience was wonderful. Everything was clearly marked, and we were up and printing in 15 minutes. That's amazing. It really is. If you're looking to buy a 3d printer and looking at CReality Ender threes, this is not the printer for you. But if you're looking at a Prusa, not the Mini, you might want to consider the x one, a fully assembled Prusa will run you about $1,100 in the Bambu is two models at $1,000.12 $100. With the more expensive one having a slightly better build quality and some extras like the webcam that I that I mentioned. There's a there is some risk with a new manufacturer. There is some risk with a new manufacturer, but they've made replacement parts for sale already and follow through on their promise to open source their slicer software. If this is what the next generation of 3d printers looks like, I'm really excited.

Tod Kurt  13:54  
That's pretty cool. I mean, just just the LIDAR kind of sold me I'm like, okay, yeah.

Paul Cutler  14:02  
Yeah, it's enclosed. It's slightly bigger than the person that Ender and 256 by 256. They've done a heck of a job. You know, this is a first generation printer from so we have to give them a little time to see how the build quality holds up. But so far, so good. 

Tod Kurt  14:19  
Totally, I can't wait to check it out. Like just to view some of the videos and stuff about it because that sounds really neat. Thank you for listening to the bootloader with your hosts Paul Cutler and Todd Kurt. Follow us on Twitter at the bootloader for shownotes transcripts and to support the show visit [The Bootloader](https://thebootloader.net). See you next episode!
