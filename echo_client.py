#!/usr/bin/env python3
#pylint: disable=W0703
"""
    Echo client.  Sends string from command line and prints stream.
    The outline for this was already completed for us.  We just had to fill in the TODO
    sections.  Takes a lot of the challange and thinking out of the assignment.
    I deleted all the instructor comments, they were cluttering up my screen.
"""

import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    """ Sends message to server and prints reply """
    server_address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.connect(server_address)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)

    received_message = ''

    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        msg = msg.encode('utf8')
        sock.sendall(msg)

        while len(received_message) < len(msg):
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message += chunk.decode('utf8')

    except Exception:
        traceback.print_exc()
        sys.exit(1)
    finally:
        sock.close()
        print('closing socket', file=log_buffer)

    return received_message


def main():
    """ We Wuz Main """
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)


if __name__ == '__main__':
    main()
