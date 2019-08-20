from _prime_tools import is_prime
from math import sqrt


def goldbach(vol=0):
    """
    Finds the smallest odd composite that is not the sum of a prime and twice
    a square.
    """
    pset = set([2, 3, 5, 7])
    cand = 9
    while True:
        while is_prime(cand):
            pset.add(cand)
            cand += 2
        cset = set([cand - 2*x*x for x in range(1, int(sqrt(cand/2)) + 1)])
        if cset & pset == set():
            if vol >= 1:
                print(f"{cand} is a counterexample.")
            return cand
        cand += 2


def solve(vol=0):
    return goldbach(vol=vol)
