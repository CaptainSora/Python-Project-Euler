"""
This module contains functions dealing with polygonal numbers.
"""

from itertools import count


def poly(n, t):
    """
    Returns term t of the n-gonal numbers.
    """
    if n == 3:
        return int(t * (t + 1) / 2)
    elif n == 5:
        return int(t * (3*t - 1) / 2)
    elif n == 6:
        return t * (2*t - 1)


def is_polygonal(n, num):
    """
    Predicate for if num is a n-gonal number.
    """
    for i in count(0):
        if poly(n, i) < num:
            continue
        elif poly(n, i) == num:
            return True
        return False
