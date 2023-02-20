# Serial

If your Python program needs to communicate with an Arduino or other micro-controllers, you would often need to use the serial protocol.
The [pySerial](https://pythonhosted.org/pyserial/) module can help with that.

PySerial does not come default with Python, so you'll need to install it.

```
python -m pip install pyserial

or

python3 -m pip install pyserial
```

## Writing Data

The sample code below prompts the user for an input, and sends it to the serial device.
It is meant for a Linux or Mac computer that has a serial device at `/dev/ttyUSB0`.
If your serial device is not at this location or if you're using Windows, the the serial device name will need to be changed.

```python
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
while True:
    msg = input('Type your msg here: ')
    ser.write(msg.encode() + b'\r\n')
```

**import serial** : Imports the serial module. Note that while the package is named **pySerial**, the module is named **serial**.

**ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)** : Create a new serial object using device `/dev/ttyUSB0` (...see the section on serial port to learn how to determine the correct device name). Baudrate is set to 9600 in this example; you need to make sure this matches the baudrate for the connected device (eg. Arduino). Some devices may require additional settings; read the [PySerial Documentations](https://pyserial.readthedocs.io/en/latest/pyserial_api.html) to learn how to set them.

**msg = input('Type your msg here: ')** : This reads a string from the user.

**ser.write(msg.encode() + b'\r\n')** : This sends the user's message to the serial device. Since serial can only send **bytes** object, we'll need to encode the string `msg` into a bytes object using `encode()`. See the next line for explanation of the `b'\r\n'`.

**b'\r\n'** : This are the **Carriage Return** (\r) and **Line Feed** (\n) characters. The `b` at the front indicates that this is a bytes object and not a string. These characters are added to the end of your message to mark the end of the line. Depending on your device, it may expect just a carriage return, just a line feed, or both.

## Reading Data

This sample code reads from the serial device, one line at a time, and prints it to screen.

Before reading this code, be sure to read the section on **Writing Data** first, as some of the code are identical and won't be explained again here.

```python
import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
while True:
    data = ser.read_until() # Blocks!
    print(data.decode(), end='')
```

**data = ser.read_until()** : Read until a (newline) character is found, then return everything. Basically, this allows you to read one line at a time from the serial port. This is a **blocking** function, which means that the next line of code will not run until serial receives the newline character.

**print(data.decode(), end='')** : This prints the data that was received. Note that the data is a [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) object, and not a string. To print it properly, we'll need to [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) it into a string first. The `end=''` indicates to the `print` function that it should not add a newline to the end when printing (...as the serial data already contains a newline).

## Serial Port

To use the serial module, you'll need to know which serial port your device is connected to.
There are a few ways to do this...

### Linux only

* Plug in your serial device (...if it's already plugged in, unplug it then plug it in again).
* In a terminal, run `sudo dmesg`. Key in your password if requested.
* Look in the last few lines for a message containing...
    * `ttyACM0`: Your device is `/dev/ttyACM0`
    * `ttyUSB2`: Your device is `/dev/ttyUSB2`
    * *Note that the actual message is longer than the above, and the exact message may vary.*

### Linux, Mac, Windows

* Unplug your serial device.
* Start up the Arduino IDE software.
* Click on **"Tools -> Port"**, and note down the devices that are listed there.
* Plug in your serial device.
* In the Arduino software, click on **"Tools -> Port"** again and note down which is the new device that appeared. That is your serial device.

On Linux and Mac, the serial device name should start with `ttyACM` or `ttyUSB`.
On Windows, the serial port name should start with `COM` followed by a number (eg. `COM3`).

## Further Readings

To learn more, read the [PySerial Documentations](https://pyserial.readthedocs.io/en/latest/pyserial_api.html).