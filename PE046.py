from _prime_tools import is_prime
from math import sqrt


def goldbach(vol=0):
    pset = set([2, 3, 5, 7])
    cand = 9
    while True:
        while is_prime(cand):
            pset.add(cand)
            cand += 2
        cset = set([cand - 2*x*x for x in range(1, int(sqrt(cand/2)) + 1)])
        if cset & pset == set():
            return cand
        cand += 2


def solve(vol=0):
    return goldbach()
