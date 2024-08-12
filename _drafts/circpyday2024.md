## Intro
* Welcome to a live edition of The Bootloader!
    * To learn more about us or to subscribe to our podcast, visit [The Bootloader.net](https://thebootloader.net).
* Have a question or comment?  Find us in the Adafruit Discord at https://adafru.it/discord

## CircuitPython over the last year

**“Life moves pretty fast. If you don't stop and look around once in a while, you could miss it.”**
― Ferris Bueller

* First CircuitPython 9.0 alpha end of October
  * [Release CircuitPython 9.0.0 Alpha 2 · adafruit/circuitpython](https://github.com/adafruit/circuitpython/releases/tag/9.0.0-alpha.2)
* 9.0 released March 18
  * [Release CircuitPython 9.0.0 · adafruit/circuitpython](https://github.com/adafruit/circuitpython/releases/tag/9.0.0)
  * MicroPython merges
    * Owe a debt of thanks to MicroPython, including Damien George and Jim Mussared and everyone who has contributed to MicroPython
      * The MicroPython merges are huge undertakings. Props to the CircuitPython team for even trying to track upstream. For example, the 1.20 update touched 779 files over 250 commits. And they did 3 merges! (MicroPython 1.19.1, 1.20.0, and 1.21.0)
    * Total CircuitPython changes from 8.2.4 to 9.0.0:
      * 8.24 released August 22, 2023
      * Comparison of 8.2.x to 9.0.0
        * 4,223 commits
        * 3,100 files changed!
  * CircuitPython 9 new features
    * ConnectionManager was released with CircuitPython 9.0 and makes managing sockets in networking much easier
      * Created by community member Justin Myers
    * `jpegio` was released in CircuitPython 9 supporting the Memento camera
    * Transparent PNG support was added just last week, so all three major image types are supported!
    * USB Host
      * Want to use a MIDI Controller?  Keyboard? Other peripherals?  You can!

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
