from itertools import count
from _prime_tools import is_prime


def quadratic_primes(bound):
    """
    Returns the product of the coefficients a, b such that n^2 + an + b
    produces the most consecutive primes for values of n starting at 0 where
    abs(a) < bound and abs(b) <= bound.
    """
    product_primes = [1, 0]
    for a in range(-1 * bound + 1, bound):
        for b in range(-1 * bound, bound + 1):
            for n in count(0):
                if not is_prime(n**2 + a*n + b):
                    break
            if n > product_primes[1]:
                product_primes = [a * b, n]
    return product_primes[0]


def solve(vol=0):
    return quadratic_primes(1000)
