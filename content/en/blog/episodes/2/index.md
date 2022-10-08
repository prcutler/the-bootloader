---
date: 2022-10-10
title: "Episode 2: M is for Makers, Music, and Machine Learning"
linkTitle: "Episode 2"
description: "M is for Makers, Music, and Machine Learning"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---
## Welcome
Welcome to The Bootloader, a bi-weekly podcast bringing you news, project updates, and product talk
from the tech and maker scenes.  Paul and Tod will bring you three interesting things and chat about them for a few minutes each.

[Full transcript available here](https://thebootlader.net/blog/2022/09/26/episode-1-transcript/).

<h2>
<blockquote class="zenplayer" data-episode-href="https://zencastr.com/embed/Lgys0J2f" style="background: black; border-radius: 12px; font-family: system-ui; width: 480px; height: 480px; position: relative; color: white; margin: 0;"> <img  style="width: 120px; display: inline-block; position: absolute; top: calc(50%); left: calc(50%); transform: translate(-50%, -50%);"  src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTE5IDE4IiBoZWlnaHQ9IjEwMCIgd2lkdGg9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTE1LjQyNSA2LjQyNTgxQzExNC4yMSA2LjQyNTgxIDExMy4yMjUgNy40MTE3MSAxMTMuMjI1IDguNjI3ODhWMTUuNjc0NUMxMTMuMjI1IDE2LjQwNDIgMTEyLjYzNSAxNi45OTU4IDExMS45MDYgMTYuOTk1OEMxMTEuMTc3IDE2Ljk5NTggMTEwLjU4NiAxNi40MDQyIDExMC41ODYgMTUuNjc0NVY4LjYyNzg4QzExMC41ODYgNS45NTIzMSAxMTIuNzUyIDMuNzgzMzMgMTE1LjQyNSAzLjc4MzMzSDExNy4xODVDMTE3LjkxNCAzLjc4MzMzIDExOC41MDUgNC4zNzQ4NyAxMTguNTA1IDUuMTA0NTdDMTE4LjUwNSA1LjgzNDI3IDExNy45MTQgNi40MjU4MSAxMTcuMTg1IDYuNDI1ODFIMTE1LjQyNVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwMi4yMjcgMC4yNjAwMUMxMDIuOTU2IDAuMjYwMDEgMTAzLjU0NyAwLjg1MTU1MSAxMDMuNTQ3IDEuNTgxMjVWMy43ODMzM0gxMDcuNTA2QzEwOC4yMzUgMy43ODMzMyAxMDguODI2IDQuMzc0ODcgMTA4LjgyNiA1LjEwNDU3QzEwOC44MjYgNS44MzQyNyAxMDguMjM1IDYuNDI1ODEgMTA3LjUwNiA2LjQyNTgxSDEwMy41NDdWMTEuMjcwNEMxMDMuNTQ3IDEyLjk3MyAxMDQuOTI2IDE0LjM1MzMgMTA2LjYyNyAxNC4zNTMzSDEwNy41MDZDMTA4LjIzNSAxNC4zNTMzIDEwOC44MjYgMTQuOTQ0OCAxMDguODI2IDE1LjY3NDVDMTA4LjgyNiAxNi40MDQyIDEwOC4yMzUgMTYuOTk1OCAxMDcuNTA2IDE2Ljk5NThIMTA2LjYyN0MxMDMuNDY4IDE2Ljk5NTggMTAwLjkwNyAxNC40MzI0IDEwMC45MDcgMTEuMjcwNFYxLjU4MTI1QzEwMC45MDcgMC44NTE1NTEgMTAxLjQ5OCAwLjI2MDAxIDEwMi4yMjcgMC4yNjAwMVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBkPSJNODguMzk0OCAxNS45MjFDODkuOTc4NiAxNi44ODk5IDkxLjU4MDggMTcuMjYgOTMuNjkyNCAxNy4yNkM5Ni4yNDQxIDE3LjI2IDk5LjU4NzYgMTYuMjAzIDk5LjU4NzYgMTMuMTIwMUM5OS41ODc2IDcuMzk0NjkgOTAuMzQ4OSAxMC4zODk1IDkwLjM0ODkgNy44MzUxQzkwLjM0ODkgNy4wNDIzNiA5MS41ODA4IDYuMTYxNTMgOTMuNDI4NSA2LjE2MTUzQzk0LjU3MjMgNi4xNjE1MyA5Ni4xMTIxIDYuNjkwMDMgOTYuNzI4IDcuMTMwNDRDOTcuMzU5MiA3LjQ5NTI5IDk4LjE2NzMgNy4yNzc5MiA5OC41MzE3IDYuNjQ1OThDOTguODk2MiA2LjAxNDAzIDk4LjY3OSA1LjIwNTE0IDk4LjA0NzggNC44NDAyOUM5Ni43MjggMy45NTk0NiA5NS4xMDAyIDMuNTE5MDQgOTMuNDI4NSAzLjUxOTA0QzkwLjI2MSAzLjUxOTA0IDg3LjcwOTMgNS40NTY4NyA4Ny43MDkzIDcuODM1MUM4Ny43MDkzIDEzLjM4NDMgOTYuOTQ4IDEwLjU2NTcgOTYuOTQ4IDEzLjEyMDFDOTYuOTQ4IDE0LjAwMDkgOTUuNTQwMiAxNC42MTc1IDkzLjY5MjQgMTQuNjE3NUM5Mi4wMjA3IDE0LjYxNzUgOTAuOTQ2NCAxNC4zMzU1IDg5LjYyNjYgMTMuNjMwOUM4OS4wMTA3IDEzLjI3ODUgODguMjE4OCAxMy41NDI4IDg3Ljg2NjkgMTQuMTU5NEM4Ny41MTQ5IDE0Ljc3NiA4Ny43Nzg5IDE1LjU2ODcgODguMzk0OCAxNS45MjFaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04My4zMSAxNS41Nzc0QzgyLjE0MzggMTYuNjI1NSA4MC42MjA5IDE3LjI2IDc4Ljk1NDYgMTcuMjZDNzUuMjg1OCAxNy4yNiA3Mi4zMTE2IDE0LjE4NCA3Mi4zMTE2IDEwLjM4OTVDNzIuMzExNiA2LjU5NTA2IDc1LjI4NTggMy41MTkwNCA3OC45NTQ2IDMuNTE5MDRDODAuNjIwOSAzLjUxOTA0IDgyLjE0MzggNC4xNTM1MSA4My4zMSA1LjIwMTZWNS4xMDQ1NEM4My4zMSA0LjM3NDgzIDgzLjkwMDggMy43ODMyOSA4NC42Mjk4IDMuNzgzMjlDODUuMzU4NyAzLjc4MzI5IDg1Ljk0OTUgNC4zNzQ4MyA4NS45NDk1IDUuMTA0NTRWMTUuNjc0NUM4NS45NDk1IDE2LjQwNDIgODUuMzU4NyAxNi45OTU3IDg0LjYyOTggMTYuOTk1N0M4My45MDA4IDE2Ljk5NTcgODMuMzEgMTYuNDA0MiA4My4zMSAxNS42NzQ1VjE1LjU3NzRaTTgzLjY2MTkgMTAuMzg5NUM4My42NjE5IDEyLjcyNDYgODEuNzEyIDE0LjYxNzUgNzkuMzA2NiAxNC42MTc1Qzc2LjkwMTIgMTQuNjE3NSA3NC45NTEyIDEyLjcyNDYgNzQuOTUxMiAxMC4zODk1Qzc0Ljk1MTIgOC4wNTQ0NiA3Ni45MDEyIDYuMTYxNTMgNzkuMzA2NiA2LjE2MTUzQzgxLjcxMiA2LjE2MTUzIDgzLjY2MTkgOC4wNTQ0NiA4My42NjE5IDEwLjM4OTVaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik02Ni4zMjg1IDYuMTYxNTNDNjMuODU5NiA2LjE2MTUzIDYxLjkyOTIgOC4wOTMwOCA2MS45MjkyIDEwLjM4OTVDNjEuOTI5MiAxMi42ODU5IDYzLjg1OTYgMTQuNjE3NSA2Ni4zMjg1IDE0LjYxNzVDNjcuNTY3NyAxNC42MTc1IDY4LjY4ODcgMTQuMjYyNyA2OS41NjYyIDEzLjY4ODlDNzAuMTc2NSAxMy4yODk5IDcwLjk5NDQgMTMuNDYxNyA3MS4zOTI5IDE0LjA3MjdDNzEuNzkxNSAxNC42ODM2IDcxLjYxOTkgMTUuNTAyNCA3MS4wMDk2IDE1LjkwMTRDNjkuNjkyOSAxNi43NjIyIDY4LjA2ODQgMTcuMjYgNjYuMzI4NSAxNy4yNkM2Mi40ODAyIDE3LjI2IDU5LjI4OTYgMTQuMjIyNiA1OS4yODk2IDEwLjM4OTVDNTkuMjg5NiA2LjU1NjQ0IDYyLjQ4MDIgMy41MTkwNCA2Ni4zMjg1IDMuNTE5MDRDNjguMDY4NCAzLjUxOTA0IDY5LjY5MjkgNC4wMTY4NCA3MS4wMDk2IDQuODc3NjVDNzEuNjE5OSA1LjI3NjY1IDcxLjc5MTUgNi4wOTUzOCA3MS4zOTI5IDYuNzA2MzRDNzAuOTk0NCA3LjMxNzI5IDcwLjE3NjUgNy40ODkxMSA2OS41NjYzIDcuMDkwMTFDNjguNjg4NyA2LjUxNjM2IDY3LjU2NzcgNi4xNjE1MyA2Ni4zMjg1IDYuMTYxNTNaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZD0iTTU1LjgxNDEgMTYuODE5QzU1LjQxOTYgMTYuNTkwNSA1NS4xNTQyIDE2LjE2MzUgNTUuMTU0MiAxNS42NzQ1VjEwLjEyNTNDNTUuMTU0MiA3LjkzNjE1IDUzLjM4MTUgNi4xNjE1MyA1MS4xOTQ4IDYuMTYxNTNDNDkuMDA4MSA2LjE2MTUzIDQ3LjIzNTQgNy45MzYxNSA0Ny4yMzU0IDEwLjEyNTNWMTUuNjc0NUM0Ny4yMzU0IDE2LjE2MzUgNDYuOTcgMTYuNTkwNSA0Ni41NzU1IDE2LjgxOUM0Ni4zODEzIDE2LjkzMTQgNDYuMTU2IDE2Ljk5NTcgNDUuOTE1NiAxNi45OTU3QzQ1LjE4NjcgMTYuOTk1NyA0NC41OTU4IDE2LjQwNDIgNDQuNTk1OCAxNS42NzQ1VjUuMTA0NTRDNDQuNTk1OCA0LjM3NDgzIDQ1LjE4NjcgMy43ODMyOSA0NS45MTU2IDMuNzgzMjlDNDYuNjQ0NSAzLjc4MzI5IDQ3LjIzNTQgNC4zNzQ4MyA0Ny4yMzU0IDUuMTA0NTRWNS4zMDgyNEM0OC4yMDI3IDQuMjExMDUgNDkuNjE4IDMuNTE5MDQgNTEuMTk0OCAzLjUxOTA0QzU0LjgzOTMgMy41MTkwNCA1Ny43OTM4IDYuNDc2NzUgNTcuNzkzOCAxMC4xMjUzVjE1LjY3NDVDNTcuNzkzOCAxNi40MDQyIDU3LjIwMjkgMTYuOTk1NyA1Ni40NzQgMTYuOTk1N0M1Ni4yMzM2IDE2Ljk5NTcgNTYuMDA4MiAxNi45MzE0IDU1LjgxNDEgMTYuODE5WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KCTxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMzEuNjIyNyAxMS43MTA4SDQxLjUxNjJDNDIuMjQ1MSAxMS43MTA4IDQyLjgzNiAxMS4xMTkyIDQyLjgzNiAxMC4zODk1QzQyLjgzNiA2LjU1NjQ0IDM5LjY0NTQgMy41MTkwNCAzNS43OTcxIDMuNTE5MDRDMzEuOTQ4NyAzLjUxOTA0IDI4Ljc1ODEgNi41NTY0NCAyOC43NTgxIDEwLjM4OTVDMjguNzU4MSAxNC40MjU2IDMyLjIyNDMgMTcuMjYgMzUuOTI5IDE3LjI2QzM4LjE3MjUgMTcuMjYgMzkuNTE1IDE2Ljc1MTkgNDAuODg0NSAxNS45MTQzQzQxLjUwNjUgMTUuNTMzOCA0MS43MDI3IDE0LjcyMDYgNDEuMzIyNiAxNC4wOTc5QzQwLjk0MjYgMTMuNDc1MyA0MC4xMzAzIDEzLjI3ODkgMzkuNTA4MyAxMy42NTk0QzM4LjUxNiAxNC4yNjYzIDM3LjY0NSAxNC42MTc1IDM1LjkyOSAxNC42MTc1QzMzLjk0MyAxNC42MTc1IDMyLjIyMTEgMTMuNDExNyAzMS42MjI3IDExLjcxMDhaTTM1Ljc5NzEgNi4xNjE1M0MzMy44MjE5IDYuMTYxNTMgMzIuMTkxMyA3LjM5Nzg3IDMxLjYxODEgOS4wNjgyN0gzOS45NzZDMzkuNDAyOSA3LjM5Nzg3IDM3Ljc3MjMgNi4xNjE1MyAzNS43OTcxIDYuMTYxNTNaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yMy45OTgyIDYuNDI1ODFMMTcuMzE5OSA2LjQyNTgyQzE2LjU5MSA2LjQyNTgyIDE2LjAwMDEgNS44MzQyOCAxNi4wMDAxIDUuMTA0NThDMTYuMDAwMSA0LjM3NDg3IDE2LjU5MSAzLjc4MzMzIDE3LjMxOTkgMy43ODMzM0gyNi45OTg0QzI3LjUyMTggMy43ODMzMiAyNy45OTU3IDQuMDkyOTQgMjguMjA2NSA0LjU3MjU1QzI4LjQxNzIgNS4wNTIxNiAyOC4zMjQ5IDUuNjExMTIgMjcuOTcxMyA1Ljk5NzM3TDIwLjMyMDEgMTQuMzUzM0gyNi45OTg0QzI3LjcyNzMgMTQuMzUzMyAyOC4zMTgyIDE0Ljk0NDggMjguMzE4MiAxNS42NzQ1QzI4LjMxODIgMTYuNDA0MiAyNy43MjczIDE2Ljk5NTggMjYuOTk4NCAxNi45OTU4SDE3LjMxOThDMTYuNzk2NCAxNi45OTU4IDE2LjMyMjUgMTYuNjg2MSAxNi4xMTE4IDE2LjIwNjVDMTUuOTAxIDE1LjcyNjkgMTUuOTkzMyAxNS4xNjggMTYuMzQ2OSAxNC43ODE3TDIzLjk5ODIgNi40MjU4MVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMTMzMzIgNS43OTk5OUMzLjg0NDY2IDUuNzk5OTkgMi43OTk5OSA2Ljg0NDY2IDIuNzk5OTkgOC4xMzMzMkMyLjc5OTk5IDkuNDIxOTkgMy44NDQ2NiAxMC40NjY3IDUuMTMzMzIgMTAuNDY2N0M2LjQyMTk5IDEwLjQ2NjcgNy40NjY2NSA5LjQyMTk5IDcuNDY2NjUgOC4xMzMzMkM3LjQ2NjY1IDYuODQ0NjYgNi40MjE5OSA1Ljc5OTk5IDUuMTMzMzIgNS43OTk5OVpNMCA4LjEzMzMyQzAgNS4yOTgyNyAyLjI5ODI3IDMgNS4xMzMzMiAzQzcuOTY4MzggMyAxMC4yNjY2IDUuMjk4MjcgMTAuMjY2NiA4LjEzMzMyQzEwLjI2NjYgMTAuOTY4NCA3Ljk2ODM4IDEzLjI2NjYgNS4xMzMzMiAxMy4yNjY2QzIuMjk4MjcgMTMuMjY2NiAwIDEwLjk2ODQgMCA4LjEzMzMyWiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KCTxwYXRoIGQ9Ik03LjAwMDA4IDE0LjJIMy4yNjY3NkMyLjQ5MzU2IDE0LjIgMS44NjY3NiAxNC44MjY4IDEuODY2NzYgMTUuNkMxLjg2Njc2IDE2LjM3MzIgMi40OTM1NiAxNyAzLjI2Njc2IDE3SDcuMDAwMDhDNy43NzMyOCAxNyA4LjQwMDA4IDE2LjM3MzIgOC40MDAwOCAxNS42QzguNDAwMDggMTQuODI2OCA3Ljc3MzI4IDE0LjIgNy4wMDAwOCAxNC4yWiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPC9zdmc+" /> <a  href="https://zencastr.com/embed/TauJ5XDW"  target="_blank"  style="color: white; position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); text-decoration: none;" >  View on Zencastr </a></blockquote><script type="text/javascript" src="https://zencastr.com/static/js/embed-player.js"></script> 
</h2>


# Show Notes

## Episode Intro
Paul - thank you and FullControl follow-up
* Paul printed the latest model, AnyAngle Phone Stand
  * Printed flawlessly at double speed!
* Thank you to [Brian Okken and Michael Kennedy of Python Bytes](https://pythonbytes.fm) for thee podcast's inspiration.

### PixelBlaze expression language (Tod #1) 1:45
  * [Lux Lavelier](https://luxlavalier.com/) wearable LED pendant
  * [Lux Lavalier Patterns guide](https://luxlavalier.com/patterns)
  * Lux Lavelier created by [GeekMomProjects (Debra Ansell)](https://www.geekmomprojects.com), [Ben Henke](https://www.bhencke.com/), [Jason Coon](https://www.evilgeniuslabs.org/)
  * [Pixelblaze](https://electromage.com/pixelblaze)
  * [Huge online library of Pixelblaze patterns](https://electromage.com/patterns)
  * [Fibonacci LED displays](https://www.tindie.com/stores/jasoncoon/)
  * [3d-printable magnetic battery holder](https://www.geekmomprojects.com/3d-printed-wearable-battery-holder/)


### Whisper OpenAI (Paul #1) 5:50
  * Blog post, paper and Google Colab example linked from their [GitHub repository](https://github.com/openai/whisper) 
    * From OpenAI, who developed Dall-E
  * [Hackaday story](https://hackaday.com/2022/09/22/openai-hears-you-whisper/)
  * Built with Python 3.9.9 and PyTorch 1.10.1
    * [Meta transfers PyTorch to Linux Foundation](https://www.hackster.io/news/meta-passes-pytorch-the-python-machine-learning-framework-to-the-linux-foundation-d48166c66500)
  * 5 models from tiny size to large - the smaller the model, the faster it is and less memory needed but the fewer words it knows 
  * * Trained on 680,000 hours of audio
  * Benefits
    * Accessibility!
    * Transcription
      * Text and VTT files
    * Translation
  * MIT Licensed, people already building on top of it:
    * [Show & Tell forum](https://github.com/openai/whisper/discussions/categories/show-and-tell)
    * [Twitter bot that extracts videos, translates and replies from a translated video](https://github.com/openai/whisper/discussions/232)
    * [Command line utility to transcribe or translate audio from livestreams in real time](https://github.com/fortypercnt/stream-translator)
    * [Subtitles in DaVinci Resolve](https://github.com/octimot/StoryToolkitAI)
      * [Announcement](https://github.com/openai/whisper/discussions/226)
  * Downsides
    * [No Speaker tagging](https://github.com/openai/whisper/discussions/104)
    * Slow if not on GPU

### Music generation in the browser (Tod #2) 11:03
  * [SuperCollider](https://github.com/supercollider/supercollider), an open source audio programming language from the 90s
  * [TidalCycles](http://tidalcycles.org/), a musiclive coding environment using SuperCollider
  * [Sonic Pi](https://sonic-pi.net/) basically an easier-to-install version of TidalCycles
  * [Tone.js](https://tonejs.github.io/) in-browser synthesis, used by the following:
  * [Acid Hit](https://cdm.link/2022/09/free-acid-303-browser)
  * [Pi Songs](https://pisongs.com/) by Canton Becker
  * [Shepard's Pi "Play something no one has ever heard before"](https://pisongs.com/shepardspi/?position=575912300&t=1664758364)
  * [Strudel music live coding](https://loophole-letters.vercel.app/strudel)
    - Example played in show: `stack("c4 f3 g4 a#4", "c2 g2".slow(2)).echo(4, 1/8, .5)`

### PolyKeyboard (Paul #2) 16:41
  * [Poly Keyboard with OLED keycaps)](https://www.tomshardware.com/news/raspberry-pi-pico-keyboard-with-oled-keycaps)
  * [Keycap demo on Twitter](https://twitter.com/thpoll2/status/1573260216426430465)
    * Split keyboard design
    * rp2040 powered
    * Bring your own key switches and keycaps (the flex cable needs to fit though the RGB slit of the key switch)
      * Compatibility chart for key switches available - needs 8.MM slit for the LED
      * Needs a 3D printed stem
    * OLED is custom with a flex cable
  * [Blog and Ko-Fi](https://ko-fi.com/polykb)
    * [Blog post comparing other keyboards](https://ko-fi.com/post/Comparing-With-Existing-Projects-S6S4F9Z98)

### Samplebrain by Aphex Twin & Dave Griffiths 21:27
  * [Samplebrain Homepage](https://thentrythis.org/projects/samplebrain/)
  * [Samplebrain manual](https://gitlab.com/then-try-this/samplebrain/-/blob/main/docs/manual.md)
  * [Good CDM article about Samplebrain](https://cdm.link/2022/09/free-sample-mashing-with-samplebrain-by-aphex-twin-and-dave-griffiths/)
  * [Aphex Twin (Richard D James)](https://www.youtube.com/channel/UC4hfA78X-lqiRERBZLTnLBw) makes weird & interesting techno & ambient music

### Kevin McAleer and the Pikon 23:48
  * [Pikon story on DigitalCameraWorld.com](https://www.digitalcameraworld.com/news/robot-builder-shares-raspberry-pi-pikon-high-quality-camera-in-3d-printed-casing)
  * [Kevin's Homepage](http://www.kevsrobots.com/)
    * [Kevin's YouTube Channel](https://www.youtube.com/c/kevinmcaleer28/)
  * So many cool projects!
    * Robots and more robots!
    * [Pomodoro Pico W Desk Robot](https://www.youtube.com/watch?v=MWg1xdmgE04)
  * [Kevin's Pikon video](https://www.youtube.com/watch?v=4BEjKUK8DSQ)
    * [Blog post](http://www.kevsrobots.com/blog/pikon-camera.html) 
    * [Raspberry Pi News Story](https://www.raspberrypi.com/news/3d-printed-pikon-camera/)
  * Next Steps
    * Python app for the Raspberry Pi to record video clips, photos and apply filters, and possibly use to livestream.


### Sponsor The Bootloader

Your financial sponsorship helps with the cost of hosting, recording and transcripts.  Thank you for your support!

[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/prcutler)
