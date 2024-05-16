# Run vs DC

In Pybricks, the **Motor** class provides both the **run** and the **dc** commands.
Each of these have its uses, and it's good to know how they work.

## DC

DC stands for "Duty Cycle".
This represents the percentage of time a device is powered.
For example, if you turn on your lights for 12 hrs per day, it will be operating at 50% duty cycle (12 hrs / 24 hrs).

When controlling a brushed motor like those used by the EV3 and Spike Prime, we often do so by switching the power on and off rapidly.
If we were to turn on the power for 10 ms and off for 10 ms, the motor will be at 50% duty cycle.
If we were to turn it on for 15 ms and off for 5 ms instead, the motor will be at 75% duty cycle.

Setting the duty cycle can approximately control the speed, but not very well.
Consider a robot going up and down a slope; at the same 50% duty cycle, it may move very slowly when going up, but very fast when going down.

If there is a lot of static friction present, the situation may be worse.
Imagine that your robot requires 70% power to overcome static friction.
At 65% power, the robot will remain stationary, but at 75% power it will overcome static friction and start moving at a high speed.
You can then lower the power to 40%, and the robot will continue moving at a lower speed, but if it encounters any obstacles, it may come to a stop again.

## Run (speed control)

To better control the motor speed, we will need some kind of feedback.
Both the EV3 and Spike Prime motors are equipped with sensors that detects the motor's rotation.
Pybricks uses this to calculate the actual motor speed, and adjust the power to the motor.
So when you tell the motor to **run(200)** (...run and 200 deg/s), what Pybricks does is...

1. Estimate the duty cycle to achieve that speed and sets it
2. Measure the actual motor speed
3. Uses a PID algorithm to calculate a correction
4. Corrects the duty cycle setting
5. Go back to step 2 and keep repeating until it receives a stop command

It takes time to measuring and adjust dc settings, which means that the motor may respond slowly to changes in speed settings.

<div class="info">
It's possible to set the PID parameters using "control.pid()".
Read the Pybricks documentation to know more.
Be cautioned that it can be very difficult and time consuming to tune PID parameters.
</div>

## Run (acceleration)

In addition, it is often undesirable to immediately go to full speed.
To rapidly go from stationary to full speed will require a high acceleration, and the robot will need to overcome a lot of inertia.
If you try to do this, the tires will likely skid, causing a loss of accuracy.

Pybricks limits the acceleration of the motors, to prevent skidding.
This means that when you change the speed from 0 to 1000, Pybricks will...

* Set speed to 10
* Wait a while
* Set speed to 20
* Wait a while
* Set speed to 30
.
.
.
* Set speed to 1000

The gradual change in speed reduces the risk of skidding, but it also means that the wheel speed will respond slower to commands.

<div class="info">
It's possible change the acceleration limit using "control.limits()".
Read the Pybricks documentation to know more.
</div>

## Effects of Slow Response

We now know that **run** can lead to delays in responds, but how does that affect our robot?
The below video simulates the effect of a delay during line following (...no delay on left, delay on right).

<video width="960" height="540" autoplay loop muted>
    <source src="images/effects_of_lag.webm" type="video/webm">
</video>

<div class="info">
This is just a simulation; the actual behavior will depend on the physical aspects of your robot and the control parameters.
</div>

## Run vs DC

### DC

* DC provides fast response, but speed may be inconsistent
* It can be difficult to achieve low speed when using DC; the power may not be enough to overcome static friction and the motor may stop

### Run

* Run provides consistent speed, but response is slower
* Can achieve low speed; if the motor stops due to static friction, the control algorithm will provide enough power to overcome it, then reduce it again to continue moving at low speed.

### EV3

Personally, I find that **dc** works better when using the large motor on an EV3.
It might be possible to achieve better results with run if you tune the control parameters, but it can be difficult to achieve a good tuning.
You should test both out and decide for yourself which works better.

### Spike Prime

Using the medium motor on the Spike Prime, I find that you may need a high duty cycle just to get the motors moving, and the motor stops easily unless you are using a very high duty cycle.
As such, using **run** works better when using the medium motor on the Spike Prime.
As always, you should test both out and decide for yourself which works better.