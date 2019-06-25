#!/usr/bin/env python3

import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)
server.bind(('localhost', 10000))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    print(f"Waiting for next event...")
    for sock in readable:
        if sock is server:
            connection, client_address = sock.accept()
            print(f"New connection from: {client_address}")
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
        else:
            data = sock.recv(1024)
            if data:
                print(f"Received {data} from {sock.getpeername()}")
                message_queues[sock].put(data)
                if sock not in outputs:
                    outputs.append(sock)
            else:
                print(f"Closing {client_address} after reading no data")
                if sock in outputs:
                    outputs.remove(sock)
                inputs.remove(sock)
                sock.close()
                del message_queues[sock]

    for sock in writable:
        try:
            next_msg = message_queues[sock].get_nowait()
        except queue.Empty:
            print(f"Output queue for {sock.getpeername()} is empty")
            outputs.remove(sock)
        else:
            print(f"Sending {next_msg} to {sock.getpeername()}")
            sock.send(next_msg)

    for sock in exceptional:
        print(f"Handling exceptional condition for {sock.getpeername()}")
        inputs.remove(sock)
        if sock in outputs:
            outputs.remove(sock)
        sock.close()
        del message_queues[sock]
