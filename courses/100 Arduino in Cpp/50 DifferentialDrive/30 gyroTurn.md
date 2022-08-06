# Gyro Turn

Before starting on this chapter, make sure you have completed the **Gyro** chapter and the **Move Tank and Move Steering** chapter.
We'll be using the **move_steering** function from the latter chapter.

<div class="important">
We assume that the angle in the Z axis increases when your robot turns left.
Depending on how your gyro is mounted, this may or may not be true.
It's not a problem, but you'll need to adjust your code to use the correct axis / direction.
</div>

## Gyro Turn (2 states)

To do a left turn using the gyro, this is the basic approach...

1. Start turning at a high speed
2. Wait until the gyro angle is close to the target direction
3. Continue turning, but at a lower speed
4. Wait until the gyro angle reaches or exceeds the target direction
5. Stop

```cpp
void left_turn(int direction) {
    move_steering(-100, 200);                      // Start turning fast
    while (mpu6050.getAngleZ() < direction - 20) { // Wait until robot is close to target direction
        mpu6050.update();                          // Need to update the gyro, else the angle will not change
    }
    move_steering(-100, 50);                       // Continue turning, but at a lower speed
    while (mpu6050.getAngleZ() < direction) {      // Wait until robot reach or exceeds the target direction
        mpu6050.update();                          // Need to update the gyro, else the angle will not change
    }
    move_steering(0, 0);                           // Stop
}
```

## Gyro Turn (Proportional)

A proportional gyro turn will gradually slow down the robot as it approaches the target direction.
As nice as it sounds, this doesn't necessarily perform better than the 2 states approach and can be harder to tune.

This is the proportional approach...

1. Calculate the error (difference between target direction and current direction)
2. If the robot is close to the target angle (...error is small), break from the loop and stop
3. Multiply the error by a gain (...gain is up to you to tune) to get the speed
4. Ensure the speed isn't too high (...to prevent turning too fast)...
5. ...or too low (...less than the minimum speed for your motors)
5. Turn at the calculated speed and repeat from step 1

```cpp
void turn(int direction) {
    while (true) {                                   // Keep repeating
        mpu6050.update();                            // Need to update the gyro, else the angle will not change
        int error = direction - mpu6050.getAngleZ(); // Calculate error
        if (abs(error) < 1) {                        // If the error is below a limit (1 degree here),
            break;                                   // break from the loop
        }
        int speed = error * 2;                       // Multiply by gain (2 here) to get speed
        if (speed > 0) {                             // Check if speed is positive or negative
            speed = constrain(speed, 50, 200);       // Constrain it to between 50 to 200
        } else {
            speed = constrain(speed, -200, -50);     // If speed is negative, constrain it to between -200 to -50
        }
        move_steering(-100, speed);                  // Turn at the calculated speed
    }
    move_steering(0, 0);                             // Stop the robot when the loop ends
}
```

Nice thing about a proportional turn is that it will automatically turn left or right depending on the target direction; there's no need for separate left and right turn functions.

<div class="important">
Depending on your robot design, minimum speed, and error limit (...less than 1 degree in the above), there is a risk that your robot may oscillate back and forth for some time before it stops.
If that happens, you can either increase the error limit or reduce the minimum speed.
</div>

## Exercise 1

Write a function to perform a right turn (2 states).

## Exercise 2

Test and tune your turn functions to suit your robot.

## Exercise 3

Sometimes you may want your robot to turn at a lower or higher speed (eg. in a dance performance).
Modify your turn functions to allow a max speed setting.

## Exercise 4

These turns are all using a steering value of **-100** or **100**, giving us an on-the-spot turn.
It may also be desirable to allow other types of turns, such as a pivot turn (...one wheel is stationary) or curve turn (...both wheels are moving in the same direction but at different speed).
Modify your turn functions or write new functions to allow different types of turns.