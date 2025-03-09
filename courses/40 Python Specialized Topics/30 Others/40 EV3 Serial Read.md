# EV3 Serial Read

The Lego EV3 can read from serial devices connected to its USB port (...the USB A port, not the micro USB port), such as an ESP32, OpenMV Cam, or Arduino.
This tutorials describes four different methods of reading from the serial device...

* Continuous data
* Continuous data (bytes array)
* Request Respond
* Request Respond (binary)

The code is meant for an EV3 running micropython, and isn't tested with cPython.

## Continuous data

In this approach, the micropython sends data continously and the EV3 will read everything.
If there are multiple sets of data received in a single read, the EV3 will process only the last value.

It can handle write rates of around 100Hz.
If the micropython device sends data faster than this, the EV3 will not be able to keep up and will hang as it never finishes reading the data.

### EV3 Code

```python
# Set baudrate in Python
# os.system() runs the specified command
# You can also run the "stty" command from the commandline.
import os
import select
os.system('stty -F /dev/ttyUSB0 115200')

# Open the /dev/ttyUSB0 file in read only mode. This file represents the serial device
# Depending on your serial device, the filename may change (eg. /dev/ttyACM0)
fd = os.open('/dev/ttyUSB0', os.O_RDONLY)

# Create a select object and register the previously opened file in input (reading) mode
# This let us check if there is data available for reading from the file.
p = select.poll()
p.register(fd, select.POLLIN)

# Create an empty bytes object to receive data from the file
buf = b''

x = 0
y = 0

# Read from serial
def read():
    global buf, x, y

    # Loop as long as data is available
    # p.poll() will return None if no data is available
    # Note that the "0" is the timeout duration
    # If absent, the poll() command will wait until data is available
    while p.poll(0):

        # Since data is available, we can safely read from the file without blocking
        char = os.read(fd, 1) # read one byte

        # Check if it's a newline character
        if char != b'\n':
            # If the char is not a newline, that means you have not reached the end of the line.
            # Add the character to the buffer
            buf += char
        else:
            # If it's a newline, make a copy of it, then empty buf
            # Checking that the len is greater than 0 is to prevent empty lines from being processed
            if len(buf) > 0:
                buf_copy = buf
                buf = b''

    # Exited from loop. That means we have read everything.
    # buf_copy should contain the last full line and we can process it

    # The "try/except" is to protect against errors. If the data is corrupted,
    # the conversion may fail. Without the try/except, your program will terminate
    # immediately. With try/except, your program will catch the error and do a
    # "pass" (ie. nothing)
    try:
        # First decode the bytes into a string
        string = buf_copy.decode()

        # If you have multiple values in each line, split the string
        # Here we split by comma, but use whatever is suitable for your data
        values = string.split(',')

        # # Convert your values from string to numbers
        x = float(values[0])
        y = float(values[1])
    except:
        pass

# Retrieve the last read value
def get():
    return x, y

# Read and discard all data from buffer.
# If the EV3 is unable to read from serial for a while, you should run this to clear the read
# buffer, else the EV3 may take a while to process all the buffered data.
def clear():
    while p.poll(0):
        os.read(fd, 100)


#########################
# Main loop for testing #
#########################

import time
timeout = 0

while True:
    read()

    # We read every loop, but prints only once per second.
    now = time.time()
    if now > timeout:
        timeout = now + 1
        print(get())
```

### Serial device code

```python
import time

while True:
    # Random code to set x and y
    # Replace with your own code
    x = time.time()
    y = x + 5

    print(str(x) + ',' + str(y))
    time.sleep_ms(10)

```

## Continuous data (bytes array)

Similar to "Continuous data", but in this version, we try to optimize the read by...

* Reading multiple bytes at a time
* Reuse a bytes array instead of creating a new bytes string with each append
* Process in bytes rather than string

It can handle a higher write rate of around 200Hz.
If the micropython sends data faster than this, the EV3 will not be able to keep up and will hang as it never finishes reading the data.

### EV3 Code

```python
# Set baudrate in Python
# os.system() runs the specified command
# You can also run the "stty" command from the commandline.
import os
import select
os.system('stty -F /dev/ttyUSB0 115200')

# Open the /dev/ttyUSB0 file in read only mode. This file represents the serial device
# Depending on your serial device, the filename may change (eg. /dev/ttyACM0)
fd = os.open('/dev/ttyUSB0', os.O_RDONLY)

# Create a select object and register the previously opened file in input (reading) mode
# This let us check if there is data available for reading from the file.
p = select.poll()
p.register(fd, select.POLLIN)

# Create a bytearray to receive data from the file
BUF_SIZE = 32 # This should be the maximum number of bytes in a line
buf = bytearray(BUF_SIZE)
buf_ptr = 0

x = 0
y = 0

# Read from serial
def read():
    global buf, buf_ptr, x, y

    # Loop as long as data is available
    # p.poll() will return None if no data is available
    # Note that the "0" is the timeout duration
    # If absent, the poll() command will wait until data is available
    while p.poll(0):

        # Since data is available, we can safely read from the file without blocking
        chars = os.read(fd, 100) # read multiple bytes

        for char in chars:
            # Check if it's a newline character
            if char != ord('\n'):
                # If the char is not a newline, that means you have not reached the end of the line.
                # First check the pointer. If it reached the end, the data must have been corrupted.
                # We'll start again from the beginning.
                if buf_ptr == BUF_SIZE:
                    buf_ptr = 0

                # Put the character in the buffer
                buf[buf_ptr] = char
                buf_ptr += 1
            else:
                # If it's a newline, make a copy of it, then start from beginning
                if buf_ptr > 0:
                    buf_copy = buf[:buf_ptr]
                    buf_ptr = 0

    # Exited from loop. That means we have read everything.
    # buf_copy should contain the last full line and we can process it

    # The "try/except" is to protect against errors. If the data is corrupted,
    # the conversion may fail. Without the try/except, your program will terminate
    # immediately. With try/except, your program will catch the error and do a
    # "pass" (ie. nothing)
    try:
        # If you have multiple values in each line, split the string
        # Here we split by comma, but use whatever is suitable for your data
        values = buf_copy.split(b',')

        # Convert your values from string to numbers
        x = float(values[0])
        y = float(values[1])
    except:
        pass

# Retrieve the last read value
def get():
    return x, y

# Read and discard all data from buffer.
# If the EV3 is unable to read from serial for a while, you should run this to clear the read
# buffer, else the EV3 may take a while to process all the buffered data.
def clear():
    while p.poll(0):
        os.read(fd, 100)


#########################
# Main loop for testing #
#########################

import time
timeout = 0

while True:
    read()

    # We read every loop, but prints only once per second.
    now = time.time()
    if now > timeout:
        timeout = now + 1
        print(get())
```

### Serial device code

```python
import time

while True:
    # Random code to set x and y
    # Replace with your own code
    x = time.time()
    y = x + 5

    print(str(x) + ',' + str(y))
    time.sleep_ms(5)
```

## Request Respond

In this approach, we send a request to the serial device, prompting it to respond with the desired data.
As the serial device will only transmit data when the EV3 request for it, there are no risks of the EV3 being unable to keep up and hanging.

It can handle request/respond rates of around 110Hz.

### EV3 Code

```python
# Set baudrate in Python
# os.system() runs the specified command
# You can also run the "stty" command from the commandline.
import os
import select

os.system('stty -F /dev/ttyUSB0 115200')

# Open the /dev/ttyUSB0 file in read write mode. This file represents the serial device
# Depending on your serial device, the filename may change (eg. /dev/ttyACM0)
fd = os.open('/dev/ttyUSB0', os.O_RDWR)

# Create a select object and register the previously opened file in input (reading) mode
# This let us check if there is data available for reading from the file.
p = select.poll()
p.register(fd, select.POLLIN)

# Read from serial
def get():
    # Flush data from read buffer
    while p.poll(0):
        os.read(fd, 100)

    # Write the trigger
    # We send an 'a' as a trigger, but you can use anything
    # You can also use different triggers to request for different data
    os.write(fd, b'a')

    # Read the data
    # The number of bytes to read should match your longest possible line
    line = os.read(fd, 100)

    # The "try/except" is to protect against errors. If the data is corrupted,
    # the conversion may fail. Without the try/except, your program will terminate
    # immediately. With try/except, your program will catch the error and return None
    try:
        # If you have multiple values in each line, split the string
        # Here we split by comma, but use whatever is suitable for your data
        values = line.split(b',')

        # Convert your values from string to numbers
        x = float(values[0])
        y = float(values[1])
        return x, y
    except:
        return None, None


#########################
# Main loop for testing #
#########################

import time

while True:
    print(get())
```

### Serial device code

```python
import time
import sys, select

p = select.poll()
p.register(sys.stdin, select.POLLIN)

while True:
    # Random code to set x and y
    # Replace with your own code
    x = time.time()
    y = x + 5

    # Check if we received a trigger
    if p.poll(0):
        char = sys.stdin.read(1)
        if char[0] == 'a':
            string = str(x) + ',' + str(y) + '\n'
            sys.stdout.write(string)
```

## Request Respond (Binary)

Similar to "Request Respond", but in this version, we try to optimize by sending data in binary format instead of text format.
This reduces the amount of data sent, and the amount of data that needs to be processed.

Drawback is that the data format must be predefined (ie. you cannot sometimes send 2 integers and sometimes 3 floats).
It also appears to be less reliable than the text version, but I did not investigate why.

It can handle request/respond rates of around 120Hz, which is only a small improvement over the text version.

### EV3 Code

```python
# Set baudrate in Python
# os.system() runs the specified command
# You can also run the "stty" command from the commandline.
import os
import struct
import select

os.system('stty -F /dev/ttyUSB0 115200')

# Open the /dev/ttyUSB0 file in read write mode. This file represents the serial device
# Depending on your serial device, the filename may change (eg. /dev/ttyACM0)
fd = os.open('/dev/ttyUSB0', os.O_RDWR)

# Create a select object and register the previously opened file in input (reading) mode
# This let us check if there is data available for reading from the file.
p = select.poll()
p.register(fd, select.POLLIN)

# Read from serial
def get():
    # We send an 'a' as a trigger, but you can use anything
    # You can also use different triggers to request for different data

    # Flush data from read buffer
    while p.poll(0):
        os.read(fd, 100)

    # Write the trigger
    os.write(fd, b'a')

    # Read the data
    # The number of bytes to read should match your data format plus 1 (for newline)
    data = os.read(fd, 5)

    if len(data) >= 4:
        result = struct.unpack('hh', data)
        return result[0], result[1]
    else:
        return None, None


#########################
# Main loop for testing #
#########################

import time

while True:
    print(get())
```

### Serial device code

```python
import time
import sys, select
import struct

p = select.poll()
p.register(sys.stdin, select.POLLIN)

while True:
    # Random code to set x and y
    # Replace with your own code
    x = time.time()
    y = x + 5

    # Check if we received a trigger
    if p.poll(0):
        char = sys.stdin.read(1)
        if char[0] == 'a':
            # The newline character appears to flush the buffer and is
            # needed as micropython do not support flush()
            sys.stdout.buffer.write(struct.pack('hh', x, y) + b'\n')
```

