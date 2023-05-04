#!/usr/bin/python3

"""
This module contains a function that calculates the fewest number of operations needed
to obtain a sequence of length n using the operations Copy All and Paste.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain a sequence of length n.
    Returns 0 if n <= 1.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        if n % factor == 0:
            operations += (n // factor)
            n //= factor
        else:
            factor += 1
    
    return operations
