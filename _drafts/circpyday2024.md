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
    * ConnectionManager was released with CircuitPython 9.0 and makes managing sockets in networking much easier
  * Created by community member Justin Myers
  * `jpegio` was released in CircuitPython 9 supporting the Memento camera
  * Transparent PNG support was added just last week, so all three major image types are supported!
  * USB Host
    * Want to use a MIDI Controller?  Keyboard? Other peripherals?  You can!
