Episode 1 Script (Paul)

### tio
The first thing I wanted to share is a about a an open source project called tio.  Martin Lund is the developer and I have a cool story about him, too.  tio just released version 2.0 on September 11th.

I’ve been using CircuitPython for a year or two and I didn’t know about tio until John Park featured it in late July in on his show, CircuitPython Parsec.  

Like most users, I used Mu to see any serial output or errors with my CircuitPython devices.  Even Adafruit’s advanced serial guide for Mac & Linux has you use screen.

Tio is a modern day replacement for the old linux tool screen.  The motivation from it's Github home page:

To make a simpler serial device tool for talking with serial TTY devices with less focus on classic terminal/modem features and more focus on the needs of embedded developers and hackers.

I’ve using a Unix like operating system for too many years and this is perfect for someone like me who is comfortable dropping down into a terminal.  I can run also run tio in my IDE’s terminal.   It has one killer feature - auto-reconnect.  If I unplug my microcontroller and plug it back in, tio automatically reconnects.  I don’t have to look up what serial device it was or type the command to connect, it’s just there and running, just like my CircuitPython code is when I plug in a board.

But that’s not the only cool part.  The Monday after the episode aired, Martin Lund joined the Adafruit Discord after he heard about John Park’s episode.  He answered some questions and asked for feedback.  It’s so cool to see open source collaboration like that in the open.

And when 2.0 came out on the 11th, Martin popped in Adafruit’s Discord to let folks know of the new release.  A couple users shared a few bugs, especially on Windows, and he 

He didn’t have to do any of that, but what a way to go above and beyond.

It’s so cool to see open source collaboration happening in real time.  If you’re looking to level up your CircuitPython skills and move on from the Mu code editor, check out tio.