#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
to achieve exactly n 'H' characters in a file.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to result in
    exactly n 'H' characters in the file.

    :param n: Number of 'H' characters to achieve.
    :type n: int
    :return: The fewest number of operations needed, or 0 if impossible.
    :rtype: int
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
