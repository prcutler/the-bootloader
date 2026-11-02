---
date:
  created: 2026-11-02
title: "Episode 38 Transcript - Saved by Zero"
---

Detailed [show notes available here](../../episodes/2026/ep038.md).

## The Bootloader Transcript

**Paul**

Welcome to the Bootloader. I'm Paul Cutler,

**Tod**

and I'm Tod Kurt. The show works like this: in each episode, we both bring three
things we're excited to share, chatting about each one for about five minutes.
For detailed show notes and transcripts, visit thebootloader.net, and stick
around to the end of the show for a special announcement. Paul, what's your
first one for us?

**Paul**

A couple years ago, I helped a friend out in fixing an old Ender Five 3D
printer. We were chatting about it recently, and he mentioned that it broke down
again, and he was giving up on 3D printing until someone created a CAD program
that could use AI prompts to create 3D printed parts. Like him, I find CAD
programs difficult to use.

At the time, I kind of chuckled, but here we are a few months later, and
PartForge AI has launched that does exactly that. I came across PartForge thanks
to Ellen Shapiro, aka Designated Nerd on Mastodon. It launched fairly recently,
and I came away pretty impressed.

PartForge lets you use natural language or prompts to describe what you want to
design and build. If you've used Claude or ChatGPT, you'll be familiar with the
process. I gave it a spin designing a stand for my podcast mixer that my XLR
microphone plugs into.

I gave it a basic prompt. I need to create a stand for the Zoom Podtrack P4.
Next, its dimensions are 126 millimeters by 120 millimeters by 40 millimeters,
and I want to build a base that sits at a 45 degrees to prop it up.

A minute later, I had a wedge-shaped stand ready to go, and it gave me some
recommendations which I'll come back to in a minute. I then quickly realized 45
degrees was way too steep and gave it a second prompt to change it to a 30
degree angle. After it finishes the design, it will give you a summary with
recommendations.

With my stand, it had cut a hole in the back for cable management, which the
PodTrak doesn't need. It also recommended a cutout for where the USB-C cable
goes for power, something I hadn't thought of. And lastly, if you're going to 3D
print it, it pointed out that this overhang might be too much in a spot where
the walls were too thin.

A couple more prompts and that was all fixed. I then noticed in the chat window
it had another suggestion and you could hit Tab to just autofill it. In this
case, it was fill the cavity under the ramp with support ribs so it prints well
at 30 degrees.

You can spin the model and look at it from all angles just like you would in a
normal CAD program. And then to the right of the model, it has a number of
sliders to quickly adjust it, such as width, depth, clearance, sidewall
thickness, how many support ribs, their thickness, and more. I've taken a couple
of screenshots of Part Forge in action and included them in the detailed show
notes available at thebootloader.net.

When you're ready to print it, there's a download button, and you can choose
from STL, STEP files, or 3MF, which is handy for Bambu printers, which I have. I
printed it out, and it was spot on. From there, you publish the part or forge,
as they call it.

You can add a render or take a picture of the final product and upload that, or
add a link to a YouTube channel if you have a video, or include a video as well.
It also has a nice feature to allow you to pick a license, such as CC Zero or
public domain, Creative Commons Attribution with or without ShareAlike, MIT, or
you can choose All Rights Reserved. Depending on the license you choose, it will
allow other users to import or modify it if the license allows it.

This is one reason why they call projects forges, like a real forge. You can
modify a final design and edit it or change it, depending on that license, of
course. Like other AI programs, it gives you a limited number of AI usage on the
free plan.

You can also choose to bring your own API key if you have a subscription to
Claude, ChatGPT, Gemini, etc. Or you can pay twenty dollars a month to Part
Forge, and they say that gets you about thirteen times the usage of the free
plan, or a hundred dollars a month for fifty times the usage of the free plan.
They even have a page in their settings that shows which models can do CAD and
how they perform, which was kind of interesting. They rank it by overall score
and a human ranking.

With Sonnet 5.5 coming in first for overall score, but Gemini 4 Argon was ranked
the best by humans. I have mixed feelings on AI and LLM usage. I don't currently
pay for any AI plans, but if I needed to design a part, I'm probably coming back
to PartForge to do it.

Give it a try at PartForge AI, or check out the detailed show notes at
thebootloader.net for some screenshots of it in action and links to PartForge
and the first forge that I designed.

**Tod**

Yeah, the the thank you for linking this to me beforehand, so I got got to play
with it as well. It's pretty useful because not only does it give you
essentially two panes where you get like the text pane that like the chat window
on one side, and then like the 3D view, the render of the thing currently being
built. But you can also ask it to create parametric sliders for things.

If you don't know the exact dimensions of something, it's like, oh, I want it to
be maybe 13 millimeters wide, but also give me a slider so I can change that
between you know 10 to 20 or whatever. That's pretty nice. You get like this GUI
where you can like on demand create a GUI where you can kind of try try things
out, and then you can.

Render each of those out as STLs or steps or whatever, and you know see if then
print the print that out, see if they work, and then choose this change the
slider and try again. That's what I was doing. I was making some, I was
programmatically making some little synth knobs, and that worked pretty pretty
well.

The other thing is the PartForge people seem to be pretty responsive. I was
having a problem with it with a step exporter crashing on Firefox, and I just
sent a little message saying like. Essentially, step exporter crashing on
Firefox, and a link to the model I was working on, and they came back within a
day, saying like, "Oh, oops, yeah, there's this problem.

It's been fixed now." So, they're currently quite responsive. And there's and
there's many of these.

Like there are apparently so many of these parametric, sorry, chat to parametric
CAD programs that there are a couple of benchmarking tools out there. Like I
think you kind of mentioned some one of the ones that that Parfor is
participating in. But there's one of them that I heard about just last week is
called BenchCAD.

Which is a specifically a benchmark for how well does a one of these tools go
from text to a parametric CAD output, and I I love the fact that like there's so
many of these things now that um there's like testing framework for them, but
but Parfor seems to be the most usable from like a person point of view.

**Paul**

You know. Also check out the benchmarks because that was one other thing I
wanted to call out. As I was actually surprised at the speed.

You know sometimes when you're using an LLM, you put something in the chatbot
and you seem to sit there and wait for thirty sixty seconds and it feels like
forever. This didn't feel like forever. It was actually pretty quick.

**Tod**

Yeah, it's really fast, and it and it as as like you describe in your in your
narrative, it is really good at intuiting the most likely things you would want,
even if you don't specify it. Which is kind of stuff we've kind of come to
expect from LLM output. So, yeah, cool, brave new world we're in.

**Paul**

That's right. And what's your first one for us?

**Tod**

Okay, so oh no, another tiny synth toy. This is the M-Vave FM One, and you may
have heard about this, even if you're not a synth person, as it's been blowing
up other hacker maker forums because of what people are doing with it. In fact,
if you listened to John Park or watched John Park's workshop on Thursday, last
Thursday, October 29th, he talks about this very synth.

The FM One is a handheld, battery powered synth with a 27 key silicone piano
like keyboard, and eight knobs and a nice color TFT display and BLE. It came out
about three months ago, only three months ago. It's designed as an FM synth,
meaning it sounds like the venerable DX7, those electric piano sounds that were
really common in the 80s is is basically what it sounds like.

And it can even load DX7 patches. And it all costs only seventy dollars. It's a
pretty great value.

But then the hackers got to it. People wondered if the FM1 was running Dexed,
the efficient open source emulation of the original DX7. There's even a Pico
Dexed if you want to install Dexed on your Raspberry Pi Pico.

A week or so after the FM1 came out, hackers started poking around the FM1's
firmware update file and found that indeed it was using Dexed. And then the
reverse engineering really began. We learned in just a few days that the chip in
the FM1 was a JieLi.

I think I pronounced that right. AC791N, a 320 megahertz dual core RISC CPU.
That is actually an evolved copy of a blackfin DSP from the early two thousands,
but has grown in functionality over the last twenty years into working like more
like a modern ARM core.

So it's this really weird sort of like alternate world of CPUs that we don't we
don't really see in the West so much because this is a very Chinese set of chips
that have been out for a long time. This is kind of one of the latest versions
made for mobile devices, made for mobile. Personal keyboards, things like that.

The chip dev kit that was likely used to develop the FM1 was found on
AliExpress, so devs could get one of those and hack on a fully open setup.
Various bootloader modes were soon discovered for the FM1, as well as a complete
pinout for all the buttons, knobs, LCD, audio codec, etc. And all this was
documented in in the open on various GitHub repos, so you could kind of watch in
real time what was going on. And so as this was all was happening, someone named
Bodgrel released FM1 plus VA, a complete alternate firmware for the FM1 that
turned it into a virtual analog synth with a beautiful UI, great sequencer, and
it sounded great.

Suddenly, your little seventy dollars toy could be something totally new. This
sort of popped out out of nowhere. It's like like the bad girls working on their
own, and and just just this came out.

And of course, you can go back to the stock firmware at any time. So suddenly,
we've got like this little synth that can be two totally different things. But
then a week or so after that, the first open source custom firmwares for the FM
one started showing up.

There's like the Felucca firmware, which turns the FM one into a four track
groove box with thirteen different kinds of synth engines, or Sloop, another
groove box that works. It looks and works much like the Teenage Engineering OP
synth. Don't spend twelve hundred dollars on an OP1.

Spend seventy dollars and use Sloop. As people on the subreddit have said, the
fascinating thing about all these is they're not. They don't only include a web
installer, so you can just quickly try it out.

But they also include a web based emulator of the FM1 with that firmware, so you
can try the firmware out online without having to have a physical box. And so,
yeah, there's the there's the r slash mwave fm1 subreddit, which whereas where
I've been seeing a lot of the the daily craziness that's been going on, people
are sharing code and compilation tricks. They're creating new firmwares based on
existing ones, making the provenance of where an idea came from a little
dizzying sometimes.

Like a new firmware will have this really cool thing. It's like, oh, it turns
out that was a subtly hidden feature of a previous firmware. So, in in response
to all this, websites have been popping up to manage this flood.

There's an atlas of firmware that you can go and. Paw through. There's an online
meta firmware catalog and installer that is a web serial based way of installing
any firmware that exists for the FM1 just by click click clicking around and
pressing install.

And so it's become there's been so many of these now firmwares that it's become
a joke on the various synth subreddits that we don't need any new synth because
there will just be another FM1 firmware that has those features. Almost all this
firmware work is vibe coded and proudly so. It's enabled those who barely know
enough about really anything about these little things, but have an idea to
realize that idea and scratch their particular itch.

So now we have for the FM1 the Ghoulbox Dungeon Synth firmware, a fork of the
Faluka firmware that is tuned for dark ambient and medieval fantasy synth music
from Old Tower and Hole Dweller to Mortis Area era dungeon sense. Which I'm sure
these are names of bands I've ever heard of them. And there's there's like an
RPG game for it.

I think there's Doom for it, of course. You know, and it appears that much much
of this reverse engineering was also done with the help of AI too. The
particular GLab chips have very little open documentation, and what does exist
is in Chinese.

I think the original reversing efforts were done in China, so they probably
found it easier going. But being able to go from a disassembly of a firmware
image file to finding out where the audio codec routines are—that kind—that used
to take months. Now it's done in a weekend, and it's incredible how fast the
reverse engineering happened and and the completeness of the of the reverse
engineering.

So the FM one's pretty fun. The custom firmwares have made it even more so. As
someone who's written synth software for years, I'm pleased to see how many of
the well-known algorithms for doing synthesis are all combined in one place.

Makes comparison easier. Like you want to compare this filter algorithm with
this other filter algorithm, or this way of doing non-aliased waveforms with
this other technique. So these firmwares almost become an archive of music DSP
code.

And watching the reverse engineering efforts in real time has been a blast. I
think what's going on with FM1 will be sort of a bellwether of things to come.
Thanks to these new AI systems, all hardware is pretty open now, even if the
manufacturer doesn't want it to be.

For customers, this increases our ability to customize and repair the products
we own, and that's a good thing. Companies will have to figure out how to deal
with this going forward. Mwave, for instance, the company that makes the FM1, is
responding really well, releasing their own open source custom firmware, and
having an official rep join the Mwave FM1 subreddit.

They're seeing what's going on and how how interest in the FM1 has exploded
because of this newfound openness. So good going, Mwave. And so if you've got a
hundred, sorry, if you've got seventy dollars burning a hole in your pocket, and
want to replace that with a little synth that you can install over a hundred
different other synths on, I say get the FM1.

**Paul**

That's pretty cool because the the Venn diagram of people who are programmers
and into music is probably pretty small. So this is a pretty pretty neat use of
AI. And you're you're absolutely right that lots of firmwares and things are
being reverse engineered.

I just saw a story that someone took the Samsung Tizen operating system that
runs on Samsung TVs, reverse engineered that and took all the bloatware and the
crapware off their TVs. So we're just going to see more and more of these these
kind of things. I think come to life with the help of AI.

**Tod**

That's awesome. Yeah. All right. So what's your next one for that for us for
this time?

**Paul**

Do you own an original iPod or iPod Mini? It might be time to dig it out of the
closet because the Sprout Pi mainboard is a drop-in replacement mainboard for
iPod third or fourth generations or the iPod Mini, with no soldering required.
Sprout Pi replaces the logic board, runs new software, and includes new features
such as Wi-Fi, Bluetooth.

It's got a Hi-Fi DAC, USB-C charging, a microSD card that can hold up to two
terabytes of music, and AirPlay and Google Cast. So even just adding Bluetooth,
now you can use your AirPods with it. But don't worry, it still has a headphone
jack if you have wired headphones.

It also reuses the original screen, the click wheel, and the ribbon cables. Just
use a screwdriver and a plastic opening tool, and you're good to go to replace
the mainboard. There are two versions: the Sprout Pi and the Sprout Pico.

The former uses a Raspberry Pi Compute Module Zero with an RP2350, and the
Sprout Pico just uses an RP2350. Since the Sprout Pi uses the compute module, it
has some features that the Sprout Pico doesn't have, such as music streaming via
Spotify or Apple Music, AirPlay streaming, and then it's got some extra custom
apps. The custom interface that it comes with should be familiar to iPod owners
and includes CoverFlow, podcasts, and search.

Sprout is also open source. Both the hardware and the software, schematics,
board layouts, and the bill of material are licensed under the CERN Open
Hardware License s version two. Firmware and software and the Sprout Pi runtime
are licensed under the MPL two point zero.

Documentation, including reverse engineering notes on the iPod display, the
click wheel, and headphone connectors, are licensed under a CC by 4.0 license.
The price and the date haven't been shared yet. That's the catch, but it is
coming soon on Crowd Supply.

I've linked to the Crowd Supply page and a two-minute demo video in the show
notes. If you have an old iPod that's compatible, stored away in a closet, it
might be time to dig it out.

**Tod**

Old iPods are so great, and I've seen a lot of kids getting back into the old
old music players because they're very single use. They're they're not
distracting. The problem is, man, thirty pin connectors on the old iPads or gusy
connectors if you're if you get one of the really old ones, both unuseful.

But like this one, especially with the the RP twenty three fifty, it's like
super small, super cheap. RP twenty three fifty means we could even put
CircuitPython on it potentially. Yeah, but um, but it's got Wi Fi too.

So and like an SD card slot. So I think getting getting music into it is like
pretty easy. Yeah, and like modern connectors like USB.

**Paul**

Yep. And and you're right with especially with the younger generations. You
know, CD sales are up 60 percent year over year.

People are buying CDs. Yeah, and it's Gen Y and Gen Z. Vinyl's still up and
growing at 20 percent year over year. So people are really going back to the to
the old way of doing things.

And I saw some other story that even iTunes is making a comeback. Labels and
artists are putting exclusives more on iTunes or Apple Music or whatever you
want to call it.

**Tod**

That's great. That's great.

**Paul**

Yeah, it's really neat to see this all coming back, and it's all very circular.

**Tod**

Yeah, I think I think I think I saw kids say the other day on social media that
they're they're gonna go and watch a movie analog style by watching it on DVD.
And I was like, hold up,

**Paul**

let's talk analog. That would be VHS.

**Tod**

But you know, I appreciate the sentiment.

**Paul**

Yes, as do I. In fact, that'll tie into my third one later. What's your next one
for us?

**Tod**

All right, my next one is KiCad in the browser. That's impossible. If you use
KiCad to make schematics and PCBs, you've likely used KiCanvas by Thea Flowers.
It's an it's an open source web viewer for KiCad schematics and PCBs. Just paste
a GitHub link into KiCad, sorry into KiCanvas, and view a semantically linked
graphical PCB and schematic view in your browser. No installation of anything
necessary.

It's incredibly handy for sharing and showing KiCad designs. Without needing to
install anything, but now you can have the entirety of KiCad in your browser
thanks to ZiroEDA. That's Z I R O EDA.

Like, what the heck? How does this even work? How can they put all of KiCad as
in a web page?

But basically, they've vibe coded a port from C plus plus from the C plus plus
of the KiCad source to TypeScript, so it's kind of as direct as possible, and it
seems to work. If you use KiCad regularly, I recommend go try ZiroEDA right now
and be a little bit flabbergasted at how it's just KiCad in the browser. It's um
sorry, KiCad.

I always forget.

**Paul**

Who knows?

**Tod**

Anyway, yeah.

Anyway, that that tool we all use, it's it's it's sort of anticlimactic.
Everything just seems to work. It's like KiCad in the browser.

Um, so it's just like you're like, yep, that's KiCad. But um, so so so if you
look into it, what the the ZiroEDA project is is on GitHub. It's GPL licensed.

You can download it and run it locally on your own computer. And they're very
quick to note that quote ZiroEDA extends the KiCad ecosystem. It does not
replace KiCad.

It's not a fork, and it's not a fork of KiCad. They have a philosophy EMD file
designed as much for humans as for LLMs, describing in detail how the project is
a complement to KiCad, not a replacement. And I like that.

I'm glad they kind of upfront are like, you know, hey, we're not trying to be
this. EDA is a service subscription service where it's all in the browser.
Unfortunately, the people behind ZiroEDA are kind of unnamed on their homepage,
but they are affiliated with the IIT Madras Nirmal.

The Indian incubator it's a it's an incubator that's part of the Indian
Institute of Technology in Madras. The commit logs for ZiroEDA show that it's
almost exclusively Akshay Rukade as the committers and Claude, of course. Hi,
Akshay.

Thank you. Thanks for ZiroEDA. This is really cool.

Note that if you use the ZiroEDA website, you'll be encouraged to create an
account. You don't need this. You can create and edit entirely anonymously.

And if you're, if you're, of course, loading up, browsing GitHub-based KiCad
projects, you don't need to have an account either. I think if you do have an
account, then that lets you save your projects to their cloud store, cloud
storage, if you want. So I find ZiroEDA fascinating, and it's really fun to use.

But I'm not sure if I'd trust it for anything yet, for anything critical. But if
I'm stuck somewhere where I just want to goof around, I might use it. I
especially like having the ability to open up and a separate KeyCAD window
because normally KeyCAD only lets you open up one project at a time, but now you
can kind of open up.

Just as many browser tabs as you have, you can have as many KiCad projects open.
And also for my work, I have a lot of 3D models attached to my parts that I use
for visualization. By the way, the 3D viewer does work in KiCad's ZiroEDA as
well.

But I'm sure there's a way of getting those 3D models up into ZiroEDA, but I
want to figure that all out. But you know, being able to like look at the look
at a schematic in the browser, be able to edit the schematic and see how it
looks on a on a PCB and stuff without disturbing my existing KiCad setup is
really great. I'll be interested to see how this goes going forward.

I've noticed several of these big vibe coded projects make a big splash, but
then go unmaintained as time goes on. Here's hoping that ZiroEDA sticks with us.
Oh, and thank you, Paul, for pointing me at ZiroEDA.

**Paul**

Oh, I had to. I don't do enough PCB design to know if this is a good project or
not. So I'm like, here, look at this.

**Tod**

Yeah, it looks good. There's also a article in Hackaday if you want to read
about it on the web. So, Paul, what's your what's your final one for this time?

**Paul**

As listeners know, I have a large vinyl record collection, as well as about 600
CDs from when I was a kid up until I started collecting records. I also own a
large collection of books. I have this collector gene, and I'm not going to
apologize for it.

I've spent years looking for a piece of software to catalog all my stuff in one
place, and have never found one I really like. I use Discogs for my records, but
I don't use Letterbox for movies or Goodreads for books for a number of
different reasons. But now I've come across a self-hosted solution called DVinyl
that was just released on GitHub a few weeks ago.

DVinyl is released as a Docker container that uses MongoDB and allows you to
catalog just about anything, including books, movies, music, video games, LEGO
sets, and board games. And each one has subcategories. When you add a book, you
can choose whether it's a hardcover, paperback, digital, manga, or a graphic
novel.

Music has CDs, digital vinyl, and cassettes, and movies has DVD, VHS, Blu-ray,
or 4K Blu-ray. You'll need to get some API keys from Discogs, Hardcover, TMDB,
and more. DVinyl has excellent documentation walking you through setup,
including getting the API keys and creating the environment variables and
importing your data from other services like Discogs or Goodreads.

It's a web app, so once you have the Docker container installed, you just
connect it in your browser on port thirty ninety nine. But what's really neat is
that it's also a progressive web app, so you can install it on your phone like a
normal app. If you've installed it on a normal web server or on a NAS that uses
HTTPS, you can use the app on your phone to scan the UPC codes of your media to
import it.

It only works with HTTPS, so you'll need a certificate. But I was able to do it
using Tailscale. It has a really well-designed user interface, a number of
different theme colors you can choose from, and a ton of different features.

And I feel like I've only scratched the surface. You can show or hide different
categories, subcategories, or genres within a category. You can choose whether
the art is square, poster, sixteen by nine, and you can see a number of
statistics about your collection at a glance, like how many record CDs or tapes
you have, your favorite genre, your favorite artist, or even your favorite
record label that you have the most albums from.

I spent a good chunk of last weekend importing my collection. I added all my
movies just by scanning the UPC and choosing what format it was in, Blu-ray or
4K Blu-ray, for example.

**Tod**

Oh wow! That's cool.

**Paul**

Yeah. And I started to import my CDs and just finished that today. So I'm
importing all my CDs into Discogs and then I use the import feature into Vinyl.

It does incremental imports, which is awesome. I'm using the hardcover API to
import my books. I have a lot of sci-fi books going back to the 80s when I was a
kid, and a lot of them haven't been found in the system, so I have to look into
that.

And my only complaint about vinyl is so minor, I'm reluctant to bring it up. But
most record collectors, including myself, will tell you that the plural of vinyl
is vinyl, not vinyls. Unfortunately, the vinyl uses vinyls in a couple spots,
which makes me tempted to open an issue or a pull request, but I don't know how
that would be received.

**Tod**

Oh, you should totally do it.

**Paul**

Well, funnily enough, I was on Reddit and in the vinyl Reddit the other day, and
someone had a "What is your old man yelling at the clouds?" moment, and a number
of the comments were in there were people who correct me on saying vinyls, and
I'm like, oh no, and I'm reading through the comments, and I quickly realized
I'm in the minority, and that does not make me happy. But anyway, you can also
back up your collection really easy, either as a zip file, JSON, or CSV. And I
really like that because just for insurance purposes, if anything were to happen
to my house, it's nice to have a record of everything that I had in case it ever
needs to be replaced.

**Tod**

Totally.

**Paul**

The last feature it has is an AI assist feature. If you bring your own AI API
key, you can take a picture of an item and the AI can find it to add it to your
collection. I haven't tried it out because I'm not paying for an AI
subscription, so I don't have a key to bring.

But overall, I really like it, and like a couple of the other topics we've
talked about today, it's vibe coded. But it is self-hosted, which is great. It's
easy to import or add items, and I like the UI and the design.

I've always wanted to catalog my collections, not just for my records, but in
case anything were to happen, like I mentioned a minute ago. I've linked to the
project in the show notes, as well as a demo test server. You can take it for a
spin and see it in action for yourself.

If you've got a collection of music, movies, books, or games, check it out.

**Tod**

I like how it's kind of a kind of a thin wrapper behind all these big data sets
that are out there that have the API keys. That like this seems like a very good
use of the AI to make a an app that joins those together with like some simple
search and a database feature and and it also I didn't even know it makes sense
now but but one of the problems I've had with these kinds of things that I've
tried to use in the past is the data ingest problem of like I've got this big
collection of CDs or whatever how do I get all that information into it and back
in like the 90s I was. Ripping to MP3 and taking pictures of the CD covers, and
it was just was like, just it just gives me nightmares.

But now just scanning the UPC code, that's just like boop, boop, boop, boop,
boop All right, so I created another weird thing, and you can pre-order it on
SmallRun.net if you want. It's a twenty-key touch USB BLE macro pad with per-key
RGB backlighting. Useful as a you know keyboard, a MIDI controller, a gamepad,
whatever you want.

I made it as a present to everyone at the Sketching and Hardware conference I
was at last week. It's about the size of a game pad with ten keys on each half
in sort of a wing pattern. The top surface is the PCB with a touch surface, and
the clip-on 3D-printed case has a small tilt to it, so it looks keyboard-like on
a desk.

I like the result. It looks both playful and weird, but also a little useful.
And hopefully, that's that's my intent anyway.

We'll see people actually use it at the conference. I had a sketching party, a
sketching pad party. Arduino app running on it to let anybody draw color
patterns on their pad, and that pattern was echoed to everyone else's pad.

No setup, just play. It was fun. Since this was the twentieth year of doing
sketching and hardware, I wanted the present that reflected that twenty in some
way, and was also about sharing and technology because that's kind of what what
sketching is all about.

The original design goal was something with capacitive touch because I've been
into that so much. Like anytime you and me have talked about little projects
I've done, it usually has a touch sensor on it.

**Paul**

Yep.

**Tod**

And I wanted something wireless because that's how else you gonna share
something, you know? So it has to be Wi-Fi or Bluetooth or something. Beyond
that, what was it?

This is I for a month I try to figure out what this is going to be, and I really
liked how on these little RGB grid controllers that I've made that I can just
strum the surface of the cap touch and watch the LEDs kind of. the The LED
trails kind of happen after my fingers. It's a really nice effect, and maybe
shareable.

We could each send each other color patterns. Maybe was the was the idea, and so
that's what made the physical design of the sketching gizmo. Is like, okay, it's
it's twenty keys for twenty years of sketching.

It's cap touch, and it's got RGB backlight keys, so they light up as you run
your fingers across the top. But then, how do we do these sharing of color
patterns? I wanted no configuration, no joining of APs, no pairing of
Bluetooths.

Just pick up the pad and draw. I tried ESP Now, which is the no config,
connectionless Wi Fi protocol that ESP thirty two s can do, and that worked. But
even with the most conservative power modes, I found the ESP thirty two way too
power hungry for a little keyboard like board.

Thankfully, the NRF52840 BLE chip does native USB, so it can be a USB keyboard
or a gamepad after the conference. And it only draws about five milliamps when
running full out, versus the fifty like the ESP32 does, and even less when you
can put it in various power save states. And Seed makes the tiny Xiao NRF52840,
which is a you know tiny one inch square board that solves all of the MCU wiring
problems.

So made it made my board's complexity go way down. I use it, and the MCU sub
circuit is done. Okay, but now how do I do this no setup color pattern sharing
with BLE?

Well, it turns out I gave a talk about abusing the BLE advertising packet for
transmitting arbitrary data back in 2014 at a Sketching and Hardware conference.
So let's use that. The BLE advertising packet is what the BLE devices emit when
they're in pairing mode.

So so normally you don't see many of these. It has 25 bytes in it that you can
use for whatever you want. So I created an LED animation event list that stores
the colors and the delta times between those colors for for a pattern.

And then an animation message format that can store multiple of these events in
an advertising packet, and so the sender just records the animation, packages it
up as a series of these messages, and broadcasts them in those packets, like one
or more of those packets. The receiver listens, reassembles the animation, and
it and it works. Abusing protocols for the win!

**Paul**

Yay!

**Tod**

Yeah, yeah. No, it was it was. I was like really chuffed when when it first
first worked. And I was like, oh my gosh, this is this is so fun. I had like
three of them set up, and I could draw my finger on one and see that echoed on
the others.

**Paul**

Oh, that's awesome.

**Tod**

Yeah, it was. It was really cool. Another of one of my design goals was as
little assembly work as possible for me.

I wanted the whole PCB to low to be low complexity and inexpensive, using the
JLC SMB PCB capabilities as much as possible. Let their robots solder most most
all the parts. I could do the light hand soldering at the end, maybe if I needed
to, which I needed to because the Xiao boards aren't normally stocked by JLC, so
I'd have to at least solder them down.

Oh, but wait! What about the twenty RGB LEDs, which is sixty LEDs really? How do
I control those?

I wanted full brightness control, so I could do cool fades. And there's this
really cool Charlieplex chip by ISSI that can drive 144 single color LEDs or 32
RGB LEDs. Would have been perfect.

It's got great brightness control and gamma correction, all this other sort of
stuff. Great power management, perfect for a low power use like this.
Unfortunately, the complexity of wiring it was too much because it's they're
wired in a matrix, and so you have to run kind of like.

Four wires to every LED, and it's just—it's just a mess. And it turns out
there's just not much space on the PCB to run traces because these touch pads
with the backlit LEDs make it so there's there's all these no go zones where you
can't run wires. So, so I tried for like two weeks to route the route the board
using this.

Gave up. Ended up using the naive approach that I've always done is that I've
done in the past, which is using these side firing SK six eight one two LEDs.
They're NeoPixel compatible.

And I found a newer version of them that only draws a quarter milliamp when
dark. Normally they draw like a milliamp or or half a milliamp. This is still a
lot for twenty LEDs.

You know, it's like like five milliamps or whatever. But I added a little
transistor to the LED power bus so I can turn off all the LEDs and to save
power. And that's that like really helps.

And then for cap touch sensing, I've done cap touch sensing with the with the
Pico just by itself because you can do that with TouchIO and CircuitPython and
similar stuff. But because this is a little Xiao board, I only have a couple
pins free. So let's use an I squared C touch chip.

And I have this little TS twenty touch chip. I really love that I found on on
LCSC a few years ago. It has twenty inputs.

And hey, twenty years of sketching seems like a faithful match. It's only a
dollar. It works great, and it's always in stock at LCSC.

So I finalized the design, did a test fab of five. They got I got them back.
They were great.

So I went to go order the big order of of all of them. Only to discover that TS
twenty was out of stock. This part that's never out of stock, and it wouldn't be
in stock, back in stock until after the conference.

So I allowed myself to freak out for about an hour. Imagine me running around
the house going like, Oh my god, oh my god, oh my god, oh my god.

**Paul**

I can see it. I can visualize that.

**Tod**

And so then I redesigned the board using two of the venerable MPR one two one
twelve channel touch chips, which which gives me twenty four inputs, and I only
needed twenty of those. I didn't have time for a test fab, so I submitted this
redesign as the big order. And then I also ordered the original big a duplicate
order of the with the original TS20 version, but without the TS20 chips soldered
down, because I have TS20 chips here, and I figured if the MPR version that I
got back, if the big bunch of them didn't work, well, I could I could at least
solder on by hand.

These little tiny annoying TS twenty chips, maybe in time before the conference.
But turned out it was okay. But so while I was waiting for the boards, I
polished the software, adding some useful examples beyond my weird sketching pad
party.

If you go to the sketching pad GitHub repo, you'll find examples of a BLE
keyboard, a BLE USB MIDI controller, BLE MIDI game pad. I'm adding some more
stuff over the next couple weeks. I also have some CircuitPython examples, but
those aren't as fully fleshed out.

Mostly because most all the stuff's in Arduino. Because with Arduino, I can get
to the lower power modes. I can get it to go to sleep at like microamp levels,
which you can't do in CircuitPython yet.

And to make installing all these firmwares easier, I made a little sketching pad
web flasher. You just go to this page, and if your browser supports web serial,
you can just click flash and get a new application for your sketching pad board
without having to like install Arduino and all that kind of stuff. And so, when
the big box of boards finally arrived with the untested NPR one one two one
version.

They all worked great.

**Paul**

Oh, thank goodness!

**Tod**

And and I was able to like add the batteries to them and give them out to
everybody at the conference. It was it was they were well received. But now I
have a bunch of these TS20 based boards that also worked great once I soldered
on those chips. So I'm putting them up in the store, which is why I'm talking
about it here, kind of. So if you want one of these, check out the smallrun.net
page in the in the show notes or poke me on socials about it.

**Paul**

So you said it was well received. Did you get any feedback on how easy it was to
use or any any specific comments that the the the people at the conference had?

**Tod**

Not too much because unfortunately my talk was on a totally different topic. I
should have made my talk be what I just said here. But mostly, mostly people
were asking like, "Oh, what can I do with this after the after the conference?"
and and it was fun.

It was mostly a fun sort of like colorful toy to play with during the
conference. So it kind of succeeded in the kind of like a badge. The way a lot
of tech conferences have badges, it was kind of that.

It kind of filled that niche. But I'm hoping like one of the problems I've had
with all these badges at all these conferences is they're fun during the
conference, but then after the conference they just sit on a shelf. I've got
I've got a whole shelf of Hackaday badges that are barely useful.

You know, I think last year's was the most useful, and so I wanted something
that was a little bit more long lived than you know not just e waste.

**Paul**

Well, that's our show. I'd like to take a moment to thank our sponsors,
especially those that have joined in the last month. If you'd like to learn more
about sponsoring the show, visit thebootloader.net/support.

Tod and I will be doing a live stream on Wednesday, November 18th at 7:30 p.m.
Eastern, 4:30 p.m. Pacific time. Find the link to our Discord in the show notes
and come hang out with us. It's open to everyone.

For detailed show notes and transcripts, visit thebootloader.net. Until next
time, stay positive.
