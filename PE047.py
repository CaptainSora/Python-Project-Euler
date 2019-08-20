from _prime_tools import sieve
from math import sqrt


def count_factors(num):
    """
    Returns a list of remainders of prime divisors for num

    e.g. input 43, test with primes [2, 3, 5], output [1, 1, 3]
    """
    pf = 0
    # Generate potential prime factors
    ppf_list = sieve(int(sqrt(num)))
    for x in ppf_list:
        if num % x == 0:
            pf += 1
            while num % x == 0:
                num /= x
        if num == 1:
            break
    if num > 1:
        pf += 1
    return pf


def consecutive(length, dpf, vol=0):
    """
    Returns the smallest of the first length consecutive integers to have dpf
    distinct prime factors.
    """
    cand = 3
    while True:
        if count_factors(cand) == dpf:
            len_so_far = 1
            lowest = cand
            # Count below
            temp_cand = cand - 1
            while count_factors(temp_cand) == dpf:
                len_so_far += 1
                lowest = temp_cand
                temp_cand -= 1
            # Count above
            temp_cand = cand + 1
            while count_factors(temp_cand) == dpf:
                len_so_far += 1
                temp_cand += 1
            # Check sequence length
            if len_so_far >= length:
                if vol >= 1:
                    print(f"Found chain starting with {lowest}.")
                return lowest
        cand += 4


def solve(vol=0):
    return consecutive(4, 4, vol=vol)
