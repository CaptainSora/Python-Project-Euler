from _prime_tools import is_prime
from _pandigital_tools import generate


def largest_pandigital_prime(vol=0):
    largest = 0
    for setlen in range(9, 0, -1):
        if largest > 0:
            break
        if vol >= 2:
            print(f"Testing subsets of length {setlen}")
        newx = generate(1, setlen)
        for c in newx:
            if c > largest and is_prime(c):
                largest = c
    if vol >= 1:
        print(f"The largest answer is {largest}")
    return largest


def solve(vol=0):
    return largest_pandigital_prime(vol=vol)
