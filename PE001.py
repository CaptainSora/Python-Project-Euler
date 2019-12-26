from math import floor


def sum_of_multiples(a, b, ceiling):
    """
    Returns the sum of all multiples of a and b below ceiling.
    """
    return sum([x for x in range(ceiling) if x % a == 0 or x % b == 0])


def solve(vol=0):
    return sum_of_multiples(3, 5, 1000)
