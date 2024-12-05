Hello, welcome to The Bootloader. I'm Tod Kurt.

And I'm Paul Cutler. We've got another special episode for you today.

If you remember, way back in Episode 6, about two years ago, Tod shared about his trip to Hackaday's Supercon.

Well, if you're like me and had a feeling of missing out, Tod attended the most recent Supercon that was held November 1st to the 3rd.

Tod, for those not familiar with Supercon, what is it?

Okay, so the Hackaday Super Conference, or just Supercon, is a three-day conference that

happens every year in Pasadena around the end of October at the Supply Frame Design

Lab and its neighbor, the LA College of Music.

It's like one building that's got sort of two units in it.

About 500 people get together and hear a collection of talks on two stages from the Hackaday or

larger tech nerd community.

Supercon is now in its eighth year.

How long have you been going?

I've been going every year except for the very first one that was up in San Francisco,

and the offshoot ones they have in Europe. I've been a big fan of Hackaday since reading

it when it founded in 2004. My wife, Carlyn, and I co-founded Crash Space, a Los Angeles

hackerspace that's going on its 15th year. By the way, if you're in SoCal on December

7th, come by Crash Space for the Crash Space Art Show and 15-year celebration. There'll

be a link to that in the show notes.

When SupplyFrame bought Hackaday back in, I don't know, 2015 or something, they invited

me and Carlin to come by and help them think about how to do a Hackaday hackerspace.

And that eventually turned into the Design Lab, which is a much nicer and cleaner space

than most hackerspaces.

It's much more usable for conferences.

Also I did a Design Lab residency at the Design Lab in 2017.

So suffice to say, I'm a big fan of Hackaday and the Design Lab, and my thoughts are colored

by the now 20 years of being in the Hackaday community. Sure. What's the biggest thing

that's changed over that period? It's been really consistent. A lot of that is due to

the consistency of venue because they have it in their own space. They can really like

make it the way they want it to feel. It's not like you're in a hotel lobby or something.

I think it's more crowded now than when it first started. Just it's become more popular.

And the consistency is really strange. I'll see friends there that I only really interact

with online because they live in New England or Germany and we're able to pick up right

off where we left off like it's another day and hasn't been a whole year.

It's very weird.

As for conference content, they've struggled with the perennial tech world issue of

having a bunch of old white guys like me on stage.

They've been struggling and trying to get better.

And I feel like this year they've made strides towards fixing that.

I really look forward to Supercon every year and I'm glad they're working

on making it more inclusive.

You know, someone has, as someone who's felt like an outsider, uh, growing up,

because, because it used to be nerds were considered outsiders.

Right.

It's like, I feel we have a duty of care to like be as inclusive as possible to everyone else who doesn't feel like they belong.

I included a link to the first day of speakers in a recent newsletter that I sent out.

And I did notice that the conference this year looked to be a lot more inclusive than it has been the last couple of years, which is great to see that kind of progress.

That's good.

Yeah.

It's, as someone who's been a Vince over years and who knows a lot of the people that come every year, it's a real struggle because I want to see.

what my friends have been working on. I want to see them up on stage, but that just leads to the same people talking every year. And so it's, it's, uh, it's really nice to see these totally new people and make new friends.

Supercon's known for their conference badges. I understand they did something a little different this year.

You hear the word conference badge and you think like the little piece of paper, uh, in a plastic holder that goes around your neck and it's got your name on it and the name of the conference. Maybe it's got like your title, like who you, maybe the company you work for.

Well, these tech conferences, these nerd conferences like Supercon and Defcon, none of that applies. The badges are PCBs. They're little electronic circuits that do something interesting, usually visually interesting. And especially with Supercon, they present a puzzle to the attendees. Like it's not a puzzle in the traditional jigsaw puzzle sense. It's a here's this artifact, you have to figure out how it works.

And so for some people, the conference is an entire weekend of hacking the badge, trying to figure it out and make it do something cool.

Because you're given the badge and you're given some documentation about what it is, but you're not given the entire story.

And that's kind of on purpose.

I mean, sometimes it's because the badge makers have been running the last minute trying to get it to work.

But usually it's on purpose.

Usually it's like meant to be a bit of a puzzle.

And it's hilarious that like, as this badge, this electronic badge idea has evolved over the last decade or so, the badges now have no spaces really to write your name.

Like they've evolved beyond being a thing that identifies you.

They sometimes will have the name of the conference you're at, but they won't have that.

And so the functionality of badges have ranged from an FPGA board that runs Linux to a 4-bit

retro computer that you program with switches like in the old days, a virtual vectorscope,

or a mesh networking chat keyboard. Oh, that's crazy. I haven't seen that one.

Yeah, yeah. And these are just the Supercon badges. There's other tech conferences that

have done other really crazy things. Another aspect of these badges has been add-ons,

little extra circuits that you can add to it that light up or add some functionality to the badge.

I'm beginning to think that this started as a way to identify the badge holder,

since the badges themselves have lost their ability to do that.

For the last six years or so, these add-ons have been codified into a standard called SAO,

which stands for Simple Add-on, originally Shitty Add-on by Brian Brenchoff, which is just a six-pin

connector a little like standard six pin pin header that provides power an I squared C bus and two pins of GPIO for whatever you want

but most add-ons just use the power to light up and do something like blinky and

These these sao badge add-ons are generally pretty small. They're about two inches on a side

if that this size and format allows for

easy exploration of PCB art

You can try out what different colors and different sort of visual textures you can get because you can put

With standard PCBs you can put two different colors on each side of the PCB and then you can have the copper that's on the actual circuit show through or not.

So you can get maybe six different shades of green or something.

And then you can also add LED backlighting and have that show through the PCB if you've got clear spots.

So, given the rise of these SAO add-ons, this year's badge for Supercon was primarily a platform to show them off.

It has six SAO sockets on the front and a Pico W and batteries on the back.

And it also comes with a small collection of starter SAOs so you can like

immediately just plug them in and have to have it do something.

But the real fun later comes as people give out and trade SAOs they've made all

during the conference.

I'll have to see if I can find some pictures of those and include them in the

show notes too, because there's some pretty cool ones that we'll talk about

later on as well. Yes, yes.

So this year they invited some makers to create simple add-ons to give to the attendees. And I understand you were picked to design an SAO to give out.

Yeah, it was it was cool. I was totally, they didn't really describe what was happening. But around back in August, Magenta and Giovanni of the Design Lab contacted me and said, "Hey, you want to make a SAO based off of my little CapTouch wheel gizmo that I've been playing with for the last year or so?"

And I'm like, yeah, sure. And it was fun scaling down that project to something that's the size of a badge and uses a ATtiny microcontroller that's more appropriate for a badge versus a Pico or something similar to that.

It was fortunate that my Arduino touch library worked well enough for this. So I was able to just kind of use that. And the Arduino core for the ATtiny816, which is a nice tiny chip for things like badges, works great. So I was able to write it all in Arduino, which is really nice.

Not having to learn yet another

SDK for a chip is like it's like super handy so I was able to do that in about a week and I got a bunch

FABed and then we went through a couple design iterations because they wanted you know, like oh, let's try out this size chip

Let's try out this these types of LEDs

Yeah, they got produced at scale and the result is what I call the touch will SAO

And how many did they make to give out? I think five or six hundred I forget it

They made as many as there were attendees and then a little more and then they're going to be making some more for some

Of their future conferences, I think

The touch will sa o board it's got it's got the iPod like touch will on the front

But then it's got three RGB LEDs on the back that shine through to indicate what sort of touch action is being done

That's really handy with cap touch sensors to actually know that it's been that your touch is being registered and then it talks over I squared

C to whoever whoever is controlling it and the ice would see protocol

I designed I try to make it as easy as possible people to get touch data out and to control its LEDs

I think I succeeded in that regard which is which is a bit happy

I was I was worried that no one would use it

But it turns out lots of people may be cool little hacks with a little bit of touch wheel

Very cool

And I wasn't convinced that the cap touch stuff would even work in the wild battery powered environment of the conference where all these other

Weird circuits are plugged into a badge, but it seemed to work

It was kind of surprising because cap touch can be really finicky when you're doing the sort of hacker

way of doing it, not using like a custom touch chip and things like that. In retrospect, I think I

should have used four interleaved pads instead of the normal three that I use for all my other stuff.

Three is the minimum, but with four you can sort of downgrade to it just being a D-pad, like up,

down, left, right, and that would have been a nice sort of way to make it ensure it worked reliably,

at least. But it looks like we didn't need it, so that was great. Okay, so that was the SAOs,

But the conference was about all the talks and at Supercon there's two stages. There's the main stage that's in the LA College of Music

That's the larger stage and there's a smaller stage that's in the design lab and the way that

Hackaday does it is they live stream the larger stages talks immediately and then a few months later the design lab talks come up

so so Paul you were able to see some of the

The main stage talks on the YouTube stream. What were some of you what were some of your favorites?

There were a couple that I really enjoyed. I think one of my favorites was the one that was with Jorvon Moss and Shawn Hymel,

talking about Digit, the little robot that Adjei created. The talk was a collaborative project between the two of them, and what they did was,

Adjei built this robot that sits on his shoulder, and I'll see if I can get a picture of it, and it's a wearable, and he's got some requirements.

It's got to be good and comfy with a unique design and the ability to be upgraded.

and he wanted to integrate chat GPT this time so he could have a conversation with Digit.

But that didn't work because there's no internet connection. If you're out and about, you don't have a reliable connection for that.

The Raspberry Pi didn't work as the large language model wouldn't fit on that.

They did end up using a large language model from Meta called the Lama38B. That fit. It was still about a 30 to 60 second wait for an answer when talking to the large language model.

So they decided to rip the Pi out and they replaced it with an NVIDIA Jetson Aura Nano,

which worked, but it's a lot more expensive than a Pi at around $500.

Shawn explains how the wake word detection works with the large language model in a Docker

container and the text-to-speech is in a separate Docker container, both on the Nano device.

And then working on prompt engineering, meaning it gives the robot personality.

Odd Jay has used Southern and Passive Aggressive prompt engineering. So it'll say things like, "Bless your heart," which is usually not used in a nice way down South. So that's a perfect Passive Aggressive Southern prompt to go with it.

That's hilarious.

The talk and the demo were great. They played off of each other. So I highly recommend checking out the video. You want to see Digit in action. They ask it to tell a joke. And I'll link to Shawn's repository in GitHub with some of the code for it as well.

Yeah, I really like trying to push the whole machine learning large language model stuff

to the edge running on devices that you have around your person as opposed to going to

the cloud because then you'll know it'll work even when your internet's down.

Right, and one of the things I did appreciate is that they called it a large language model.

They did not use the word AI, which just drives me crazy.

So it was pretty cool to see a good, interesting use for a large language model.

What was one of your favorite talks that you saw?

For this podcast, I'm focusing mostly on the Design Lab stage talks, just because you won't

hear about them until another couple of months, hopefully sooner. But for me, it's the Circuit

Graver by Zach Frieden. And there's a post on Hackaday about it already that we'll have

in the show notes. It's essentially a computer-controlled drag knife that can cut through copper-clad

boards. And I don't know if you've ever seen these little computer-controlled drag knives,

like the the cry cut I think but you you can use it to make custom vinyl stickers

where you put in like a sticker sheet and you upload a vector art piece and it'll

like cut out the sticker for you it's really cool yeah my wife has a silhouette

and my laptop is covered in vinyl stickers that I've had her make me

perfect perfect yeah and so and so it's a really it's really fun to watch because

it's like a little exacto knife on a swivel that and the little head moves

around and the knife sort of follows the head and cuts out the sticker and so

So it's super simple in some ways, but it's like, you know, just an incredible bit of

a little amazing engineering.

But it can only cut through paper.

And Zach has been working on making a thing that will cut through copper.

And this required like a lot of downforce.

And it's basically like, it's called the Circuit Graver because graver, graving is an action

that like jewelers do and stuff to like sort of cut out designs from a piece of metal.

He designed this whole custom CNC system that is a, that is this drag knife thing.

And the cool thing about it is that the result looks a lot like a CNC milled PCB, but it's

much faster.

Because the CNC bit normally has to travel and kind of grind away the copper as it moves,

whereas this one is just kind of like shaving off the copper.

So it's really fun to watch.

So Zach's a friend, I've known him for like almost 10 years I think, and he's been making

crazy circuits by just carving copper by hand forever.

would just take a piece of copper clad board and just carve out places where he doesn't want the circuit to be.

That's crazy.

Solder down parts and do these incredibly tiny things.

And now he's got a computer, a computer can do it.

It's just, it's just incredible.

So hopefully the video will come out and so we'll have a follow up in some future episode.

We'll all say, go watch this talk.

So what's your second cool thing you saw in the Hackaday livestream?

One of the ones that grabbed my eye because it had the word 3D printing in the title was Solving the Last Mile with 3D Printed Packaging by Christina Cyr.

Christina is the CEO of Detour and created the Circle Phone.

She's got a background as an electrical engineer.

And I got to learn a new word, which is called Dunnage, which is the packaging that comes inside a box when you buy a product.

So think about the tissue paper, the plastic bags, peanuts, bubble wrap, or molded, folded cardboard like smartphones have today.

So what she wanted to do with her Circle phone was figure out how can you use a 3D printer to create that packaging inside?

And there were a number of challenges.

The first one is that typical CAD software isn't used for designing packaging.

There are two specialty programs that do CAD design for packaging called RTL's CAD and Casemake.

But you can't just scale your product design to allow for packaging.

One of the materials she tried to print with was TPU and soft TPU didn't work at all.

She tried both in a bamboo and an aprusa, but could print it on a Creality.

One of the lessons she learned is that she could have shipped with bubble wrap

that is made from 80% recycled nylon and is stronger than regular bubble wrap.

But still, all the learnings that she shared around creating that dunnage

were pretty cool. It's stuff that I've never thought about.

And when you open a box, especially, you know, everyone uses Apple as an example.

You open that Apple box and everything is laid out in different layers, right?

That first layer, there's your there's your laptop.

and then you lift that out and below that is the power supply kind of a deal.

The thought and design that has to go into just that.

Everyone's always focused on product design, but packaging design in and of itself

is an art form, it seems like.

It's fascinating that she mentioned that like there isn't really a CAD program

for enclosure design, for I mean, for packaging design, because like when

for the things that I've done with Thingamodel company,

we pretty much just give a Illustrator file PDF

that is the sort of unwrapped version of the box that with colors that indicate, oh, this is a fold line.

This is a cut line.

And then you have to like, talk to the person who is like the enclosure engineer, uh, that actually writes whatever custom software they use to, to do the packaging to like tell them to walk them through how the box goes together.

And it's just like, yeah, okay.

I, I guess I would not use Fusion 360 or Onshape for this.

Right.

What would I use?

[LAUGHS]

So it's just interesting, all the thought that really

needs to go in, and especially when you have something

like a phone that's got a bunch of different cables that go

with it.

You've got your 3.5 millimeter headphone.

This phone in particular had USB-C and micro USB.

So laying that all out and forming that packaging around it

was pretty cool to hear how she brought that to market.

Yeah.

Tod, what's the next one that you saw that you liked?

All right, so this is a pretty quick one.

There's a talk called "In Living Color, A New World of Full-Color PCBs" by Joe Long. Joe runs Hackerboxes, a monthly subscription service that has cool little PCB-based nerd toys. He's been doing PCB art type things for a while because all of his PCBs look really interesting. And he's jumped in early on the full-color PCB services that both JLCPCB and PCBWay offer.

I've been assuming to look into this myself, but like, there's this level of doing things that's different that I just haven't gotten over into.

He went into his past attempts at doing full color stuff, which he did with stickers. Using like a Cricut or similar vinyl cutter, he would cut out stickers and register them on the PCBs, put them down, and that looks pretty good, you know? [laughs]

But it's like a lot of work because you have to, you know, do hand accurate stickering onto things. [laughs]

And so nowadays you can just upload a file to these PCB services when you're getting your PCB made.

And so he walks through how to do that. And each company has a different way of doing it, but it looks pretty approachable.

So like maybe in the near future you'll see a color PCB from me at some point.

Oh, exciting.

All right. And so for our final talk, let's talk about the craziest talk that was at the Supercon.

Paul, why don't you talk about it first? Yeah, this one was way over my head and I'm just going to

put that out there. And I took copious notes. I felt like I was almost in school, but the whole

time I'm going, "You can do that with a microcontroller?" So the name of the talk was

"Microcontrollers are Just Radios in Disguise" by Charles Lohr. And what he did is walk through how

he took a microcontroller without a radio to get it to broadcast. So he has a few rules to his

hardware hacking. The one to take away is using a microcontroller to do what the original chip

designers expect to be impossible. So that's his goal. So he's a fan of the ATtiny85 and he figured

out how to use it to transmit radio signals just using GPIO. There's no radio, there's no wi-fi,

there's nothing built into this. So he's got a toolbox. He cannot use the built-in radios like

I mentioned. So the tools that he does have available are a digitally controlled oscillator,

frequency modulation, dithering, PWM for output, or harmonic output. So he was able to do it

using all of that. And then, even crazier than just radio signals, he wanted to transmit NTSC

video using these same tools, which is much more complicated than just sending FM. So he moved to

an ESP8266, but he's not using the Wi-Fi that's built in. That was the hilarious, most hilarious

part. Exactly. So there's no PWM in the challenge but it does have I2S used for audio so it can

playback bit streams and broadcasting NTSC and black and white video just worked. The challenge

was to get color working and using a simulator he figured out that the NTSC harmonics and reflections

that allowed it. So he reverse engineered all this stuff so he can take a microcontroller using the

the GPIO that broadcasts a signal to your old television that it can actually see. Then the next thing that he talked about was could they transmit

LoRa on a microcontroller without a LoRa radio. LoRa stands for long range. It sends radio packets at 900 megahertz. So he first tried out on an ESP32-S2. That didn't work. Two chips did. The CH32V203 and an ESP8266, not using the radio again, but using PWM.

He wrote his own entire LoRa stack to work with LoRaWAN and figured out how to send packets

up to a half a kilometer away without a LoRa radio built in.

Just crazy.

Now, the transmitting is the easy part.

Could he figure out how to receive and figure out the timing?

So he used the CH32V003 chip, which is only 10 cents, and he figured it out and had to

figure out why it was working and why it was so weak.

he could pick up the signal at 500 feet without any radio hardware. And he ended up using

the CH32V203 to create the receiver as it was slightly faster and needed for tuning

the AM frequency. I recommend checking out this talk. I'm not doing it justice because

half the technical jargon that was used was way over my head. But you could tell that

the crowd was really into it and jaws were just hitting the floor at what he was able

to do.

who has used the ATtiny85 since 2005, it just boggles my mind. You think of like, "Oh, radios

must be a special thing. They must have a bunch of special components and have an antenna." But

no, it turns out, what is a radio signal but just a wiggle on an electrical line before the electrical

line becomes just the antenna. So what can microcontrollers do? They can wiggle the voltages

on their GPIO lines and and they run at like several megahertz. So I can twiddle the GPIO line

at several megahertz. That's cool. Okay, so I can I can see how I can do a several hundred kilohertz

AM radio station with an ATtiny, say, but he's doing these signals that are up into the hundreds

of megahertz range in the case of Laura because he's using the fact that when you wiggle a signal

at like say 10 megahertz it's actually creating all these harmonics at higher frequencies above

that because of just how how signals work like anytime you make you make one signal you're

actually making a bunch of signals because square waves have in them a bunch of sine waves that's

That's called Fourier analysis, which I used to know a long time ago.

And so, yeah, he's not outputting very much power, but it turns out,

Laura is designed for not very much power, so he can use the super low,

900 megahertz harmonic of whatever real signal he's generating.

It just makes no sense. So, yeah, please go watch this video.

Even if you don't understand it, it's an amazing ride.

All of the videos that I talked about are live on YouTube.

And we've got links in the show notes to them.

And as Tod mentioned, the talks that he mentioned

will be up in a few months.

So keep an eye out on the Hackaday YouTube channel

for those.

Wrapping up, let's go back to the simple add-ons.

They have about a 90-minute video.

It was pretty long.

I skipped through it.

That actually is the award ceremony

for the different simple add-ons.

So I just wanted to call out a couple that I saw that I thought

were pretty cool that were part of the award ceremony.

The first one was an Etch-a-Sketch SAO, a tiny little,

like you said, these are two inch,

these aren't big PCBs or products that they're building.

And he's got a full-blown Etch-a-Sketch working on it.

The one that won best overall was a digital multimeter

that's working built into the badge.

- It's so nice.

And it looks like a Fluke multimeter

with like the yellow case and with probes.

- One of my favorites, though it was ineligible

due to using last year's badge, was Instant Arcade's Pac-Man SAO.

And the way it worked is it had a little circular screen

where you could actually play Pac-Man.

And oh, on top of the SAO were a Pac-Man and four ghosts.

So that's on the top.

And then it's connected to the little circular piece

where you actually play the game.

And when you eat a power pill,

the colors of the ghosts actually change.

So you can see the state that they're in

based on the game state.

That just cracked me up.

- He showed an early version of that,

that polar orientation Pac-Man last year,

because that was last year's badge

that had the round display on it.

So having a round Pac-Man seemed appropriate.

- Steven, a Simon clone was shown, which used your SAO,

which I thought was kind of cool.

And the two that I wish I could have seen,

and I heard about that, that someone had like a turntable SAO

and me being such a big vinyl music lover.

I'm curious to learn more about that one.

And then one that I actually saw a couple months ago when it was in development, not realizing what it was for, was someone created a Marvel X-Men SAO.

And you have to see Wolverine and how they created the PCB with Wolverine's claws.

And that's how I came across it. He was talking about it on social media originally.

But it's one that I wanted to see the final product that I thought was pretty cool.

Yeah, I saw that post too, but I didn't see it in real life. I think I just didn't run into the person who had made it.

I did see the the turntable SEO. It's it's a there's a link. They'll be linked to it in the show notes

It's called the record scratch SEO by Simon Sorensen looks like a little record you can scrub your hand

You're sorry scrub your finger along the record and it'll make scritch-a-scritching noises and then we let up it'll it'll play the record because

Underneath in on the other side is a full like rp2040 Pico like system that has

100 and a flash memory to store a sample and some clever code to do the audio scrubbing of course the top is a

Is a cap touch wheel kind of like my kind of like my wheel and so yeah, it's just it works really well

I have one one of one of my favorite ones

That also was a cap touch on the front and an awful rp-2042 in the back was the TARS

SAO by Dave Darko it looked like the TARS robot from interstellar Dave makes a ton of SAOs

He's like a really good SAO maker to crib from if you ever want to like make some of these yourself

He's got a bunch of his designs up on github and you can like learn so much just by looking at like the techniques

He used the Atari's SAO has a full color TFT display a speaker the touch pads

It's driven by this wave share rp2040 zero board. So it wasn't even like a

His approach was like my approach which was like let's use a pre-existing board

You can just sort of like plug on rather than like implementing the entire circuitry again

And it comes with a bunch of different fun little apps a little piano app and a I scored C scanner

Which is really handy when you're doing SAO stuff

It's so cool to see the creative genius at work and all these different SAOs that people are working on

I I can't imagine coming up with all those different ideas and then actually bringing those projects to life

It's just it's so cool watching it from afar. Yeah, it was it was really cool

There's I think like one of the things that that I was always a little bit jealous of in past super cons is that a

Lot of people would like just dive into figuring out the badge and the badge was usually really complicated and like I didn't want to

Like avoid everybody and try to like dive into this thing and also I can't really work

Well in a big crowd of people like that during a conference, so it's like I feel like well

Geez, should I go somewhere else to figure this out or like no, I just won't work on it

I'll just like write my name is Sharpie on the badge and that'll be my hacking of the badge

And so I think a lot of people felt like that. And so having it be a very SAO-focused badge where everyone can kind of like, pre-think about their circuit and have it made and like maybe make several of them and give out to friends and stuff when they're there, it made it a lot more egalitarian, it felt like.

Well, that's Supercon 2024. I hope that you, like me, no longer have a feeling of missing out,

you've learned a little bit, and have a couple talks that you might want to go watch.

For detailed show notes and links to all of these shows, visit thebootloader.net,

and don't forget to sign up for our newsletter when you're there.

Thanks for listening, and until next time, stay positive.

