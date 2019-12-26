from itertools import count
from _pandigital_tools import is_pandigital


def pand_products():
    """
    Returns the sum of all numbers n which have a factorization a * b = n such
    that a, b, n are (cumulatively) 1 through 9 pandigital.
    """
    total = set()
    for a in range(2, 100):
        for b in count(a):
            if len(str(a) + str(b) + str(a * b)) > 9:
                break
            elif is_pandigital([a, b, a * b]):
                total.add(a * b)
    return sum(list(total))


def solve(vol=0):
    return pand_products()
