"""
This module contains functions related in some way to pandigital numbers.
"""

from itertools import permutations
from _int_tools import int_array_to_int


def generate(start, stop):
    """
    Generates a list of all pandigital numbers between start and stop inclusive

    requires: 0 <= start <= stop <= 9
    """
    return [
        int_array_to_int([b for b in a])
        for a in permutations(range(start, stop + 1), stop-start+1)
    ]


def is_pandigital(numlist, n=9):
    """
    Predicate for whether all values in numlist are 1 through n pandigital.

    Accepts list of num or list of str
    """
    PANDIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return PANDIGITS[:n] == sorted(map(str, numlist))
