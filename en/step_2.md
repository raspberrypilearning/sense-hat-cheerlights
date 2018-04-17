## What you will need

### Hardware

- Raspberry Pi
- Sense HAT

Alternatively, you can use the [Sense HAT emulator](http://sense-emu.readthedocs.io/) on a PC.

### Software

- Mu
- colorzero

To install colorzero, type the following into a terminal window and press <kbd>Enter</kbd>.

```bash
sudo apt install mu python3-colorzero
```

## Files

Download the starter code by entering the following into a terminal window:

```bash
mkdir cheerlights
cd cheerlights
wget http://rpf.io/shcheer -O cheerlights.py
wget http://rpf.io/shcheerauth -O auth.py
```

Create Twitter API keys (read-only) at [apps.twitter.com](https://apps.twitter.com/) and enter them into `auth.py`.
