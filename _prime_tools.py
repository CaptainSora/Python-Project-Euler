"""This module contains prime-testing functions."""
from itertools import compress
from time import perf_counter

# Required for the Miller-Rabin Primality Test
smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
ceilings = [
    2047,
    1373653,
    25326001,
    3215031751,
    2152302898747,
    3474749660383,
    341550071728321,
    341550071728321,
    3825123056546413051,
    3825123056546413051,
    3825123056546413051,
    318665857834031151167461,
    3317044064679887385961981
]


def is_prime(n):
    """Tests if a number is prime using the Miller-Rabin Primality Test.

    n: works up to 3.31 x 10 ^ 24
    """
    # Size verification
    if n <= 1:
        print("Requires n >= 2.")
        return False
    elif n >= ceilings[-1]:
        print("Too big! Test failed.")
        return False
    # Prime testing setup
    index = 1
    while n > ceilings[index - 1]:
        index += 1
    # Miller primality test with smallprimes[:index]
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = int(d / 2)
        r += 1
    for a in smallprimes[:index]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        if x == n - 1:
            continue
        # Composite
        return False
    # Prime
    return True


def primegen():
    yield 2
    p = 3
    while True:
        while not is_prime(p):
            p += 2
        yield p
        p += 2


def sieve(size, floor=2):
    """
    Returns a list of all primes up to and including size.

    Optionally, excludes primes below floor.
    """
    is_prime = [True] * (size + 1)
    for i in range(2, size):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])
    return [x for x in list(compress(range(size), is_prime)) if x >= floor]
