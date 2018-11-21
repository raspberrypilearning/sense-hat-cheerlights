## Introduction

Tweet a colour to light up your Sense HAT!

--- collapse ---

---
title: What you will need
---

- Raspberry Pi computer
- Sense HAT

If you have a Raspberry Pi but no Sense HAT, you can use the Sense HAT emulator in Raspbian. Simply change the import line at the top of your code from:

`from sense_hat import SenseHat`

to:

`from sense_emu import SenseHat`

You'll need to install Mu and colorzero, and download the starter code. Open a Terminal window and enter the following commands:

```bash
sudo apt install mu python3-colorzero -y
cd mu_code
wget http://rpf.io/shcheer -O cheerlights.py
wget http://rpf.io/shcheerauth -O auth.py
```

Create Twitter API keys (read-only) at [apps.twitter.com](https://apps.twitter.com/) and enter them into `auth.py`.

For full instructions on setting up API keys, see the [Getting started with the Twitter API](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api) project.

--- /collapse ---

--- collapse ---

---
title: What you will learn
---

- Different ways to represent colours
- How to light up the Sense HAT display with a single colour
- How to connect to the Twitter API
- How to use tweets to control the colour of a Sense HAT

--- /collapse ---
