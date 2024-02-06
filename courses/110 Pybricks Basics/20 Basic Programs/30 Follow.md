# Follow

For this next challenge, use [this GearsBot world](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Ffiles.aposteriori.com.sg%2Fget%2Fvvj6X5nYNz.json).
If you're using a physical robot, you can simulate the moving green box by moving a box by hand.

This program makes the robot move forward if the green box is more than 150mm away, and back if it is less than 100mm away.

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

while True:
    dist = ultrasonic_sensor_in2.distance()
    if dist > 150:
        robot.drive(200, 0)
    elif dist > 100:
        robot.drive(0, 0)
    else:
        robot.drive(-200, 0)
```

Let's look at what each line does...

## while True

```python
while True:
```

A `while` loop will repeat as long as the provided condition is true.
Since `True` is always true, a `while True:` loop will repeat forever.

If you have used Scratch, this is similar to a repeat forever loop, but unlike Scratch, it is possible to exit a `while True:` loop by running a `break` command inside the loop.

## dist variable

```python
    dist = ultrasonic_sensor_in2.distance()
```

We will be comparing the distance multiple times later in the `if` statements, so here we read the distance once and store the result in the `dist` variable.
This is slighly more efficient than using `ultrasonic_sensor_in2.distance()` multiple times (...but it'll work even if you do that).

`dist` is just a name, and you can use any names that you like (eg. `how_far = ultrasonic_sensor_in2.distance()`), but it is always best to use a descriptive name that helps the reader of your code understand what is being stored.

## if elif else

```python
    if dist > 150:
        robot.drive(200, 0)
    elif dist > 100:
        robot.drive(0, 0)
    else:
        robot.drive(-200, 0)
```

`if dist > 150:` Here we first check if the distance is greater than 150mm.
If it is, we run `robot.drive(200, 0)` to start the robot moving forward at 200mm/s.

`elif dist > 100:` Else, if the distance is greater than 100mm (ie. it is between 100mm to 150mm), we'll stop the robot.

`else:` Else, if none of the conditions are true (ie. the distance is less than 100m), we'll move backwards.

Note the indentation of the code.
In Python, we use indents to indicate which statement comes under which condition.
Here's another example...

```python
if dist > 150:
    print('forward')
print('always')
```

In the above example, the word **forward** will only be printed if the distance is greater than 150, but the word **always** will always be printed as it is outside of the `if`.

## Comparison

The `>` symbol means **greater than**, just like in math.
So the line `if dist > 150:` is read as **if dist is greater than 150**.

Other available operators includes...

* `<` less than
* `>=` greater or equal to
* `<=` less than or equal to
* `==` exactly equal to
* `!=` not equal to

Note that when performing a comparison, we use double equals `==`.
A single equal `=` is used when assigning a value (eg. `a = 1` this assigns the value 1 to the variable **a**).

Some examples...

```python
if dist == 120:
    print('exactly 120')
elif dist <= 100:
    print('less than or equal to 100')
```

<div class="think">
When comparing sensor values, we rarely use ==, that's because the sensors don't return an exact integer value.
You may want your robot to stop when it is exactly 100mm from the wall, but will it ever get that value?
The robot may see 105.32mm, 102.51mm, 99.87mm, 98.11mm, etc... but may never land on exactly 100mm.
It's usually better to use a range instead.
</div>

## Jerky movements?

You may have noticed that the robot moves in a rather jerky manner when it is close to the wall.
That's because the robot is rapidly switching between moving and stopping when the distance is close to 150mm or 100mm.

We can make this smoother by adding more conditions...

```python hl_lines="3 4 7 8"
    if dist > 150:
        robot.drive(200, 0)
    elif dist > 125:
        robot.drive(150, 0)
    elif dist > 100:
        robot.drive(0, 0)
    elif dist > 75:
        robot.drive(-150, 0)
    else:
        robot.drive(-200, 0)
```

The above is a 5-states algorithm, as the robot can be in 5 different states (...speed of 200, 150, 0, -150, and -200), while the earlier algorithm is 3-states.

## Proportional Control and Math

We can make it the movement even smoother by adding more states, but this get rather tedious (...try creating a 21 states algorithm).
A better way is to make the robot's speed proportional to the distance.

```python
while True:
    dist = ultrasonic_sensor_in2.distance()
    error = dist - 100
    correction = error * 4
    robot.drive(correction, 0)
```

`error = dist - 100` Our desired distance is 100mm, and the **error** is the difference between the actual distance and the desired distance.

`correction = error * 4` The **correction** is what we apply to try and minimize our error.
To calculate our correction factor, we multiply the **error** by a value called the **gain**.
In this case, the **gain** is **4**.

<div class="note">
In programming, the * is the multiplication symbol, and the / is the division symbol.
</div>

`robot.drive(correction, 0)` In this case, we'll apply the correction to the robot's speed.
The larger the correction, the higher the speed.

To illustrate, let's imagine that the distance is 200mm.
This means that...

```python
error = dist - 100
error = 200 - 100   # dist is 200
error = 100
```

...and **correction**...

```python
correction = error * 4
correction = 100 * 4    # error is 100 as calculated above
correction = 400
```

...finally our speed...

```python
robot.drive(correction, 0)
robot.drive(400, 0)         # correction is 400
```

The robot drives forward at a speed of 400.
What happens when the distance is 100mm? Or 50mm?
Try to work through the math and figure it out.

## Challenges

* Experiment with different **gain** and observe how that affects the robot's behaviour.

* If the green box is far away, the speed (correction) may be very high.
We want the maximum speed to be 200 mm/s.
Can you use an `if` condition to check if the speed is greater than 200, and if it is, set it to 200?

* Similarly, we don't want the backwards speed to be lesser than -200.
Add appropriate code to limit the speed to not less than -200.