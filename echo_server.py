#!/usr/bin/env python3
# pylint: disable=W0703, R1702
"""
    Echo server.  Awaits for connection, and replies with what it receives
    The outline for this was already completed for us.  We just had to fill in the TODO
    sections.  Takes a lot of the challange and thinking out of the assignment.
    I deleted all the instructor comments, they were cluttering up my screen.
"""

import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    """ Echo server """

    server_address = ("127.0.0.1", 10000)
    try:
        while True:

            print("making a server on {0}:{1}".format(*server_address), file=log_buffer)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(server_address)
            sock.listen(1)

            print("waiting for a connection", file=log_buffer)
            conn, addr = sock.accept()

            try:
                print(f"connection - {addr[0]}:{addr[1]}", file=log_buffer)

                while True:
                    data = conn.recv(16)
                    if not data:
                        break
                    print(f'received "{data.decode("""utf8""")}"')

                    conn.sendall(data)
                    print(f'sent "{data.decode("""utf8""")}"')

            except Exception:
                traceback.print_exc()
                sys.exit(1)
            finally:
                sock.close()
                print("echo complete, client connection closed", file=log_buffer)

    except KeyboardInterrupt:
        sock.close()
        print("quitting echo server", file=log_buffer)
        sys.exit(0)


def main():
    """ REEEEEEEEEEEEEEEEEE """
    server()
    sys.exit(0)


if __name__ == "__main__":
    main()
