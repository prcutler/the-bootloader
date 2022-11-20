---
date: 2022-11-21
title: "Episode 5: Pandas and Breadboards"
linkTitle: "Episode 5"
description: "Pandas and Breadboards"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---
## Welcome
Welcome to The Bootloader, a bi-weekly podcast bringing you news, project updates, and product talk
from the tech and maker scenes.  Paul and Tod will bring you three interesting things and chat about them for a few minutes each.

[Full transcript available here](https://thebootloader.net/blog/2022/11/21/episode-5-transcript/).

<blockquote class="zenplayer" data-episode-href="https://zencastr.com/embed/PAqwzCPC" style="background: black; border-radius: 12px; font-family: system-ui; width: 480px; height: 480px; position: relative; color: white; margin: 0;"> <img  style="width: 120px; display: inline-block; position: absolute; top: calc(50%); left: calc(50%); transform: translate(-50%, -50%);"  src="data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTE5IDE4IiBoZWlnaHQ9IjEwMCIgd2lkdGg9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTE1LjQyNSA2LjQyNTgxQzExNC4yMSA2LjQyNTgxIDExMy4yMjUgNy40MTE3MSAxMTMuMjI1IDguNjI3ODhWMTUuNjc0NUMxMTMuMjI1IDE2LjQwNDIgMTEyLjYzNSAxNi45OTU4IDExMS45MDYgMTYuOTk1OEMxMTEuMTc3IDE2Ljk5NTggMTEwLjU4NiAxNi40MDQyIDExMC41ODYgMTUuNjc0NVY4LjYyNzg4QzExMC41ODYgNS45NTIzMSAxMTIuNzUyIDMuNzgzMzMgMTE1LjQyNSAzLjc4MzMzSDExNy4xODVDMTE3LjkxNCAzLjc4MzMzIDExOC41MDUgNC4zNzQ4NyAxMTguNTA1IDUuMTA0NTdDMTE4LjUwNSA1LjgzNDI3IDExNy45MTQgNi40MjU4MSAxMTcuMTg1IDYuNDI1ODFIMTE1LjQyNVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwMi4yMjcgMC4yNjAwMUMxMDIuOTU2IDAuMjYwMDEgMTAzLjU0NyAwLjg1MTU1MSAxMDMuNTQ3IDEuNTgxMjVWMy43ODMzM0gxMDcuNTA2QzEwOC4yMzUgMy43ODMzMyAxMDguODI2IDQuMzc0ODcgMTA4LjgyNiA1LjEwNDU3QzEwOC44MjYgNS44MzQyNyAxMDguMjM1IDYuNDI1ODEgMTA3LjUwNiA2LjQyNTgxSDEwMy41NDdWMTEuMjcwNEMxMDMuNTQ3IDEyLjk3MyAxMDQuOTI2IDE0LjM1MzMgMTA2LjYyNyAxNC4zNTMzSDEwNy41MDZDMTA4LjIzNSAxNC4zNTMzIDEwOC44MjYgMTQuOTQ0OCAxMDguODI2IDE1LjY3NDVDMTA4LjgyNiAxNi40MDQyIDEwOC4yMzUgMTYuOTk1OCAxMDcuNTA2IDE2Ljk5NThIMTA2LjYyN0MxMDMuNDY4IDE2Ljk5NTggMTAwLjkwNyAxNC40MzI0IDEwMC45MDcgMTEuMjcwNFYxLjU4MTI1QzEwMC45MDcgMC44NTE1NTEgMTAxLjQ5OCAwLjI2MDAxIDEwMi4yMjcgMC4yNjAwMVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBkPSJNODguMzk0OCAxNS45MjFDODkuOTc4NiAxNi44ODk5IDkxLjU4MDggMTcuMjYgOTMuNjkyNCAxNy4yNkM5Ni4yNDQxIDE3LjI2IDk5LjU4NzYgMTYuMjAzIDk5LjU4NzYgMTMuMTIwMUM5OS41ODc2IDcuMzk0NjkgOTAuMzQ4OSAxMC4zODk1IDkwLjM0ODkgNy44MzUxQzkwLjM0ODkgNy4wNDIzNiA5MS41ODA4IDYuMTYxNTMgOTMuNDI4NSA2LjE2MTUzQzk0LjU3MjMgNi4xNjE1MyA5Ni4xMTIxIDYuNjkwMDMgOTYuNzI4IDcuMTMwNDRDOTcuMzU5MiA3LjQ5NTI5IDk4LjE2NzMgNy4yNzc5MiA5OC41MzE3IDYuNjQ1OThDOTguODk2MiA2LjAxNDAzIDk4LjY3OSA1LjIwNTE0IDk4LjA0NzggNC44NDAyOUM5Ni43MjggMy45NTk0NiA5NS4xMDAyIDMuNTE5MDQgOTMuNDI4NSAzLjUxOTA0QzkwLjI2MSAzLjUxOTA0IDg3LjcwOTMgNS40NTY4NyA4Ny43MDkzIDcuODM1MUM4Ny43MDkzIDEzLjM4NDMgOTYuOTQ4IDEwLjU2NTcgOTYuOTQ4IDEzLjEyMDFDOTYuOTQ4IDE0LjAwMDkgOTUuNTQwMiAxNC42MTc1IDkzLjY5MjQgMTQuNjE3NUM5Mi4wMjA3IDE0LjYxNzUgOTAuOTQ2NCAxNC4zMzU1IDg5LjYyNjYgMTMuNjMwOUM4OS4wMTA3IDEzLjI3ODUgODguMjE4OCAxMy41NDI4IDg3Ljg2NjkgMTQuMTU5NEM4Ny41MTQ5IDE0Ljc3NiA4Ny43Nzg5IDE1LjU2ODcgODguMzk0OCAxNS45MjFaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04My4zMSAxNS41Nzc0QzgyLjE0MzggMTYuNjI1NSA4MC42MjA5IDE3LjI2IDc4Ljk1NDYgMTcuMjZDNzUuMjg1OCAxNy4yNiA3Mi4zMTE2IDE0LjE4NCA3Mi4zMTE2IDEwLjM4OTVDNzIuMzExNiA2LjU5NTA2IDc1LjI4NTggMy41MTkwNCA3OC45NTQ2IDMuNTE5MDRDODAuNjIwOSAzLjUxOTA0IDgyLjE0MzggNC4xNTM1MSA4My4zMSA1LjIwMTZWNS4xMDQ1NEM4My4zMSA0LjM3NDgzIDgzLjkwMDggMy43ODMyOSA4NC42Mjk4IDMuNzgzMjlDODUuMzU4NyAzLjc4MzI5IDg1Ljk0OTUgNC4zNzQ4MyA4NS45NDk1IDUuMTA0NTRWMTUuNjc0NUM4NS45NDk1IDE2LjQwNDIgODUuMzU4NyAxNi45OTU3IDg0LjYyOTggMTYuOTk1N0M4My45MDA4IDE2Ljk5NTcgODMuMzEgMTYuNDA0MiA4My4zMSAxNS42NzQ1VjE1LjU3NzRaTTgzLjY2MTkgMTAuMzg5NUM4My42NjE5IDEyLjcyNDYgODEuNzEyIDE0LjYxNzUgNzkuMzA2NiAxNC42MTc1Qzc2LjkwMTIgMTQuNjE3NSA3NC45NTEyIDEyLjcyNDYgNzQuOTUxMiAxMC4zODk1Qzc0Ljk1MTIgOC4wNTQ0NiA3Ni45MDEyIDYuMTYxNTMgNzkuMzA2NiA2LjE2MTUzQzgxLjcxMiA2LjE2MTUzIDgzLjY2MTkgOC4wNTQ0NiA4My42NjE5IDEwLjM4OTVaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik02Ni4zMjg1IDYuMTYxNTNDNjMuODU5NiA2LjE2MTUzIDYxLjkyOTIgOC4wOTMwOCA2MS45MjkyIDEwLjM4OTVDNjEuOTI5MiAxMi42ODU5IDYzLjg1OTYgMTQuNjE3NSA2Ni4zMjg1IDE0LjYxNzVDNjcuNTY3NyAxNC42MTc1IDY4LjY4ODcgMTQuMjYyNyA2OS41NjYyIDEzLjY4ODlDNzAuMTc2NSAxMy4yODk5IDcwLjk5NDQgMTMuNDYxNyA3MS4zOTI5IDE0LjA3MjdDNzEuNzkxNSAxNC42ODM2IDcxLjYxOTkgMTUuNTAyNCA3MS4wMDk2IDE1LjkwMTRDNjkuNjkyOSAxNi43NjIyIDY4LjA2ODQgMTcuMjYgNjYuMzI4NSAxNy4yNkM2Mi40ODAyIDE3LjI2IDU5LjI4OTYgMTQuMjIyNiA1OS4yODk2IDEwLjM4OTVDNTkuMjg5NiA2LjU1NjQ0IDYyLjQ4MDIgMy41MTkwNCA2Ni4zMjg1IDMuNTE5MDRDNjguMDY4NCAzLjUxOTA0IDY5LjY5MjkgNC4wMTY4NCA3MS4wMDk2IDQuODc3NjVDNzEuNjE5OSA1LjI3NjY1IDcxLjc5MTUgNi4wOTUzOCA3MS4zOTI5IDYuNzA2MzRDNzAuOTk0NCA3LjMxNzI5IDcwLjE3NjUgNy40ODkxMSA2OS41NjYzIDcuMDkwMTFDNjguNjg4NyA2LjUxNjM2IDY3LjU2NzcgNi4xNjE1MyA2Ni4zMjg1IDYuMTYxNTNaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZD0iTTU1LjgxNDEgMTYuODE5QzU1LjQxOTYgMTYuNTkwNSA1NS4xNTQyIDE2LjE2MzUgNTUuMTU0MiAxNS42NzQ1VjEwLjEyNTNDNTUuMTU0MiA3LjkzNjE1IDUzLjM4MTUgNi4xNjE1MyA1MS4xOTQ4IDYuMTYxNTNDNDkuMDA4MSA2LjE2MTUzIDQ3LjIzNTQgNy45MzYxNSA0Ny4yMzU0IDEwLjEyNTNWMTUuNjc0NUM0Ny4yMzU0IDE2LjE2MzUgNDYuOTcgMTYuNTkwNSA0Ni41NzU1IDE2LjgxOUM0Ni4zODEzIDE2LjkzMTQgNDYuMTU2IDE2Ljk5NTcgNDUuOTE1NiAxNi45OTU3QzQ1LjE4NjcgMTYuOTk1NyA0NC41OTU4IDE2LjQwNDIgNDQuNTk1OCAxNS42NzQ1VjUuMTA0NTRDNDQuNTk1OCA0LjM3NDgzIDQ1LjE4NjcgMy43ODMyOSA0NS45MTU2IDMuNzgzMjlDNDYuNjQ0NSAzLjc4MzI5IDQ3LjIzNTQgNC4zNzQ4MyA0Ny4yMzU0IDUuMTA0NTRWNS4zMDgyNEM0OC4yMDI3IDQuMjExMDUgNDkuNjE4IDMuNTE5MDQgNTEuMTk0OCAzLjUxOTA0QzU0LjgzOTMgMy41MTkwNCA1Ny43OTM4IDYuNDc2NzUgNTcuNzkzOCAxMC4xMjUzVjE1LjY3NDVDNTcuNzkzOCAxNi40MDQyIDU3LjIwMjkgMTYuOTk1NyA1Ni40NzQgMTYuOTk1N0M1Ni4yMzM2IDE2Ljk5NTcgNTYuMDA4MiAxNi45MzE0IDU1LjgxNDEgMTYuODE5WiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KCTxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMzEuNjIyNyAxMS43MTA4SDQxLjUxNjJDNDIuMjQ1MSAxMS43MTA4IDQyLjgzNiAxMS4xMTkyIDQyLjgzNiAxMC4zODk1QzQyLjgzNiA2LjU1NjQ0IDM5LjY0NTQgMy41MTkwNCAzNS43OTcxIDMuNTE5MDRDMzEuOTQ4NyAzLjUxOTA0IDI4Ljc1ODEgNi41NTY0NCAyOC43NTgxIDEwLjM4OTVDMjguNzU4MSAxNC40MjU2IDMyLjIyNDMgMTcuMjYgMzUuOTI5IDE3LjI2QzM4LjE3MjUgMTcuMjYgMzkuNTE1IDE2Ljc1MTkgNDAuODg0NSAxNS45MTQzQzQxLjUwNjUgMTUuNTMzOCA0MS43MDI3IDE0LjcyMDYgNDEuMzIyNiAxNC4wOTc5QzQwLjk0MjYgMTMuNDc1MyA0MC4xMzAzIDEzLjI3ODkgMzkuNTA4MyAxMy42NTk0QzM4LjUxNiAxNC4yNjYzIDM3LjY0NSAxNC42MTc1IDM1LjkyOSAxNC42MTc1QzMzLjk0MyAxNC42MTc1IDMyLjIyMTEgMTMuNDExNyAzMS42MjI3IDExLjcxMDhaTTM1Ljc5NzEgNi4xNjE1M0MzMy44MjE5IDYuMTYxNTMgMzIuMTkxMyA3LjM5Nzg3IDMxLjYxODEgOS4wNjgyN0gzOS45NzZDMzkuNDAyOSA3LjM5Nzg3IDM3Ljc3MjMgNi4xNjE1MyAzNS43OTcxIDYuMTYxNTNaIiBmaWxsPSJ3aGl0ZSI+PC9wYXRoPgoJPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yMy45OTgyIDYuNDI1ODFMMTcuMzE5OSA2LjQyNTgyQzE2LjU5MSA2LjQyNTgyIDE2LjAwMDEgNS44MzQyOCAxNi4wMDAxIDUuMTA0NThDMTYuMDAwMSA0LjM3NDg3IDE2LjU5MSAzLjc4MzMzIDE3LjMxOTkgMy43ODMzM0gyNi45OTg0QzI3LjUyMTggMy43ODMzMiAyNy45OTU3IDQuMDkyOTQgMjguMjA2NSA0LjU3MjU1QzI4LjQxNzIgNS4wNTIxNiAyOC4zMjQ5IDUuNjExMTIgMjcuOTcxMyA1Ljk5NzM3TDIwLjMyMDEgMTQuMzUzM0gyNi45OTg0QzI3LjcyNzMgMTQuMzUzMyAyOC4zMTgyIDE0Ljk0NDggMjguMzE4MiAxNS42NzQ1QzI4LjMxODIgMTYuNDA0MiAyNy43MjczIDE2Ljk5NTggMjYuOTk4NCAxNi45OTU4SDE3LjMxOThDMTYuNzk2NCAxNi45OTU4IDE2LjMyMjUgMTYuNjg2MSAxNi4xMTE4IDE2LjIwNjVDMTUuOTAxIDE1LjcyNjkgMTUuOTkzMyAxNS4xNjggMTYuMzQ2OSAxNC43ODE3TDIzLjk5ODIgNi40MjU4MVoiIGZpbGw9IndoaXRlIj48L3BhdGg+Cgk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTUuMTMzMzIgNS43OTk5OUMzLjg0NDY2IDUuNzk5OTkgMi43OTk5OSA2Ljg0NDY2IDIuNzk5OTkgOC4xMzMzMkMyLjc5OTk5IDkuNDIxOTkgMy44NDQ2NiAxMC40NjY3IDUuMTMzMzIgMTAuNDY2N0M2LjQyMTk5IDEwLjQ2NjcgNy40NjY2NSA5LjQyMTk5IDcuNDY2NjUgOC4xMzMzMkM3LjQ2NjY1IDYuODQ0NjYgNi40MjE5OSA1Ljc5OTk5IDUuMTMzMzIgNS43OTk5OVpNMCA4LjEzMzMyQzAgNS4yOTgyNyAyLjI5ODI3IDMgNS4xMzMzMiAzQzcuOTY4MzggMyAxMC4yNjY2IDUuMjk4MjcgMTAuMjY2NiA4LjEzMzMyQzEwLjI2NjYgMTAuOTY4NCA3Ljk2ODM4IDEzLjI2NjYgNS4xMzMzMiAxMy4yNjY2QzIuMjk4MjcgMTMuMjY2NiAwIDEwLjk2ODQgMCA4LjEzMzMyWiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KCTxwYXRoIGQ9Ik03LjAwMDA4IDE0LjJIMy4yNjY3NkMyLjQ5MzU2IDE0LjIgMS44NjY3NiAxNC44MjY4IDEuODY2NzYgMTUuNkMxLjg2Njc2IDE2LjM3MzIgMi40OTM1NiAxNyAzLjI2Njc2IDE3SDcuMDAwMDhDNy43NzMyOCAxNyA4LjQwMDA4IDE2LjM3MzIgOC40MDAwOCAxNS42QzguNDAwMDggMTQuODI2OCA3Ljc3MzI4IDE0LjIgNy4wMDAwOCAxNC4yWiIgZmlsbD0id2hpdGUiPjwvcGF0aD4KPC9zdmc+" /> <a  href="https://zencastr.com/embed/PAqwzCPC"  target="_blank"  style="color: white; position: absolute; bottom: 12px; left: 50%; transform: translateX(-50%); text-decoration: none;" >  View on Zencastr </a></blockquote><script type="text/javascript" src="https://zencastr.com/static/js/embed-player.js"></script> 

# Show Notes

## Episode Intro
Welcome!

### [Micropython by Arduino Labs](https://blog.arduino.cc/2022/11/10/micropython-officially-becomes-part-of-the-arduino-ecosystem/) (Tod #1)
  * It works well! Simple and clean, with what you need: code editor + terminal window
  * Works with any MicroPython device with USB serial, from my limited testing
  * No serial plotter, no library manager, no board manager. This is a first step
  * However, it is yet-another-[Electron](https://www.electronjs.org/) app, so it's fairly pudgy memory-wise
  * Alternatives:
    * [Thonny](https://thonny.org/) -- beloved by many. I do not like it, find it unattractive and confusing
    * [Mu](https://codewith.mu/) -- cleaner and has a nice serial plotter like Arduino IDE
    * Any text editor + [picotool](https://github.com/raspberrypi/picotool) -- my preferred choice
    * What I do not recommend: any "micropython extension" for VS Code/Atom/etc.
      The ones I've tried are flaky and presume too much, taking over other Python projects

### Home Assistant and the [State of the Open Home](https://www.youtube.com/watch?v=D936T1Ze8-4) (Paul #1)
  * Home automation platform focused on local control and privacy
    * No vendor log-in
    * Your smart home shouldn't require the cloud
  * State of the Open Home is an annual look at the smart home ecosystem and Home Assistant
    * Livestreamed Nov 13, 2022  
    * #2 open source project on Github by contributor contributions
    * Home Assistant Cloud from Nabu Casa processed 50,000 webhooks per second
    * 190,000 instances of HA opted in to reporting
      * Estimated 500,000 - 600,000 installations of HA
    * 2023: Year of Voice
      * Rhasspy voice assistant: https://github.com/rhasspy/rhasspy by Michael Hansen
        * Can function completely disconnected from the Internet
        * Are entirely free/open source with a permissive license (MIT)
        * Works well with freely available home automation software
        * Optimized for working with MQTT, HTTP and Websockets with Home Assistant having built in support
        * Support for over 25 different languages
      * Hired by Nabu Casa to work on and integrate Rhasspy full-time
      * [Summary video](https://www.youtube.com/watch?v=krQjw-j7rXI)

### [WithDiode.com](https://www.withdiode.com/explore) -- 3d breadboard simulation in the browser (Tod #2)
  * omg. this is the best. so fun
  * Created by [Kennth Cassel](https://twitter.com/KennethCassel)
    * (who also created a nice [Vim tutorial site called vim.so](https://www.vim.so/)
  * I saw it first from [Clive Thompson (@clive@saturation.social) on Mastodon](https://mastodon.social/@clive@saturation.social/109344907748519044)
  * I was able to implement some of the oscillators we did during
    [Deep Fried Neurons](https://blog.crashspace.org/tag/deep-fried-neurons/)
    * [DeepFriedNeurons breadboard oscillators](https://blog.crashspace.org/2021/05/dfn-happy-hour-no-43-good-vibrations/)
  * But... it's actually kinda harder to use than real breadboards
  * Other tools I find useful in this space:
    * [Wokwi simulator](https://wokwi.com/) lets you simulate Arduino, Micropython, and CircuitPython
    * [Fritzing](https://fritzing.org/) lets you visually breadboard up circuits,
      with accompanying breadboard & PCB layout

### GitHub in the news (Paul #2)
  * Follow-up: the investigation has spawned a [GitHub Copilot lawsuit](https://www.theregister.com/2022/11/11/githubs_copilot_opinion/)
    * [Verge](https://www.theverge.com/2022/11/8/23446821/microsoft-openai-github-copilot-class-action-lawsuit-ai-copyright-violation-training-data)
  * [Hey Github](https://githubnext.com/projects/hey-github)
    * Imagine being able to code hands free
    * This could be big for accessibility
    * Use natural speech, for example: Saying "Import pandas" results in `import pandas as pd`
    * In the features, Github shares:
      * Write / edit code (using GitHub Copilot)
      * Go to the next method with code navigation ("Hey GitHub go to line 34 or method X)
      * Run the program and control your IDE using any VS Code command
      * Code Summarization: Ask "Hey GitHub!" to explain lines 3-10 and get a summary of what the code does


### [RNBO "rainbow"](https://cycling74.com/products/rnbo) -- Turn Max patches into VST plugins (Tod #3)
  * Ever wonder how people make virtual synths / audio effects, or even real synths & effects?
  * [Max](https://cycling74.com/products/max) is a way to create custom virtual instruments or effects, and custom UI. Make it look like a real thing if you want
  * Max is often a good solution to mocking up ideas for these, kinda like CircuitPython and Arduino is for microcontroller projects
    * Max is a stand-alone application or part of Ableton Live
    * It's what's called a "patching environment", a "nodes & flows" graphical programming tool
    * The "flows" are audio & MIDI, kinda like modular synths cabling stuff together
    * I've used in on-n-off (mostly off) since the 90s (could never quite get into it)
    * But Max patches have to live inside Max (or inside Max in Live)
  * RNBO let's you create a "compilable" versions of Max patch
    * It is inclucded with Max or $299 for permanent license or $10/month subscription
    * RNBO is actually a parallel thing to Max, but implements most all of Max
    * But does Turns any Max patch into a C++-based stand-alone VST
    * Can even target Raspberry Pi, so you can make custom Pi-based synths & pedals
    * Or can export to Web Audio, with Javascript control!
  * [good CDM article about RNBO](https://cdm.link/2022/11/rnbo-max-for-web-hardware-plugin/)
  * [good synthanatomy article too](https://www.synthanatomy.com/2022/11/rnbo-turns-your-max-patches-into-hardware-vst-plugins-and-web-applications.html) about why this is cool
  * [Online (paid) class for how to use it by Music Hackspace](https://musichackspace.org/product/getting-started-with-rnbo-in-max/) Here's a [preview on youtube](https://www.youtube.com/watch?v=XK6crVcXefk)
  * Open source alternative to Max is [PureData (aka 'Pd')](https://puredata.info/)
    * Pd & Max have common roots, Pd is a bit rougher looking than Max, but very capable
    * And it runs on a Raspberry Pi
    * And there's a [huge community](https://patchstorage.com/explore) of existing Pd patches.
    * And there's the [free online Heavy compiler](https://www.rebeltech.org/2018/09/12/compile-pure-data-patches-with-free-online-heavy-compiler/) for Pd patches

### Mastodon (Paul #3)
  * [Hope for a Post-Musk Net](https://medium.com/whither-news/hope-for-a-post-musk-net-f156d0cdf431) by Jeff Jarvis
  * [Choosing a Mastodon instane by Sage Sharp](https://twitter.com/_sagesharp_/status/1592188538921316352)
  * [A Warning about Mastodon.social by Sumuna Harihareswara](https://www.harihareswara.net/posts/2022/mastodon-fediverse-warning-mastodonsocial/)
  * [How to Move from Twitter to Mastodon - Toms Hardware by Les Pounder](https://www.tomshardware.com/how-to/move-from-twitter-to-mastodon)
  * [How to get Started on Mastodon - Wired by Justin Pot](https://www.wired.com/story/how-to-get-started-use-mastodon/)

### Support Sponsor The Bootloader

If you like what you hear, one of the best things you can do to help the show is tell a friend or write a review.

Consider supporting the show financially - your support helps with the cost of hosting, recording and transcripts.  Thank you for your support!

[![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/prcutler)
