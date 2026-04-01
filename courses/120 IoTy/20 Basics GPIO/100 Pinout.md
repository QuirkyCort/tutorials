# Pinouts

## ESP32-WROOM

![](images/esp32Pinout.webp)

Most of the pins on the ESP32 can be used for inputs and outputs.
Exceptions are labelled above and described below.

| Label | Description |
| --- | --- |
| VIN | You can power the device by supplying 5V to 12V to this pin. If connected to USB, this pin will output 5V. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. Both GND pins are the same, so you can use either. |
| INPUT ONLY | These pins can only be used as inputs. You cannot write to these pins. They also do not have internal pull-up resistors. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | Only these pins can be used for touch read. |
| LED | This pin is connected to the onboard blue LED. |
| BOOT | This button is connected to Pin 0. Pin 0 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use as output, but they may output a signal during boot-up. |
| EN | This pin is connected to the EN (Reset) button. When connected to GND, the device will reset. |

## ESP32-S3

![](images/esp32s3Pinout.webp)

Most of the pins on the ESP32 can be used for inputs and outputs.
Unlike the ESP32, the ESP32-S3 has no input only pins; all pins are capable of output.

| Label | Description |
| --- | --- |
| 5V | You can power the device by supplying 5V to this pin. By default, this pin does not output any voltage when connected to USB. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. |
| USB | These are used for the USB connection. You cannot use them. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | Only these pins can be used for touch read. |
| WS2812 LED | This pin is connected to the onboard WS2812 (Neopixel) LED. You can control it using the Neopixel extension. |
| BOOT | This button is connected to Pin 0. Pin 0 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use as output, but they may output a signal during boot-up. |
| EN | This pin is connected to the EN (Reset) button. When connected to GND, the device will reset. |

## ESP32-S3-Cam (Freenove)

![](images/esp32s3camPinout.webp)

There are many varients of the ESP32-S3-Cam with different pinouts.
This is for the Freenove (...and clones) version.
Many of the pins have special uses, so check the table below before choosing a pin to use.

| Label | Description |
| --- | --- |
| 5V | You can power the device by supplying 5V to this pin. If connected to USB, this pin will output 5V. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. |
| USB | These are used for the USB connection. You cannot use them. |
| PSRAM | These are used for the PSRAM (Pseudo-Static RAM). You cannot use them. |
| CAMERA | These are used for the camera. If you have a camera connected, you cannot use them. |
| SD card | These are used for the SD card. If you have a SD card plugged in, you cannot use them. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | Only these pins can be used for touch read. |
| LED | This pin is connected to the onboard blue LED. |
| WS2812 LED | This pin is connected to the onboard WS2812 (Neopixel) LED. You can control it using the Neopixel extension. |
| BOOT | This button is connected to Pin 0. Pin 0 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use as output, but they may output a signal during boot-up. |
| EN | This pin is connected to the EN (Reset) button. When connected to GND, the device will reset. |

## ESP32-C3 Super Mini

![](images/esp32c3SuperMini.webp)


| Label | Description |
| --- | --- |
| 5V | You can power the device by supplying 5V to this pin. If connected to USB, this pin will output 5V. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | None of the pins on the ESP32-C3 supports touch. |
| LED | This pin is connected to the onboard blue LED. |
| BOOT | This button is connected to Pin 9. Pin 9 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use as output, but they may output a signal during boot-up. |

## ESP32-S3 Super Mini

![](images/esp32s3SuperMini.webp)


| Label | Description |
| --- | --- |
| 5V | You can power the device by supplying 5V to this pin. If connected to USB, this pin will output 5V. |
| 3V3 | This pins outputs 3.3V. |
| GND | Ground pin. |
| ANALOG READ | Only these pins can be used for analog read. |
| TOUCH | Only these pins can be used for touch read. |
| BOOT | This button is connected to Pin 0. Pin 0 will return a 0 (LOW) when the button is pressed, and 1 (HIGH) when it is not. |
| UART0 RX/TX | These pins are connected to the micropython terminal. You should not use them. |
| STRAP | These pins are generally ok to use as output, but they may output a signal during boot-up. |
| Pin 48 | This pin is connected to both a red LED as well as a WS2812 (Neopixel) LED. Setting it to 1 (HIGH) will turn the red LED on, and 0 (LOW) turns it off. Use the Neopixel extension to control the WS2812 LED. |
| Battey LED | This blue LED shows the charging status when connected to battery. On when charging and off when full. When batteries are not connected, it will blink continuously. |