"""
This module contains functions related to integer sequences.
"""


def Collatz(n):
    """
    Returns the number of steps required for n to reach 1.
    """
    for i in count(0):
        if n == 1:
            return i
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1


def Fibonacci():
    """
    Fibonacci number generator.
    """
    a = 1
    b = 1
    yield a
    yield b
    while True:
        b += a
        a = b - a
        yield b
