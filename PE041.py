from _pandigital_tools import generate
from _prime_tools import is_prime


def largest_pandigital_prime():
    """
    Returns the largest n-digital pandigital prime.
    """
    largest = 0
    for setlen in range(9, 0, -1):
        if largest > 0:
            break
        for c in generate(1, setlen):
            if c > largest and is_prime(c):
                largest = c
    return largest


def solve(vol=0):
    return largest_pandigital_prime()
