from _prime_tools import primegen


def nth_prime(n, vol=0):
    pg = primegen()
    for a in range(1, n - 1):
        next(pg)
    return next(pg)


def solve(vol=0):
    return nth_prime(10001, vol=vol)
