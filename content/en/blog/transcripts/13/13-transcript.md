---
date: 2024-10-07
title: "Episode 13 Transcript"
linkTitle: "Episode 13 Transcript"
description: "Episode 13 Transcript - Welcome Liz Clark"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Welcome to The Bootloader.

I'm Tod Kurt.

And I'm Paul Cutler.

We have a special episode for you today as we welcome our first guest, Liz Clark of Adafruit Industries.

Liz, welcome to the show.

Hey, thanks so much for having me on.

I'm glad you could be here.

We've each brought two things to share.

We'll chat about each one for a couple of minutes, but no more than five.

Liz, why don't you start us off?

All right.

Yeah.

So as Paul said, I work with Adafruit Industries.

And so as a result, I have to confess my first choice is a little biased.

It's the Adafruit It's a Snap iOS app.

And I'm mildly obsessed with it.

I've done a couple of Learn Guides with it recently.

And this app is done by our iOS developer, Trevor.

And it basically acts as a bridge between your iOS devices and your Adafruit I/O feeds.

So if there's ever been something on your phone that you've wanted to log to Adafruit I/O or have Adafruit I/O control something on your phone, now you can do that.

And the way that you build it up is using Apple shortcuts.

And if folks don't know, in Apple shortcuts, you can kind of make these like mini scripts using kind of these little widgets.

So you can kind of you can even use scripting things like if statements, you can do Base64 encoding, all that kind of stuff.

So there's a lot of functionality.

Recently, I've done two guides using it.

The first was I used a shortcut to send my iOS photos up to Adafruit I/O using Base64 encoding.

And then I'm using a Qualia S3, which has an ESP32 S3 on it, with a 720 by 720 round display to take the data down from the Adafruit I/O feed, decode it, and then display it on the display.

I just think that's really awesome because otherwise you'd usually have to like create all the bitmaps or JPEGs ahead of time so it'd be able to be displayed.

But this you can kind of do it on the fly just by like running the shortcut, sending it to the I/O feed if it's a snap.

So I'm really into that.

And then the other one that I did is using Apple HomeKit using off-the-shelf smart home devices.

I used a temperature and humidity sensor and a light sensor.

And I was able to get that data into Adafruit I/O and display it on a dashboard.

And then the final thing is I got a light strip that's a matter-controlled light strip.

And I was able to set up kind of a feedback loop where if I change the value on a feed in Adafruit I/O, it would send a text to my phone.

And then I was able to use a text automation with shortcuts so that it would then control the light strip.

So basically I'm able to change the value on the dashboard and control the light scene, which I think is really cool.

And then I was able to write some CircuitPython code to use a feather TFT with some buttons.

So I'm controlling the light strip from the feather using this kind of bridge in between.

Oh, very cool.

Yeah.

So I'm really excited about it to snap.

I think Trevor's done a really awesome job with it.

He also has his own guides.

He's done a health status board where he's able to log all his workouts for the week.

And he's also done a weather project.

You can send the weather from your phone for your location up to Adafruit I/O as well.

And with weather projects, you often have to have an API key and all that.

But this, you avoid all that.

You're just sending the data straight to it.

And then with CircuitPython, you can just read the feed directly and display it.

I liked his project using the health kit with the health statistics.

It showed how many steps he had taken for the day.

And I could totally see putting something like that on my desk to guilt me into getting the 10,000 steps a day that I need.

Absolutely.

Yeah.

Totally.

Yeah.

The whole shortcuts thing, I really want to get into it because Apple has forever had this on the desktop, this AppleScript language, which is this weird English-like language that you can use to have programs talk to each other, which is fascinating.

And so I think shortcuts is built on that.

I think so.

Yeah.

And so by Trevor making an app that's just another shortcuts participant, everything else that speaks shortcuts, which is every other app on the phone or on the iPad, can now participate.

And now you can do what you did, like send photos up trivially using MQTT or whatever.

Yeah.

It's just so crazy.

Yeah.

And I'd never used shortcuts before or anything like that.

And once you get into it, it kind of blows your mind because it's all the stuff you can automate.

And every app does seem to have its own functions that are available too.

Yeah.

I think Apple almost mandates that you have certain shortcut capability.

You can open a file, save a file or something.

When you submit an app to the App Store, it's like, "Hey, you need to implement this to become part of the ecosystem."

Okay.

Gotcha.

Well, that was a good first one.

Tod, what do you have for your first one this episode?

Even though I was a big machine learning person back in the day, I've been very down on most of the modern LLM "AI" in quotes, if you can see my fingers making air quotes, AI stuff.

But there are certain cases where I'm a big fan of it.

And Raspberry Pi just introduced a new camera module for their Raspberry Pi little computers.

It's called the AI Camera.

And it plugs into the normal CSI port of Raspberry Pi, just like any other camera you'd get for the Raspberry Pi.

But it's got a little bit of extra special sauce.

And some of that extra special sauce is that it's got an embedded RP2040 microcontroller with 16 megabytes of flash.

And what that's doing is it's snooping on the camera data and you can use it to have a pre-trained AI model loaded up into the camera module.

And so you just get down the video feed and then the machine learning results.

It's like synced to the camera over I squared C over the single cable.

And so this like offloads all the hard work of doing machine learning stuff on the Pi and puts it in this little camera module, which is pretty cool.

And philosophically, I love these where the models are running on device at the edge, rather than where they have to make a network request out to the world that is charging you some dollars per request.

And it might go down.

And so it's pretty interesting that they're able to get the functionality and stick it in the camera module.

And so you just talk to it like a normal camera.

And then if you want to talk to it like a normal camera plus some other stuff, you can load up some machine learning model into it.

Like the two demos they give are a pose estimation.

So it can just look at the video and kind of see how a human is positioned in 3-space, like where their arm is, where their head is.

And one of the other examples is sort of the hello world of vision machine learning, which is the object detection.

So you like hold up a coffee cup to it.

It'll draw a rectangle around it and say cup.

And so these are just the demos they give out.

They've got a whole repo with a bunch of other examples.

And the show notes, there'll be links to all this.

There's a pretty good Hackster article that shows them trying to use it and getting started with it.

But there's also a GitHub repo, a really nice getting started guide on the Raspberry Pi documentation website.

And Adafruit has these in stock or they had them in stock.

I think they're out of stock currently.

I was surprised to see that they're $70 more than the cost of the Pi itself.

But when you actually look at all the functionality, it kind of starts to make sense.

Yeah.

I mean, I think one of the reasons why it's so much more expensive, because you're thinking, oh, if it's just essentially a Raspberry Pi Pico and a webcam module smashed together, why is that like double the price?

Well, it's like they're actually using a really good camera module.

They're using this Sony FX100 module.

Because with this machine learning stuff, it's really garbage in, garbage out.

So having a really good image sensor to get the best quality image you can before you feed that through your model is really important.

So they have a really good sensor on the front end, better than the most sensors.

So I was thinking of getting this module mostly just because it's a good camera.

And then playing with AI stuff, because I don't really have a use for doing this sort of stuff.

It might be fun to maybe turn on lights when I walk in the room or something.

I don't know.

But yeah, so that's out now.

And it's cool because I know when I've tried to do machine learning stuff on the Pi, just running models on the Pi is kind of a pain.

Yes.

So I saw that all go by when it came out, and I didn't look too into it because I assumed it was just a camera.

I didn't realize it also had the RP2040 on there.

So that's really cool.

And 16 megabytes of flash.

Yeah.

And if you're looking for a similar idea to have it be much cheaper, is for the last two years now, there's been this little $10 board called the Person Sensor by Useful Sensors.

You can get them at SparkFun.

They have them in stock right now.

Me and Paul talked about this back in episode three of the bootloader.

And this is around Halloween time as well.

So I made at that time a little CircuitPython eyeball that would track you around the room as it recognized your face.

And so it's much simpler.

It's running on a very cheap STM32 with a really cheap little webcam sensor.

But it's $10, and it can recognize a face to tell you if a face is looking at it, which is really useful for a lot of cases.

Like if you've got some sort of UI that you want to save power and have some of it powered down when no one's paying attention to it.

But if you walk up to it, it'll light up.

It'll turn on.

It'll say, "Hey, I'm here.

Press this button to go."

So I think having people detection without having to know who the person is, is really useful.

And both of these cameras can do that.

And if you just need that, spend $10 instead of $70.

So yeah, so that's my first one.

How about you, Paul?

What's your first one for this week?

My first one is the Bumpin' Sticker by Guy DuPont.

I love all of Guy's projects, probably because so many of them have a musical take to them.

I had him on the CircuitPython show a couple of years ago, and he also did a maker chat with Liz this past August on CircuitPython Day.

And I'll link to those in the show notes as well.

If you haven't come across Guy's projects before, you should definitely check them out.

The Bumpin' Sticker project is a take on the bumper stickers you might have seen on some cars that say, "Keep honking.

I'm listening to insert your favorite band here."

Except with the Bumpin' Sticker, Guy is sharing what he's listening to in real time.

He picked up an HDMI screen from AliExpress for about $60 and hooked it up with a Raspberry Pi.

He used his Last.fm account, which tracks everything you listen to, which is hooked up to his Spotify account.

This lets you use almost any streaming service with the project as long as you have Last.fm, so it doesn't matter if you're using YouTube Music, Apple Music, Spotify, et cetera.

He then wrote a couple of TypeScript programs using Valtown that scrapes his Last.fm page.

And then lastly, he added a Particle IoT board with cellular service.

That board gets the data of what he's listening to, I think via JSON from the Valtown TypeScript program, passes it to the Raspberry Pi, which then generates the image and displays it on the HDMI screen as a bumper sticker on the back of his car.

He also shows how he wired it for power from the car's wiring and how he mounted all of it and even weatherized it.

All in all, it's a really cool project.

I loved that project.

Just how all the pieces came together.

I also think the video is an excellent explainer on how it all worked.

The video is so good.

Yeah, so good.

It's excellent.

Yeah, he does such a great job.

And I think in the time that he's released that in the last couple of weeks, he's already released two new projects just this week that I'm trying to catch up on.

He even has a new Mastodon bot account that I won't spoil, but I saw him post up today.

Yes, that was the one that I saw this morning.

So we'll link to that in the show notes as well.

Excellent, I haven't heard of this.

There's two aspects of his project that I really enjoyed as a nerd.

One is the HDMI display he used wasn't like your standard 4x3 or 16x9 display.

It's like a 4 to 1 format.

It's like this really long rectangle.

I think it's meant to be like a smart rear view mirror or something, but it's like it's the size of a bumper shape of a bumper sticker rather than like, obviously a screen.

And so to have it change when it's on the back of his car and it changes, you're like, wait, that wasn't a bumper sticker.

That's something else.

Yeah.

I can't imagine driving around Boston and actually encountering that and trying to figure out how that was actually done.

And the other is it.

Oh, yeah, sorry.

Go ahead, Liz.

Speaking as someone who's around Boston, that probably wouldn't even be the weirdest thing you see on the road that day.

And the other thing is he's using this thing called Valtown, which is a like their little slogan is, if GitHub Gists could run and AWS Lambda was fun.

It's like there's all these services out there that will run code for you and charge you and all that kind of stuff.

But Valtown is free for like trying it out and doing some like open source stuff.

And it is just like you have a function and you say, go run this function when this happens, like when this URL comes in.

And that's pretty cool.

I've been wanting to have a project that uses this because it looks like actually kind of interesting and fun to play with.

Time to dust off your JavaScript and TypeScript skills.

Yeah, totally.

All right, Liz, what's your second one for us?

So my second one's a little bit of a left turn from my previous one, but it's the nothing to see/hear wireless fuzz pedal.

So I follow quite a few guitar pedal folks on Instagram and newest post from different noises last week is a wireless fuzz, quote unquote, that completes the circuit by transmitting it via an infrared LED.

So the circuit converts the signal from guitar level to headphone audio level, and then again into light that's sent out through an infrared LED into a transmitter.

And what I love about different noises is he includes a schematic for all his custom pedals.

So if you scroll through his feed, it's just schematics of pedals you could breadboard together real quick.

And he includes some video explaining the circuit and also proving that when he blocks the IR light, there is no sound.

And when he lifts it back up, you have it.

And he said he got it to think about 50 feet between the LED and the transmitter.

So it's still like a kind of a standard fuzz circuit.

It didn't seem to affect the sound of it.

Of course, fuzz is always a little low fidelity to begin with.

But I just think it's so cool.

I love when people like figure out weird ways to transmit signals, you know, whether it's like an audio jack for a soldering iron or, you know, anything like that.

So I thought that was really cool.

And in general, his work's always really interesting.

I was looking at his Instagram page and I love, like, there's this whole community of pedal builders and DIY electronic builders that work on these strip boards.

And they have these like way of describing how the circuit is both like how you would build it by just saying like, this is where the parts would go on the strip board.

And it's just really beautiful because it's like the strip board is like a horizontal rows of copper are connected and that's how the holes are.

So it's sort of like breadboards, but, you know, it's a whole 20 pin row is connected.

And so you can like make these pretty complicated circuits without really much wiring.

You just have to be really clever on where your components straddle the rows and stuff.

And so it's really fun to look at them just without even knowing what they're doing.

It's like little cityscapes.

And I love the DIY guitar pedal community, similar to the maker community.

They're always sharing.

They're really welcoming.

And it's just folks having fun experimenting.

Very cool.

Tod, what's your second one for us?

All right.

Well, so I'm kind of sniping one of your topics a little bit here, Paul, because you're the one who's got the Bambu printer.

So my 3D printer, it's a Prusa Mark 2.5 S that I've had for, I don't know, six or so years.

And it works great.

But, you know, in the intervening years, 3D printers have gotten much better, like surprisingly to me, but like the Mark 4 S Prusa and the BambuLab, they both literally print twice as fast as my printer.

Like I loaded up profiles for both and like sliced it and see how long, like what the slicer said it was going to take.

I'm like, oh, really?

Come on.

So I've been, I've been looking around.

I've been trying to figure out, should I go Prusa again?

Because open source, you know, but I really like having the enclosed frame.

And so I'd love to, so like the BambuLab X1 is really appealing to me because of that.

And so I stumbled upon that there is an open source firmware for the Bambu, which kind of blew my mind.

And it's sort of like, it's a, it's a thing that, that modifies the application processor board of the X1.

So the X1 apparently works kind of like a, like my Prusa with Octoprint, where there's the Octoprint Raspberry Pi that kind of controls the user interface.

And then there's the motion control system that is controlling the actual motors and the extrusion of plastic and stuff.

And the Bambu is set up very similarly.

And this open source firmware called X1 Plus only runs on the application processor and only modifies it slightly so that it will run an alternate firmware off of the micro SD card.

So if you want to run, if you want to go back to running stock Bambu, you still can.

But if you want to run this new open source version, you can try it out.

And this new open source firmware is just basically a different user interface.

It doesn't affect the motion control aspect of the printer.

So it's still going to be fast and good and all that kind of stuff.

And so, so I've been like, huh, maybe this is the path I take for a new printer is, is I kind of do both closed source and open source at the same time.

And the reason why I discovered this is because the people behind the X1 Plus firmware also have come out with a crowd supply campaign for an expansion board that will let you add like more cameras or lights or other sort of sensors and actuators that you can trigger via your G code or whatever.

And so it's not, it's not required to run the firmware, but it's like a, if you have the firmware, you can use this cool extra little plugin board and do a bunch of other, other interesting stuff.

So that's why, that's what I'm kind of thinking right now.

It's like, should I, should I get a new printer?

And should it be one of these?

Should it be a Bambu with this new crazy open source firmware, which is very intriguing.

I don't know if it'll run on your printer.

Cause I, Paul, cause I think yours is a P, a P1, is that right?

I have a P1P and yeah, I did look at it.

That was the first thing I looked for and nope, this is just for the X1 Carbon.

So the higher end one, I was too cheap to get the open source version I guess.

But I'm, I'm interested to hear that, that you're thinking about joining the dark side and going with a closed source printer, even though you could argue that the new Prusas aren't very open source to begin with either.

And this is almost a luster of two evils.

Yeah.

That's the thing is I've, I've been doing open source printers since like the very first MakerBot.

And so yeah, it's, it's the fact that Prusa has been going more closed sources has even made me think of going to other printers that are not, not open because, because of that aspect.

And so yeah, it's, it's still, it's still in the thought processes for me.

One of the things that's, that's forestalled my choice is there is a service called CraftCloud, which is a website you can go to and submit, upload an STL and it will essentially request quotes from hundreds of 3D printer companies across the U.S. and then it'll, it'll sort them by price and you can, and other features that you care about.

And then you can order like one or, or in my case, I ordered like a, like a small batch of like 10 and 20 of a little synthesizer enclosure.

And the quality was great.

It was from some company in Georgia and, and you know, they shipped within like, they printed in two days and shipped within, I mean, it got here to me in like two days.

So it was like about a, like less than a week of time, physical time.

Yeah, it's great.

So I'm like, well, geez, maybe I just don't get a fancy new printer.

Maybe I just use this service for some of the things I care about.

Well, that is a consideration.

How many times have you heard someone buy a 3D printer and a year later, it's just sitting there collecting dust too.

Exactly.

And, and, and, and the costs are, the costs are right at the, at the, right at the perfect place of where I'm like, ah, you know, if it was a little cheaper, I just would use this all the time.

But if it was a little more expensive, I just would buy the 3D printer.

I would recommend that if you're looking at printing ABS, but especially ASA, which isn't nearly as bad as ABS to get the X1 carbon.

If you're only going to stick with PLA and PETG, any other printers are good enough to print PLA these days and get the speed increases that you're talking about.

But that enclosure really makes a difference, especially for ASA being the common one and ABS probably a little more uncommon.

Yeah.

Yeah.

I'm not really into those fancy plastics, but.

I had the same printer that you had, Tod, and like three or four years ago, I updated to a Creality Ender and it was kind of amazing to see just the, the jump in performance.

Yeah.

I think you would definitely appreciate it.

Yeah, totally.

And I will say, Noe is considering the Bambu X1 right now.

Yeah.

Yeah.

It's so good.

I mean, the thing is, is that, is that the, the Mark II, my Mark II 5S, it has been an appliance where like I've got Octoprint running and I will just send a print job to it knowing that like, oh yeah, I cleaned the bed three days ago and that's clean enough for the thing I'm doing.

And I just print and I can watch it on the camera.

I'm like, yep, it's printing.

There's nothing wrong.

For the longest time, 3D printing was never just an appliance.

It was always this like little, little fiddly thing you were messing around with the entire time, doing, doing more to it than getting out of it.

And so, yeah, it's it's kind of amazing.

It is.

It really is.

All right, Paul, what's our final thing for this week, this month?

This one I'm very excited about.

Steph Piper, aka Maker Queen, is a library makerspace manager in Queensland, Australia.

She's come up with a great way to visualize your skill level and skill gaps in 45 different disciplines with her Maker Skill Trees.

Similar to how in a video game, when you get enough experience points to level up, you can put skill points into your character to get better.

This is the same concept, but for you.

It can help gauge where you are in your learning journey for each of the different skills.

Each skill is made up of 73 hex boxes.

You start at the bottom with some of the basic tasks and work your way up at both skill and complexity.

You don't need to do them in order, though they get a little harder the higher up you climb the skill tree.

What's also neat about it is that it might show some gaps that you might have in a given skill.

And now you're incentivized to try something new and fill in those gaps.

Or for the person that says, what do I do or what do I learn next?

This has plenty of inspiration to draw from.

Just a few of the almost 60 disciplines are 3D modeling, 3D printing, amateur radio, coding, cooking, crochet, Dungeons and Dragons, music, PCB design, robotics, sewing, woodworking, and so many more.

That's just a small selection.

So you can see that there's things from the maker world, the crafter world, the coding world, and all of those have Venn diagrams that probably cross over each other in so many different ways.

Steph Piper gave a great talk on the maker skill trees at the Open Source Hardware Association earlier this year.

It's under 10 minutes long and it's worth watching to learn more about it and I'll link to it in the show notes.

She's also working on a book that uses the skill trees, including 13 makerspace skill trees, self-reflection activities, and a life progress dashboard for how you are doing across many of the skill trees.

I think it's definitely worth checking out and everyone, every makerspace should have a copy of this printed, I think.

That's really cool.

And I am a really visual person, so I appreciate having it all laid out.

Some things that you may forget or not think about or not know about, like you said.

So it's really cool.

I really like Steph Piper's work in general too.

Yeah.

She made a very conscious decision that it should be printed on paper and should be a tactile experience filling in those boxes, circling them or crossing them out or however you want to do it and get you off the screens to do it.

I like how it's laid out as a sort of a honeycomb hexagon thing rather than a tree where there's like a linear progression because when you're learning stuff, it's never a linear progression.

You might bust ahead really far on certain topics, but still be like down farther on other topics.

And so having it be sort of like, oh, this amorphous, you just kind of grow from the bottom towards the top is really nice.

I agree.

Yeah.

Well, that's our show.

For detailed show notes or to join our newsletter, please visit thebootloader.net and a special thank you to Liz Clark for joining the show this episode.

Until next time, stay positive.
