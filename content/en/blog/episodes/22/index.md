---
date: 2025-07-07
title: "The rant and the love letter"
linkTitle: "Episode 22 - July 7, 2025"
description: "The rant and the love letter"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

## Welcome to the show

In this episode, Tod and Paul discuss a MIDI chip, a board game, Tod shares an epic rant, and Paul shares a love letter.

Follow the show on [Mastodon](https://www.circuitpythonshow.com/@thebootloader/follow) or [Bluesky](https://bsky.app/profile/thebootloader.net).

## Listen to the podcast

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/the-rant-and-the-love-letter/embed/dark"></iframe>

## Show Notes

### SAM2695 General MIDI chip (Tod #1)
You know my continuing quest to make micrcontrollers act like synthesizers.
Well, what if there was a single chip that you could talk to with a single serial
wire that not only gave you a single voice synth, but was a 64-voice synth! With 128 different
sounds, includuing piano, strings, bass guitar, and a full drum kit! And it can
play these all simultaneously: it's multi-timbral. It can play a different sound
per MIDI channel, selected with MIDI Program Change messages.
Oh it also has audio effects to apply to those sounds, like EQ, reverb and chorus.
And a mic input treated with those effects!  This thing is bonkers.
It's called the SAM2695. It's a full General MIDI synth on a chip.

You may remember "General MIDI" or "GM" from PC video games in the 90s where,
if you had a special soundblaster card or an outboard GM MIDI module, your games
would have much more cinematic sound than normal.  I remember playing Tie Fighter
on a friend's computer that had one of these and, man, it felt like I was in a movie.

This SAM2695 chip is from a French company called Dream.
They seem to specialize in one-chip solutions to many "music hobbyist" needs like
"keyboard synthesizer chip", "USB audio interface chip", and "81 voice piano chip".

The SAM2695 is an earlier effort, aimed at low-cost applications.  It's around
$4 in quantity and requires only a few support components. It can be
completely controlled by a single logic-level MIDI input serial line,
making it really easy to embed.

In fact, you can get some pre-made modules right now from Seeed or M5stack, like:
  - [Seeed XIAO MIDI](https://www.seeedstudio.com/XIAO-MIDI-Synthesizer-p-6462.html)
  - [M5stack MIDI Synth w/ speaker](https://shop.m5stack.com/products/midi-synthesizer-unit-sam2695)
  - [M5stack Unit w/ MIDI in/out](https://shop.m5stack.com/products/midi-unit-with-din-connector-sam2695)

If you'd like to learn more about this chip and the M5stack board for it, Kevin
from DIYElectroMusic has a [great series of articles using the M5stack MIDI version](https://diyelectromusic.com/2025/06/26/xiao-esp32-c3-midi-synthesizer/) with a
XIAO/QTPy board.

On Dream's website, the SAM2695 is marked "not recommended for new designs",
but seems like that's not stopping the above companies.
I wonder what happens to the above products if this chip really goes away?
I don't think they're working off copies.  I hope it continues to be made forever.

I've got the M5stack versions and they're really fun. And super cheap too: 12 bucks for the
one with built-in speaker and TTL MIDI and $14 for the one with real MIDI ports
and an TRS audio output jack.

Links:
  - [Seeed XIAO MIDI](https://www.seeedstudio.com/XIAO-MIDI-Synthesizer-p-6462.html)
  - [M5stack w/ speaker](https://shop.m5stack.com/products/midi-synthesizer-unit-sam2695)
  - [M5stack w/ MIDI in/out](https://shop.m5stack.com/products/midi-unit-with-din-connector-sam2695)
  - [DIYElectroMusic articles](https://diyelectromusic.com/2025/06/26/xiao-esp32-c3-midi-synthesizer/)
  - [SAM2695 datahsheet](https://docs.dream.fr/pdf/Serie2000/SAM_Datasheets/SAM2695.pdf)
  - [Tod demo on Adafruit Show-n-Tell](https://www.youtube.com/live/sQW1XVhu-iw?si=TsH9pujz_LLW6hGb&t=342)


### Supercollider Synth Engine and Supriya Python API (Paul #1)

Correction Notice: Paul mistakenly gave credit to Andrew Clark for Supriya, when it should be [Joséphine Wolf Oberholtzer](https://github.com/josephine-wolf-oberholtzer/).

The [Supercollider synth engine](https://supercollider.github.io/) has been around since 1996 and open sourced in 2002.  Supercollider includes there components: scsynth, a real time audio engine implemented as a server, sclang, an interpreted program language that acts as a client to the server that is similar to Smalltalk, and `scide`, an editor for sclang with an integrated help system. The server and client communicate using OSC - Open Sound Control.

I looked at some SuperCollider examples, but couldn't quite wrap my head around it.  Thankfully Andrew Clark wrote a Python API to Supercollider he calls calls [Supriya](https://github.com/dayunbao/supriya_demos). And he wrote a dozen examples and published them on GitHub.  They include an arpeggiator, an LFO, drum sequencers, and more. Then he takes it to the next level - he created a [subreddit](https://www.reddit.com/r/supriya/) where explains each demo, including an introduction to the concept, code for each demo, and then a walkthrough.

If Python isn't your thing, there are also APIs for JavaScript, Haskell, or Scala.

### Rant about STM32 dev tools (Tod #2)

I'm going to rant about STM32 development tools.
Now, realize, I'm a Makefile and text editor guy.
My debugger is print statements, pin toggles, and oscilloscopes.
I've developed for just about every low-cost microcontroller, except for STM32.
Since I now have work-based reasons to get into STM32, I started the dive, thinking it
would be similar to other ARM-based MCUs I've worked with.

I quickly find that it seems the majority of people are using ST's collection of IDE tools.
Oh no. Vendor-required IDEs.

You know what's worse than trying to use Arduino to write microcontroller code?
Trying to use Eclipse to write code!  What's worse than that?
Using a vendor's wrapped version of Eclipse. And worse than that?
A vendor-skinned Eclipse that has sub-apps that run in an entirely differnet JVM to configure the chip with a GUI.
Worse than that? The only build for MacOS is Intel, so it runs in x86 Rosetta emulation.
Thus, a keystroke you type goes from native code to emulated x86 to Java VM to Eclipse GUI to
vendor wrapper to finally your screen.
TO SAY IT'S "SLOW" IS TO BE KIND
On top of all of that, seems like everyone in the STM32 world relies on this dang GUI to configure the chips. Sigh.2

I kind of blame Arduino for this situation.

Before Arduino, programming microcontrollers was a real pain: Windows only, using
proprietary IDEs written in Visual Basic invoking proprietary compilers, all costing
thousands of dollars. But around 1999, avr-gcc and avr-libc was created by some kind hackers.
A fully open-source compiler suite for the very nice Atmel AVR microcontroller chips!
Of course Atmel wanted nothing to do with this, but everyone loved it.
And when Hernando Barragán created his "Wiring" thesis project in 2003 by smashing
avr-gcc together with a hacked version of the Processing IDE, the beginning of what
we now know as Arduino was created:
a fully open-source cross-platform IDE for writing and debugging micrcontroller projects.

I've used the Arduino IDE as a starting point for many projects and moving to a commandline-based
Makefile with avr-gcc was pretty painless, letting me use any more advanced code editor.
Because Arduino cores are open source, if you want to know how Arduino is configuring a chip,
or setting up pins, just poke around the core and find how this chip's `digitalWrite()` works.

People bag on the Arduino IDE now, but it was revolutionary. It set the new
baseline for MCU development apps: based on GCC, Windows/Mac/Linux builds,
and the core compiler tools and libraries better be open source.
And it doesn't try to lock you into the IDE.

Microcontroller vendors of course wanted more features than the Arduino IDE could manage
so what to do? At that time, the Eclipse IDE was the VS Code of the day:
a highly-extensible IDE that could take plugins and be reskinned.
Unlike VSCode, Eclipse was slow, bloated and terrible to look at, to me at least.
And the MCU vendors didn't help this with their often sloppy wrapping of Eclipse
in their own toolkits to "help" the user. It further obfuscated what I was
trying to do. Just give me a well-organized Makefile, decent standard library
with docs, and some example projects!

If you've done ESP32 or Raspberry Pi Pico development, you've experienced the
benefits Arduino started: good open standard libraries, good docs, GCC compiler,
immensely scriptable via Makefiles or CMake, very open source. All you need to
write code for these chips is a text editor and a terminal window.

And then STM32, the only MCU platform I've not delved into. Their chips
are great! I've been envious of my compatriots who have facility with them.
But the tooling!  It's like stepping back into the early 2000s with the weirdly
slow proprietary IDEs, especially on MacOS currently.

Thankfully, under the hood, it's all standard arm-gcc with a decent
set of libraries for the chips. But I can only find API docs in their crazy IDE, no
website, no PDFs. It's maddening. One "sub app" of the IDE is called STMCubeMX,
a code generator to help do proper chip configuration and startup.
This is useful. It "only" takes 15 seconds to start.
It seemingly has example projects it will generate for your chip,
but good luck finding them when every character typed into the search bar
causes a several second delay as the GUI redraws.
It is very powerful and generates code that works.
And blessedly it can generate Makefile-compatible projects, but
these code generators are fairly "one-way".  I can already see I need to make
some chip configuration changes and it seems like the fastest way is to
start a new project, make those changes, then copy over all my code into the new
files.  In theory there are regions in the code files that are safe from the code
generator, but not everything that needs to be modified are in those regions.

So that's my rant. I'm loving the STM32 chips. I've already got first light
on a project using the chips. And I'm learning them enough I can
almost ween myself off the weird GUIs, but it's slow going.


### Why I love building things with microcontrollers; A love letter to embedded systems (Paul #2)
V. Hunter Adams, a professor at Cornell University, teaches (what I think) is a graduate level course on microprocessor based embedded controllers using an rp2040 and the Pico C SDK. [Hackaday shared a link](https://hackaday.com/2025/05/28/a-love-letter-to-embedded-systems-by-v-hunter-adams/) to his [November 2023 lecture, "Why I love building things with microcontrollers."](https://www.youtube.com/watch?v=-TFsfcIx04Q)

It's a full lecture, so it's a little long at about 37 minutes. He talks why it's important to build tings and have a project portfolio.  Building things is hard - nothing ever just works. He talks about simulation vs real world building and I wrote down this quote: *"It fills you with humility and wonder.  You will weep in aweo of things like keyboards".*

He then goes on to ask: What makes embedded system projects special? He talks about how engineering is the mechanism for him to learn other stuff.  He then goes off on a tangent about Leondardo DaVinci, who is a genius in multiple fields, but would study those fields for years in-depth.  He also talks about how microcontrollers offer constraints and constraints beget creativity.  And microcontrollers are just the right amount of complexity - for example a datasheet can be hudnreds of pages, which is compolex, but not behond the capacity of single person.

I've sometimes struggled to explain why I enjoy microcontrollers when asked about my hobbies, and I thought Hunter Adams summed it up nicely: They sit on the boundary between the natural world and the computational world and offer unique views of each.

### Alternate musical keyboard layouts (Harmonic Table, etc) (Tod #3)

Ever wonder about those grid layouts that some synthesizers or MIDI controllers have?

The linear arrangement of the piano is conceptually simple but actually
terrible for performance. If you've played with a guitar, especially the lower four
strings, you've experienced a 2D note layout that's more intuitive and easier for
transposing: chord shapes stay the same as you move along the fretboard.

For keyboard players we've seen an explosion of 2D layouts of these 2D "grid" instruments
like the Monome, Launchpad, and my favorite: Synthstrom Deluge. These have rational guitar-like
layouts where a specific arrangement of buttons means "major chord" or "minor chord" and
you can play that arrangement anywhere. And since they're still "linear" for each row,
it makes sense when coming from a piano.

But is there an even better layout? Better for perfomance and has some music theory
baked in to make playing even easier? Yes! The Harmonic table note layout. This layout
has the keys in a hexagonal grid, but not linearly as the grid instruments. Instead,
the notes are spaced according to a "tone net" ("tonnetz" in German), where notes
are arranged how they relate harmonically to each other. Orignally devised by
Leonhard Euler in the 1700s!

How do you use this? Imagine a hexagon grid. Pick a hexagon, that's your root note,
like "C".  The hexagon right above is a perfect fith above the root, the "G" for "C".
The hexagons to the left and right are the minor or major third notes, respectively.
("D#" or "E")

Sounds confusing but visually it's really easy.
To play an entire chord, like the major C chord "C-E-G" (root, fifth & major third),
those three keys are right next to each other. And you can do it with one finger,
since those three hexagons meet at one intersection. One finger for three notes in a real chord!

It's a wild layout but one I've been wanting to build a MIDI controller around
for a while.  And just recently, the maker of the Teenys controllers, PJRC, just
posted this really nice build of a harmonic table MIDI controller using keyswitches.
It's got some other tricks like velocity sensitivity for comptuer keyswitches,
a topic I've also been exploring. I'll probably talk about it in a future episode.

If you're looking for something to play with right now, there's a web-based
keyboard called HarmoApp in the notes.  And if you want a real controller that
does this, there was a MIDI controller called the AXiS that you can
find on Ebay or Reverb. Should I make a Harmonic Table controller using a Pico &
captouch to match my other controllers I have?

- [Harmoapp - online demo](https://www.harmopark.app/)
- [MIDIHex Harmonic Table MIDI](https://www.pjrc.com/midihex-harmonic-table-midi-device/)
- [Harmonic table note layout](https://en.wikipedia.org/wiki/Harmonic_table_note_layout)
- [Wicki-Hayden note layout](https://en.wikipedia.org/wiki/Wicki%E2%80%93Hayden_note_layout)
- [Farewell to Axis keyboards](https://www.musicscienceguy.com/2014/11/farewell-to-the-axis-keyboards.html)

### Spintronics (Paul #3)
Thanks to Mastodon user GeekandDad, I came across [Spintronics](https://upperstory.com/en/spintronics/), which is a board game for players 8 and up to build mechanical circuits to solve puzzles. I love the description on their webpage: *Feel the pull of voltage and see the flow of current.  Electronics is abstract, but Spintronics makes circuit tangible, irresistbly touchable, and deeply intuitive.*

There are three parts available for purchase,  Act One is about $84 and introduces basic concepts including series and parallel, capacitor circuits, logic circuits, and more. Act Two introduces the transisitor and the inductor with intermediate and advanced concepts like amplification, power conversion, feedback and oscillators.  You can get a bundle of those two for about $150 or add the Power Pack and get all three for about $180.
