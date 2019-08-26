from _prime_tools import sieve


def summation_of_primes(ceiling):
    """
    Returns the sum of all primes below ceiling.
    """
    return sum(sieve(ceiling))


def solve(vol=0):
    return summation_of_primes(2 * 10**6)
