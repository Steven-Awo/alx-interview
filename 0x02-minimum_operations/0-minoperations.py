#!/usr/bin/python3
"""
The minimum's Operations
"""

import math


def factors(n):
    """The factors that are of the n number"""
    my_list = []
    while n % 2 == 0:
        my_list.append(2)
        n = n / 2
    for a in range(3, int(math.sqrt(n)) + 1, 2):
        while n % a == 0:
            my_list.append(a)
            n = n / a
    if n > 2:
        my_list.append(n)
    return my_list


def minOperations(n):
    """Calculating for the minimum's operations"""
    if type(n) != int or n < 2:
        return 0
    else:
        num_of_Operations = sum(factors(n))
        return int(num_of_Operations)
