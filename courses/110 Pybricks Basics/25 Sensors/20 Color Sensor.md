# Color Sensor

There are two main uses for the color sensors...

* To detect color of blocks
* To align the robot to the playfield (eg. black lines, red lines)

Both the EV3 and Spike Prime can return the **color** (...in the form of a code/object), **reflection** (...the amount of light reflected off a surface), and **ambient** (...the amount of light recieved from the environment).

Both sensors can also provide you with the raw color readings, but the EV3 color sensor returns values in **RGB format**, while the Spike Prime returns values in **HSV format**.
To convert from one to the other, you can refer to the section on [HSV and RGB](99-Special-Topics/20-HSV-and-RGB.html).

To understand the HSV format, you can play around [with this demo](https://math.hws.edu/graphicsbook/demos/c2/rgb-hsv.html).
Notice that...

* Changing **Hue** will change the color
* Reducing **Saturation** makes the color more "white". If saturation is zero, the color will be white regardless of hue.
* Reducing **Value** makes the color more "black". If value is zero, the color will be black regardless of hue or saturation.
* **Hue** ranges from 0 to 360, and a hue of 0 and 360 are identical (red).

## Initialize and Read the Color Sensor

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
#!/usr/bin/env pybricks-micropython

# Import the necessary libraries
from pybricks.parameters import *
from pybricks.ev3devices import *

# Initialize the sensor
color_sensor = ColorSensor(Port.S1)


# Here is where your code starts
if color_sensor.color() == Color.RED:
    print('color is red')
else:
    print('color not red')

print('reflection:', color_sensor.reflection())
print('ambient:', color_sensor.ambient())

color = color_sensor.rgb()
print('RGB (Red):', color[0])
print('RGB (Green):', color[1])
print('RGB (Blue):', color[2])
```

```python
# Import the necessary libraries
from pybricks.parameters import *
from pybricks.pupdevices import *

# Create the sensors and motors objects
color_sensor = ColorSensor(Port.C)


# Here is where your code starts
if color_sensor.color() == Color.RED:
    print('color is red')
else:
    print('color not red')

print('reflection:', color_sensor.reflection())
print('ambient:', color_sensor.ambient())

color = color_sensor.hsv()
print('HSV (Hue):', color.h)
print('HSV (Saturation):', color.s)
print('HSV (Value):', color.v)
```
</div>

### color()

The value returned by `color()` should only be compared to the properties in the `Color` object (eg. `color_sensor.color() == Color.RED`).
You can find a list of available colors here for [EV3](https://pybricks.com/ev3-micropython/parameters.html) and for [Spike Prime](https://docs.pybricks.com/en/stable/parameters/color.html).

<div class="important">
The colors are tuned for specific shades of Lego blocks and at a distance of around 1 to 3 cm.
This means that color() may be unreliable for non-Lego colors, Lego blocks of a different shade, or when detecting at a long or short distance.
For a more robust detection, you can use the RGB/HSV values and perform your own calibration.
</div>

### reflection()

Reflection is typically used in line following, where the line is black/white and you don't care about colors.
It'll return a value between 0 to 100; black will be close to zero and white close to 100.

On the EV3, reflection is based on the reflection of a **red** light, so a red surface will give a high value, similar to a white surface, while a green surface will give a low value, similar to a black surface.

On the Spike, reflection is based on the average of the Red, Green, Blue values.
This means that a white surface will give the highest reading, while a colored surface (eg. Yellow, Red) will give a lower value, while black will give the lowest value.

### ambient()

Ambient is useful when you want to measure the light level from the environment (eg. room light).

If you shine an external light on the sensor (eg. using a torchlight), you can use `ambient()` to detect when something crosses the light beam and cast a shadow on the sensor.

### Custom Color Detection with rgb() / hsv()

When detecting colors, it's best to use HSV values, as color is largely determined by Hue.
If you're using an EV3, you can convert the RGB values to HSV using the functions in [HSV and RGB](99-Special-Topics/20-HSV-and-RGB.html).

First, run the following code to print out the HSV value.
Run it multiple times with the sensor at different distances and position from the target.

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
print(rgb_to_hsv(color_sensor.rgb()))
```

```python
print(color_sensor.hsv())
```
</div>

Tested against a yellow surface, I got the following values (...on the EV3, the values will be formatted differently)...

```
Color(h=40, s=67, v=17)
Color(h=60, s=49, v=100)
Color(h=40, s=75, v=17)
Color(h=40, s=71, v=42)
Color(h=37, s=68, v=26)
Color(h=42, s=61, v=30)
```

* Hue: Range from 37 to 60
* Saturation: Minimum of 49
* Value: Minimum of 17

We can then write a function to check if a color is yellow...

<div class="important">
You should perform your own calibration!
There are many different shades of each color, so you may not get the same values.
</div>

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
def is_yellow(hsv):
    if (36 < hsv[0] < 61) and (48 < hsv[1]) and (16 < hsv[2]):
        return True
    else:
        return False
```

```python
def is_yellow(hsv):
    if (36 < hsv.h < 61) and (48 < hsv.s) and (16 < hsv.v):
        return True
    else:
        return False
```
</div>

Note that low saturation and value makes the color white and black respectively, but there are no issues if these values are high, so there's no need to set an upper limit.

Red is a little special, as the hue of red is either close to zero or close to 360...

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
def is_red(hsv):
    if (hsv[0] < 20 or hsv[0] > 340) and (49 < hsv[1]) and (17 < hsv[2]):
        return True
    else:
        return False
```

```python
def is_yellow(hsv):
    if (hsv.h < 20 or hsv.h > 340) and (49 < hsv.s) and (17 < hsv.v):
        return True
    else:
        return False
```
</div>

We can detect white by ignoring hue, and checking for a low saturation and high value...

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
def is_white(hsv):
    if (hsv[1] < 20) and (25 < hsv[2]):
        return True
    else:
        return False
```

```python
def is_white(hsv):
    if (hsv.s < 20) and (25 < hsv.v):
        return True
    else:
        return False
```
</div>

For black, the saturation and value will both be low...

<div class="tabs">
    <label>EV3</label>
    <label>Spike Prime</label>

```python
def is_black(hsv):
    if (hsv[1] < 20) and (hsv[2] < 20):
        return True
    else:
        return False
```

```python
def is_black(hsv):
    if (hsv.s < 20) and (hsv.v < 20):
        return True
    else:
        return False
```
</div>

If you need to differentiate between black and "nothing", you can do so by checking the value.
A black block will have a low value, but it will typically be at least 4 or 5.
If no blocks are present, the value would be even lower and may be zero.

Note that depending on the detection distance and material, it can be difficult to differentiate between black and no blocks.