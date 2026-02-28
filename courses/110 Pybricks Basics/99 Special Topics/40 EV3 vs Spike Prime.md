# EV3 vs Spike Prime

Pybricks works largely the same on the EV3 and Spike, but there are a few differences that you need to watch out for.

## Hub

On the EV3, the hub is initialized using...

```python
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()
```

On the Spike Prime, the hub is initialized using...

```python
from pybricks.hubs import PrimeHub

hub = PrimeHub()
```

## Importing Devices

On the EV3, the devices (ie. motors and sensors) are imported using...

```python
from pybricks.ev3devices import *
```

On the Spike Prime, the devices are imported using...

```python
from pybricks.pupdevices import *
```

<div class="info">
"pup" stands for "Powered Up".
This is a series of Lego devices that uses the same type of connector (...like what the Spike Prime uses).
</div>

## Sensor Ports

On the EV3, the sensors ports are numbered (ie. 1, 2, 3), while the motor ports are alphabets (ie. A, B, C).
So on the EV3, you may initialize your motors and sensors like this...

```python
motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S1) # Number port
```

On the Spike, both motors and sensors shares the same alphabet ports, and you would initialize your motors and sensors like this...

```python
motor = Motor(Port.A)
color_sensor = ColorSensor(Port.B) # Alphabet port
```

## Motor Direction

Robots built using the EV3 large motors, would usually have both motors facing the **same** direction.
So this code would work fine...

```python
from pybricks.parameters import *
from pybricks.ev3devices import *
from pybricks.robotics import DriveBase

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

robot = DriveBase(left_motor, right_motor, 56, 152)
robot.straight(200)
```

But robots built using the Spike Prime large or medium motors, would usually have the motors facing **opposite** directions.
If you use the above code (...with the appropriate changes for Spike), you'll see one motor moving forward, while the other moves in reverse.

So for a Spike Prime robot, you'll usually need to change the positive direction of the left motor to counterclockwise like so...

```python
from pybricks.parameters import *
from pybricks.pupdevices import *
from pybricks.robotics import DriveBase

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

robot = DriveBase(left_motor, right_motor, 56, 152)
robot.straight(200)
```

<div class="important">
This isn't always true; it's rare, but possible for an EV3 robot to have motors facing opposite directions, and for a Spike robot to have both motors facing the same direction.
</div>

## Gyro

On the EV3, the gyro is an external device, and you would initialize and use it like this...

```python
from pybricks.ev3devices import *

gyro_sensor = GyroSensor(Port.S3)

print(gyro_sensor.angle())
```

On the Spike, the gyro is built into the hub.
You only need to initialize the hub, then you can use it like this...

```python
from pybricks.hubs import PrimeHub

hub = PrimeHub()

print(hub.imu.heading())
```