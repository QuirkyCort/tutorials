# Gyro Move

Before starting on this chapter, make sure you have completed the **Gyro** chapter and the **Move Tank and Move Steering** chapter.
We'll be using the **move_steering** function from the latter chapter.

<div class="important">
We assume that the angle in the Z axis increases when your robot turns left.
Depending on how your gyro is mounted, this may or may not be true.
It's not a problem, but you'll need to adjust your code to use the correct axis / direction.
</div>

## Gyro Move (3 States)

To move straight in a given direction, this is the basic approach...

1. Check if the gyro angle is greater than the target direction, if it is, turn slightly to the right
2. Check if the gyro angle is less than the target direction, if it is, turn slightly to the left
3. If neither of the above are true, go straight


```cpp
void move(int direction, int speed) {
    mpu6050.update();                       // Need to update the gyro, else the angle will not change
    float gyro_angle = mpu6050.getAngleZ();
    if (gyro_angle > direction) {           // Gyro angle greater than target direction...
        move_steering(10, speed);           // ...turn slightly right
    } else if (gyro_angle < direction) {    // Gyro angle less than target direction...
        move_steering(-10, speed);          // ...turn slightly left
    } else {                                // Neither of the above are true...
        move_steering(0, speed);            // ...go straight
    }
}
```

<div class="important">
If the robot or motors are imbalanced (...causing the robot to tend to turn towards one side), the steering (...10 and -10 in the above example) may be insufficient to turn the robot back and you may need to increase it.
If the steering is too high, the robot may wobble as it moves.
</div>

## Gyro Move (Proportional)

A proportional gyro move will adjust the steering value based on the difference between the target direction and the gyro angle.

This is the proportional approach...

1. Calculate the error (difference between target direction and current direction)
2. Multiply the error by a gain (...gain is up to you to tune) to get the steering
3. Ensure the steering isn't too low or high (...with -100 to 100)
4. Move at the calculated steering

```cpp
void move(int direction, int speed) {
    mpu6050.update();                            // Need to update the gyro, else the angle will not change
    int error = direction - mpu6050.getAngleZ(); // Calculate error
    int steer = error * -5;                      // Multiply by gain (-5 here) to get steer
    steer = constrain(steer, -100, 100);         // Constrain it to between -100 to 100
    move_steering(steer, speed);                 // Move at the calculated steering
}
```
<div class="info">
The gain is a negative value, because when the error is positive (...target direction is larger than gyro angle), we need to turn to the left (...negative steer value).
</div>

### Residual Error

A proportional control will suffer from some residual error.
What this means is that if your robot / wheels are not perfectly balanced, the proportional control will get your robot to point close to, but not exactly at the target direction.
This is called the residual error.

You cannot completely eliminate residual error with a proportional only control, but you can reduce it by setting a high gain.
Be warned however, that setting a high gain may cause the robot to oscillate back and forth.

## Looping

None of the **move** functions above will work correctly, as they will only check the angle once.
To continuously check and correct for errors, the above **move** functions will need to be placed in a loop.
The simplest will be a **while (true)** loop...

```cpp
while (true) {
    move(0, 150);
}
```

## Move for Milliseconds

The **while (true)** loop will get the robot moving straight, but it'll never ends.
Unless you just want your robot to move straight forever, it's not very useful.

An alternative would be to get the robot to move straight for a duration and then stop.
The approach here is to...

1. Record the start time
2. Calculate the stop time
3. Repeat the **move** function until the stop time is reached
4. Stop

```cpp
void move_ms(int direction, int speed, int duration) { // duration is in milliseconds (ms)
    unsigned long start = millis();                    // Record the start time
    unsigned long stop = start + duration;             // Calculate the stop time
    while (millis() < stop) {                          // Repeat until stop time is reached
        move(direction, speed);
    }
    move_steering(0, 0);                               // Stop
}
```

## Move until ???

Besides moving for a duration, you can also write other version of the **move** functions, such as...

* Move until the distance detected by the ultrasonic sensor is less than / greater than a given distance
* Move until a particular command is received via serial
* Move until a button is pressed
* Move until a proximity sensor detects an object

Which you'll need will depend on what you want your robot to do.

## Exercise 1

If you have learned how to use read a digital input, write a version of the **move** function that moves until a button is pressed or a proximity sensor detects an object.

## Exercise 2

If you have learned how to use the ultrasonic sensor, write a version of the **move** function that moves until the distance is less than / greater than a given distance.

## Exercise 3

If you have learned how to send and receive serial commands, write a version of the **move** function that moves when a move command is received and stops when a stop command is received.
This can be useful in complex robots where there are multiple micro-controllers in use.