from math import prod
from _pythagorean_tools import find_pythag_trips


def pythagorean_triplet(total):
    """
    Returns the product abc of a pythagorean triplet a^2 + b^2 = c^2 where
    a + b + c = total.
    """
    return prod(find_pythag_trips(total)[0])


def solve(vol=0):
    return pythagorean_triplet(1000)
