---
date: 2024-06-03
title: "Episode 9 Transcript"
linkTitle: "Episode 9 Transcript"
description: "Episode 9 Transcript - Beautiful Bezier Curves"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
Welcome to the Bootloader.

I'm Tod Kurt.

And I'm Paul Cutler.

This is episode 9 and the show works like this.

Tod and I have each brought three things to share.

We'll chat about each for a few minutes but no more than five.

If you want to learn more visit the detailed show notes at thebootloader.net.

Tod what's your first one?

Alright so I'm gonna start it off really nerdy.

You know I like the little tiny microcontroller boards that do various fun things and I just discovered one a couple weeks ago called the M5 Stack Cardputer.

Like computer but card.

It's about the size of a deck of playing cards and it's got an ESP32-S3 chip in it which means it does Wi-Fi and Bluetooth.

It's got a little screen a little keyboard and it's all in a little case.

So it's almost like a little consumer electronics product.

It's pretty well designed our industrial design wise but it's got a full QWERTY keyboard in something the size of a deck of cards.

So the buttons are very small especially for my big old meat meaty mitts but they work.

And so it's it's it's a pretty useful little device just right there just with those features just with the screen keyboard and having Wi-Fi and Bluetooth.

But it's also got a microphone and an I2S amplifier to a speaker.

It's got a microSD slot.

It's got infrared I think both to receive and send.

And then it's also got a 1400 milliamp hour battery so it can just be this like you know portable thing you can have in your bag to play with all the time.

And on top of all this it's only $30.

So I got a couple couple weeks ago been playing around with it.

The little app that comes with it is actually remarkably full featured.

It's like a little almost tiny little OS you to choose from different little apps.

There's a pretend your Bluetooth keyboard pretend your Wi-Fi keyboard.

There's you know scan your Wi-Fi.

There's a full Python REPL.

You can just like start and then start doing MicroPython.

A bunch of other stuff and of course that all that code is available so you can download and look at it and everything else.

But because it's ESP32-S3 it works with all the other software that we've been using in Arduino and CircuitPython all these years.

Like there's a CircuitPython build for it which you can just run it and it sets up the display and all the keys and stuff for you.

So you can just like start going or going doing CircuitPython stuff with it.

While it is a Chinese based company M5Stack makes all these interesting little sort of pluggable computer things.

They're sort of like the QDPI in size but they have a much higher density pinout because they're made to be plugged into into PCBs rather than plugged into a breadboard.

But you can get them shipped from the US from electromaker.io.

And so I got a couple I've been playing around with them.

I'm a big fan of the ESP32-S3 chipset because it can do Wi-Fi and it's very fast.

It's good for doing synthesizer stuff.

So I've been doing a little synthesizer experiments on it because hey it's got that speaker output that's hooked up to an I2S audio DAC.

And yeah it's a I think if someone wants to have something to play with that's really tiny and you can just kind of kind of you know hide it in your bag.

I say it's a good $30 well spent.

I've been following along with some of the pull requests to get that up and running with CircuitPython.

I didn't realize it was only 30 bucks.

Yeah.

That's amazing how much functionality comes for that price.

Yeah I mean especially because it's got this full multi-piece injection molded enclosure with a bunch of buttons and stuff.

It's like you know just the injection molding of that is pretty expensive and so they it seems like they approached it as almost a consumer product.

Like how much consumer productness can we fit with a retail price of $30 and using ESP32 and they just went from there.

What comes pre-loaded on it?

Is it MicroPython?

It's an Arduino sketch.

I think that somehow is embedding MicroPython.

I need to look into it more.

I unfortunately blew it away because I was playing around with CircuitPython stuff.

But on my to-do list is to read I think I found the code that came on it.

I want to like recompile it and reload it and see if I can get it and see what actually going on because it was amazing what it did.

It had these little apps and you go back back to the main app launching screen.

It's kind of surprising how good it was.

You'll have to give us an update next episode.

Yeah totally.

Alright so what's your number one for this week?

My first one is RadioFreeFedi and I'm all in on the Fediverse.

I really enjoy using Mastodon for social media, PixelFed for sharing photos usually of which records I'm playing, and then there's RadioFreeFedi.

Longtime listeners know I'm really into music and I have to give a shout out to Axwax on Mastodon for introducing me to RadioFreeFedi.

Axel if you're listening, thank you.

RadioFreeFedi is an online music stream dedicated to independent artists on the Fediverse.

It turns out there's a whole world of artists making music on the Fediverse in every genre.

If you visit RadioFreeFedi.net you will find three channels you can listen to.

The first is the main channel.

You'll hear songs from almost every genre and as the website says some of the songs will challenge you with music you may not normally listen to but it is curated and if you don't like a song another one will be on in just a few minutes.

The second channel is called Comfy which smooths out the edges for those who might want a softer experience.

This is my go-to channel in the mornings when I want something a little quieter than the main channel.

And then there's a specialty channel which hosts a block of songs around a theme which changes every hour.

They also at the top and bottom of the hour have a little spoken word section.

Sometimes this could be a poem but it's really it's a really neat feature that they break up the music with with spoken words and people can actually volunteer to read station IDs as well.

I need to work up the courage and volunteer to do that because I really enjoy RadioFreeFedi.

That sounds fun yeah.

If I was smart I would have mentioned RadioFreeFedi on the last episode because in May they host FediVision which just wrapped up.

It's a take on Eurovision where Feddy artists submit songs from fictitious countries and listeners can vote on their favorite songs.

It was really fun listening to all the entries on the special channel that RadioFreeFedi set up to stream those songs.

Going back to my shout out to Axwax who tirelessly promotes musicians on the Fediverse especially on Bandcamp Friday and Faircamp Friday.

If you haven't heard of that Bandcamp used to host Bandcamp Fridays where 100% of the music proceeds would go to the artists and none of the fees went to Bandcamp.

And it started during the pandemic as a way to help boost those artists revenue streams because they couldn't tour for example.

Yeah well Bandcamp's been sold twice in the last few years and an alternative open source solution has popped up called Faircamp.

Musicians can install Faircamp pointed at a directory of songs and it will create a static website you can host to stream the songs and it integrates with payment processors like Stripe so you can offer purchases to your listeners as well.

If you enjoy music and if you enjoy being on the Fediverse I strongly encourage you to check out RadioFreeFedi.

There's links in the show notes to some of the artists I've discovered that I like and if you like RadioFreeFedi check out their state of the station on how they're doing and how to support them.

Running an online radio station isn't cheap and if you come across an artist you like share it on the Fediverse and let others know.

That's really cool I really like the Faircamp thing because I mean it's a static site generator geared towards making playlists that you can listen to stream audio online from various websites.

That seems to be one of the places where the static site generators I've seen kind of fall down they don't really have a way of serving up mp3s or whatever and so yeah that's pretty cool.

I'm a big fan of online streaming radio stations I've been a big supporter of Soma FM but they're like more traditional like real quote unquote real musicians that have record deals and such.

I really like the "hey let's all listen to each other's stuff" because it's so nice and easy to make your own music now.

Yeah and Faircamp's really neat if you don't have cover art it's got a generative AI built in so it'll create cover art for you.

That's hilarious.

Yeah what's your next one?

All right so I build a lot of little circuits I make PCBs to house those circuits or to be the infrastructure for those circuits and for about 20 years I've used this program called Eagle to design those PCBs.

It was a okay program it's gone through multiple users sorry multiple owners over that 20 year period the latest of which is Autodesk and Autodesk initially improved it a lot but in the last several years like last four years or whatever they've kind of abandoned it and they've officially said in 2026 they're going to stop supporting Eagle at all which is frustrating because one of the last changes they made was you had to log into the Autodesk authentication servers to use the program which I assume means in 2026 I won't even be able to open up Eagle anymore.

So it's been on my to-do list to shift to this open source schematic program called KiCad or KiCad.

I think KiCad is the appropriate way to pronounce it but I always pronounce it KiCad because I'm American I guess and earlier earlier this year I finally made the jump and I decided that for my next circuit board I'm going to design it in KiCad KiCad and for every circuit board after that I'm going to try to do it in KiCad.

Looking around there's lots of instructional material on it which is on KiCad which is great but it's been around for a long time and it's been evolving and getting so much easier to use than it has than it was just a few years ago and so it's like well what which videos should you watch and also for me I'm kind of this immigrant from from Eagle like which one is more appropriate to me because I know the concepts of how to do schematics I just don't know the particulars and so I found this one really great YouTube channel called Plum Pot.

Plum Pot is a couple it's um Carrie Plumstead and JP Potgieter so Plum Pot they had this really great long playlist of YouTube videos that's how to go from installing KiCad to creating the symbols in the schematic and the footprints on the PCB and to ordering those PCBs with generating the Gerber files that the PCB house needs and while it is an older series it was done with KiCad 5 almost everything they've talked that they talk about is relevant especially some of the more advanced topics which hasn't really changed much like in the last several several versions of KiCad they have made the UI a lot easier to to work with at least to me when I like back when I tried this a couple years ago I found I found KiCad kind of weird and this is someone who has used Eagle for so many years which has the weirdest UI but but in the last several years it seems like the usability has has just gone over a hill where it's just everything is so much simpler and that's been really great so I was able to do some of the like just getting started stuff much easier than I could before but some of these tricky things I couldn't quite get going and watching the PlumPot videos really helped thank you to Kerry Plumstead and JP Pottinger for helping me get over the hump of getting into KiCad and I'm full full-time KiCad person now what's been the most challenging part of the transition from Eagle to KiCad for you so I think the main thing is in Eagle when you so in circus you have you have a part like say a a knob a potentiometer and you have two different representations of that part you have the schematic symbol that's the sort of semantic how the pot is wired up to your circuit and then you have the physical layout of that pot solder footprint which is somewhere on your PCB like physically like it's three inches over and two inches down and it's rotated 90 degrees and all that kind of stuff and in Eagle those two representations these sort of semantic schematic representation and the physical layout footprint specification are joined together and that makes it it's very it's a very logical way of thinking about it in some ways because you're like oh yeah I just want to plop down this exact pot the downside with the Eagle format is that there are literally tens of thousands of different kinds of potentiometer so you have this you have this one single symbol in the schematic but you have 10 the 10,000 different variations in your circuit board in the in the physical reality of it you know is it a horizontal potentiometer that sticks out towards kind of towards you or does it a vertical potentiometer that sticks up it is a six millimeter or nine millimeter potentiometer it's like there's all these different variations and so if Eagle you could run into the problem where you have in your schematic the choice of like well which several hundred of those did these different same looking symbols am I going to use and whereas KiCad it's totally separate you have just the potentiometer symbol that you use when you're drawing schematics and then at some point later you have to you have to go through this process of assigning the footprints where you say this part needs that exact footprint and in retrospect now that makes a lot of sense but at the time I was like how do I take my schematic and turn it into the actual PCB it was like it just seemed like it didn't make much sense to me that was like the biggest hurdle for me was getting over this binding of the schematic to the PCB footprint part problem that that Eagle kind of solves invisibly for you.

Has there been something that surprised you on how easy it was to do in KiCad?

Oh yeah the 3d visualization so when you're laying out a circuit board and you're like putting down like a switch and a knob and a display and like the some micro controller board it's kind of hard to tell how how that will actually look and so like what are the things one would do to visualize that that is one of the things I used to do is I would print out on paper a one-to-one representation of that circuit board and then I would lay parts on top of it to sort of feel kind of how the parts are interacting because because you're looking at a 2d representation just a flat sort of vector art view of what the PCB looks like but real parts have 3d height and they kind of overlap a little bit sometimes they have overhangs sometimes when you need to place a part your fingers have to go on each side of it so there needs to be room on each side of the part so your fingers can actually push the part in things like that and so it was really hard it's like okay well I'll print it out on paper and I'll lay the parts out like a little scale model or what I was doing in Eagle is I was exporting a version of it into fusion 360 which is a 3d CAD program and finding 3d representations for close enough analogs to the parts I was going to use and plopping them onto this this 3d model and then looking to the 3d model in KiCad keycad you can just press option f3 or something and it will generate a 3d model for you right there so you can just immediately go what does this look like and you just see what it looks like you go oh okay it's actually these two these parts that you close together I'll never get be able to get my fingers in between there and so you can just start nudging nudging it and so being able to just really quickly see the visual 3d representation of the board is so cool very cool anyway yeah KiCad very awesome so so Paul what's your number two my number two is André Costa and the Pico W air so continuing on that meet the maker thing I started last episode I wanted to share a cool product by André the Pico W air André is more well known for being the creator of RPI locator a website and mastodon bot that alerts you in a Raspberry Pi becomes available for sale online he was recently in magpie magazine who did a great story on him and RPI locator I'll link to that in the show notes but he's also created the Pico W air a wireless air quality monitor powered by CircuitPython and CircuitPythons HTTP server I don't think I've seen another product for sale that actually uses CircuitPythons HTTP server and for just under 13 bucks you get a custom PCB with a Pico W mounted to it with a connector for a particulate matter sensor and a quick connector for additional sensors like the recommended temperature and humidity sensor for example he also has a particulate matter sensor available as an add-on for sale on his Tindie store so you could actually bundle them both together what I think is innovative is not only does it have MQTT but it takes advantage of HTTP server just add your Wi-Fi settings in the settings that Tomo like you would do in a normal CircuitPython microcontroller find the IP of the device and you can connect to it from your phone or from another computer and you can view all the stats right there in a web browser nicely formatted so you can see it what's your air quality what's the temperature what's the humidity if you have added those sensors for example and since it works with MQTT it's easy to add to home assistant as well it also has a JSON API so you can interact with it through the API too.

I talked about the micro dot web server last episode in the fact that MicroPython has over a dozen different web servers CircuitPython has just this one and I think this is a really interesting use case for it yeah totally I really like how he supports multiple ways of looking at the data like over the net like he's got MQTT HTML and JSON API like that's like normally in these CircuitPython projects you kind of see these really stripped down examples of how to do one aspect of that but he's developed a full application that kind of offers all the things you want to have when you have something like a sensor like this exactly it's a really neat product and I'll make sure I link to his Tindie store and to follow him on Mastodon in the show notes as well 

Yeah I'm looking at it right now and it's great because the whole PCB with the Pico mounted is like basically the size of you know it fits in your hand and the look the sensor is basically the same size so it's made to go just right on top of the sensor that's great yep 

What's your next one?

This is another YouTube thing this is so there's this game designer named Freya Holmér and she makes I think I think mostly her job like her job she does for money is she designs tools and shaders for unity which is a 3d game engine and but one of the things that I mostly know her from are these beautiful YouTube videos that she makes about algorithms the reason why this came up recently is because just a day or two ago she released a talk that she gave called lerp smoothing is broken and lerp is a is the sort of gaming term for linear interpolation it's when you have it reaches it reaches destination in a smooth fashion rather than abruptly so it feels more realistic you might you might you might hear easing as a nether way of doing that but easing is more fixed in the way it approaches its destination whereas lerp is kind of responsive to the changes in the destination the reason why this perked up my ears is because the the equation for lerp is very similar to the technique I use to smooth sensor inputs like knob inputs called exponential smoothing or basically you take the last value and multiply it fractionally plus the new value of your pot reading say and you combine them together to give you a smoother thing and both of these techniques both lerp and exponential smoothing suffer from the problem of they change how they look with the frame rate changing because the way it works is you multiply a percent of the old value add it to a percent of the new value if you're reading the new for exponential smoothing if we're reading that value a lot your resulting smooth value kind of matches too quickly your red value so the filtering doesn't look as good so you kind of want to slow that down and similarly in lerp if you if your frame rate is lower the object appears to move slower because it's not being updated as frequently and so so she talks about and this video is great because it talks about some frame rate independent techniques for dealing with changeable frame rate like in in her case because she's a game person she's like well you know some people might be what playing this game at a cinematic 20 frame 24 frames per second but some person might might have a high-end gaming rig that's had 120 games 20 hundred 120 frames per second and those two people will have two very different experiences because the lerp will be essentially five times slower on the on the slower frames per second person's computer and the video before that that I was I was most enamored with was this one called the beauty of bezier curves and I don't know i'm sure everyone has has used a graphics program like illustrator and they've tried to use the bezier design tool and it's always been a little bit mystifying to me about how the heck it's supposed to work like i just want the curve to kind of look like this how am I supposed to do that with these control points or whatever and this like almost hour-long video talks about the math behind bezier curves and explains what's going on and gives you a sort of intuition as to what's happening with those control points and why why you would put them where you'd want to put them and so it's i don't know I i plus her animations she does for the for these videos are just spot on so so wonderful looking so I say put this on you might learn some things if not it's really cool to look at yeah it's on my list to watch I didn't get a chance to watch it before we recorded but it sounds really neat especially the bezier curves one because as you said that's just a mystery on how that works totally and then one last one last video is if you're doing anything in uh say CircuitPython Arduino with any type of little video game you want to make or any sort of little generative art you almost will always be using vectors you know vectors are really just two numbers like usually x comma y that you use to represent a position in space or maybe a direction in space and you usually want to combine vectors like if you're a spaceship spaceship has a velocity and when you push the go button you've got a thrust acceleration vector that needs to be added to your spaceship's velocity vector how do you do that and so there are many different ways to multiply vectors some of them give you interesting information like how close the vectors are pointing towards each other other ones would be like how to just scale a vector the other is uh how to tell like together what direction the two vectors are sort of pointing right angles to so like you if you have an x and y if you look at them in a certain way and multiplying a certain way it'll tell you which way is z which which is really handy and so she goes into this really really great discussion as to how to think about the many different ways you can multiply vectors because it's not a straightforward thing just as multiplying two numbers 

And you used it in a game i understand?

If I would have watched her video I might have been able to write my little arcade game called CircuitPython starroids um a little faster because a lot of this vector stuff i learned way back in college and kind of forgot because you know when I was doing web stuff you don't really use these sort of game vectors right.

okay paul what's your number three?

My last one is the CircuitPython online ide so as folks who use CircuitPython know there's a number of ways you can program your microcontroller and CircuitPython most folks just plug it into usb and use a text editor to do it but you can program it over bluetooth there's now the web workflow where you can do it wirelessly and there's also code.circuitpython.org where you can use a chrome based browser and program it right there in your browser River Wang has also created an online editor for CircuitPython which i've linked to in the show notes it has some really innovative features and if someone was going to ask which online editor they should use this is the one i'd pick over the one that Adafruit developed when you first load the web page it has three steps for you to connect making it super easy to understand you install CircuitPython on your microcontroller if you haven't done that already open the CIRCUITPY drive and then connect to the serial port that's it it also has a nice youtube video embedded with a quick start guide for additional help if you need it once you're connected there's a folder view on the left that lists all the files on your microcontroller that's something that code.circuitpython.org doesn't have so you can edit your settings at toeml you can edit your code.py you just double click to edit it and the file opens right there in your browser the serial console is on the right making it really easy to see if you have any errors in your code or what's going on behind the scenes a couple of things that set it apart is that it has tabs so you can have multiple files open right in your browser it has easy access to control d and control c as buttons so if you want to stop or restart the program it's just click of a button in your browser and it also has a plotter function similar to Mu though you have to add some code to make the plotter work but it has a good example to get you started I think that's pretty cool because a lot of people graduate fromMuto a text editor that no text editor that i've seen other than Mu has that plotter built in the other thing I think is just awesome is I love seeing community members create projects like this it shows the growing community around CircuitPython and you don't always have to rely on Adafruit for everything I especially like how River is driving innovation by using the browser to write your code another interesting use case might be hosting your own server I can see a classroom environment doing that especially with Mu not getting a lot of love the last couple of years there hasn't been a moo release in almost two years a couple of the bugs are starting to surface but if you're interested check out the links in the show notes to the online ide and give it a try yeah it's it's I i follow river on mastodon and i'm really impressed whenever they make up an update to it because it just keeps getting better and better.

I didn't know about the plotter function that's one of the things I really miss about the Adafruit sorry the Adafruit the Arduino ide is it's got a really good serial plotter it's kind of a hidden like special feature special uh yeah special feature of the app and sometimes I will actually open up Arduino just to run the serial plotter for a CircuitPython sketch just so I can get the really good plotter but uh but that's really troublesome because Arduino likes to sort of try to connect to the serial port when you're when you're trying to use it so it's be nice to have it all in one thing yeah 

I agree. 

Well that's our show, for detailed show notes visit thebootloader.net you can follow Tod and I on Mastodon check out thebootloader.net for links to that as well and we will see you next episode.

Stay positive!