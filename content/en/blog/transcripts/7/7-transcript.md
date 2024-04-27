---
date: 2024-04-29
title: "Episode 8 Transcript"
linkTitle: "Episode 8 Transcript"
description: "Episode 8 Transcript - Built from the ground up"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
(upbeat music) - Welcome to The Bootloader, I'm Paul Cutler. - And I'm Tod Kurt.

Each podcast we'll be bringing you news, project updates, product talk from the tech and maker scenes.

And for each episode, we'll be talking about it around three, no more than five things and chat about them for a few minutes each.

Paul, what do you have for us this week for your first one? - First up, I've got a segment that I like to call Meet the Maker.

And first up is Carrie Sundra of Alpenglow.

Now I've never met Carrie.

I just follow her on Mastodon and the socials.

And shame on me, but I've never took a good look at the products and services offered by Alpenglow.

I visited their website and if you visit the about page, I wanted to share Alpenglow's mission statement, which is to teach you about electronics without gatekeeping.

It goes on to say, we are passionate about representation in electronics.

The field is still overwhelmingly white and male with only 10% of electrical engineers identifying as women.

Having worked in the field for over 20 years, we know how much gatekeeping and hostility there can be.

We aim to provide a welcoming space where adults can learn about electronics without judgment or any previous experience.

So right there, you know it's a business that you want to support and do business with.

That is just such a cool mission statement to share with the world.

And it's something that I'm passionate about too, that whole women in tech and under-representation in tech.

And it's great to see her trying to bring people into electronics and soldering.

What sparked my interest was on Mastodon a couple weekends ago they shared a learn to solder surface mount kit.

And that got me to visit the shop and I saw the various learn to solder through hole kits as well as surface mount.

Now I'm terrible at soldering.

I just started soldering within the last couple of years.

And if I had known about this a couple of years ago, I probably would have picked one out.

I still don't know how to do surface mount soldering.

So I'm tempted to buy one of those.

And the kit, which is called the SMT Garden, it's only 20 bucks and it includes over a hundred different pieces from practice capacitors to different colors of LEDs, as well as resistors and a battery holder.

So there's tons of stuff that you can practice soldering on.

There's so many cool things in the shop that I encourage you to go spend a few minutes browsing, pick up something if you're looking to learn to solder or improve your soldering skills.

And that's not all she does.

She also runs a learn electronics workshop and a learn to solder workshop and encourages those underrepresented in tech to attend.

Be sure to check it out.

I've included a number of links in the show notes. - I follow her on Acidon too.

And like, I'm always seeing these great soldering classes and electronics classes that she gives.

And like most soldering kits are kind of boring.

They're like little square things that have like, you know, four little LEDs or something and they just blink or just go on.

But her PCB designs are beautiful, like little bits of art that light up.

And it's, especially for SMD, it's a really great intro because like SMD seems kind of scary, but like, oh, this is just LEDs.

You know, if you mess one up, you still have three or four others that are gonna light up for just this one part.

And there's like four different parts of the whole PCB.

And so, yeah, just even if it's not turned on, it looks cool. - Yes. - And then if you add to it, then it'll look even better. - Her products do look cool.

I mean, there's holiday themed one.

There's a light up Krampus.

There's some no soldering ones that are available.

So depending on what your skill set, there's a little bit of everything for everyone, I think. - Yeah.

Yeah, it's really cool 'cause electronics is not that scary.

It just kind of looks scary. - It does.

And I would say that's my experience in the last few years is I really came into this thinking it was a lot scarier than it is.

And it's just amazing how much you pick up just doing it over and over again in the practice, which is perfect for something like this. - Yeah, like so much of things.

If you don't keep using it, you kind of lose it. - Absolutely.

What did you have up for us next? - From like intro to electronics to like some of the most complicated electronics that I know of is how to make a synthesizer.

And so from previous shows and just if you follow me, you've probably seen that I've made little toy, kind of toy synthesizers using either Arduino with this library called Mozi or in circuit Python with the new synth IO functionality that's built in a circuit Python.

But they're kind of toys.

Like there are a lot of real synthesis platforms out there that let you do like professional quality synthesizers.

And I've never really gotten into them until recently.

There's one module, it looks kind of like an Arduino called Daisy Seed from this company called Electrosmith.

We'll have a link to it in the show notes.

And it's 25 bucks and it's a Cortex-M7 chip, which is one of the most powerful microcontrollers you can get on a tiny board.

And it has 65 megabytes of RAM.

So like, you know, RAM is important in when you're making synthesizers or digital effects, like pedals, like guitar pedals and stuff, because you need that memory to act as the buffer for like the delay effect or something or the reverb effect.

You kind of need to store copies of the sound.

With this chip, sorry, this board, this Daisy Seed board also has a professional quality 24-bit 96 kilohertz audio input and output and stereo.

And then for like knobs and stuff, it's got 16 ADC, sorry, 12 16-bit ADC pins and two 12-bit DACs to control stuff.

31 GPIO pins to like let you control LEDs or like drive a display or something or like read from an SD card.

And it fits on a breadboard.

So it's kind of like, you know, if someone made an Arduino and it grew up and wanted to make music, it's kind of what the Daisy Seed is.

And Electrosmith provides all these really great libraries for it, but they're pretty complicated C++ libraries.

They've got a Arduino library that wraps the C++ stuff, but it's still, you need to kind of know how to C++.

So it's pretty daunting if you just like go and look at it and go through their tutorials, it's like, whoa, that's a lot.

But thankfully there's this nonprofit in the UK called Synth UX Academy, sorry, not in UK, in the Netherlands.

And they've been doing these online classes and, sorry, in-person and online classes that they've been streaming for free on YouTube and putting their code up on GitHub so that you can follow along.

And they're only using the Daisy Seed and they have this really great little PCB set they sell that's like a little tiny synthesizer like platform.

Their whole idea was that like, hey, here's a big gridded PCB with a lot of holes in it where you can put the knobs kind of wherever you want to design what interface you want your synthesizer to have and just quickly wire them up to the Daisy Seed and like wire up an output jack and boom, you've got a synthesizer.

And so it's been a really nice sort of intro level getting you slightly involved in the whole Daisy Seed way of thinking about how to deal with audio and how to generate audio or how to generate like a guitar pedal effects and stuff.

So it's been really cool.

I've been wanting to play with the Daisy Seed for years.

I supported their Kickstarter back in like 2020 and it's been sitting in a box since then. (laughs) But I finally, like just like in the last two weeks I've like gotten out of the box, started playing with it.

And it's all because of this, the Synth UX Academy YouTube videos and their GitHub stuff.

So if you're into this sort of thing, check it out.

It's really cool. - It looks just like, it's just a microcontroller.

It looks a little bigger than a Pico.

And it was only $21 when I looked at the website.

I was kind of taken aback by how cheap it is for that much RAM and M7, like you said. - Yeah, and it's used in like real products.

Like there's some guitar pedals that use it.

There's some like official, you can go and buy them at like Guitar Center, I think.

There's some synthesizers, like the thing called the Chompy.

That's like this cute little synthesizer that has like uses computer key switch keys for its keyboard.

It uses a Daisy Seed inside of it.

And then there's a bunch of Eurek modules that use the Daisy Seed internally.

And you wouldn't know it.

They're just like, they're hidden and they just, oh, here's this platform to do cool audio stuff. - That's pretty neat. - So what's your second one for this week? - My next one is the Microdot web framework.

I've shared before that I enjoy programming for the web and Python.

I've used both Pyramid and FastAPI web frameworks, but I recently came across the Microdot web framework for CPython and MicroPython, which I thought was interesting. - Interesting, yeah. - It was created by Miguel Grinberg, who wrote the Flask mega tutorial, Flask being a popular Python web framework as well.

Microdot's homepage describes it as the impossibly small web framework for Python and MicroPython.

And it's inspired by Flask.

What is interesting is that you'll be able to prototype and write all your code and have it run on desktop Python, on CPython before you bring it over to a microcontroller running MicroPython.

Virgin 2 was released this past December, and it looks like there may even be CircuitPython support.

I saw Miguel had filed a few bugs with CircuitPython, so the Microdot test suite would pass, which is how I first came across Microdot was seeing the bug reports.

So I haven't looked to see if it actually runs on CircuitPython, but it does run on MicroPython, and I was surprised to learn that there's over a dozen different web frameworks for MicroPython, including Microdot.

So if you're coming from the world of CPython and you've used Flask and you're coming to the world of microcontrollers, it really looks like Microdot might be the perfect web framework to bridge both of those worlds. - That's really amazing.

I'm really impressed.

Like I did some networking, some UDP networking stuff a couple months ago.

That was mostly for CircuitPython, but because the API, the network API is a CircuitPython and normal Python, or CPython, are so close, I was able to have my library support both.

And that was really cool because yeah, I could do all my development on the desktop and then try it in CircuitPython and it would just work.

I'm just like, this is kind of the promise of why MicroPython and CircuitPython exists is that you can take your learning from DesktopPython and apply it to embedded microcontrollers, which is amazing. - Exactly, or even the other way around as well. - Yeah, yeah, that's very much true for me 'cause I actually don't know DesktopPython too much.

I have heard of Flask though, so I'm gonna look at this Microdot thing. - There you go.

What do you have for us next? - To go even deeper.

So like what's lower level than CircuitPython? - C. - C, right, yeah, exactly.

I was gonna say the next step down might be Arduino.

Lower than that would be C with like say a vendor SDK.

Like you see you need to have some way of knowing some functions you can call to do like, make the pin go high, make the pin go low.

But what's even lower than that, you could write C code that manipulates a chip's registers directly because that's really all this vendor SDK does is you can just know what memory locations, where the pin register lives and modify that with C.

Or you go even lower, you could do assembly language, which I don't know if you ever heard of assembly language, but it's pretty much the lowest level.

It is these tiny instructions that represent the actual bits that are sent to the CPU and the CPU decodes those bits.

And then that's an instruction and it does one of the instructions, which could be load something by memory or add two registers together or something like that.

And so Carlinorama, disclosure, she's my wife, has been doing a deep dive on ARM assembly language.

And I've been finding this really fascinating.

See, she started out, she knows Arduino and low level Arduino and AVR stuff very well for me.

Original Arduino back in 2006 or so, she wrote some of the original documentation for the Arduino website back in 2006.

She knows all about like low level, bare bones, AVR stuff.

And so she decided to kind of get back into it by writing some bare metal C code to drive an AC tiny 45, and which is a little eight pin AVR, unlike the larger like 28 pin AVR that's in an Arduino.

And she got that to work and it was like, that was a cool couple of days of work.

But now, 'cause like her real target is to learn, not necessarily to learn ARM assembly, but to learn how ARM chips work.

Because she has some like, she has some plans down the road.

And so she went to a Trinket M0, which is a SAMD21 ARM chip and started, instead of just programming an Arduino or programming C, she's like, nope, I'm gonna go with the bottom level.

I'm gonna figure out how this chip starts up when you apply power, what does the chip start to do?

Okay, I'm gonna feed it code to know how to do that.

And then within about a week or so, she got it to blink an LED.

And then a couple of days later, she got it to read a button using the lowest level code as the ARM assembly.

And it's really cool because like, ARM chips are what are in all of our devices now, like our phones, our computers, they all use the ARM processor, the ARM instruction set.

And so, unfortunately, the instruction set on these little chips, like the little ones that run Arduino and CircuitPython, they're a kind of ARM called the Cortex-M series.

And it's the lowest level of the Cortex-M, the Cortex-M0.

And so each one of those, each one of those sort of subsets are a smaller and smaller number of instructions that are available to you from what the big ARM instruction set has.

So the big ARM instruction set has like really big, cool instructions for doing DSP functions and stuff like that.

But when you're on the little microcontroller, you get like the bare minimum.

So trying to figure out when you just type in ARM assembly on Google, gives you this wide range of information and you have to figure out what part of this is applicable to these tiny chips.

And so that was like coming into one of the first hurdles that I was watching her get over.

Like, I don't know any of this.

I know assembly a little bit from like Apple II, you know, way back a long time ago. - Sure. - But my current assembly language knowledge is pretty, pretty scant.

So it's really fun to like just kind of sit back and see her figure out this stuff and then kind of draft off her and kind of do it off to the side myself to see if I can make stuff work.

And sometimes I can't.

But it's these instruction sets, the really cool thing about the ARM instruction set is it's really regular.

Like the old instruction sets of like the Apple II and the x86 chips, they were what's called the complex, CISC, complex instruction set.

What does the C stand for?

The complex CISC, complex instruction set, something.

And then RISC, which is what ARM is, is the reduced instruction set, something.

And so the cool thing about RISC is that you have a fewer number of instructions overall, but the instructions are very regular.

And so you don't have all these different ways of loading from a memory location.

You just have one.

And then you do have to do everything in the register.

It's hard to explain, but without going into a hour long description of like instruction sets.

But I know a little bit about this now. (laughs) - That's pretty cool.

You've got to be pretty curious to go all the way down to that low level and start building back up. - Yeah, no, she's very much like a documentarian approaching it.

She's been blogging about all of this in this little blog she has off to the side of her main sort of blog of like, let's see what are all the different possible ways this can be done and then figuring out the way that actually is the right way.

'Cause not only is there this subsetting of the ARM instruction set, but there's also all these different chips that implement the Cortex-M0 instruction set.

There's the SAMD21, which is what we're familiar with, like the original QTPI.

There's the STM32 chips, which are really, really popular and really common, but neither of us have any experience with STM32, but yet there's a lot of documentation on the STM32 assembly language for some reason.

And then there's like people talking about these more complicated STM32 ARM chips for audio stuff, which is what I was running into.

'Cause I was seeing that like, oh, some of these synthesizer people implement large chunks of their very complicated DSP code as really tight assembly language loops inside of a much larger C program that does the synthesizer.

And so it's like, well, that's not applicable to this problem of like programming a QTPI, (laughs) but it's interesting. - Right. - But like along the way, she also learned that there's a really great ARM simulator, online ARM simulator you can go to and you can like just type in some language instructions into it and compile it in the browser.

And you can kind of step through it with a little built-in debugger and it's like cycle accurate emulation apparently for a bunch of different types of chip architectures.

And that was really, really fascinating to see that.

She also learned how to actually run and use GDB, which I don't know if you ever had to use GDB before, I've used it once, you know, 20 years ago, but it's a way of hooking into your program and telling it to stop and telling it to step, step, step, one instruction at a time and setting break points at certain parts in your code so you can kind of inspect the state of the program without having to use print statements.

So it's really powerful way of debugging your program.

Usually pretty hard to do on an embedded system, but these ARM chips have a built-in debugging system called SWD, software debugging I think is what it stands for.

And so you can use these little $10 programmers that just hook into a couple of pins on the chip and then you can just use GDB to it and tell it to stop and inspect registers and inspect memory locations and see, okay, yes, my code did accurately twiddle this one little memory location that represents the pin register to cause it to be like turn the LED on or off or whatever. - Very cool. - Yeah, so it's incredibly fascinating.

It makes me appreciate all the work that goes into when you write in Arduino, say pin mode and input pull-up, or when you say in Circuit Python, button equals digital in out and your pin number.

There's a lot of stuff, like you just look at the C code that it goes, that goes and does that, maybe it's only one or two lines, but then you see all the assembly language instructions that have to happen to make that work and it's pretty cool.

And then her next steps are, I think, going to move to the Clang compiler system.

So there's this kind of two different ways of compiling for chips.

There's the older and more sort of established GCC toolset and then there's this new thing called Clang and LLVM, Clang is kind of the front end, LLVM is kind of the back end, I think.

And that's, I think the future maybe.

So that's where she's heading next, I think.

And I'm fascinated to see that 'cause I know nothing about Clang. - Yeah, it'll be fun to watch. - It's all right.

So what's your third one today? - Mine is a callback to way back in episode one in September of 2022.

I had talked briefly about the bamboo X1 carbon 3D printer, which had just hit the market at the time.

I had mentioned a good friend of mine had bought one and I questioned how long it would last.

Well, after watching him have his for about six months later, I bought one.

So I've just passed the one year mark of having one and I have the P1P model.

I know it's not an open source printer and I'll take some flack from it, but I gotta say a year later, it still just works. - Oh, wow. - I don't have to fiddle with the bed.

I don't get clogged nozzles.

Now I know that I went from an Ender 3 to a bamboo, which is kind of like going from a really cheap car to a really nice car.

But the worst thing I can say about it is that I have to keep my greasy fingers clean when I'm taking things off the bed.

Just trying to keep the bed clean is probably the worst problem I have.

And if that's the worst problem you have when you come to 3D printing, then you're doing something right. - Yeah, I've heard so many good things about it.

People are claiming it's like a toaster where you just go to it and you just push the button and it works and it seems so fast to print from what I've heard.

It's like, man, that's amazing. - Well, that's been my experience.

And bamboo was actually in the news this week.

It looks like they tried to slip something by their users and it didn't get through, which was claiming that their software would only be updated through 2025.

Well, there was a big brouhaha about it and they came out today actually and said, "Nope, they're gonna support the printer's firmware through 2027 and security fixes through 2029."

So that's pretty interesting when you think 2027, that'll give the printer four years of life, which in this industry is probably not too bad. - Yeah, totally.

But yeah, that's always the danger with any of these complicated computing-based devices is how long does their support last because things seems to always decay.

Like the software-based things always decay unless you keep updating them nowadays. - Right, and you could argue that their firmware is exactly that.

People either love it or hate it every time an update comes out, it seems.

But they've done a good job with documentation.

They've got a Wiki which includes maintenance tips and when to perform them.

I know the bamboo costs more than your average 3D printer, but for me, it's been worth every penny 'cause as I said, it just works. - Yeah, yeah, I've been involved trying to play 3D printer for jeez, forever, like since kind of the first MakerBots.

And I got so sick of having them be a hobby rather than a tool.

And so at one point, I bought like a really expensive one just to like get, just to get out of the morass of like always tuning the printer to get it to work properly.

And then just like pay too much money and get a printer that works.

And thankfully now, getting a printer that works is really low cost comparatively.

Used to be like $20,000. - Right.

Now anywhere from 300 to call it $1,600 if you get like a fully loaded bamboo with the AMS and all that kind of stuff. - The AMF, that's the one where it can like change the filament color or change which filament you're printing with. - Yep, up to four filaments you can have loaded at any time and it can auto switch them out. - That's crazy.

It's like, yeah. - I did not shell out for that.

The printing I do is still pretty basic.

It's prototypes and that kind of stuff.

I don't need, you know, I'm kind of, I've been through the phase where I printed the pretty toys that was already behind me by the time I got this.

So I didn't need an AMS to do the multicolor printing. - Totally. - What's your last one for us this week? - All right, so let's talk about capacitive touch sensors and sliders.

So if you haven't followed me again, you've probably been seeing that I've been playing with, I've been exploring capacitive touch sensors and they're a really great way of adding buttons to your project without actually having to have any extra hardware, except for like one little resistor per button.

And so if you can make a PCB, you can have 10, 20 buttons.

Like I've got a little a MIDI keyboard that's got I think 25, it's a 25 key keyboard I think, you know, just with cap touch pads and an Arduino, sorry, a Raspberry Pi Pico.

One of the things I've been wanting to play with is the little sliders, like you've seen, like the most famous is like the second version of the iPod touch wheel or scrolly wheel.

And the first one was a mechanical little thing that moved, but the second version and kind of all the way up to I think till the end, was this non-moving capacitive touch surface that you just kind of scrolled your finger around on.

I've seen in some of the capacitive touch design guidelines, how to make one of these types of little wheels and the wheels are actually just a special case of a linear slider uses the same technique.

And so I'm like, let me try to build something like this.

And so first, how do these capacitive sensors work?

The way that the technique that I use, that is one of the really common ones is, so all wires, all traces on a PCB are actually little capacitors.

Like when you set them high, it actually takes some time to get to that high state because the capacitance of the metal and the fiberglass and the ground plane on the bottom, that forms a little capacitor and it has to take time to charge up that wire that is your signal trace or your capacitive touch pad takes some amount of time.

And then when you make it go low again, it takes some time.

It's not instantaneous.

Nothing in electronics is instantaneous, even though you said, go low now.

It's like, well, it takes a little bit of time.

And that time is driven by that capacitance of the physical copper on the PCB.

And so you can use that effect if you make that piece of copper bigger, like finger sized.

And then if you tell your microcontroller to raise that pad to the high state and then time how long it takes to go low, you are now able to detect, is there a person touching the pad or not?

Because what happens is if you put your finger next to a copper trace, you add your body's capacitance to the capacitance that's inherently on the PCB.

And it like, I think it's like maybe two or three times.

It's almost like you're adding another capacitor's worth of charge when you put your finger next to it.

So it's kind of cool.

It's like this like really ambient physical effect.

You can, there was normally like a bad thing in electronics that like, oh, your finger's affecting the circuit, but we're using it to actually affect a usable, useful technique, which is like, oh, and I have a little fake button by having just a piece of copper on a PCB.

And so that's how just on/off buttons work.

Well, the sliders work by just having three or more of these copper surfaces and they interleave them.

Kind of like if you take your two fingers and sort of like, sorry, take your two hands and sort of splay your fingers and put them together.

When you interleave the copper traces like that, and if you then put your finger somewhere on that gradient of like the two copper pieces, if you're like, if you're to touch, say on your left side of your hand, when your fingers are kind of connected like that, then you'll get just the left hand.

And as you move your finger across to the right hand, you'll get less and less of the left hand and more and more of the right hand as you move your finger across.

And so that's kind of how these things work is you, instead of reading like just an on/off value, you kind of read a analog value of what that capacitance changes in the pads.

And you can have not just two pads that are interleaved, you can have say three or four or five, six, seven pads, and that will give you more resolution in a way, because you're using more little individual pads to indicate where things are.

I'm not sure how many of the original iPod slide, the touch wheel had, but the minimum that I've seen is about three.

You need three pads.

And my little Pico slider toy, that little PCB that I came out with, uses this three pad technique for doing two rotary dials and three vertical sliders.

It actually kind of works.

It's using a Raspberry Pi Pico, and the code for it is pretty simple code.

It's like just simple sort of algebra, sort of linear sliding two values next to each other.

And I don't know, I'm pretty excited on like, what other dumb things I can do with it.

Like the real downside of the capacitive touch is that there's no feedback.

You know, with a button, when you push the button, you hear a click. - Right. - Some people pay a lot of money on the mechanical keyboards to get even a louder click than normal.

And, but you get some sort of pushback, and there's no pushback with these capacitive touch things.

It's one of the downsides.

It's one of the things that people levied against our phones compared to the phones that preceded it, because the big black screen of a iPhone doesn't have any ridges to tell you where the buttons are, because you know, every interface has a different layout of buttons.

But we're getting used to it.

So I feel like, you know, the capacitive touch is sort of like due for a comeback in terms of microcontroller interfaces, because we're so used to the non-tactility of a phone surface that, you know, these flat capacitive touch surfaces of a microcontroller touch interface would be okay. - Right.

So you link to the code for both the touch wheels and the Pico Slider toy.

Is the Pico Slider toy available on your Tindy store as well? - Oh yes, by the way, I have a Tindy store.

And I have both the larger Pico Slider toy, which has something like 16 different controls and two rotary sliders, three linear sliders, and a bunch of buttons.

And then also the prototype, my little touch wheel zero, that's just one of those little rotary controls, like an iPod slide wheel.

And those are both in the Tindy store if you want to try them out.

And the code for it is like, yeah, like 10 lines of circuit Python. - That's all we have for you this episode.

For detailed show notes and for transcripts, visit thebootloader.net.

I'm Paul Cutler. - And I'm Tod Kurt. - Until next time, stay positive.

You