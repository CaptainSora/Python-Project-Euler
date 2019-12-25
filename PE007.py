from _prime_tools import primegen


def nth_prime(n, vol=0):
    """
    Returns the nth prime using primegen.
    """
    pg = primegen()
    for _ in range(n - 1):
        next(pg)
    return next(pg)


def solve(vol=0):
    return nth_prime(10001, vol=vol)
