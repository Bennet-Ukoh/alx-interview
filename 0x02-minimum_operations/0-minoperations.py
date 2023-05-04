#!/usr/bin/python3

"""
This module contains a function that calculates the fewest number of
operations needed to result in exactly n H characters in a text file
using only the Copy All and Paste operations
"""


def minOperations(n):
    """
Returns the fewest number of operations needed to result in
exactly n H characters in a text file using only the Copy All
and Paste operations
"""
    if n <= 1:
        return 0

    factor = 2
    operations = 0

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
