## Code and colours

Colours can be represented in different ways:

- Colour names like 'red'
- RGB colour values from 0 to 255, e.g. (255, 0, 0)
- RGB colour values from 0 to 1, e.g. (1, 0, 0)
- Hex colour codes like #f00 or #ff0000

--- task ---

Open **Mu** from the main menu. Click the **REPL** icon to open up a Python shell.

--- /task ---

--- task ---

Import the `colorzero` library by typing:

```python
from colorzero import Color
```

--- /task ---

--- task ---

Create a colour object with the word 'red':

```python
c = Color('red')
```

--- /task ---

--- task ---

Inspect the different representations of the colour by typing each of these in turn:

```python
c.rgb
c.rgb_bytes
c.html
```

--- /task ---

--- task ---

You should see the colour red represented in different ways. Try the same with a different colour name.

--- /task ---

--- task ---

The Sense HAT library expects RGB values from 0 to 255. Try setting the LEDs to different colours using:

```python
from sense_hat import SenseHat
from colorzero import Color

sense = SenseHat()

color = Color('red')

sense.clear(color.rgb_bytes)
```

--- /task ---
