# Detect and Stop

In this program, we move the robot forward until it sees green, then stop the robot.

You can use [this GearsBot world](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Ffiles.aposteriori.com.sg%2Fget%2FA4uymkuMAk.json) for easy testing.
If you choose to use a physical robot, be sure to measure the RGB value of your green and modify the program accordingly.

```python
#!/usr/bin/env pybricks-micropython

# Import the necessary libraries
from pybricks.parameters import *
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Create the sensors and motors objects
ev3 = EV3Brick()

motorA = Motor(Port.A)
motorB = Motor(Port.B)

color_sensor_in1 = ColorSensor(Port.S1)
ultrasonic_sensor_in2 = UltrasonicSensor(Port.S2)
gyro_sensor_in3 = GyroSensor(Port.S3)

# Create a drive base

robot = DriveBase(motorA, motorB, 56, 152)

# Here is where your code starts

def is_green():
    color = color_sensor_in1.rgb()
    if 0 < color[0] < 8 and 85 < color[1] < 93 and 2 < color[2] < 10:
        return True
    else:
        return False

robot.drive(200, 0)
while is_green() == False:
    pass
robot.drive(0, 0)
```

Let's look at what each line does...

## is_green Function

```python
def is_green():
    color = color_sensor_in1.rgb()
    if 0 < color[0] < 8 and 85 < color[1] < 93 and 2 < color[2] < 10:
        return True
    else:
        return False
```

This bunch of code creates a new function named **is_green**.

`color = color_sensor_in1.rgb()` reads the RGB values from the color sensor and save it to a new variable named `color`.

`color`, `color[0]`, `color[1]`, `color[2]` the color sensors returns a tuple of 3 values; Red, Green, and Blue.
To access each individual value, we'll need to use an index.
`color[0]` means the first value (Red), `color[1]` means the second value (Green), and `color[2]` means the third value (Blue).

`0 < color[0] < 8` this checks if `color[0]` (red) is greater than 0 and less than 8.

`85 < color[1] < 93` this checks if `color[1]` (green) is greater than 85 and less than 93.

`2 < color[2] < 10` this checks if `color[2]` (blue) is greater than 2 and less than 10.

`if 0 < color[0] < 8 and 85 < color[1] < 93 and 2 < color[2] < 10:` here we check if all three colors are within the specified range.
We combine the 3 condition using the `and` operator, so ALL the individual conditions must be true for the overall condition to be true.

If all the conditions are true, we'll `return` a `True` value.
When a function `return`, it no longer run any more code within the function.

`else:` if the above condition is not true, the function will return a `False` value.

<div class="info">
True and False are special values in Python.
They must be spelt exactly as written, with the first letter capitalized.
</div>

<div class="info">
Where did we get the ranges for Red, Green, and Blue from?
Move the robot to the green area and use a print statement to display the rgb values for the color sensor.
Remember than sensors rarely give an exact value, so we need to use a suitable range to ensure our detection is robust.
</div>

## Move and Stop

```python
robot.drive(200, 0)
while is_green() == False:
    pass
robot.drive(0, 0)
```

`robot.drive(200, 0)` this starts the robot moving forward at a speed of 200 mm/s.
The second parameter is the rate of turn; zero in this case (ie. going straight)

`while is_green() == False:` as long as the `is_green()` returns `False`, we will repeat the code within the `while` loop.

The only line inside this `while` loop is a single `pass`.
`pass` is a special command that does... nothing.
We can't have an empty `while` loop, so we place a do-nothing `pass` inside.

`robot.drive(0, 0)` this stops the robot and hold the motor at its stop position.

## Challenges

* Modify the program so that the robot stops at the other colors

* Try [this all green world](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Ffiles.aposteriori.com.sg%2Fget%2FkKixmnYESi.json). All the colors are green. How can you program your robot to stop at the second or third green?
