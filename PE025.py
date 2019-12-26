from itertools import count
from _sequence_tools import Fibonacci


def large_fib(d):
    """
    Returns the index of the first term to have at least d digits.
    """
    fg = Fibonacci()
    for i in count(1):
        if next(fg) >= 10 ** (d - 1):
            return i


def solve(vol=0):
    return large_fib(1000)
