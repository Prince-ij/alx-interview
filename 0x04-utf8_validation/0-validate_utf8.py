#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data.
    :type data: list
    :return: True if data is a valid UTF-8 encoding, otherwise False.
    :rtype: bool
    """
    def is_valid_byte(byte):
        """
        Check if a byte is a valid UTF-8 continuation byte (starts with 10).
        :param byte: The byte to check.
        :type byte: int
        :return: True if valid continuation byte, otherwise False.
        :rtype: bool
        """
        return (byte & 0b11000000) == 0b10000000

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                num_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if not is_valid_byte(byte):
                return False
            num_bytes -= 1

    return num_bytes == 0
