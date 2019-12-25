"""
This module contains functions related in some way to prime numbers.
"""

from itertools import compress
from functools import reduce
from time import perf_counter
from math import sqrt

# Required for the Miller-Rabin Primality Test
SMALLPRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
CEILINGS = [  # https://oeis.org/A006945
    9,
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
        return False
    elif n <= SMALLPRIMES[-1]:
        return n in SMALLPRIMES
    elif n >= CEILINGS[-1]:
        print("Too big! Test failed.")
        return False
    # Prime testing setup
    index = 1
    while n >= CEILINGS[index - 1]:
        index += 1
    # Miller primality test with SMALLPRIMES[:index]
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = int(d / 2)
        r += 1
    for a in SMALLPRIMES[:index]:
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
    size += 1
    is_prime = [True] * (size)
    for i in range(2, size):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])
    return [x for x in list(compress(range(size), is_prime)) if x >= floor]


def prime_factors(num, mode="count"):
    """
    "count" : Returns the number of unique prime factors of num.
    "max"   : Returns the greatest prime factor of num.
    "min"   : Returns the smallest prime factor of num.
    "list"  : Returns a list of prime factors of num.
    "dict"  : Returns a dict of the prime factorization of num.

    e.g. input 43, test with primes [2, 3, 5], remainder [1, 1, 3]
    """
    pfactors = {}
    # Generate potential prime factors
    ppf_list = sieve(int(sqrt(num)))
    for x in ppf_list:
        if num % x == 0:
            pfactors[x] = 0
            while num % x == 0:
                pfactors[x] += 1
                num /= x
        if num == 1:
            break
    if num > 1:
        pfactors[num] = 1
    pflist = list(pfactors.keys())
    pflist.sort()
    # Output based on mode
    if mode == "count":
        return len(pflist)
    elif mode == "max":
        return pflist[-1]
    elif mode == "min":
        return pflist[0]
    elif mode == "list":
        return pflist
    elif mode == "dict":
        return pfactors


def all_factors(num, mode="list"):
    """
    "list" : Returns a list of all proper divisors of num.
    "sum"  : Returns the sum of all proper divisors of num.
    """
    pfac_dict = prime_factors(num, mode="dict")
    pfac = [[x, pfac_dict[x]] for x in pfac_dict]
    pfac.sort(key=lambda x: x[0])
    fac_list = []
    pfac_cur = [[x[0], 0] for x in pfac]
    while pfac_cur != pfac:
        fac_list.append(int(reduce(lambda x, y: x * y[0]**y[1], pfac_cur, 1)))
        pfac_cur[0][1] += 1
        for i in range(len(pfac_cur)):
            if pfac_cur[i][1] > pfac[i][1]:
                pfac_cur[i][1] = 0
                pfac_cur[i+1][1] += 1
            else:
                break
    if mode == "list":
        return fac_list
    elif mode == "sum":
        return sum(fac_list)


def LCM(numlist):
    """
    Returns the least common multiple of all natural numbers in numlist.
    """
    numlist = [int(x) for x in numlist if x > 1]
    LCMdict = {}
    for a in numlist:
        numdict = prime_factors(a, mode="dict")
        for b in numdict:
            if b not in LCMdict:
                LCMdict[b] = 0
            LCMdict[b] = max(LCMdict[b], numdict[b])
    # Remultiply to get result
    product = 1
    for c in LCMdict:
        product *= c ** LCMdict[c]
    return product
