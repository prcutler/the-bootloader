---
date: 2022-11-06
title: "Episode 4 Transcript"
linkTitle: "Episode 4 Transcript"
description: "Episode 4 Transcript - What's the Matter?"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---

Paul Cutler  0:01  
Welcome to The Bootloader. I'm Paul Cutler.

Tod Kurt  0:04  
And I'm Tod Kurt. And this is episode four. The show works like this, Paul and I each have brought three things to share with you. We'll spend a few minutes talking about each but no more than five. If you want to learn more, we have detailed show notes available at the bootloader dotnet. And give us a follow on Twitter at the bootloader. So Paul, why don't you start us off this week.

Paul Cutler  0:20  
So the big one is probably the Mac OS Ventura was recently released, got a couple new features couple cool ones like continuity camera, but you can't use finder to drag and drop you have to in hex files anymore, gives you a nice little error every time you try. Now, Adafruit and Raspberry Pi both have excellent blog posts on it. So I'm not going to spend any time going through the technical how I also would recommend watching the November 2 escan, engineer with Lady Ada, where she actually goes in does a great overview of how this happens. But there's two workarounds for now one, you can drop down to a terminal and use the Copy command. The other one that I don't think has got a lot of news is that Alistair Allen, the author of the Raspberry Pi blog post that I mentioned posted a Mac OS shortcut you can use. So download, install the shortcut, you have to enable a shortcut setting for shell scripts, but it's just two clicks. And then when you download a UF to file now when you right click it, hover over quick actions and transfer to RPI is right there. So you don't have to drop down to a terminal. So it makes it really almost similar enough if you're not comfortable at the terminal that this will work out. But the biggest thing you can do is if you're a Mac OS user, is help file a bug report with Apple. Again, read the Raspberry Pi blog post it has detailed instructions and how to submit feedback to Apple. And the more people that speak up, the faster this will probably get fixed.

Tod Kurt  1:46  
Yeah, I can't stress that enough it like apples issue tracking system is very complete. But we see none of it like all we see is that used to be a thing called radar. Now there's this thing called feedback assistant. And it's got a nice little like combo sort of decision tree where you just say where you're having problems with music and you say finder and you say what you're having. And then it'll give you a little feedback number. But you should also in your text reference the feedbacks that have been done by the Raspberry Pi foundation and Adafruit because then they can all tie them all together and they can get into then get a sum up of like, oh, turns out a lot of people care about this one feedback issue. And it's there's been evidence that this works like we don't get get to see the internals where we do with like a GitHub project. It's been known that like, it does help if people speak up

Paul Cutler  2:28  
data driven decisions, the more data they have, the faster they'll make the decision. Totally that what's the first item that you have for us this week, 

Tod Kurt  2:37  
I want to talk about matter. What's the matter? Alright, so matter is a new protocol for doing home automation, Internet of Things type stuff. It's an open standard that's been happening for kind of been in process for a while for about maybe three years or so it actually is sort of an outgrowth of the ZigBee. Alliance, which was a commercial group to sort of promote ZigBee, which is a BLE like Wi Fi protocol that happened like about 20 years ago, and was a computer of Bluetooth, but really was supplanted by Bluetooth low energy, like they took a lot of the ideas of ZigBee and put them into BLE. And so that's why we've now got these really great low power devices that work really easily compared to old Bluetooth, which was kind of a pain to get kind of connected up. But the cool thing about matter is that it's IP based, so everything's got an IP address, but it's also mesh networking, there's doesn't have to be like a single router, if you've got a bunch of different matter devices in your house and they all can see the net. But if one of them kind of goes away for some reason, like maybe it just gets unplugged or something that won't take down your whole home automation system. The devices can then route through one of the other matter gateways matter works with either Wi Fi or works with this new protocol called thread. Which is sort of a really low level BLE like protocol that is explicitly mesh networked and and federated and stuff but the the examples I've seen there are some examples you can play with right now on ESP 32 Those are the ones I've only seen do Wi Fi but in the coming months you'll see more stuff that actually has these thread radios in them a lot of stuff have been shipping through radios kind of under the covers for the last year or two and so there'll be able to enable a matter support really easily I'll put a link in the in the show notes about like what existing things that the thread group has says like these are officially thread based things. The reason why I have noticed this as well first, the matter standards just got like ratified officially released like just a few days ago. Also there's this cool YouTuber named that project that's his channel name has his name is Eric, he posted on the ESP 32 subreddit that, hey look, if you just compile one of these ESP 32 examples from the matter GitHub repo and run it on your ESP dev board, iOS 16.1 just sees it as a HomeKit device and you can just start controlling it. So his example was up was a lamp, little RGB lamp And that's pretty great that like, not only matter, not only are they talking and talking to talk of an open standard, you've got to GitHub with working examples on existing dev boards that are like really cheap, you just compile and run right now. And, you know, Android also has having thread and matter support. And I think that's all turned on. But I don't really know Android that much. So I don't know what the details are. What I'm really excited by is this whole inherently federated, or multi admin controller that they call it in matter where there isn't a single router, because one of the things in the home automation stuff now is you have to buy a special border gateway that will talk ZigBee or whatever on one side, and then we'll talk to the internet on the other side. And if that goes down, then then your light switches work. Or the other problem is, I've got these Alexa products, and I've got these HomeKit products. And I either control them with one or the other. And matter will let you control them with either so you don't you can buy a home kit daily and have it work with your Alexa products. You can buy Alexa thing and have your home get product does matter. So I'm really excited about this, even though I don't do home automation stuff, because I don't know, most of it's a little overkill for for my thinking like this kind of stuff, where it's like, open and cross company, I think is the way it should be. And so I'm glad to see it going out that way.

Paul Cutler  6:16  
I agree. And there's some big names. I mean, we're talking Google and Apple and Microsoft. Yeah, it's every one that needs to be in this is finally in Yes.

Tod Kurt  6:24  
Yeah. It's not just like random little companies. It's big companies.

Paul Cutler  6:28  
And if you're into home assistant, which I use, I only have three or four integrations. I don't have a smart home at all, but home assistant is both matter and thread ready right now. They're just waiting for the devices. So if you think about how many, you know, hundreds of 1000s of installations they have.

Tod Kurt  6:42  
Yeah, okay. Yeah, yeah, I've been really I've been meaning to play with home assistant because it looks really powerful. And it plugs into all the HomeKit stuff.

Paul Cutler  6:49  
The new Apple TV that just launched this week is launching with Mater support as well.

Tod Kurt  6:54  
Oh, that's awesome. Yeah, see? So, yeah, everything's coming up matter. Alright, so what's what's your number two thing this week.

Paul Cutler  7:01  
Number two is 3d printing for a good cause. And I have two examples that are out there that came across my desk. The first one is 3d printing for mental health and suicide prevention. This idea was started by a teacher Abby Brown at Torrey Pines High School in San Diego. Each year, the school has a Yellow Ribbon Week where the students learn about crisis resources and risk factors for suicide. She designed the keychains to give away to our students at the end of the week is a special way to end the Yellow Ribbon Week. Each keychain contains a word such as smile, inspire, create with about 10 different words. But what's cool is there's a fundraising campaign that goes along with it. She posted the designs to cult 3d And if you print one in tager, on Instagram, or on Twitter, she and a number of other organizations including Joel telling, printed solid alien 3d and more will donate $2 up to over $4,000 for the campaign. So you can get a cool inspiring keychain and, you know, help money for a great cause.

Tod Kurt  8:02  
That's awesome.

Paul Cutler  8:03  
It is awesome. The second one is 3d printed Toys for Tots. So most people have probably heard of Toys for Tots. My family actually has volunteered the last few years. It's a great organization. But this one was organized by a company called Ice 3d in 2018. And they work with volunteers in the 3d printing community to print toys for kids. Last year in 2021, they printed over 69,000 toys. This year, they have over 140 volunteers and have printed 27,000 toys so far. Unfortunately, Signups are closed for this here because I look to go sign up for that. But you can donate financially or sign up for next year. And the toys are pretty cool. There's an articulated alligator there's a train engine, there's cars, there's low poly dinosaurs. And similar the maker deck that I mentioned in the last episode, they have a Twitch TV channel where you can watch the 3d printers whirring away printing the Toys for Tots.

Tod Kurt  8:57  
As wonderful as this is so great because um, friend of mine who's got a couple of couple of kids of the like, you know, five to nine year old age, he got one of these like really cheap like $20 Monoprice printers, and then just like gave the kids the URL to Thingiverse or printables, whatever and said, Hey, find find things you want to print and they just had fun just like going like, oh, let's print out yet alligator. Let's print out this bracelet. And they just, they just he just would set it up and go and they would have fun watching it. They'd have fun playing with the thing when it was done. But you know, a lot of the a lot of toys of kids have a sort of a limited life cycle. Even if the toy stays together. It kind of like fades from the interest. And so he's like, Okay, well, I guess I can print something else. You know, each one takes maybe an hour or whatever. Right? Only a couple of grams of plastic.

Paul Cutler  9:43  
Exactly. It costs, you know, pennies on the dollar compared to normal toys.

Tod Kurt  9:47  
Yeah. So that's awesome. I saw I liked seeing the idea. The ideas spread out to a larger community who don't just because not everyone has a 3d printer.

Paul Cutler  9:54  
Exactly. But it's cool to see that people that do actually using it for a great cause. What's your next one?

Tod Kurt  10:01  
All right, so have you ever taken a camcorder and pointed it at the TV that is showing the image from the camera? Weird video feedback? Yeah. Look at these like trippy algorithmic screen savers that maybe like synced to music or whatever. If you wanted to do something like this yourself, how would you do it right, you could get a camera and monitoring. Or you can get a video synthesizer. This is a thing that exists been around forever furnished ever since cameras existed, this video synthesizers have existed. So I was at synth Plex. Last weekend. It's this sort of synthesizer convention. But there were a few non audio synthesizers there, one of which was a which really intrigued me was called Hypno, by sleepy circuits. And physically, it's a small box with knobs, sliders, buttons, and an HDMI port. And it's got a bunch of little jacks for like plugging cables into like you would a normal synthesizer. And so the sort of user interface of it is you look at the screen, it's got like weird triangles, or squares, or whatever. And as you turn the knobs and, and slide the sliders, those shapes will morph and feedback and transform. Those are just two of the video oscillators you can give it, you can also give it a live camera feed, you can give it video files, and then those become the oscillators that you then tweak and feed back sort of in the box itself without having to have a camera pointed at a monitor. That in itself is pretty cool. There's just like this appliance, you just plug a HDMI cable into and start tweaking knobs and you get crazy trippy visuals that you can then fully control. But it's a breads, berry pie based thing, which I thought was really interesting. It's also got Eurorack compatible jacks on it. So you can just plug in cables to your little synthesizer and then have the visuals sync to the music in ways that are there more interesting than just the standard like audio boop, boop, boop, this has been developed by this this guy since like 2018 or so there's an active forum, there's lots of documentation. It's not fully open source, it doesn't look like but it's a Raspberry Pi. So it's, I don't know, it just seems seems like a nice hacker hacker level tool. There's a bunch of examples of it on his Instagram page or on the products Instagram page, I'll put a link to that in the show notes as well. And it's just a lot of fun. It's um, it seems like a pretty pro level product. Like even though it's a Raspberry Pi, you treat it as an appliance you don't like, you know, you don't ever log into it with SSH or whatever you just like turn it on, plug it in and start tweaking stuff. And it's a lot of fun.

Paul Cutler  12:23  
So you literally just take it, plug the HDMI source into a monitor or a TV and start and start tweaking the dials from there.

Tod Kurt  12:31  
Exactly. And and if you want to have it as part of your live streaming setup, it also outputs NDI over USB, so you can treat it as a camera source in OBS or any other sort of streaming setups. So you can just have it like you know, Chroma Key in like up to the camera and it Chroma keys that and feeds it ball back and then feeds it and then you ship that back to your streaming setup. So you can get you can get totally crazy with it if you want.

Paul Cutler  12:57  
Well, that's great. And it's offloading the processing power to the pi. So your computer that's using OBS is running just fine. Let's

Tod Kurt  13:03  
access marks. It's just seeing another camera source. So how about you? What's your third thing for this week?

Paul Cutler  13:09  
My last one is I came across an article on Hackster. IO. And it's called the IO rodeo launches the open colorimeter a circuit Python analysis tool for citizen science. It's a mouthful, but what grabbed my attention was circuit Python being a member of the circuit Python community. And I actually read through that article and didn't understand most of the science behind it. It's been way too many years since I was in school. But here's how I O rodeo describes it, it's the open colorimeter is an instrument with many applications, including measuring contaminants and pollutants in soil and water. So that sounds pretty cool. It's actually an Adafruit pi badge with a 3d printed case. And I think it's pronounced a cuvette, where you add the soil or the liquid that you're measuring. But the other thing that's cool is this is all open. It's published under an open license for the firmwares under MIT, in the physical designs under a Creative Commons 4.0 License. And they have excellent documentation with product guides and project tutorials. The first that I came across for tutorials were to use the color ammeter to measure the blue dye in sports drinks. And like what a great experiment. So you read through that. And again, I couldn't keep up with all of the science, but it walks you through exactly how to use the color emulator to do that. And their mission is to increase accessibility to scientific data collection tools by creating low cost open hardware instrumentation. Everything's open on their GitHub repository, which is pretty cool. But really what caught my eye was that circuit Python, I expect to see micro Python and commercial applications. I'm always surprised and delighted when I find out that there's circuit Python ones out there too.

Tod Kurt  14:45  
Totally. Yeah, I actually actually ran into the IRS to people about 10 years ago. They've been around for a long time doing doing this sort of always open, low cost scientific tools for kind of for education, but they've figured out ways to take You know, Arduino class hardware and make it actually produce usable scientific results. So it's like, oh, here's the thing you can teach in your high school class, to your chemistry students, but you're actually getting real data out that's, you know, comparative to other stuff. I love it. It's all using like, just the boards we have kind of sitting around on our desk. Like their, their cleverness is like the way that they've got the system set up to observe the substances being color rumored to rise,

Paul Cutler  15:28  
right? I didn't know they had been around for a decade. That's great, especially for having an open company like that. Yeah, with that kind of longevity. That's great to see. Yeah, they're awesome. And what's your last one for us this episode?

Tod Kurt  15:41  
Alright, so this is kind of nerdy. I mean, this whole podcast is kind of nerdy. A goal. Alright, so there's this tool called FFmpeg that I've used forever. It's a command line tool. And at the least, the least of what it can do is convert video file formats. So you've got an AVI and in some with some weird codec, and you want to convert it to an mp4 that'll play on your phone, you can just do f of MPEG dash I've weird file dot Avi, output to phone dot mp4, and it'll figure it all out for you. But it does so much more. It's the back end for a lot of GUI applications. Like if you ever use handbrake, or VLC, or in player. It's also used by a lot of websites that do video like I know.

Paul Cutler  16:29  
Did you just say M player? Yeah. Wow. I'm having flashbacks. Many, many years ago. That's impressive. I'm sorry, I interrupted. Keep going.

Tod Kurt  16:39  
No, no, no, yeah. No, it's a thing I used to use in player all the time. It was like the best video player on the maxvill for was. But yeah, I mean, it's in player, a cross platform video player, like, how do you do that? You know, but like some of the things that some of the ways that I use it is I use it to down convert HDR video to SDR for like for all the for a while chrome didn't support HDR content. So it look all weird and blown out. And so you had to down converted to like non HDR. HDR is high dynamic range where they kind of fake the exposure to make it look like it's better. Anyway, I also use it to quickly crop video. If I you know, we shoot with a wide lens and you like, oh, actually, the thing I care about is in the middle, like you know half of the video, you can just use it to, to crop the image, but keep it at 720 p, I use it to decompress for K down to 1080 P because I don't want to spend the time to upload a 4k video to YouTube or whatever. I also use it to convert audio from any audio format, be it in a audio file or video file to a WAV file, which you can then use it with circuitpython I'll link a page of a bunch of cool ffmpeg commands in the show notes. Because it's a great swiss army knife for doing any kind of AV thing. But if you do anything more complicated than just a simple file and file out the syntax for the command lines, arguments diff of impact is crazy. So this person, Zach, his Twitter handle is Zach overflow, he created this thing called FFmpeg dot guide. It's a website that lets you visually create a flow of video and audio that will that FFmpeg will act upon. And so the output is a crazy long FFmpeg Command Line command, you can just copy and paste. And the end, what you see is a bunch of little nodes and flows between nodes. And then you type in parameters between between the nodes and stuff like that. So it's so if you think in a flows a node sort of way, it's like Oh, fine, I can use that sort of thinking to design how I want my FFmpeg command to be. And so I'm just now trying to play with it. You know, it's also complicated because it's recreating what FFmpeg can do. And so he's going to have a paid version, if you want to do really complicated nodes and flows. But if you're just doing up to five nodes, which is quite a lot of functionality, I was just totally free. And so you gotta FFmpeg dot guide website and just try to use it also download FFmpeg anyway, it's totally awesome. Yeah, I

Paul Cutler  19:07  
was playing around with it. It is a great no code solution. I don't know any of the command line arguments to pass to FFmpeg. And I was able to in just a couple of minutes figure out okay, if I drag this here and put this there, then it gives it does it for me. It tells me exactly what I need to do.

Tod Kurt  19:23  
Yeah, yeah, I'm wondering how much it will replace my, my FFmpeg dot tips dot txt that I've had in my home directory for like 10 years. Because I can never remember how to do things.

Paul Cutler  19:35  
Right. So what else have you been working on in the last couple of weeks?

Tod Kurt  19:40  
I've been building more synthesizer bits if the the trip to the simplex convention last week was very fun, and also put me more in the mind of doing synthesizer thing. And so I'm doing that and then in a couple of days, there's Hackaday super con, which I'm going to because it's in Pasadena, it's like two miles away from my house. I'm kind of required to go almost.

Paul Cutler  20:02  
Yes, you are. And we expect to report back. Yeah, it'll,

Tod Kurt  20:06  
it's, you know, it's been really hard to go to like big public gatherings because I've not been like Cineplex was the first one I've been to and like three years. And so I miss all these people that I that I really liked to see on in real life that don't really see it in real life at Supercon. So really nice, but it's also like, oh, I don't know, bunch of people.

Paul Cutler  20:27  
I'm right there with the I'm on the fence about going to PyCon next year for that exact reason I want to go but large crowds, and you got to weigh those pros and cons.

Tod Kurt  20:37  
Thankfully, it's like there's a lot of big rooms and there's a bunch of outdoor newness to the whole setup. And so I think it'll be good, but yeah, how about you anything? Anything you've been up to this week,

Paul Cutler  20:49  
released a new episode of the circuit Python show one that I'm particularly proud of speaking of circuit Python in the wild, I drove two hours east of the twin cities here in Minnesota dual Claire, Wisconsin and visited with Jason P core, who was part of a team who built three circuit Python powered trolls for kids to play on in a park. Great episode, check out circuit Python show.com. Check out the shownotes there's links to pictures. The YouTube version of the show has like the Ken Burns effect with the pictures. But it was a beautiful fall day that we were there and it's a really neat installation.

Tod Kurt  21:24  
Yeah, I saw some of the photos that you shared and those those really look cool. They're much bigger than when you said oh, they're trolls. I was thinking like, you know, but no, they're they're pretty large 

Paul Cutler  21:34  
five foot tall trolls. Thank you for listening for shownotes transcripts and to support the show, visit the bootloader dotnet or follow us at the bootloader until next time, stay positive

Transcribed by https://otter.ai
