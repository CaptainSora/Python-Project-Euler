"""
This module contains functions related in some way to pandigital numbers.
"""


import itertools


def generate(start, stop):
    """
    generates a set of all pandigital numbers between start and stop inclusive

    requires: 0 <= start <= stop <= 9
    """
    x = set(itertools.permutations(range(start, stop + 1), stop-start+1))
    newx = []
    for a in x:
        new = 0
        for b in a:
            new = 10 * new + b
        newx.append(new)
    return newx
