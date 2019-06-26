#!/usr/bin/env python3
# pylint: disable=W1401
""" Prints the services associated with specified port range """

from socket import getservbyport
import sys


def servicve_by_port(start, end):
    """ Determines service on port and prints result """
    for port in range(start, end + 1):
        try:
            print(f"Port {port}: {getservbyport(port)}")
        except OSError:
            print(f"Port {port}: No service found on port")


def main():
    """
       _____      _____  .___ _______
      /     \    /  _  \ |   |\      \
     /  \ /  \  /  /_\  \|   |/   |   \
    /    Y    \/    |    \   /    |    \
    \____|__  /\____|__  /___\____|__  /
            \/         \/            \/
    """

    # Thought I'd try a different approach for input checking...
    #   Try to throw an error, if you can't, things must have been OK.
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        assert -1 < end < 65536
        assert -1 < start <= end
    except (ValueError, IndexError, AssertionError):
        print("Usage: service_by_port.py <start port> <end port>")
        print("Port range values: 0 - 65535")
        sys.exit(1)

    servicve_by_port(start, end)


if __name__ == "__main__":
    main()
