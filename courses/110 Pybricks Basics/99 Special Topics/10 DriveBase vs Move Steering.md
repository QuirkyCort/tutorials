# DriveBase vs Move Steering

The **DriveBase** provided by Pybricks can be useful in some cases.
Some benefits of the **DriveBase** includes...

* Move by distance
* Turn by degrees
* Gradual ramp up/down of speed when moving and turning

All of these can be replicated using just the normal **Motor** class, but the third one can take a bit more work to do.

When using the **drive** method in **DriveBase**, you specify the speed and rate of turn (deg/s).
This causes a few problems...

* When turning, the outer wheel will speed up. This may bring it above the max speed of the motor, causing inconsistent behaviour.
* The turn radius is dependent on the speed. At higher speed, the turn radius will be larger, and the robot may not be able to make a sharp turn.
* To make the sharpest turn, the robot speed must be set to zero.
* Response may be slower due to internal speed control loop.

These can be compensated by slowing down the robot when making a turn, but to fully compensate for all the problems will require some rather complicated code.

# Move Steering

The **Move Steering** function is available in EV3Dev_Python, EV3Lab, EV3Classroom, and Spike Prime (v3 only).
Unlike the **drive** method in **DriveBase**, the **Move Steering** functions takes a speed (%) and a "steering" value (-100 to 100) as input.

The "steering" value control the ratio of speed between the left and right wheel, as illustrated below

| Steering | Left Wheel | Right Wheel |
| --- | --- | --- |
| 0 | 100% | 100% |
| 25 | 100% | 50% |
| 50 | 100% | 0% |
| 75 | 100% | -50% |
| 100 | 100% | -100% |

The equation for the **Move Steering** function is...

```python
def move_steering(speed, steer):
    if steer > 0:
        left_motor.dc(speed)
        right_motor.dc(speed - steer * speed / 50)
    else:
        left_motor.dc(speed + steer * speed / 50)
        right_motor.dc(speed)
```

Advantages of the **Move Steering** function includes...

* None of the wheels will speed up when turning. This avoids issues with exceeding the max motor speed and make for a smoother turn.
* Turn radius is not dependent on speed. As long as the steering value is the same, the robot will always make the same turn regardless of speed.
* By changing the steering value only, you can fully control the turning radius from the maximum to the minimum value.

Note that the above function changes the **duty cycle** (ie. power) of the motor, and not the speed.
One advantage is that this avoid Pybrick's internal speed control loop, allowing a faster response.
