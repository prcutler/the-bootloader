
## Intro
* *(When you hit record, wait 10 seconds)*
* Welcome to a live edition of The Bootloader! I'm Paul Cutler
* And Hi, I'm Tod Kurt
  * To learn more about us or to subscribe to our podcast, visit [The Bootloader.net](https://thebootloader.net).
* Have a question or comment?  Find us in the Adafruit Discord at https://adafru.it/discord
  * my handle is "todbot" and Paul's is "prcutler"

## CircuitPython over the last year

(Paul) As we were preparing for the show, I realized how far CircuitPython has again come in the last year.  While we're always looking forward to the next thing, such as Bluetooth on an ESP32-S3 or the rp2350, I'm reminded of the quote from Ferris Bueller's Day Off:

**“Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.”**
― Ferris Bueller

So we thought we'd take a look at the CircuitPython project itself in the last year since last CircuitPython Day:

* First CircuitPython 9.0 alpha end of October
  * [Release CircuitPython 9.0.0 Alpha 2 · adafruit/circuitpython](https://github.com/adafruit/circuitpython/releases/tag/9.0.0-alpha.2)
* 9.0 released March 18
  * [Release CircuitPython 9.0.0 · adafruit/circuitpython](https://github.com/adafruit/circuitpython/releases/tag/9.0.0)
  * MicroPython merges
    * (Tod) Owe a debt of thanks to MicroPython, including Damien George and Jim Mussared and everyone who has contributed to MicroPython.  CircuitPython is a kind of Micropython, don't forget that.
      * The MicroPython merges are huge undertakings. Props to the CircuitPython team for even trying to track upstream. For example, the 1.20 update touched 779 files over 250 commits. And they did 3 merges! (MicroPython 1.19.1, 1.20.0, and 1.21.0)
    * (Paul) Total CircuitPython changes from 8.2.4 to 9.0.0:
      * 8.24 released August 22, 2023
      * Comparison of 8.2.x to 9.0.0
        * 4,223 commits
        * 3,100 files changed!
  * CircuitPython changes in the last year (both in CirPy 9 and generally)
    * (Paul) ConnectionManager was released with CircuitPython 9.0 and makes managing sockets in networking much easier
      * Created by community member Justin Myers
    * (Paul) `jpegio` was released in CircuitPython 9 supporting the Memento camera
    * (Paul) PNG support! Transparent PNG support was added just last week, so all three major image types are supported!
    * (Tod) synthio -- music synthesizer in your CircuitPython!
      * Started in mid-2023, but got tuned and features added in the last year
      * My [circuitpython-synthio-tricks](https://github.com/todbot/circuitpython-synthio-tricks) is just over a year old!
    * (Tod) USB Host
      * Pico can be both a USB peripheral (CIRCUITPY drive) and a USB host to other USB peripheralsn
      * Want to use a USB MIDI Controller?  Keyboard? Other peripherals?  You can!
    * (Tod) paralleldisplaybus
    * (Tod) mp3decoder improvements
      * Higher bitrates and URL streams (on ESP32)


## Theme: "Using CircuitPython in larger projects, what to watch out for" (Paul & Tod)

 * How to go from a sensor demo to a full app or full circuit?
 * Here's a couple of larger projects we've done and some tips that may be helpful

## Card-sized sample playing drum machine : picotouch_drumcard  (Tod #1)

I made a tiny drum machine that plays samples. Or it's also a synth. Or maybe it's a Macropad.

### Evolution from "picotouch_bizcard", "picoslidertoy", "picotouch" boards

* Show demo of those boards
* Show how minimal parts count they are
* Discuss issues of reading so many touchio inputs
  * 7 milliseconds to read ~20 inputs; 1/32nd note is 63 millis @ 120 bpm

### The challenge: design / build / code a tiny drum machine in 2 weeks

* Desired features:
  * Size of a pack of playing cards
  * Audio out (PWM audio)
  * MIDI In & Out (TRS serial MIDI)
  * 17 touchpads:
    * 8 pads for drum triggers
    * 3 for play/pause/rec
    * 6 for modifers: select/up/down & A/B selection & shift
  * LED indicators for the pads, should be PWM dimmable
  * No electronics on touch surface!
  * Battery powered

* Result:
  * Small demo of "picotouch_drumcard"
  * Instead of `touchio` using odd little TS20 touch chip now
  * It kinda works! But...

#### Problems with current design

* Top touch traces create false readings
* Can't PWM the LEDs  (or can't PWM all of them)
* Battery charger circuit is totally non-functional




### Aside: Using CircuitPython to "validate" a board before it's built

Use CircuitPython to test a board pinout before making a board

* Steps:
  * Open up a REPL to a board with the chip you want to use
  * Start creating CircuitPython objects: button inputs, LED outputs, i2c, display, audio, etc.
  * If you can create them all, your board will work, almost 100% guaranteed
  * If it doesn't, maybe you swizzled I2C, or need to use a different pin pair
* If I would've done this for the drumcard, I would've found out I cannot PWM all the LEDs with how they're currently wired up

### Other tips when using CircuitPython on big projects
* REPL for great success  (especially "Ctrl-E" paste mode)
* Separating code in different files / objects helps

## SongMatrix (Paul #1)

The [SongMatrix project](https://paulcutler.org/project/songmatrix/) combines a Raspberry Pi with a [microphone](https://www.adafruit.com/product/3367) with an [S3 MatrixPortal](https://www.adafruit.com/product/5778) and an RGB Matrix. The Raspberry Pi listens in the background to the music playing, uploads it to Adafruit IO, and displays the song info on the RGB Matrix.

### Raspberry Pi setup
* You can use almost any Raspberry Pi (I'm using an old Raspberry Pi 2)
* The Python application on the Raspberry Pi uses `asyncio`, `shazamio`, and Adafruit IO.
    * `shazamio` is a Python library that reverse engineered the Shazam API
    * `shazamio` uses `asyncio`
* It records a 30 second sample to the Raspberry Pi, uploads it to Shazam, and prints out the results with the song title and artist
* It's then uploaded to Adafruit IO as "Song Title by Artist Name"

### CircuitPython on the Matrix Portal

* Should work on either the S3 or M4 Matrix Portal (it's just text!)
* Create your `settings.toml` with your Wi-Fi settings and Adafruit IO username and API key
* Import `MQTT` and `adafruit_io`
* Setup Wi-Fi and then the Matrix Portal
* Use `adafruit_io` to get the last message stored in Adafruit IO with `aio.receive_data('audio')` and display on the Matrix Portal
* Setup MQTT as normal but include `socket_timeout` as it is needed when using `asyncio`
* Add two `asyncio` functions - one to connect to MQTT and the other to update the text when a message is received

## RP2350 and CircuitPython (Tod & Paul)

* (Paul & Tod) About RP2350 and how it improves on RP2040
  * Same ease-of-programming as original Pico / RP2040, e.g. UF2 boot-loader
  * New faster Cortex-M33 core vs Cortex-M0+ core
    * floating point, DSP, cryptography
* (Tod) Demo of SparkFun RP2350 Pro Micro synth stuff
