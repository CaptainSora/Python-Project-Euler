from _prime_tools import LCM


def smallest_multiple(start, stop):
    """
    Returns the smallest positive number which is evenly divisible by all of
    the numbers between start and stop inclusive.
    """
    return LCM(list(range(start, stop + 1)))


def solve(vol=0):
    return smallest_multiple(2, 20)
