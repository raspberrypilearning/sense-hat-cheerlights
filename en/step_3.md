## Code and colours

Colours can be represented in different ways:

- Colour names like "red"
- RGB colour values 0-255 like (255, 0, 0)
- RGB colour values 0-1 like (1, 0, 0)
- Hex colour codes like #f00 or #ff0000

1. Open **Mu** from the taskbar

1. Click the **REPL** icon to open up a Python shell

1. Import the `colourzero` library by typing:

    ```python
    from colorzero import Color
    ```

1. Create a colour object with the word "red":

    ```python
    c = Color('red')
    ```

1. Inspect the different representations of the colour by typing each of these in turn:

    ```python
    c.rgb
    c.rgb_bytes
    c.html
    ```

1. You should see the color red represented in different ways. Try the same with a different colour name.

1. The Sense HAT library expects 0-255 RGB values. Try setting the LEDs to different colours using:

    ```python
    from sense_hat import SenseHat
    from colorzero import Color

    sense = SenseHat()

    color = Color('red')

    sense.clear(color.rgb_bytes)
    ```
