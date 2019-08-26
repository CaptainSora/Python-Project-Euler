from _prime_tools import prime_factors
from _polygonal_tools import poly
from _int_tools import product
from itertools import count


def highly_divisible_poly(n, req_factors):
    """
    Returns the first n-gonal number to have req_factors divisors.
    """
    for i in count(1):
        pfactors = prime_factors(poly(n, i), mode="dict")
        if product([pfactors[x] + 1 for x in pfactors]) >= req_factors:
            return poly(n, i)


def solve(vol=0):
    return highly_divisible_poly(3, 500)
