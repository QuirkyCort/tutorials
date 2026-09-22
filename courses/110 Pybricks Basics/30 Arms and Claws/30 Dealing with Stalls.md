# Dealing with Stalls

Sometimes the motor is unable to reach the desired position.
For example, you want to move an arm down to 0 deg, but it hit the wall at 30 deg and can't go any lower.
This condition is called **stall**.

In Pybricks, when a motor stalls, the default behaviour is to keep on trying until the motor reaches the specified position.
Try this code...

```python
print('start')
motor.run_target(200, 90)
print('end')
```

Run this code while holding the motor to prevent it from turning.
You'll see that "end" will only print after you release the motor.

This means that if an arm or claw gets stuck on something and can't reach their desired position, your program will stop there and won't continue.

## wait = False

By setting the `wait=False` parameter, we can tell the `run_target` command not to wait for the motor to reach the target position and immediately continue running the next line of code.
This is call **non-blocking** code, while `run_target` with `wait=True` would be a **blocking** code.
We can then make our own function that continues with the program if the motor can't reach the desired position after some time.

```python
from pybricks.pupdevices import Motor
from pybricks.tools import wait, StopWatch

motor = Motor(Port.E)

def move_arm(speed, position, time_limit=2000):
    timer = StopWatch()
    motor.run_target(speed, position, wait=False)
    while True:
        if motor.angle() == position:
            break
        if timer.time() > time_limit:
            break

print('start')
move_arm(200, 90)
print('end') # Continue with other code even if position is not reached
wait(5000)   # The wait is just a placeholder for other code
```

Here we have a `move_arm` function, with a default time limit of 2000ms (2 seconds).
At the start of the function, it creates a `StopWatch()` object, which allows us to take timing.
It then starts the motor moving using `run_target`, but with `wait` set to `False`.

Next, it runs a `while True` loop, and continuously check if the...

* motor has reached the target position

* time limit is reached

If either of these are true, it'll exit the loop and continue with the program.

You can test this by running the program while holding the motor to prevent it from turning.
You'll see the word "end" printed after 2 seconds even if you don't release the motor.

## Summary

Making your own arm / claw movement function with `wait=False` can make your robot more robust.
If the arm / claw gets stuck on something, the robot can still continue with its mission.

Note that depending on how the arm / claw is stuck, continuing with the mission may still lead to failures, so don't expect this to fix every problem.