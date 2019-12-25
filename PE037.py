from _prime_tools import is_prime


def truncatable(num):
    """
    Returns true if num is a truncatable prime from left to right and right to
    left.
    A truncatable prime is a prime which remains prime as digits are removed
    from either end.
    """
    if len(str(num)) < 2 or not is_prime(num):
        return False
    return all(
        [is_prime(int(str(num)[:b])) for b in range(1, len(str(num)))] +
        [is_prime(int(str(num)[b:])) for b in range(1, len(str(num)))]
    )


def sum_truncatable_primes(ceiling):
    """
    Returns the sum of all truncatable primes below ceiling.
    """
    return sum([a for a in range(ceiling) if truncatable(a)])


def solve(vol=0):
    return sum_truncatable_primes(1000000)
