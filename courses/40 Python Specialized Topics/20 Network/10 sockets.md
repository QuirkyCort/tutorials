# Sockets

Sockets is an [application programming interface (API)](https://en.wikipedia.org/wiki/Application_programming_interface) to allow two programs to send data to each other.
While sockets can be used between two programs on the same computer, it is most commonly used to communicate between two computers over the internet.

Today, nearly all operating systems (eg. Linux, Mac, Windows) and programming languages supports some form of sockets.

In this section, you'll learn to create a socket server (...which waits for a connection), and a socket client (...which initiates the connection), and send messages between the two.
You can test your program using just a single computer, but for a complete test (...which includes ensuring your router and firewall is suitably configured), you'll need at least two computers.
Either way, you will need to write **both** the server and client program in order to perform any testing.

## Server

The server is the program that waits for a connection.
Once the connection is made, there are no significant differences between the server and the client; both of them can send and receive messages.

Here's the code for the server...

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1337))
s.listen()

conn, addr = s.accept() # Blocks!
print('Connection from : ' + addr[0])
while True:
    data = conn.recv(1024) # Blocks!
    if not data:
        break
    print(data.decode())
    conn.sendall(b'Got it!')
```

**import socket** : This imports the socket module.

**s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)** : This creates a new socket. The `socket.AR_INET` indicates that this is socket is using an internet [IPv4](https://en.wikipedia.org/wiki/IPv4) address, while the `socket.SOCK_STREAM` indicate this is a [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) socket type.

<div class="info">
TCP is the most commonly used socket type.
The HTTP connection used by your browser for retrieving webpages is a TCP connection type.
</div>

**s.bind(('', 1337))** : This associates your socket with a particular address and port on your computer. The empty string ('') indicates that this socket will accept connections coming in on any IPv4 interfaces. For the port number, you can choose any number above 1023. Port number at or below 1023 are reserved, and may require the program to have special priviledges to run.

<div class="info">
A computer will typically have more than one IP address.
Besides the address allocated to your computer by your router, it will at least have the "127.0.0.1" address for the <a href="https://en.wikipedia.org/wiki/Localhost">Loopback</a> interface.
If you want your server to only respond to connections coming from the same computer, you should replace the empty string in "bind" with '127.0.0.1'.
</div>

**s.listen()** : Tells the socket to start listening for incoming connections.

**conn, addr = s.accept()** : This line waits for a connection from the client. This is a **blocking** function, which means that the next line of code will not run until a connection arrives. It returns a new socket object (`conn`) and the address (`addr`) of the connected client. The first element in `addr` is the IP address of the client, while the second element is the port.

**data = conn.recv(1024)** : This waits for data from the client. The `1024` indicates that we should receive a maximum of 1024 bytes at a time. Note that this is a **maximum**, and that the actual data received may be less. This is another **blocking** function, meaning that the program will not move on to the next line of code until some data is received.

**if not data:** : If `data` is empty, this indicates that the connection is closed by the client and we should exit the `while True` loop.

**print(data.decode())** : This prints the data that was received. Note that the data is a [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) object, and not a string. To print it properly, we'll need to [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) it into a string first.

**conn.sendall(b'Got it!')** : This sends the message 'Got it!' to the client. Notice the `b` at the front? This indicates that this is a bytes object and not a string. Sockets can only send bytes and not string. If you have a string, you'll need to [encode](https://docs.python.org/3/library/stdtypes.html#str.encode) it first.

## Client

The client is the program that initiates a connection.
Once the connection is made, there are no significant differences between the server and the client; both of them can send and receive messages.

Before reading the client code, be sure to read the section on **Server** first, as some of the code are identical and won't be explained again here.

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1337))
while True:
    msg = input('Type your msg here: ')
    s.sendall(msg.encode())
    data = s.recv(1024) # Blocks!
    print(data.decode())
```

**s.connect(('127.0.0.1', 1337))** : This connects to the server at address `127.0.0.1`. If your server and client are on different computers, you'll need to specify the IP address (...that's allocated by the router) of the server here.

**msg = input('Type your msg here: ')** : This reads a string from the user.

**s.sendall(msg.encode())** : This sends the user's message to the server. Since sockets can only send **bytes** object, we'll need to encode the string `msg` into a bytes object using `encode()`.

**data = s.recv(1024)** : Wait for data from the server. Read the server section for details.

## Testing the program

### Local Connection

A local connection is when both the server and the client programs are running on the same computer.

Start the server program first.
It won't do anything yet, as it is waiting for the client to connect.

In a separate terminal, start the client program next.
The server program should now display a message indicating that the client has connected, while the client should now prompt the user for inputs.

Type in your message and press enter.
The message should be printed on the server terminal, while the client terminal should display 'Got it'.

### Remote Connection

In a remote connection, the server and client are running on different computers.
Due to restrictions by the operating system and router, you may need to perform some configuration changes to make it work.

* Make sure your computer allows incoming connections. In Windows, you should make sure your network is configured to **Private**.

* If you have a firewall setup on your computer, you'll need to configure it to allow incoming connections on the port you choose.

* Both the server and client should be connected to the same router.

* While it's possible to make this work even if they are on different routers, you will need to make some additional router configurations, and that is beyond the scope of this tutorial. It's also possible that your ISP will not allow this at all.

* Your router must allow the computers connected to it to communicate with each other. Most home routers allows this by default, while phone hotspots usually do not. If your home router do not allow this, you'll need to change your router configurations, and the steps will depend on your router. If you're on a phone hotspot, this may not be possible at all.

## Further Readings

Sockets can be a big topic, and this tutorial only touches the very basics.
To learn more, read the [Python Sockets Documentations](https://docs.python.org/3/library/socket.html).