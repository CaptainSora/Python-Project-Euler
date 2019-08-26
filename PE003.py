from _prime_tools import prime_factors


def largest_prime_factor(num):
    """
    Returns the largest prime factor of num.
    """
    return prime_factors(num, mode="max")


def solve(vol=0):
    return largest_prime_factor(600851475143)
