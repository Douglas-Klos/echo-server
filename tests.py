#!/usr/bin/env python3
# pylint: disable=C0103
""" echo server tests """
import socket
import unittest
from time import sleep
from echo_client import client


class EchoTestCase(unittest.TestCase):
    """tests for the echo server and client"""

    def send_message(self, message):
        """Attempt to send a message using the client

        In case of a socket error, fail and report the problem
        """
        try:
            reply = client(message)
        except socket.error as e:
            if e.errno == 61:
                msg = "Error: {0}, is the server running?"
                self.fail(msg.format(e.strerror))
            else:
                self.fail("Unexpected Error: {0}".format(str(e)))
        return reply

    def test_short_message_echo(self):
        """test that a message short than 16 bytes echoes cleanly"""
        sleep(0.01)
        expected = "short message"
        actual = self.send_message(expected)
        self.assertEqual(
            expected, actual, "expected {0}, got {1}".format(expected, actual)
        )

    def test_long_message_echo(self):
        """test that a message longer than 16 bytes echoes in 16-byte chunks"""
        sleep(0.01)
        expected = (
            f"Four score and seven years ago our fathers brought forth on "
            f"this continent, a new nation, conceived in Liberty, and "
            f"dedicated to the proposition that all men are created equal."
        )
        actual = self.send_message(expected)
        self.assertEqual(
            expected, actual, "expected {0}, got {1}".format(expected, actual)
        )


if __name__ == "__main__":
    unittest.main()
