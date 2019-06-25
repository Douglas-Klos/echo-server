#!/usr/bin/env python3
import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    """ Echo server """

    server_address = ('127.0.0.1', 10000)
    try:
        while True:

            print("making a server on {0}:{1}".format(*server_address), file=log_buffer)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(server_address)
            sock.listen(1)

            print('waiting for a connection', file=log_buffer)
            conn, addr = sock.accept()

            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                while True:
                    data = conn.recv(16)
                    if not data:
                        break
                    print('received "{0}"'.format(data.decode('utf8')))

                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))

            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                sock.close()
                print('echo complete, client connection closed', file=log_buffer)

    except KeyboardInterrupt:
        sock.close()
        print('quitting echo server', file=log_buffer)
        sys.exit(0)


def main():
    server()
    sys.exit(0)

if __name__ == '__main__':
    main()
