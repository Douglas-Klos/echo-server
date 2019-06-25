#!/usr/bin/env python3
import socket
import sys

messages = [ 'This is the message. '.encode('utf8'),
             'It will be sent '.encode('utf8'),
             'in parts.'.encode('utf8'),
             ]


server_address = ('localhost', 10000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

# Connect the socket to the port where the server is listening
print(f"connecting to {server_address[0]} port {server_address[1]}")
for sock in socks:
    sock.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for sock in socks:
        print(f"{sock.getsockname()}: sending '{message}'")
        sock.send(message)

    # Read responses on both sockets
    for sock in socks:
        data = sock.recv(1024)
        print(f"{sock.getsockname()}: received '{data}'")
        if not data:
            print(f"closing socket {sock.getsockname()}")
            sock.close()
