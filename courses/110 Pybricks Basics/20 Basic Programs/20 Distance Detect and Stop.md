# Detect and Stop

In this program, we move the robot forward until it sees the wall, then stop the robot.

You can use [GearsBot](https://gears.aposteriori.com.sg) for easy testing.
If you choose to use a physical robot, place a box infront of it to replicate a wall.

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

robot.drive(200, 0)
while ultrasonic_sensor_in2.distance() > 100:
    pass
robot.drive(0, 0)
```

Let's look at what each line does...

## DriveBase

```python
robot = DriveBase(motorA, motorB, 56, 152)
```

This creates an object that represents a two-wheeled robot.
The first two parameters are the left and right motors.
The third parameter is the size of the wheel.
The fourth parameter is the distance between the left and right wheel.

<div class="think">
The DriveBase provides convenient functions for moving a robot, but I personally feel that the choice of units for turns (deg/s) makes it difficult to use.
By default, GearsBot do not use the DriveBase and provides functions for replicating the move_tank and move_steering functions found in EV3Lab and EV3 Classroom.
</div>

## Move and Stop

```python
robot.drive(200, 0)
while ultrasonic_sensor_in2.distance() > 100:
    pass
robot.drive(0, 0)
```

`robot.drive(200, 0)` this starts the robot moving forward at a speed of 200 mm/s.
The second parameter is the rate of turn; zero in this case (ie. going straight)

<div class="think">
The standard EV3 wheel diameter is 56mm, and the maximum speed for the large motor is around 1000 deg/s.
What is the maximum speed (in mm/s) that the robot can move at?
</div>

`while ultrasonic_sensor_in2.distance() > 100:` as long as the distance is greater than 100mm, we will repeat the code within the `while` loop.

The only line inside this `while` loop is a single `pass`.
`pass` is a special command that does... nothing.
We can't have an empty `while` loop, so we place a do-nothing `pass` inside.

`robot.drive(0, 0)` this stops the robot and hold the motor at its stop position.
You can alternatively use `robot.stop()`, but this will not hold the motor in place, and the robot may coast forward a little. (Try it!)

## Challenges

* Program the robot to turn on the spot. Read the [Pybricks documentation site](https://pybricks.com/ev3-micropython/ev3devices.html) to see what method you can use for this.

* Program the robot to move in a curve to the left or right by adding a rate of turn to the `drive` method. Try different rate of turn and see how the robot behaves.