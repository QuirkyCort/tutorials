# GPIO Pins

![](images/esp32Pinout.webp)

Most of the pins on the ESP32 can be used for inputs and outputs.
Exceptions are labelled above and described below.

| Label | Description |
| --- | --- |
| VIN | You can power the ESP32 by supplying 5V to 12V to this pin. If connected to USB, this pin will output 5V. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. Both GND pins are the same, so you can use either. |
| INPUT ONLY | These pins can only be used as inputs. You cannot write to these pins. They also do not have internal pull-up resistors. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | Only these pins can be used for touch read. |
| LED | This pin is connected to the onboard blue LED. |
| BOOT | This button is connected to Pin 0. Pin 0 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use, but they may output a signal during boot-up. |
| EN | This pin is connected to the EN (Reset) button. When connected to GND, the ESP32 will reset. |

## Breadboard

Breadboards and dupont wires provides an easy way to connect components to your device.

![](images/breadboard.webp)

When connecting your ESP32 to a breadboard, it is recommended to plug in only one side to each breadboard.
Like this...

![](images/esp32Breadboard.webp)

If you need to use the other side as well, use a second breadboard.

## Digital Output (Write)

Writing a `1` to a pin will set it to `HIGH` (3.3V).
Writing a `0` to a pin will set it to `LOW` (0V).

### Wiring Example

![](images/blinkWiring.webp)

If you do not have a suitable LED, you can use `Pin 2` instead.
`Pin 2` is connected to an internal Blue LED.

<div class="info">
The pins on the ESP32 outputs 3.3V. White and Blue LEDs works around that voltage, while most other colors requires a lower voltage (eg. 1.8V for Red). If you need to use a different color LED, you may need to add a resistor to reduce the voltage.
</div>

### Code

This example code turns the LED on/off every 1 second.

### Blocks

![](images/blink2.webp)

### Python

```python
import time
from ioty import pin

while True:
    pin.digital_write(15, 1)
    time.sleep(1)
    pin.digital_write(15, 0)
    time.sleep(1)
```

## Digital Input (Read)

Reading a pin will return `1` when it is `HIGH` (3.3V), and a `0` when it is `LOW` (0V).

It is often useful to enable the internal pull-up resistor when using a pin as an input; this will ensure that the pin is `HIGH` when it is not connected to anything, and `LOW` when connected to `GND`.
Without a pull-up resistor, the pin will be indetermined when not connected, and may give you random values.

### Wiring Example

![](images/btnWiring.webp)

If you do not have a suitable push button, you can used `Pin 0` instead.
`Pin 0` is connected to the `BOOT` button on the ESP32.

### Code

This example code turns the built-in LED (Pin 2) on when the button is pressed, and off when it is released.

### Blocks

![](images/btn.webp)

To add the `else` to an `if` block, use the gear icon.
You can use the same method to add an `else if` if you require it.

<video width="584" height="334" autoplay loop muted>
    <source src="images/ifElseElseif.mp4" type="video/mp4">
</video>

### Python

```python
from ioty import pin

pin.set_pin_mode(4, pin.PULL_UP)
while True:
    if pin.digital_read(4) == 0:
        pin.digital_write(2, 1)
    else:
        pin.digital_write(2, 0)
```