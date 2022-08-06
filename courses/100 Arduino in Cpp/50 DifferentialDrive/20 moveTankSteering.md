# Move Tank, Move Steering

Those who are familiar with the older EV3 Lab software for the Lego EV3 robot should recognize the terms **Move Tank** and **Move Steering**.
These functions remains available in the newer EV3 Classroom software, but these terms are no longer in use.

In this section, we'll look at what each of these function do, and replicate them for our robot.

## Move Tank

The **Move Tank** function simply allows us to control both the left and right wheel speed in a single function call.
It's simple...

```cpp
void move_tank(int left_power, int right_power) {
    left_motor(left_power);
    right_motor(right_power)
}
```

<div class="important">
The above function requires that you have the <strong>left_motor</strong> and <strong>right_motor</strong> functions already written.
If you haven't done that, refer to the section on H-Bridge Control and write those functions first.
</div>

## Move Steering

One drawback of using **Move Tank** is that if you need to change the speed of a move, you'll need to change the speed for both the left and right wheels.
To maintain the same turning radius, you'll need to ensure that the speed ratio of the left and right wheels are the same.

The **Move Steering** function separates the turning radius from the speed, allowing you to change each of these independently (eg. change speed without affecting the turning radius).

Following the convention used by the EV3 software, we'll implement our **Move Steering** function with a steering value that ranges from **-100** (on the spot left turn) to **100** (on the spot right turn).
If you prefer, you can also implement it with a range of -255 to 255, or -1.0 to 1.0, but note that programmers often avoid floating point values, as many microcontrollers have poor floating point performance.

```cpp
void move_steering(int steer, int speed) {
    if (steer > 0) {
        left_motor(speed);
        right_motor(speed - steer * speed / 50);
    } else {
        left_motor(speed + steer * speed / 50);
        right_motor(speed);
    }
}
```

<div class="info">
<p>
    Note that we use <strong>steer * speed / 50</strong> and not <strong>steer / 50 * speed</strong>.
    These may be identical mathematically, but in the C++ programming language, there is a subtle difference.
</p>
<p>
    Here we are working with integer numbers, so the result of each operation is always an integer.
    Consider...
</p>
<pre>
int steer = 50;
print(steer / 50);                 // This will output 1.

int speed = 100;
print(speed - steer / 50 * speed); // This will output 0.
</pre>
<p>
    What if we change <strong>steer</strong> to <strong>70</strong>?
</p>
<pre>
int steer = 70;
print(steer / 50);                 // This will still output 1! It can't be 1.4 as that is not an integer!

int speed = 100;
print(speed - steer / 50 * speed); // This will still output 0. Same speed as before!
print(speed - steer * speed / 50); // This will output -40 which is the correct result
</pre>
<p>
    When working with integer numbers, it's often best to multiply first before dividing to avoid such problems.
</p>
</div>

The way the above code works is...

* Outer wheel always runs at the specified speed (...when turning right, the left wheel is the outer wheel).
* Inner wheel speed is reduced based on the steering value...

### steer == 0

```cpp
// Inner wheel speed
speed - steer * speed / 50
speed - 0 * speed / 50      // Replace "steer" with 0
speed - 0
speed                       // Inner wheel runs at "speed", same as the outer wheel
```

If steering is 0, there is no reduction and the inner wheel runs at the same speed as the outer.
Robot travels straight forward.

### steer == 50

```cpp
// Inner wheel speed
speed - steer * speed / 50
speed - 50 * speed / 50     // Replace "steer" with 0
speed - speed               // 50 / 50 = 1
0                           // Inner wheel is stopped
```

If steering is 50, the inner wheel is stopped.
Robot turns with one wheel stopped.

### steer == 100

```cpp
// Inner wheel speed
speed - steer * speed / 50
speed - 100 * speed / 50    // Replace "steer" with 0
speed - 2 * speed           // 100 / 50 = 2
-speed                      // Inner wheel runs at same speed as the outer wheel, but opposite direction
```

If the steering is 100, the inner wheel runs at the same speed but opposite direction from the outer wheel.
Robot turns with one wheel moving forward and the other wheel moving backwards.

## Speed or Power?

While we have been using the term **speed** through out this section, the **left_motor** and **right_motor** functions from the H-Bridge Control section actually controls the power delivered to the motors and not the speed.
To actually control the speed of the motor, we'll need to add additional sensors (eg. motor encoders) and a control loop to regulate the motor speed.

Thankfully, the motor speed is largely proportional to the motor power, so controlling power isn't too terrible an option.
With just power control, you should not expect the robot to drive straight when commanded to, but you won't expect it to spin crazily in place either (...unless you screwed up somewhere).

If you do add in motor encoders and code for speed control, you can replace the **left_motor** and **right_motor** functions with their speed based equivalent.
This will give you some improvement in movement accuracy (ie. the robot will drive a little straighter).
An alternative is to stick to the power based functions, but use gyros and other sensors (eg. ultrasonic) to control the direction and position of the robot; these can provide better accuracy than relying on motor encoders.

## Low Power Caveat

While the motor speed is largely proportional to motor power, this approximation falls apart at low power / duty cycle and you may find your motors performing very inaccurately or even stop completely.
Depending on your hardware and PWM frequency, this low power limit can be anywhere from 10% to 50%.
If you find that you are unable to achieve a sufficiently low speed, reducing your PWM frequency can help; read the **Analog Output (Frequency)** chapter to learn how.