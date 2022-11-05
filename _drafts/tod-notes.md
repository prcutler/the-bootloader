# Tod's Notes for Future Episodes

## Brainstorming

* [Kaluma Javascript runtime for Raspberry Pi Pico](https://kalumajs.org/)

* [DSP56300 emulator of 1990s Virtual Analog synths (Virus, Supernova, Microwave, Nord)](https://dsp56300.wordpress.com/)

* [Black "Pico" w/ USB-C, 16MB & Neopixel](https://www.aliexpress.com/item/3256804258715020.html)

* [Machine Sewable LED strips](https://hackaday.io/project/186907-machine-sewable-led-strips)

   - and [Twitter thread](https://twitter.com/sjpiper145/status/1562006047635558401)

* [Belay library for CPython to control Micropython (firmata-like)](https://github.com/BrianPugh/belay)

* [Handwriting recognition in CircuitPython on Pico w/ OV7670 camera & Machine Learning](https://ashishware.com/2022/09/03/pipico_digit_classification/)

* [FullControl Design Library, Python 3D Gcode paths](https://fullcontrol.xyz) and https://twitter.com/FullControlXYZ

* [Switching Voltage Regulators in 7805 package](https://hackaday.com/2022/09/05/the-7805-is-dead-long-live-the-7805/)
    - https://github.com/wagiminator/Power-Boards

* [Diffusion Bee - one-click Stable Diffusion for M-chip Macs](https://github.com/divamgupta/diffusionbee-stable-diffusion-ui)
   - Instead of installing Anaconda and the rest of the crazy ML Python, just run this app!

---

* PixelBlaze expression language (not new but interesting)
  - https://luxlavalier.com/code  (@jasoncoon_ (Jason Coon), @GeekMomProjects (Debra Ansell), @ledmage (Ben Hencke)
  - https://github.com/simap/pixelblaze/blob/master/README.expressions.md
  - https://electromage.com/patterns


* samplebrain by Aphex Twin & Dave Griffiths
  - https://thentrythis.org/projects/samplebrain/
  - https://gitlab.com/then-try-this/samplebrain/-/blob/main/docs/manual.md
  - https://cdm.link/2022/09/free-sample-mashing-with-samplebrain-by-aphex-twin-and-dave-griffiths/

* Tone.js in-browser synthesis (https://tonejs.github.io/), and examples using it, like:
  - Acid Hit https://cdm.link/2022/09/free-acid-303-browser/
  - Pi Songs - https://pisongs.com/
    - "Play something no one has ever heard before" - https://pisongs.com/shepardspi/?position=575912300&t=1664758364
  - Strudel live coding music making
    - https://loophole-letters.vercel.app/strudel
    e.g. `stack("c4 f3 g4 a#4", "c2 g2".slow(2)).echo(4, 1/8, .5)`

* 4-axis non-planar 3d printing
  - Modifies a Prusa MK3 to add a rotating 45 degree tilted extruder
  - https://www.youtube.com/watch?v=7LRWuccMGjc
  - https://www.cnckitchen.com/blog/the-rotbot-4-axis-non-planar-3d-printing
  - https://www.printables.com/model/288723-4-axis-modification-for-mk3s-with-rotational-print

----

* New WCH chip is Arduino-class and only $0.10
  - https://twitter.com/Patrick_RISCV/status/1580384430996484101
  - https://github.com/openwch/ch32v307 (slightly better version that has USB)
  - akiba's tweet: https://twitter.com/freaklabs/status/1580560030146867200


* Person Sensor by Useful Sensor
  Detects faces, basic facial recognition, "looking at", for $10!
  - https://www.sparkfun.com/products/21231
  - https://github.com/usefulsensors/person_sensor_docs/blob/main/README.md
  -  https://github.com/usefulsensors/person_sensor_screen_lock/blob/main/code.py

---

* Matter officially supported in iOS 16
  Matter is an open standard for smart home IoT stuff (Apple, Google, Amazon, etc all signed on)
  - https://www.youtube.com/watch?v=i2doZomr9V0
  - https://www.reddit.com/r/esp32/comments/yfvpxu/finally_apple_officially_supports_matter_in_161/
  - https://github.com/project-chip/connectedhomeip
  - https://nabucasa.github.io/matter-example-apps/

* Hypno video synthesizer from Sleepy Circuits
  RasPi 3 or 4-based video synth with Eurorack-compatible controls
  - https://sleepycircuits.com/hypno
  - https://www.instagram.com/sleepycircuits/

* https://ffmpeg.guide
  Flows & nodes-based GUI for generating FFMPEG commandline commands
  - https://ffmpeg.guide/
  - free for up to 5 nodes
  - https://twitter.com/zack_overflow/status/1586288992680493057

* ERAE Touch
  - MPE (MIDI Polyphonic expression) controller
  - 1000 FSR (Force-sensing resistor) sensors & 1000 RGB LEDs
  - 1 ms response time / 100 um XY precision
  - a pad the size of a big laptop screen, covered in a stiff silicone mat
  - 2020 Kickstarter https://www.kickstarter.com/projects/erae-touch/erae-touch-the-expressive-music-controller-0/description
  - 2018 started development
  - 2022 now for sale
  -

* Follow-up:
  * 10 cent Arduino-class RISC-V chip from WCH now has a dev board on Tindie
  * Chip is WCH CH32V003  (2kB RAM, 16kB flash)
  * Tindie page: https://www.tindie.com/products/adz1122/ch32v003-risc-v-mcu-development-board/
  * Was $6 now $10 (due to demand probably)
  * [More info on Hackster.io](https://www.hackster.io/news/wch-launches-a-sub-10-risc-v-microcontroller-while-a-6-90-dev-board-gets-you-started-90b1ffd7490a)
