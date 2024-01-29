# CircuitPython 9 Release Show

CircuitPython 8.0 was released on February 3rd, 2023

## New Features

* `jpegio` - decode jpegs
  * Memento Camera support
  * bitmapfilter
* `synthio`
  * Add `synthio.Synthesizer.note_state`.
  * Add `synthio.Note` `.loop_start` and `.loop_end` properties.
  * Increase synthio channels from 2 to 12
* USB Host
  * Available on iMX RT and RP2040 chips only
  * Keyboards: Keyboards are treated specially by CircuitPython. It should automatically read the keyboard and convert keypresses into a serial stream.  Then you can do `input()` like you normally would. (https://github.com/adafruit/circuitpython/pull/8155)
  * MIDI controllers?
* RGB “dot clock” displays paired with the ESP32-S3 Quaila board
* The combination of USB Host + RGB “dot clock” displays could become a standalone CircuitPython computer.  See Scott’s CircuitPython2024 blog post:  [Scott’s \#CircuitPython2024 @tannewt](https://blog.adafruit.com/2024/01/24/scotts-circuitpython2024-tannewt/)
* Add `repl.py` which runs right before the real starts - [add support for "repl.py" by jepler · Pull Request \#8344 · adafruit/circuitpython](https://github.com/adafruit/circuitpython/pull/8344)

## Notable Changes
* Reorganize and split `displayio` (`display.root_group`)
  * Split off parts of displayio into multiple modules: busdisplay, fourwire, epaperdisplay, i2cdisplaybus, paralleldisplaybus. The existing displayio hierarchy will still be available 9.x.x, but is deprecated, and will be removed in 10.0.0. ~[\#8493](https://github.com/adafruit/circuitpython/pull/8493)~.
* CircuitPython drives now mount on Android devices
* **WARNING for nRF52 boards only:** If your board has an nRF52 UF2 bootloader whose version is before 0.6.1, you will not be able to load CircuitPython 8.2.0 and later, due to increased size of the firmware. See ~[these instructions](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader)~ for updating your bootloader.
* Overall size of CircuitPython - what happens to M0 and SAMD21 boards in the future?

## MicroPython Merge

MicroPython 1.20 merge PR: https://github.com/adafruit/circuitpython/pull/8481
MicroPython 1.21 merge PR: https://github.com/adafruit/circuitpython/pull/8508

ESP IDF 5.0: [ESP-IDF Release v5.0 Is a Major Update | Espressif Systems](https://www.espressif.com/en/news/ESP-IDFv5)

From danh:

The "split heap" code from MicroPython now enables us to use heap allocation outside the VM, which was very awkward before: any dynamic storage allocation could only be done once, before the VM started. The heap then used the remaining RAM. Now there is an "outside" heap which can be used while the VM is running, and that storage will not be GC'd. So various storage allocations that used to be static can now be dynamic, such as stuff needed for USB setup.  We also removed the "long-lived storage" scheme that was added a long time ago to reduce fragmentation. In that scheme, storage that we expected to live a very long time (mostly allocations for compiled bytecode) was allocated at one end of the heap, and shorter-lived storage (like the temp storage used during compilation) was allocated at the other end. Part of the scheme involved moving allocated objects and adjusting pointers. The moving caused some inherent but obscure problems where objects' identities seemed to change.

Now long-lived storage is gone, because it was not very compatible with the split-heap scheme. This may cause some projects on small-RAM boards like SAMD21 not to work any more due to increaed fragmentation. We have some ideas for doing something like long-lived storage in a different way that wouldn't involve moving objects, but that won't be in 9