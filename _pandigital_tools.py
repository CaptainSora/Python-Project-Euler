"""
This module contains functions related in some way to pandigital numbers.
"""

from itertools import permutations


def generate(start, stop):
    """
    Generates a set of all pandigital numbers between start and stop inclusive

    requires: 0 <= start <= stop <= 9
    """
    x = set(permutations(range(start, stop + 1), stop-start+1))
    newx = []
    for a in x:
        new = 0
        for b in a:
            new = 10 * new + b
        newx.append(new)
    return newx


def is_pandigital(numlist, n=9):
    """
    Predicate for whether all values in numlist are 1 through n pandigital.

    Accepts list of num or list of str
    """
    PANDIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return PANDIGITS[:n] == sorted(list(''.join(list(map(str, numlist)))))
