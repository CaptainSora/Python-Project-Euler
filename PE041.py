import itertools
from primalitytest import is_prime
from pandigital import generate


def largest_pandigital_prime():
    largest = 0
    for setlen in range(9, 0, -1):
        if largest > 0:
            break
        print(f"Testing subsets of length {setlen}")
        newx = generate(1, setlen)
        for c in newx:
            if c > largest and is_prime(c):
                largest = c
    print(f"The largest answer is {largest}")
    return largest


def solve():
    return largest_pandigital_prime()
