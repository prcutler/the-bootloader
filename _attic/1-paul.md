# TBL E1 Script
## tio
The first thing I wanted to share is a about a an open source project called tio, t-i-o..  Martin Lund is the developer and I have a cool story about him, too at the end.  tio just released version 2.0 on September 11th.

I’ve been using CircuitPython for a year or two and I didn’t know about tio until John Park featured it in late July in on his show, CircuitPython Parsec.  

Tio is a modern day replacement for the old linux tool screen.  If you go to tio’s Github page, Martin share the motivation for tio:

To make a simpler serial device tool for talking with serial TTY devices with less focus on classic terminal/modem features and more focus on the needs of embedded developers and hackers.

Like most users, I used Mu to see any serial output or errors with my CircuitPython devices.  

Even Adafruit’s advanced serial guide for Mac & Linux has you use screen.

I’ve using a Unix like operating system for too many years and this is perfect for someone like me who is comfortable dropping down into a terminal.  I can run also run tio in my IDE’s terminal.   It has one killer feature - auto-reconnect.  If I unplug my microcontroller and plug it back in, tio automatically reconnects.  I don’t have to look up what serial device it was or type the command to connect, it’s just there and running, just like my CircuitPython code is when I plug in a board.

But that’s not the only cool part.  The Monday after the episode aired, Martin Lund joined the Adafruit Discord after he heard about John Park’s episode.  He answered some questions and asked for feedback.  It’s so cool to see open source collaboration like that in the open.

And when 2.0 came out on the 11th, Martin popped in Adafruit’s Discord to let folks know of the new release.  A couple users shared a few bugs, especially on Windows, and he 

He didn’t have to do any of that, but what a way to go above and beyond.

It’s so cool to see open source collaboration happening in real time.  If you’re looking to level up your CircuitPython skills and move on from the Mu code editor, check out tio.


## Rivers Cuomo
I’m big into music and this next one is a little fun for me. This is from the department of rock stars can be developers, too. Rivers Cuomo, the lead singer of the band Weezer, whom you may know from such hits as Buddy Holly, Beverly Hills, and Pork and Beans, was recently spotted on Github.  

It turns out he’s an open source developer when not writing songs!  He submitted a PR to another open source project and he also has his own project on GitHub.  He’s written a Python app and released it under the GPL.  

Here’s the description from the GitHub repository:

> A python script to update a Spotify playlist every day with all the songs from any significant new albums. It shouldn’t include single-only releases. Anything older than a month should be deleted.  

And Mr. Cuomo goes in to a little more detail in the About section:

> GitHub - riverscuomo/new-albums: This project is for me to experiment with open-source collaboration. So please feel free to chime in and participate.  I’ve been learning programming since 2015 but I’ve been mostly working on my own. So my github/collaboration skills are weak. I’d like to learn more about collaboration so I can accomplish more as a programmer through teamwork.    

He goes on to say: 

> So this project will be a first, low-risk, foray into the field of open-source collaboration. If things go well here, maybe I can start to open up some of my other repositiories. I could sure use some help. And I love that thought that some of my programs could be useful to others.  My first goal here is to understand how different developers can work on a codebase together without sharing credentials;   

I don’t have Spotify to test it out, but you’ll need a Spotify client ID and secret and you can customize the program to exclude certain genres, too.    But if you do have a Spotify account and know a little Python, check it out.

Link: [GitHub - riverscuomo/new-albums: This project is for me to experiment with open-source collaboration. So please feel free to chime in and participate.  I’ve been learning programming since 2015 but I’ve been mostly working on my own. So my github/collaboration skills are weak. I’d like to learn more about collaboration so I can accomplish more as a programmer through teamwork.  One reason I’ve hesitated so long to try this is I’m worried about accidentally exposing API keys, secrets, credentials, and access to my users’ data (not that I have much). So this project will be a first, low-risk, foray into the field of open-source collaboration. If things go well here, maybe I can start to open up some of my other repositiories. I could sure use some help. And I love that thought that some of my programs could be useful to others.  My first goal here is to understand how different developers can work on a codebase together without sharing credentials; to create a program that different people can use with their own credentials. I’ve attempted this by requiring collaborators (including myself) to use environment variables.](https://github.com/riverscuomo/new-albums)


## Bambu Labs X1 Carbon

Tod: do you own a 3D printer?

Tod: 

You may or may not have heard of the Kickstarter campaign earlier this summer for a new 3D printer from a startup called Bambu Labs.

Now, a rule in the 3D printer community is to never to buy a printer on Kickstarter, for a number of different reasons.  I think Bambu knew that, because before the Kickstarter went live, they sent out a ton of review units to YouTube hosts and other influencers.  

They all came back glowing about it and a couple that I follow even said they’d be spending their own money to buy one, it was that good.  The Kickstarter launched and they raised about 10 times what they were looking for.

The X1 is generational and this printer sets the bar for the next generation of printers.  It has built-in LIDAR for auto bed leveling and some other bells and whistles.  But it’s fast.  4x faster than a Prusa or Ender 3.  And the quality is great.  I had a chance to help set up my best friend’s X1 Carbon and the hype is real.  The out of box experience was wonderful - everything was clearly marked and we were up and printing in fifteen minutes.

Now if you’re looking to buy a 3D printer and looking at Creality Ender 3s, this isn’t the printer for you.  But if you’re looking at a Prusa, not the Mini, you might want to consider the X1.  A fully assembled Prusa will run you $1100, and the Bambu has 2 models at $999 or $1199, with the more expensive one being made of slightly better materials and comes with some extras, like a webcam to monitor your print.

There’s a little risk with a new manufacturer, but they’ve made replacement parts for sale already and followed through on their promise to open source their slicer software.  If this is what the next generation of 3D printers looks like, I’m excited.


https://us.store.bambulab.com/products/x1-carbon-3d-printer?variant=40475104641160

https://www.kickstarter.com/projects/bambulab/bambu-lab-x1-corexy-color-3d-printer-with-lidar-and-ai?ref=checkout_rewards_page

[Original Prusa i3 MK3S+ 3D printer | Original Prusa 3D printers directly from Josef Prusa](https://www.prusa3d.com/product/original-prusa-i3-mk3s-3d-printer-6/)

BV3D: [YouTube](https://www.youtube.com/watch?v=iuVwHXg1vVQ)

Edge of Tech: [YouTube](https://www.youtube.com/watch?v=yvFznQa9miI)

