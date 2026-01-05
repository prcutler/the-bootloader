---
date: 2022-12-05
title: "Episode 6 Transcript"
linkTitle: "Episode 6 Transcript"
description: "Episode 6 Transcript - Supersized for Supercon"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---

Tod Kurt  0:03  
Welcome to The Bootloader. I'm Tod Kurt.

Paul Cutler  0:05  
And I'm Paul Cutler. Today we have a special supersized edition of the bootloader for you. Rather than covering a number of topics for five minutes, Tod just got back from Supercon in I've been peppering him with questions about it. So I thought we'd bring some of those questions to the show for those of us like me who couldn't be at Supercon. So with that, Tod, tell us what is super kind of where's it held?

Tod Kurt  0:26  
So Supercon is the is the long long name is the Hackaday super conference. hackaday.com is a blog that's been around for like 15 years originally started, I think by Phil Torrone now of Adafruit. Its whole purpose was to showcase interesting, cool hardware hacks that are happening in the community. You know, back in the old days, it was maybe only once a day, but now there's like tons of content. So if you ever want to like learn how to do cool hardware, hacking things from like, simple stuff, to really complicated things, Hackaday is a really good resource for that. I've learned so much just by reading the website. And so super con is a way of getting a lot of people that do a lot of the stuff together, like, hey, let's have a conference of all these cool hacking projects. And this has been, I think, maybe this is like the eighth year or something. It's been going on for a while. And it's been held mostly in Pasadena, California, which is just outside of Los Angeles, there's a reason why it's there is because supply frame, the now owners of Hackaday, their headquarters is in Pasadena. And they've got a supply frame design lab, which is sort of a sort of like a hackerspace. But it's more like a design studio with really good tools like laser cutters and CNC mills and resin printers and a bunch of other really interesting stuff. And so it's held there and next door with there's this LA College of Music has a really big, nice big stage with really good lighting and stuff. And so there's like the main stage, the LA College of Music, this little literally right next door. And in the Design Lab, that's sort of the second smaller stage. And they have talks going on concurrently. And both of those, and then in between in the alley, there is a bunch of tables set up, where probably like 100, people can just unlock a bunch of soldering irons and like parts sponsored by Digi key, we're going to start go and start hardware hacking your your things. And so a lot of people will bring their projects that are like in a mostly finished state. And they'll go there and they'll be hacking on things. There's also batch hacking, which we'll talk about in a second.

Paul Cutler  2:15  
That's so cool. I had no I had no idea that they actually had soldering irons on site right there where you can actually start hacking on your hardware. 

Tod Kurt  2:22  
Yeah, it's amazing. And people will bring bring stuff like this year, I saw a fully functioning Apple two plus, I saw some weird CPM computer with full CRT monitor, there's just like some really weird ancient stuff that people will somehow just cart to the conference and just set up on these tables. And then the start soldering onto it. You know, some people were setting up your rack, little synthesizers they were making by themselves and they implemented they integrated the badge into the Eurorack system, somehow it was, it was just crazy. And these people are overall, much better engineers than me, I would say. So it's really interesting to see a lot of the stuff stuff people are doing. There's like super high density, surface mount soldering going on that like people bring microscopes. So they can like look at the surface mount soldering. It's just, it's just insane.

Paul Cutler  3:15  
That's amazing. So we hinted at it. But tell me about the badge. So I think it actually started at DEF CON, where they converted badges to actually microcontrollers or circuit boards,

Tod Kurt  3:25  
I find that the fact that we're calling them badges are kind of hilarious, because as someone who loves to go to these some of these conferences, but have kind of a hard time interact with people, I really liked the actual badge of a conference because I can see their name, I can see their name and their face. And I could like you know, kind of get oh, and then maybe their company that has a badge of the company. So I could have this nice little package that helped me remember this person, because I'm terrible, that kind of stuff. Now, what are badges now badges are special purpose microcontroller boards that are designed for the event, they're a one time created thing, they're more of an art piece than a than a product. With a lot of these badges, you're expected to modify the badge on site. During the three days of the conferences, we DEF CON works is the way super con works. And there's other conferences that have similar things this year is bad. Looks like this will include a picture of that in the show notes. Yeah, if you're watching on the video, and we kind of have this little bit, it is a recreation in a way of the old computers from like the 70s, where you had keyboards and screens, you had DIP switches and lights. And so the way you keyed in the program is you flip the various switches that indicated the bits of the command and the bits of the data and you flip the switch the said load and that would that would change one memory address and then you would go to the next memory address and flip the flip the switches and eventually you would input like 100 or 200 instructions and then you'd flip the run switch and your program would run and the lights would would change and you'd see The output and so that's what this is. It's a it's a recreation of that it's running on a PIC microcontroller. And some people there were keying instructions on the little like switches that are on the badge by hand. But there's also a serial port. And if you go to the serial port, you can upload the via like a bootloader process, you can upload a precompiled sort of machine code thing on the event, people were writing web based compilers for this thing for in various languages and stuff. And so it's got like, like, you know, 30 bytes of RAM, it's got it's got some, some very small amount because it is a recreation of these really, like initial computers that existed back in the in the 60s and 70s.

Paul Cutler  5:36  
That's pretty cool is there one or two badges that you saw that really stood out? The cleverness

Tod Kurt  5:41  
is, so there's there's the cleverness of just hacking the badge, sorry, of just programming the badge. Like just to be able to do that, like I wasn't able to actually really get into the programming because, you know, I did, I did the sort of machine language stuff when I was first learning computers on an Apple two, I don't really want to do that and don't do that anymore. Not a nostalgia for to it for me, but just people doing some amazing like, I think someone had like a fractal render written in this machine code. But like the one of the best ones that I think it won the badge hacking contest that happens at the end of the event was Zach, and I forget who too long time Hackaday member Hackaday community members made a punch card reader for as a way to input programs into the into the badge. And instead of using like extra components to actually unsoldered some of the LEDs that were on one badge to turn the LEDs into sensors. Because LEDs, LEDs work both ways. They both can emit light and the consensus light. So they had the sandwich of of a row of LEDs on one side and a row of LEDs a sensors on the other side. And if you fed paper in between, then you could read the dots or gaps or whatever in the in the punch card feeding through. And so people were writing programs on the punch cards to submit to them, so they could run it through their system to load onto their badge.

Paul Cutler  7:00  
That's amazing. So you came for the talks, and the talks that are on the main stage have been released to YouTube or most of them. So we'll link to the ones that we talked about.

Tod Kurt  7:09  
So they they recorded. So there there's two tracks of talks happening simultaneously. And the one they're both being recorded, the ones in the bigger stage are streamed live to YouTube. So if you can't make it to Supercon, next time, I would say try to watch the streams live because they're, it's a really good, they've got a really good AV setup, they've got multiple camera angles, they've got a switcher that's switching between the slides of the presenter, and that way you can kind of participate on social media with people if you can't make it because, you know, really, the only reason why I made it is because I also live in Pasadena. Sure. But but they did record all the ones. And so there was a really good ones in the Design Lab stage, a smaller stage, but those weren't streamed though, I think they will release those in a maybe a month or two. So watch for them as they kind of clean up and make a whole package of all the videos and I think that's that's going to come out at some point soon.

Paul Cutler  8:01  
So as we were preparing for the show, I was watching some of the videos and that there was one thing I learned was don't judge a book by the cover a couple of the videos that I would not have watched because of the title that because I just personally didn't find it interesting. You recommended and I found them to be the best ones of the bunch. So let's start with the first one. Let's talk about the DIY vacuum tubes from Nick.

Tod Kurt  8:22  
So Nick Poole is a he was like one of the most cyberpunk looking fellows. I know he's got these these awesome, like dark black Angular tattoos on his face and arms. It just looks amazing. And he's got these these cool jackets and clothes that he wears that just makes him look something like something out of a out of a movie. It's it's just amazing. He's a really nice guy. He does sort of like design, like like inventor experimentation at SparkFun. I think like he creates some of the new cutting edge stuff that SparkFun does. But he wanted to like I think he was playing around a whimsically wanting to like imagine a world where we humans missed the boat on semiconductors and started miniaturizing vacuum tubes. And so imagine this world sort of like maybe like in the Fallout universe where we have these surface mount vacuum tubes, and we've got because of a vacuum tube computers that are small and fit on a on your wrist or something. And so he's like, Well, what's the smallest vacuum tube I can make? And can I a normal human make vacuum tubes. And so in this whole sort of journey of what does it take to make vacuum tubes? Turns out, it's hard. It's not just pulling a vacuum and putting the glass envelope around it. There's a bunch of stuff going on and so, so he made a vacuum tube, a little tiny one, and it has little Hackaday logo inside. It's just beautiful.

Paul Cutler  9:42  
His journey was pretty amazing. He reached out to a number of commercial companies who wanted to sell him, you know, lots of 1000s of pieces is just trying to build a couple right. But he was able to get samples and you know, it was a really interesting story as as, as he went along on that journey

Tod Kurt  10:00  
One of the most interesting things is that there's some sort of chemical that you put inside the vacuum tube. And when you like energize it or heat it up, that chemical vaporizes and plates onto the electrodes to make them appropriately doped to be the cathode and anode are something I didn't fully, fully understand it because vacuum tubes man, there's like this whole level of engineering and physics that we don't really think about much anymore, because that was 50 years ago.

Paul Cutler  10:31  
So let's talk about electric scooters, which was another kind of a journey talk or presentation that was given that I found fascinating.

Tod Kurt  10:38  
Bradley growth he's on he's on social media is a tall, dark, and we really think he works with Shaw and conservative by doing like these really interesting environmental sensing platforms that can go out into the rough and tumble world. And since the world in various chemical and environmental waste, he also is a real big fan of personal electric vehicles or Utrecht scooters, it's it's a really interesting journey through the fact that, oh, there's a lot of bad actors, like the bird scooter company, and things that are just like taking this interesting idea of a small electric scooter and polluting our environment with him. Just just tripping, like if you walk down a modern city nowadays, you have to trip over these dang scooters that have been abandoned. But there's all this open source efforts to make them usable by normal people not locked into any one corporation. And there's a single person he he talked about that is making open source firmware for these electronic speed controls and all the various critical electronics to control and deal with the charge of the scooter. And he ended his talk with one of the best sort of call to actions of, you know, like this guy doing this open source control, or in keeping keeping us or we're not locked in to this world of bird is making a difference. And every one of us in the audience, watching that video can make a difference if we just care about one thing enough to like, you know, to work on it. So it was very inspirational. It's.

Paul Cutler  12:07  
And that was his message was find a community, join it and start a fight as he put it, right. He didn't mean a literal fight. But he's like, get engaged. And yes, it's a great talk. If you do watch it stick to the end. So you can see that piece. You'll learn a lot about personal electric vehicles, a lot of stuff I didn't know. But you're right. That end was just a kicker. It was great.

Tod Kurt  12:28  
Yeah, I've I've never been interested much in scooters. But I do find the the study of them interesting, because it's this type of electronics. It's like high current electronics that I never deal with, like all the the chunks I deal with. They're like in the orders of 10s of milliamps. And here's like, you have to deal with potentially 50 100 million milliamps on these scooters, or just any electric vehicle. And it's just it's just a different way of thinking about electronics, which I find really fascinating. And then on top of it, his call to action.

Paul Cutler  12:59  
The next one I wanted to ask you about was Sammys random walk exploration. So I watched the video on this one as well. And he starts off, I'll let you tell the story. But he starts off in one place and ends in another and it's just a great story. It's just this delightful

Tod Kurt  13:15  
effect he ended up creating at the conference, if you're just running to Sammy, it looked like he was wearing this sort of crystal pendant around his neck. But he would sort of surreptitiously flip a switch. And suddenly that crystal pendant would start to glow with a sort of neon like glow. And you'd ask him what is that he's like, it's my breath. It's in this and what that was is a a super thin flexible tesla coil that his that is under his shirt. So it's probably something you shouldn't wear if you're if you have a pacemaker. And then that the crystal little like pendant isn't is actually a glass and fuel that's holding that is holding is a little evacuated chamber, sort of like a vacuum tube that is holding his breath. And that's sitting on top of the tesla coil and you know, Tesla coils can ignite neon tubes. So it's basically acting like a little neon tube. The semis got an amazing curiosity about the world. And he just was like, going through and learning about stuff and came across, like came onto this very beautiful piece of art. Yeah, he

Paul Cutler  14:21  
shared his journey starting with a big vacuum pump everything from you know, making ice cream and it's in a vacuum because Right, right the pressure and the temperature. He talks about how he, how he was looking for people who could train them in some of the glassblowing techniques. I believe it was, yes, yeah. And travels to Milwaukee. And just based on an email when he finally found someone shows up at her house knocks on the door. She's not there. He's like I've already paid Peter for the training. I have a plane ticket to Milwaukee, Wisconsin in the middle of winter where it's freezing and she's not there. So he calls her Of course she transposed to the numbers. she's, you know, 10 houses down this demonstrate. But it was it was engaging, it was great. And it was really interesting, like you said his curiosity of how he went from project to project to project to get to that end result that, you know, first ever wearable tesla coil was pretty cool.

Tod Kurt  15:14  
Yeah, the challenge both both at Sammy and Nick had of how do you pull a vacuum of a volume of stuff something it's, you get these vacuum pumps, you might see those will take you down to like maybe 1/10 or 100 atmospheric pressure. But if you need something that's like really a vacuum, that's hard, you get these really weird pumps that can kill themselves if you have a little bit of tiny impurities in the air that's running through them. And so it's a level of technique and technology that is just amazing.

Paul Cutler  15:45  
The last one, I wanted to ask you about the videos not out yet because it was on the Design Lab stage. But tell me about Chris combs talk.

Tod Kurt  15:51  
So Chris combs is a artist who makes Blinky art things. It's like really refined versions of things that you've seen a lot of people do. But it's it actually, he's actually thinking about it from an artistic point of view. And he's in dialogue with a lot of the other artists and he has taken the time to actually figure out how do you integrate this kind of technical art into normal art museums or art galleries. And so he's worked with these galleries, trying to get them to understand trying to figure out that like, Oh, this is a thing that needs to be plugged in, you know, the pictures on a wall. So don't have you don't have power requirements. But his his talk was, was really about you know how to sell your art, like, if you a lot of us make cool little things, and we want to like maybe maybe this would be useful just show off to people in an artistic way, it was also really nice to have this talk to a lot of people who might not consider the things they are making art. It's like, but we all create all this stuff all the time. And so you know, what, why don't you think of this as art, you know, you just have to kind of recontextualize some of your creations and start to talk to other people who are doing similar things. And then it's art, you know, and but a lot of galleries don't quite know how to do this sort of stuff yet. And it's hard. And so so he he had like this nice sort of how to guide on most of like, what to do, how to look for the galleries, there are minimal how to talk to them, when when you find places how to not give up how to, like present your pieces so that they are actually people that actually want to bring them in on an unknown gallery and me and like how much to charge for them. You know, how many do you want to make of a thing? Do you want to make just one of the thing? Or maybe you know, it's probably actually better if you make like, say 20 of a thing? Because then it because then it's a limited series, you know, people like limited series, they're able to say, Oh, look, I'm I'm four of 20. So it was really nice, because because a lot of the a lot of my cohort, I feel are have art tendencies. But there's no real path like who do you talk to, you can't just like, go to the Getty Art Museum and say, Hey, hang my Blinky thing on the wall.

Paul Cutler  17:58  
Right? This is our to

Tod Kurt  18:01  
do but he presents a way that you can start the process of getting, if you want to express yourself more publicly, I found that really nice, especially for the for the crowd, that the super con is. That's

Paul Cutler  18:13  
great. And speaking of the crowd, this was the first time since 2019. And the pandemic started that the that SuperCam was in person. How was it to be back in person at a conference like that?

Tod Kurt  18:23  
It was really nice, but I am so out of practice being amongst crowds of people. It was it was very strange, because a lot of these people I see only on the internet, I see only via video calls. I don't I just chats on social media. I don't really see them in real life except during these these types of conferences. And so it was very strange, because some of these people I had not seen since 2019. And it was and because the last time I saw them wasn't super con. It was almost as if nothing had happened in the last three years. It's like, hey, it's nice to see you again. You know, I just saw you last week. Well, I mean, not last week, but you know, last week for your three years

Paul Cutler  18:59  
ago. That's pretty cool that you can just pick up from where you were. Yeah.

Tod Kurt  19:02  
But it was super exhausting for me, because I'm just not used to I'm always tired out by by lots of people and Ted, like have gone for like three years not really being around people. And then suddenly, people,

Paul Cutler  19:14  
I bet. Well, thanks for taking the time to share how Supercon went.

Tod Kurt  19:18  
Thanks. Yeah, it's really great. I recommend anybody or everybody who's interested in this kind of stuff. Go to the academic comm site. Look for Supercon links. We'll have a bunch in our show notes about the stuff you've been talking about. And when the videos come out, watch them. They're almost all like super, super useful and super fun. Yeah,

Paul Cutler  19:36  
they did a great job picking out speakers. Great. Well, we'll each leave you with one other news item this episode. My first one is Python in the browser. So if you think back to PyCon back this past April, the CEO of Anaconda Peter Wang announced pi script in PI script allows you to run Python in the browser using PI iodide. Pi iodide takes C Python and compiles it down to a web assembly. So you can use it as in a browser. The challenge is, is that's about an 11 meg download. Right? We complain about large JavaScript downloads today. Well, 11, Meg's isn't gonna fly. What's pretty cool is they were able to replace C Python with micro Python and get that down to 300k, which is way smaller than a lot of JavaScript libraries. py script is a framework that you build on top of pi iodide. And now you just use the target of micro Python instead. And now you can use Python right there in the browser, no JavaScript needed. I'm pretty excited about it. I use Python on the server side for a couple of my websites. But now you'll be able to reuse code. In my personal opinion pythons a little easier to learn than JavaScript. And imagine that we can do that and how we can enable the education system using you know, cheaper computers, or if it's in a web browser, you can use mobile devices, it's you know, the possibilities are endless. Now, with that said, there's a lot of excitement, you can see my excitement, but it's still really, really early. Everything I've read talks about that. And there's a great podcast this week, listen to the talk Python podcast with Michael Kennedy. He's got guests, including Brett cannon, Fabio plugger. And Nicholas taller Bay, who was on the circuit Python show earlier this year was was a fantastic guest. But they go into the technical details of it. So if you want to learn more, listen to that. And sometime in the next year or two, I'm excited to see what pi script is gonna really look like in a browser.

Tod Kurt  21:27  
Yeah, it's so crazy to you look at some of the postscript examples. And it's like, oh, it's during the year sort of like basic sort of here's how to do some initial little little web, like dynamic web things, either view source, and that's like your standard web you things of like linking to CSS and HTML body, and then the PI script tag, and then Python,

Paul Cutler  21:47  
a pure Python I'm where it really gets exciting if you think about it, not just education. But if you can include the data science tools like NumPy and SCI pi, yeah, right in a browser where you can just show and manipulate them that could be pretty exciting. What is your last item for us today?

Tod Kurt  22:02  
It's a Tod-tastic episode this this episode.

Paul Cutler  22:06  
Didn't have it any other way.

Tod Kurt  22:08  
I guess in August, I made this little gizmo called the PICO step seek, which is a tiny MIDI step sequencer. Using these eight levers switches that have built in LEDs that are they're very popular on synthesizers and drum machines and 1980s Adafruit, I just started carrying them. And two weeks before circuit Python day, I was like, I'm gonna see if I can build a sequencer using these switches and a Raspberry Pi Pico and a little OLED display and a rotary encoder, and I'm gonna like design the PCB get it fam to write the firmware in circuit Python and design a little 3d printed case for it that looks very at style. And I did it I was kind of surprised it all it all just kind of fell together, I didn't make any major mistakes on the PCB. And the circuit was pretty simple. So it was there's a few things to mess up on the circuit Python was really quick to implement the ideas even though the timing for doing MIDI is a little, a little loose in circuit Python, because there's no way of doing like things on a specific clock. But it worked. The description of hold of that is now an article in The Magpie magazine which is the sort of official magazine of the Raspberry Pi foundation and so it's both on their website and in their print version. I'm very excited I was trying to find how have we get a version of this this magazine in the in California like is there a way and I I couldn't find a way so I ordered one from their website in England I'll be getting at some point a physical magazine all the way from the UK

Paul Cutler  23:39  
to I get to tease you that they called you an expert in micro Python and that circuit Python

Tod Kurt  23:44  
Yeah, it's it's it has hilarious because I know so little about micro Python because they're they're actually quite different if anyone has not played with either. There's a lot of overlap. But yeah, there's there's enough difference that it's hard to know sometimes what's going on. It's like check

Paul Cutler  23:58  
out the magpie you can read the article online. Also check out John parks workshop, the November 30 episode where he demoed one radon video so you can see it in here.

Tod Kurt  24:09  
Yeah, we'll have that we'll have that link in the show notes to jump mark is another call up because it was his little demo of the steps switches, that levers switches that made me go hmm, I wonder if I can make a sequencer so it was like like a week previous? It was his what does he call it? John parks pic of the Week show that made me go haha.

Paul Cutler  24:30  
Gotta get your inspiration from anywhere you can.

Tod Kurt  24:32  
That's right. But Oh, also, the magpie magazine is totally free as a PDF download. If you want to get the print version in PDF form, you can donate to them because they are finishing one. But

Paul Cutler  24:43  
yeah, I recommend it. Well, that's that's our show. It was very Tod tastic. Thanks for listening. can follow us on Twitter at the bootloader or look for us on mastodon. You can find Tod there and I'm there as well. Until next time, stay positive

Transcribed by https://otter.ai
