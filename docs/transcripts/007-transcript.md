---
date: 2024-03-22
title: "Episode 7 Transcript"
linkTitle: "Episode 7 Transcript"
description: "Episode 7 Transcript - The CircuitPython 9 Release Show"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

[MUSIC] Hi, welcome to the Bootloader.

I'm Tod Kurt.

I'm Paul Cutler.

We're back after an extended break with a special episode breaking down the recently released CircuitPython 9.

It's been just over a year since CircuitPython 8 was released in February 2023, and Tod and I are going to chat about what's new and what we think is cool in CircuitPython 9.

With that said, Tod, what are you excited about in this release?

All right.

There's a ton of things, but I'm going to list four real quick without any explanations.

We can get to them in detail as we go.

JPEG I/O, parallel display bus, USB host, and ESP-IDF update.

How about you?

What are some of the things you're excited by?

JPEG I/O and the Momento camera definitely.

CircuitPy on Android, I think is pretty cool.

Brand new connection manager and USB host, I'm excited to learn more about.

I haven't played with it yet.

So let's jump in.

We both had JPEG I/O on our list.

The Momento camera just came out in the last couple of months and was just unveiled in the latest AdaBox as well.

Have you had a chance to play with a Momento?

I have.

Yeah.

I ended up getting a board before the AdaBox, but then I also got the AdaBox.

Of course, there was JP's wonderful unboxing video that he did last night, which was the 20th of March, 2024.

So there have been other, so it's an ESP32-S3, I think, baseboard that has on it a camera module, microphone, SD card slot, bunch of this stuff, accelerometer.

But it's ESP32, so it's Wi-Fi capable, Bluetooth capable.

But the camera module writes JPEG.

Like when you turn it on and say, "Take a picture," it spits out JPEG data that you're supposed to just save to disk as a JPEG file.

So that raises the question, how do you read that on a CircuitPython device?

So now we have JPEG I/O, which allows you to decode JPEGs and load them, load JPEG images into CircuitPython and display them on a screen.

That's a big deal.

I mean, we had a bitmap support and most everything is using bitmaps, but there's also ping support, but you don't see a lot of it.

But JPEG is the standard for everything.

You can get small enough file sizes and all that fun stuff.

So it's pretty cool to see that added.

Yeah.

It's incredible.

The one downside of JPEGs compared to the other image formats that we like to use in CircuitPython, the BMP or the PNGs, is those can be palletized, which means you can choose exactly how many colors your image has.

So if you have a specifically just black and white image, you can say, "Only use one bit per pixel for this image," which makes the image on your disk a little bit bigger because there's no real compression in BMPs.

But it means that in memory, the CircuitPython image buffer will be much smaller.

With JPEGs, JPEGs are like the full color space.

So I think that it stores them as a 16-bit color, two bytes per pixel.

So it's a bit bigger.

So JPEG I/O will only probably work really well on ESP32 devices, things with lots of RAM, but it's like we got it.

I think one of the really neat things about it too is it shows how Adafruit's innovating around the product, the hardware, and the software coming together to create the product.

Yeah.

It's almost Apple-like that when you can have influence over both of those things, you can have an experience that's really pretty cool.

Yeah.

I've had a couple of these little ESP cams.

You can get them pretty cheap off of AliExpress or whatever that are what the Memento was based on.

It's got ESP32 with one of these little low-cost camera modules hooked up to it, and some simple C code that shows basically how to just write the file.

But it's not a product.

It's not really anything that's usable.

Whereas the Memento is super usable, partly because it's got a good design physically, but also because now you can do it all in CircuitPython.

The first open-source powered camera.

Yeah.

That's pretty darn cool.

Yeah, it's pretty awesome.

One of the other things I like about the Memento effort was that one of the CircuitPython devs, Jepler, added a bunch of image effects in a general way with this thing called a new library in the core called Bitmap Filter.

This lets you do what's called convolution filters, which is your standard Photoshop filters.

You can do things like sepia tone or blur or unsharp mask or whatever.

But it is pretty cool how that piece of hardware is driving the software innovation that Adafruit is working on.

Totally.

Next up, let's chat about USB host.

I understand you've played around with that a bit.

I have not.

I've played around with a little bit on other systems, not much in CircuitPython world yet.

But yeah, the thing I've mostly played around with is that there are a lot of really interesting little USB MIDI keyboards out there in the world that are only USB.

It'd be really cool if you could plug these into something that's not a full computer, but something that's smaller that could then create normal MIDI, standard five-pin MIDI, or it could be a synthesizer in itself.

So with this new USB host functionality, we might actually get that.

The other thing it adds is keyboard support.

Oh, like for computer keyboards.

Yes, it does.

Scott, I think earlier this year, blogged in a CircuitPython 2024 wish list about how close we're getting to an actual CircuitPython powered computer.

We've got the bigger displays and the quality is right.

You've got USB host, so you can actually have the keyboard, and now you've got the microcontroller working as a full-blown computer.

It's almost back to the eight-bit days of yore.

Yeah.

Back when we could turn on the computer and it would immediately give you a little prompt to let you start programming, like that was amazing.

You'd have to wait for it to boot up because you just turned it on and there it was.

It's funny, I think not that it's in CircuitPython 9 specifically, but I've seen work going on with a soft keyboard, so a software keyboard, as well as just a couple of weeks ago in Discord, and I don't know the details, but someone was talking about how could we have a terminal actually in CircuitPython.

Oh, interesting.

Right.

I don't know how that would work if it's connected to the REPL or what, but there were some questions.

I'm like, "Oh, every day we seem to get just a little bit closer."

Yeah.

It's amazing.

It's a pretty complicated problem, it seems, where right now when you want to talk to CircuitPython, you connect via the serial REPL, this USB interface over generally the USB interface, but it looks like a serial port to your computer and you can control-C your program and you can start the program back up again and you can see printouts.

But then there's also what's called the web workflow, where you can do that same interaction but via a web page.

There's also a Bluetooth workflow where you can do something similar, but with a little BLE app.

Now we might have something where there's a different workflow where the keyboard and the screen are connected directly to the microcontroller.

Somehow these all work without them colliding.

If I do something in the web workflow, I can still see it in the serial REPL, I think.

It's just a tour de force of programming to make all this work together.

It absolutely is.

With that said, we have to give credit to MicroPython.

CircuitPython is a downstream fork of MicroPython.

Every major release of CircuitPython, they merge back in all the changes within MicroPython.

In this release alone in CircuitPython 9, there were three MicroPython merges that they made, 1.19.1, 1.20, and 1.21, were all merged into CircuitPython 9, which brings a lot of innovation.

There's one thing called the split heap management.

I actually looked into it and couldn't understand it, so I went to one of the core developers, and Dan Halbert gave me a really great explanation.

It's a little long to read here, I'll include it in the show notes.

But especially if you have some of the boards with smaller amounts of memory like the SAMDs, you might have some memory issues going forward to watch out for.

But overall, it's a really innovative change.

I've also been looking at the piece of text that Dan gave you.

I'm a pretty good coder, I feel, but this is a little bit beyond me.

Those of you who want to know the guts and internals of CircuitPython, I want to know about what changed.

We've got the info for you.

Just go to the bootloader.net and read the show notes.

Totally.

About the merge, I don't know how many people who are listening have actually done merges to an upstream fork of code they're using.

But it is a ordeal because you take this code, some piece of code, and you fork it, you make your own changes, and then the original makes their changes.

And if you want to track what they've done, you have to go through this merge process.

Man, if you've changed the same file, if you've decided to re-architect something to have a different way of thinking about a problem, it's just a huge problem.

And the fact that they're still doing upstream merges, where they're still trying to track what MicroPython is doing, so that CircuitPython is a subset of MicroPython is amazing.

And I was looking at the changes just for the 1.2.0 MicroPython merge, the commit for that in CircuitPython touched 779 source files over 250 commits.

And that's pretty much- And they merged three of those.

Three of those. (laughs) It's like, this is a huge undertaking.

And it seems to work, you know, that like, so we get some of the new thinking from MicroPython into CircuitPython.

And sometimes some of the CircuitPython ideas bubble up to MicroPython, but sort of in an out of band way, because it would be hard for CircuitPython to sort of push changes back up directly.

But yeah, I think it's really cool that we're working together with MicroPython, CircuitPython.

Yeah, the beauty of open source.

Yep.

Next up, let's chat about parallel display bus.

What's going on there?

Ah, okay, so if you've used a little display, little like, you know, LCD or TFT OLED or something, you can talk to it via the I2C bus, which is two little wires kind of slowed around 400 kilohertz, or you can use the SPI bus, which is also two wires, but can operate to like 30 megahertz or so.

And anytime you want to rewrite the entire screen, that could be kind of slow because you're transmitting, you know, several hundred thousand bytes of data to rewrite all the pixels.

'Cause these displays are pretty dense, you know, like one of the ones I like to use is 240 by 240 pixels.

And so you do your remote, you do your best to minimize whole screen updates.

You just want to change little bits that are changing on the screen rather than rewrite the whole screen each time.

But there are some really nice boards that LilyGo has made.

They're another like maker of little microcontroller gizmos that have these really beautiful TFT color displays with an ESP32 board on the back.

And, but they're hooked up via what's with a parallel technique, which is eight data bits instead of the one data bit that SPI has.

And so you can essentially get like eight times the bandwidth.

So it's like an eight times faster display.

And CircaPython has sort of supported this, but only for certain chips and not for these cool LilyGo chips, which are ESP32.

And so lately the parallel display bus has been turned on and fixed for ESP32.

Now we can use these cool boards that have the really fast displays and you can update them really quickly. - So on the LilyGo displays, they're actually built into the boards similar to like the reverse TFTs that Adafruit sells. - They look a lot like the reverse TFTs.

Yeah, yeah.

And so it wouldn't surprise me if Adafruit comes out with something similar 'cause they can now take advantage of these parallel displays.

And it's kind of like, it's really the native way of how you talk to these displays is via these parallel interfaces.

You have to go through extra work to talk via SPI or I swear to see.

So yeah, so I'm excited by it because I like to do a lot of cool graphic stuff with these little computers and watching things load the display is kind of, it's like, oh man. - Sure. (laughing) - That's not good for a little video game. - Next up, one of the things that I'm excited about, and you were just talking about something related to this is you have a number of different ways that you can work with CircuitPython.

You can plug, with most of the boards, you plug it in as the USB drive, it sees it, and you can edit the code.py right on there.

There's the web workflow now where you can connect wirelessly and edit your code.

You can do it via Bluetooth.

Now you can do it on an Android device.

They updated CircuitPython 9 with Android support.

So you can plug in a CircuitPython 9 device and actually write to your code.py right on there and unplug it and your microcontroller will run the code. - Oh, that's so cool.

Yeah, because on Android, you can do serial devices over the cable, right? - I believe it's over USB. - Yeah, yeah, 'cause I think that's one of the restrictions on iPhones is you can't do USB serial or something, but that's so cool.

Yeah, 'cause we should be able to edit these things with a tablet, right?

(laughing) - Right, we should be.

But as you said, Apple's got all that market share, so not yet. - They prefer you to do everything via Bluetooth rather than with a physical cable for reasons that are only clear to them. (laughing) - This is true.

Next up, let's chat about the ESP-IDF. - Ah, yeah, so this is because I'm a big fan of these WiFi chips, ESP32.

There's a bunch of different types of ESP32s that are, unfortunately, they all have the name ESP32 and they're very, very different.

So like the ESP32-S2 is a single core WiFi only, but the ESP32-S3 is dual core with WiFi and Bluetooth.

So it's just very confusing.

But the underlying sort of code API that we all use to write software for these is called the ESP-IDF.

It's an SDK that Espressif, the company that makes ESP32s, puts out.

And for the longest time, CircuitPython was using ESP-IDF 4, which was like two or three years ago version, and it supported only a certain amount of chips, a certain number of the chips, and it only supported certain of the features.

Most notably, we couldn't get, I think, Bluetooth support on some of the newer chips we like to use.

And so through a big effort, similar to the effort of merging with upstream MicroPython, was updating the ESP-IDF to version 5, which enables CircuitPython to have new chip support.

Like there's this ESP32-C6 coming out soon that I think has WiFi mesh or something.

I forget, but there's all these new ESP32 chips coming out, and also it fixes some of the Bluetooth stuff.

So we should have BLE support for ESP32s soon, which has been a sticking point.

People are like, oh, you know, CircuitPython has such good Bluetooth support.

Well, only for the Nordic NRF chips. - Right.

And I'd caution you, I wouldn't say that expressive Bluetooth support is coming soon. - Oh, no. - Hopefully it's coming. - Yeah, no, no.

It's like now it's possible, whereas before it wasn't even possible. - Right.

So I don't want people to get their hopes up too much right away. - Yeah, yeah, yeah.

But if anyone knows ESP-IDF and wants to help kind of flush out the Bluetooth support for CircuitPython for the ESP chips, you know, go to the GitHub and you can help out immensely. - Or join the CircuitPython Discord.

There's a user, a community member working on Bluetooth support for the Pico right now. - All right. - Being done via community members.

So, you know, which is a great segue to the next thing that I'm excited about, which is Connection Manager. - Yeah, what is this?

I've only heard about it obliquely. - So from what I understand, and I haven't updated my wireless code yet, is they've standardized the ability of how you connect to Wi-Fi when you're instantiating the network on the microcontroller itself.

So if you were using an airlift, you did it one way.

If you did it with built-in Wi-Fi, you did it a different way.

From what I understand, if I'm understanding it correctly, a lot of that code has just been simplified so there's one right way to do it and it figures it out for you.

Don't quote me on that.

What I think is so cool about it is a couple of different things.

One, it's snuck in right under the release.

But two, it was done by a gentleman by the name of Justin who's a community member.

He partnered up with the core developers, figured out how to build CircuitPython, how the CI works.

It was great seeing him get involved and it's great seeing that a community member's involvement resolves in a whole new library built into CircuitPython. - That's great.

That is one of the nicest things about the CircuitPython team, the distributed global community that's working on this, which some of them work at Adafruit, is that they're very welcoming.

It's like, oh, if you've got something that you wanna contribute, submit a PR, let's try it out.

Yeah, I've created a couple different libraries and people are like, yeah, we'll put it in the official bundle that you can then use to, that anyone can then easily install.

So, yay.

I can't wait to try out this connection manager 'cause that's always been the real bummer is that if you are using one of these Wi-Fi add-on boards, the way you started up the Wi-Fi was totally different.

The way you got sockets and stuff was totally different than doing the ESP32 native Wi-Fi stuff. - And I'm not the most technical, so don't quote me, but that's my understanding of how it works.

And I'm sure if I'm wrong, I'll hear about it and we can issue a correction notice next episode. - Well, that's how we get the viewer numbers up, right?

Or the listener numbers up is we say something purposefully wrong so that we'll get more engagement. (laughs) - Oh, a little controversy for you right there. (laughs) Last up, we would be remiss if we didn't mention some of the things that CircuitPython 9 no longer supports.

So there's a couple of things that have been deprecated.

The big one for me personally is using display.show, parentheses, and then you would put your group name in the function.

Now it's display.groupgroup equals the group name that you created earlier in the process.

So that's a big one for me as I'm going through slowly and updating all my devices that have displays so that they work correctly.

Next up is file system mounts need to be on an existing directory.

So no longer can you have the drive blank, you need to manually create a /sd directory, for example, if you're using SD cards. - Yeah, that one, I'm not, even though, so as an old Unix nerd who knows that like, whenever you mount a disk, you must first create the directory and then use the mount command to say, put this disk at this directory.

So it's always a two-step process.

I really liked the old CircuitPython way of just like, hey, mount this thing at that directory. (laughs) It was so much simpler. - Sure. - But yeah, so now it's more in line with how real Python works, but I kind of miss the old way. - Yup.

And speaking of being more in line with how C Python works, the last change is CircuitPython now requires explicit socket port reuse. - Yeah. - So you can see in the show notes, the actual command that you would have to use. - Yeah. - But that aligns to how C Python does it, which makes sense why they would make a breaking change like that. - Yeah.

Yeah, I'm glad they're getting more and more close to C Python, to the desktop Python, 'cause I wrote a networking library, a little UDP library recently, and I was able to support both C Python and CircuitPython with just a very small, like two or three line changes in the middle of like, basically, how do you get a socket?

And I'm like, oh, this is nice, 'cause this means I could do like almost all my testing on my laptop with no device connected, and then like just do the couple line changes and try it out on a CircuitPython device, and it all works. - Well, that's pretty cool.

So lastly, I think we should give some credit to everyone who contributed to CircuitPython 9's development, who beta tested it through the long beta testing process that went on, who filed issues, who left feedback in Discord, who participated in the CircuitPython 2024 wishlist.

It's a great community.

That's why I did the CircuitPython 9 show.

That's how we met.

We're both still in the Adafruit community.

So thank you to everyone who's had any part in bringing CircuitPython 9 to life, and thank you to Adafruit for sponsoring CircuitPython. - Totally, and if anybody is interested in like, kind of getting in and like kind of listening to the development process of CircuitPython, there's a weekly meeting via Discord audio, whatever that feature's called.

You can join just to listen in.

You don't have to present or anything.

The core developers, but also people that are just like writing libraries and stuff, and you can listen in and see if you want to participate actively, or it's also good just to get a behind the scenes as to what's kind of coming up in CircuitPython, 'cause you'll see somebody, like I saw that Jepler was working on JPEG I/O like three months ago or whatever, (laughs) and I was like, "Oh, I can't wait." (laughs) - Right, and that's where Connection Manager has been discussed in the Weeds section at the end of the meeting.

So that's a great idea.

It's Mondays at 2 p.m.

Eastern.

Check it out if you're interested in joining the CircuitPython community.

We're members, we love it.

I think that enthusiasm comes through, and thanks for listening to the episode.

And I'm Paul Cutler. - And I'm Tod Kurt. - Thank you for listening to The Bootloader.

For show notes and transcripts, visit thebootloader.net.

If you use Mastodon, you can follow the show on Mastodon to be notified when new episodes are released.

Visit thebootloader.net, click on the follow us link, and enter your Mastodon handle.

Until next time, stay positive.

[MUSIC PLAYING]