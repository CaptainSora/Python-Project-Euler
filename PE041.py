import itertools
from primalitytest import is_prime
from pandigital import generate

def largest_pandigital_prime():
    largest = 0
    for setlen in range(9, 0, -1):
        if largest > 0:
            break
        print("Testing subsets of length %d" % setlen)
        newx = generate(1, setlen)
        for c in newx:
            if c > largest and is_prime(c):
                largest = c
    print("The largest answer is %d" % largest)

largest_pandigital_prime()