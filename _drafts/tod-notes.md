# Tod's Notes for Future Episodes

## Links:

* Booting Raspberry Pis off USB drives
  - rpi-clone - easily clone running Pi to USB drive
    - https://github.com/geerlingguy/rpi-clone
  - log2ram - put /var/log in RAM disk tmpfs
    - https://github.com/azlux/log2ram
  - https://www.dzombak.com/blog/2024/04/pi-reliability-reduce-writes-to-your-sd-card/
  - Remove SD card and RasPi automatically boot from USB
  - Much faster, and SD cards aren't made to be disk drives

* Mutable Instruments Braids/Plaits synths ported to Arduino-Pico
  - https://github.com/poetaster/arduinoMI/tree/main
  -  https://github.com/poetaster/scarp

* ripgrep
  - https://linuxhandbook.com/ripgrep/

* "analog keyboards"
  - (wait until I have a PCB ready)

* Datamosh stuff
  - Supermosh - datamosh in the browser - https://supermosh.github.io
  - talk about the fun of MPEG encoding


* "history of reverb" discussion
  - my own thoughts
  - rooms -> spring -> plate -> bucket-brigade -> digital
  - https://precastreinforced.co.uk/2025/07/20/echo-and-reverb-the-mechanical-ghosts-of-wide-open-spaces/
  - "MIDIverb history and reverb history" - https://www.youtube.com/watch?v=2yYiWOHwHSo
  - "reverse engineering the MIDIverb" - https://www.youtube.com/watch?v=z4cIt1VPAjU&t=251s

* Scrappy - https://pontus.granstrom.me/scrappy/
  - "make little apps for your friends"

* Cosmolab - https://cosmolab.faselunare.com/
  - new Daisy Seed interface thing

* "AlgoRave"
  - DJ_Dave: https://www.instagram.com/p/DL0P-2WusOO/
  - Strudel: https://strudel.cc/
  - Originally mentioned in Bootloader Ep2

* PlugData.org
  - Write Pd (visual audio coding language) that can compile to Daisy Seed
    microcontroller or VSTs or other things
  - https://www.youtube.com/watch?v=yU3jR0EpsGQ
  - https://www.youtube.com/watch?v=45YNmjSBS_8

* https://graphite.rs
  - motion graphics tool, open source, web based

* https://weatherstar.netbymatt.com
  - https://bsky.app/profile/thomasfuchs.at/post/3lqbs33ibvk2g

* De-Amazon your Kindle - https://www.youtube.com/watch?v=Qtk7ERwlIAk

* x SAM2695 General MIDI chip
  - imlementations:
    - Seeed - https://www.seeedstudio.com/XIAO-MIDI-Synthesizer-p-6462.html
    - M5stack w/ speaker - https://shop.m5stack.com/products/midi-synthesizer-unit-sam2695
    - M5statck w/ MIDI in/out - https://shop.m5stack.com/products/midi-unit-with-din-connector-sam2695
  - SAM2695 datahsheet - https://docs.dream.fr/pdf/Serie2000/SAM_Datasheets/SAM2695.pdf
  - unfortunately not recommended for new designs

* x Resurrecting Sinistar https://www.youtube.com/watch?v=lCuoUSDBVac
* x Hyperwood - https://hyperwood.org/ - from https://macaw.social/@andypiper/114392576041698951

* 3d-printable keycaps - https://github.com/braindefender/KLP-Lame-Keycaps

* MIDI with Perl! - https://www.perl.com/article/enhancing-your-midi-devices-round-ii/

* TR909 Drum circuit analyzed & redesigned - https://www.youtube.com/watch?v=Xbl1xwFR3eg

* x 200Mhz Clock Support for RP2040
  - https://github.com/raspberrypi/pico-sdk/releases/tag/2.1.1
  - https://www.hackster.io/news/the-raspberry-pi-rp2040-gets-a-surprise-speed-boost-unlocks-an-official-200mhz-mode-d6c9d267de5a
  - https://bsky.app/profile/thejpster.org.uk/post/3lijrgmptnc2a
  - "I already use a pretty aggressive overlock to 366MHz" - @polpo.org / PicoGUS


* YoutubeSequencer.com
  - https://youtubesequencer.com

* JetKVM
  - https://jetkvm.com
  - https://github.com/jetkvm/kvm
  - https://www.jeffgeerling.com/blog/2024/jetkvm-tiny-ip-kvm-thats-not-apple-watch


## Brainstorming 2024

* x FlatMac : https://www.youtube.com/watch?v=Grd_a4oi7qU

* Supercon2024 and SAOs
  - https://github.com/flummer/dmm-sao
  - Erik Klein CO2 monitor
  - https://hackaday.io/project/198320-bus-pirate-5-sao
  - POV SAO (I have one)
  - https://hackaday.com/2024/11/09/the-badge-hacks-of-supercon/
  - https://www.youtube.com/watch?v=Iz-HrZkzUlk

  unsorted links:
  - https://hackaday.io/project/198943-sao-infinity-mirror
  - https://github.com/Hack-a-Day/2024-Supercon-8-Add-On-Badge
  - https://github.com/davedarko/TARS-SAO
  - https://hackaday.io/project/198918-duckglow-sao
  - https://hackaday.io/project/198458-record-scratch-sao


* Sandify -- generative geometric patterns for sand art / plotters
  - https://sandify.org/
  - https://github.com/jeffeb3/sandify
  - DONE in newsletter 13

* Raspberry Pi AI Camera Module
  - [Raspberry Pi blog poast](https://www.raspberrypi.com/news/raspberry-pi-ai-camera-on-sale-now/)
  - [Hackster hands-on article]( https://www.hackster.io/news/raspberry-pi-s-ai-eye-hands-on-with-the-raspberry-pi-ai-camera-module-383fb34afcf7)
  - [Pose estimation demo](https://www.youtube.com/watch?v=rloJNA_VuSA)
  - [Object detection demo](https://www.youtube.com/watch?v=D-foRupzOiY)

  Also see:

  - [Person sensor by UsefulSensors $10](https://www.sparkfun.com/products/21231)

* iPhone 16 electrically-released battery adhesive
  - [iFixit video](https://www.youtube.com/watch?v=M6jBXI6CR9s)
  - [iFixit article](https://www.ifixit.com/News/100352/we-hot-wired-the-iphone-16)
  - [Hackaday article](https://hackaday.com/2024/09/22/hands-on-with-new-iphones-electrically-released-adhesive/)

* wasm2mpy - Compiling Rust, GoLang, Zig, WebAssembly to Micropython MPY modules
  - [initial annoucement](https://github.com/orgs/micropython/discussions/15702)
  - [repo](https://github.com/vshymanskyy/wasm2mpy)
  - only ESP32 really so far (and Raspberry Pi)

* X1Plus alternative open source Bambu X1 firmware
  - [X1Plus](https://github.com/X1Plus/X1Plus/wiki)
  - [X1Plus expansion board](https://www.crowdsupply.com/accelerated-tech/x1plus-expansion-board)
  - [Hackster article](https://www.crowdsupply.com/accelerated-tech/x1plus-expansion-board)

* Tulip Creative Computer and Amy synth library
  - [Tulip homepage](https://github.com/shorepine/tulipcc)
  - [Floyd Steinberg's video on Tulip](https://www.youtube.com/watch?v=1lYFjQp7Xrw)
  - [AMY - Additive Music librarY](https://github.com/shorepine/amy)
  - DONE on Episode 11 (Aug 2024)

* Embedded Swift
  - https://www.cnx-software.com/2024/06/13/embedded-swift-esp32-c6-raspberry-pi-rp2040-stm32f7-nrf52840-microcontrollers/
  - https://www.hackster.io/news/apple-embeds-swift-into-hardware-125131557514
  - https://www.youtube.com/watch?v=LqxbsADqDI4
  - Swift Matter Examples - https://github.com/apple/swift-matter-examples/tree/main/smart-light
  - DONE on Episode 10 (July 2024)

* M5Stack Cardputer
    - https://docs.m5stack.com/en/core/Cardputer
    - ESP32-S3 w/ display, microphone, speaker, IR, battery w/ case & magnet & Lego connection
    - DONE on Episode 9 (3 Jun 2024)

* Plum Pot Kicad Tutorials
    - https://www.youtube.com/playlist?list=PLZNH6jlLeFXsg9ohRMbJ0qqSfUrRyAn7b
    - older but still really helpful
    - btw, I am now Kicad compliant!
    - DONE on Episode 9 (3 Jun 2024)

* BLE on Arduino using USB Host
  - https://www.bleuio.com/blog/integrating-bleuio-with-adafruit-feather-rp2040-for-seamless-ble-applications-part-2/
  - https://github.com/smart-sensor-devices-ab/bleuio_arduino_sensor_example

* Capacitive touch wheels
  - like my `touchwheel0` & `picoslidertoy`
  - DONE on Episode 8 (29 Apr 2024)

* THX Deep Note?
  - my recreations in Mozzi - https://www.youtube.com/watch?v=7fX8cBwbOmU

* Carlyn's ARM assembly deep dives
  - https://www.whynotestflight.com/excuses/its-alive-samd21e18a-assembly-no-sdk/
  - DONE on Episode 8 (29 Apr 2024)

* Let's talk about Hash Tables
  - https://craftinginterpreters.com/hash-tables.html

* SynthUX academy and Daisy Seed
  - https://www.synthux.academy
  - DONE on Episode 8 (29 Apr 2024)


-------------------------------------

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

---

* WithDiode.com -- 3d breadboard simulation in the browser
  - omg
  - this is the best
  - so fun
  - I saw it from Clive Thompson (@clive@saturation.social) on Mastodon
    - https://mastodon.social/@clive@saturation.social/109344907748519044
  - [DeepFriedNeurons breadboard oscillators](https://blog.crashspace.org/2021/05/dfn-happy-hour-no-43-good-vibrations/)
  - also see [Wokwi simulator](https://wokwi.com/)

* RNBO -- Turn Max/MSP patches into VST plugins
  - https://www.synthanatomy.com/2022/11/rnbo-turns-your-max-patches-into-hardware-vst-plugins-and-web-applications.html

* gpu-io - GPU accelerated WebGL library for physics simulations
  - homepage: https://github.com/amandaghassaei/gpu-io
  - examples: https://apps.amandaghassaei.com/gpu-io/examples/
  - mastodon post I saw: https://mastodon.art/@amandaghassaei/109433326067044608
