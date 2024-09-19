# Python Docs - pin

# `pin` - control GPIO pins

The `pin` object is meant to be easy to use, and do not provide all the capabilities available in micropython.
If you need more capabilities, you can use the `Pin` class provided by micropython [https://docs.micropython.org/en/latest/library/machine.Pin.html](https://docs.micropython.org/en/latest/library/machine.Pin.html).

Usage Model:

```python
from ioty import pin

# Set mode of pin 0 to input with pull-up
pin.set_pin_mode(0, pin.PULL_UP)

# Print the value of pin 0
print(pin.digital_read(0))

# Set pin 2 to 1 (HIGH)
pin.digital_write(2, 1)

# Print the analog value of pin 32 (0 to 65535)
print(pin.analog_read(32))

# Print the touch value of pin 4 (0 to ~1000)
print(pin.touch_read(4))

# Set the PWM frequency for pin 13
pin.set_analog_write_freq(13, 1000)

# Write the PWM value of 512 (around 50%) to pin 13
pin.analog_write(13, 512)

# Set the servo connected to pin 17 to 90 degrees
pin.servo_write_deg(17, 90)

# Print the distance measure by an ultrasonic sensor on pin 12 and 14
print(pin.hc_sr04_ping_cm(12, 14))
```

!!!!!
## Constructors

None.

Use the `pin` object directly.

## Methods

### pin.set_pin_mode(pin, mode)

This method allows you to set the pin mode.
The mode is set automatically when reading or writing to a pin, so this method isn't always required.
Automatic setting of mode will not use pull-ups, so pull-up should be set using this method if required.

The arguments are:

* `pin` An integer number specifying the pin number.

* `mode` The pin mode, which can be one of the following:

    * `pin.OUT` Set the pin to output mode.

    * `pin.IN` Set the pin to input mode without pull-up resistor.

    * `pin.PULL_UP` Set pin to input mode with pull-up resistor.

Returns `None`.

### pin.digital_read(pin)

This method gets the value from the pin.

The arguments are:

* `pin` An integer number specifying the pin number.

Returns either an integer `1` (HIGH) or `0` (LOW).

### pin.digital_write(pin, value)

This method sets the value of the pin.

The arguments are:

* `pin` An integer number specifying the pin number.

* `value` An integer `1` (HIGH) or `0` (LOW).

Returns `None`.

### pin.analog_read(pin)

This method gets an analog value from the pin.

The arguments are:

* `pin` An integer number specifying the pin number.

Returns an integer ranging from `0` to `65535`.

### pin.touch_read(pin)

This method gets a capacitive touch value from the pin.

The arguments are:

* `pin` An integer number specifying the pin number.

Returns an integer ranging from `0` to around `1000`.

### set_analog_write_freq(pin, freq)

This method sets the frequency for PWM output.

The arguments are:

* `pin` An integer number specifying the pin number.

* `freq` An integer ranging from `1` to `40000000` representing the frequency in Hz.

Returns `None`.

### pin.analog_write(pin, value)

This method sets the value of the pin.

The arguments are:

* `pin` An integer number specifying the pin number.

* `value` An integer ranging from `0` (0%) to `1023` (100%) representing the PWM duty cycle.

Returns `None`.

### pin.servo_write_deg(pin, deg)

This method sets a PWM signal on the specified pin suitable for controlling an RC servo.
The output PWM width will range from 500us (0 deg) to 2500us (180 deg).

The arguments are:

* `pin` An integer number specifying the pin number.

* `deg` An number (int/float) ranging from `0` to `180` representing the angle in degrees.

Returns `None`.

### pin.servo_write_us(pin, us)

This method sets a PWM signal on the specified pin suitable for controlling an RC servo.

The arguments are:

* `pin` An integer number specifying the pin number.

* `us` An number (int/float) representing the pulse width in microseconds.

Returns `None`.

### pin.hc_sr04_ping_cm(trig, echo, timeout=4000*2*3)

This method triggers a measurement on the ultrasonic distance sensor, and returns the measured distance in centimeters (cm).

The arguments are:

* `trig` An integer number specifying the pin connected to the TRIG of the ultrasonic. This must be an output capable pin.

* `echo` An integer number specifying the pin connected to the ECHO of the ultrasonic.

* `timeout` An integer representing the duration in microseconds to wait for the echo.

Returns `-1` on timeout, else it will return a float representing the measured distance in centimeters (cm).

### pin.hc_sr04_ping_us(trig, echo, timeout=4000*2*3)

This method triggers a measurement on the ultrasonic distance sensor, and returns the measured distance in microseconds (us).

The arguments are:

* `trig` An integer number specifying the pin connected to the TRIG of the ultrasonic. This must be an output capable pin.

* `echo` An integer number specifying the pin connected to the ECHO of the ultrasonic.

* `timeout` An integer representing the duration in microseconds to wait for the echo.

Returns `-1` on timeout, else it will return a integer representing the time for the echo to return in microseconds (us).
!!!!!