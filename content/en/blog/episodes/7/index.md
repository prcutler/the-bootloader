---
date: 2022-11-21
title: "Episode 7: The CircuitPython 9 Release Show"
linkTitle: "Episode 7"
description: "The CircuitPython 9 Release Show"
author: Paul Cutler ([@prcutler](https://hachyderm.io/@prcutler))
---
## Welcome
Welcome to The Bootloader.  We're excited to return after an extended break.  For episode 7, we dive into the just released CircuitPython 9 and discuss what we're excited about and some of the new features.

[Full transcript available here](https://thebootloader.net/blog/2022/11/21/episode-5-transcript/).

<iframe width="100%" height="112" frameborder="0" scrolling="no" style="width: 100%; height: 112px;  overflow: hidden;" src="https://www.circuitpythonshow.com/@thebootloader/episodes/pandas-and-breadboards-y5nqd/embed/dark"></iframe>

# Show Notes

## Episode Intro

Welcome!  This is all about the new [CircuitPyton 9.0 release](https://blog.adafruit.com/2024/03/18/circuitpython-9-0-0-released/)


### What are we excited for in CircuitPython 9?
  * Tod: `jpegio`, ESP-IDF update, USB Host, `parelleldisplaybus`
  * Paul: Memento camera / `jpegio`, CIRCUITPY on Android, ConnectionManager, USB Host

### `jpegio` and the Memento Camera
  * Memento Camera from Adafruit
  * [AdaBox 21](https://learn.adafruit.com/adabox021)
    * [AdaBox 21 Unboxing Video](https://www.youtube.com/watch?v=H9vWXmL2HIk) hosted by John Park
  * [`jpegio`](https://docs.circuitpython.org/en/latest/shared-bindings/jpegio/index.html) 
    * one downside of JPEG vs BMP or PNG files: JPEGs are not palletized
    * based on ["TJpgDec"](http://elm-chan.org/fsw/tjpgd/) 
  * [`bitmapfilter`](https://docs.circuitpython.org/en/latest/shared-bindings/bitmapfilter/index.html) 
    * Convolusion (kernel) image filter
    * Photoshop-like image effects in CircuitPython

### USB Host
  * [`usb.core`](https://docs.circuitpython.org/en/latest/shared-bindings/usb/core/index.html)
    * Tries to be as much like [PyUSB](https://github.com/pyusb/pyusb) as possible
  * [USB MIDI Controllers with USB Host](https://github.com/adafruit/Adafruit_CircuitPython_USB_Host_MIDI) is coming
  * Keyboards on USB Host
    * Scott theorized about a CircuitPython "computer" in his [CircuitPython2024 blog post](https://blog.adafruit.com/2024/01/24/scotts-circuitpython2024-tannewt/) earlier this year

### MicroPython and merging its changes into CircuitPython
  * New split heap management.  Here's a comment from CircuitPython Core Developer Dan Halbert:
> The "split heap" code from MicroPython now enables us to use heap allocation outside the VM, which was very awkward before: any dynamic storage allocation could only be done once, before the VM started. The heap then used the remaining RAM. Now there is an "outside" heap which can be used while the VM is running, and that storage will not be garbage collected. So various storage allocations that used to be static can now be dynamic, such as stuff needed for USB setup. We also removed the "long-lived storage" scheme that was added a long time ago to reduce fragmentation. In that scheme, storage that we expected to live a very long time (mostly allocations for compiled bytecode) was allocated at one end of the heap, and shorter-lived storage (like the temp storage used during compilation) was allocated at the other end. Part of the scheme involved moving allocated objects and adjusting pointers. The moving caused some inherent but obscure problems where objects' identities seemed to change.

> Now long-lived storage is gone, because it was not very compatible with the split-heap scheme. This may cause some projects on small-RAM boards like SAMD21 not to work any more due to increaed fragmentation. We have some ideas for doing something like long-lived storage in a different way that wouldn't involve moving objects, but that won't be in 9.

  * The MicroPython merges are huge undertakings. Props to the CircuitPython team for even 
trying to track upstream. For example, the 1.20 update touched 779 files over 250 commits. And they did 3 merges! (MicroPython 1.19.1, 1.20.0, and 1.21.0)

### `paralleldisplaybus`
  * 8x faster display using `paralleldisplaybus` instead of SPI
  * Currently for ESP32- and RP2040- based chips
  * e.g. [LilyGo T-Display S3 AMOLED](https://www.lilygo.cc/products/t-display-s3-amoled) and
     [LilyGo T-Display S3](https://www.lilygo.cc/products/t-display-s3)

### CircuitPython for ESP32 updates to ESP-IDF 5
  * CircuitPython 9 moves from using ESP IDF 4.x to [ESP IDF 5](https://www.espressif.com/en/news/ESP-IDFv5)
  * This will enable new features and new boards, like [ESP32-C6](https://www.espressif.com/en/products/socs/esp32-c6)
  * Potential future support for Bluetooth on ESP32 boards that support BLE

### ConnectionManager
  * Paul got his description wrong - ConnectionManager is used by `adafruit_requests` and MiniMQTT to manage sockets.
  * Created by community member Justin Myers
  * It's great how even with Adafruit funding three core developers that it's truly a community project and a community member can add a new library and way of doing things to CircuitPython.
  * Makes socket tasks easier, like [this example](https://docs.circuitpython.org/projects/connectionmanager/en/latest/examples.html)

### Breaking Changes in CircuitPython
  * [`displayio`](https://docs.circuitpython.org/en/latest/shared-bindings/displayio/index.html) changes:
    * `display.show()` deprecated 
    * `displayio` drivers have moved
    * [See this FAQ](https://learn.adafruit.com/circuitpython-display-support-using-displayio/faqs)
  * Mounting a filesystem (SD card) requires an existing directory, like CPython
  * CircuitPython now requires explicit socket port re-use. Use `socket.setsockopt(pool.SOL_SOCKET, pool.SO_REUSEADDR, 1)`, as in CPython.


### Support The Bootloader

If you like what you hear, one of the best things you can do to help the show is tell a friend or write a review.

