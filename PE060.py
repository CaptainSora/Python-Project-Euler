import time
import json
from runtime import record_time
from Miller_Primality import is_prime

filestart = time.perf_counter()

f = open('sieve-10m.txt', 'r')
primes = json.load(f)
f.close()

searchlen = len([x for x in primes if x < 10**4])


def pairwise(a, b):
    """ Determines if the concatenation of a and b in both ways is prime.

    >>>pairwise(3, 7)
    True
    """
    if is_prime(int(str(b) + str(a))) and is_prime(int(str(a) + str(b))):
        return True
    return False


pair_dict = {}

for a in range(searchlen):
    for b in range(a + 1, searchlen):
        if pairwise(primes[a], primes[b]):
            if primes[a] in pair_dict:
                pair_dict[primes[a]].append(primes[b])
            else:
                pair_dict[primes[a]] = [primes[b]]

solution = []
minsize = 0


def find_pair_set(depth, value, intersection):
    global solution
    if value not in pair_dict:
        return False
    common = intersection & set(pair_dict[value])
    if len(common) < depth - 1:
        return False
    if depth == 2:
        if len(common) >= 1:
            solution.extend(list(common))
            solution.insert(0, value)
            return True
        return False
    for prime in common:
        if find_pair_set(depth - 1, prime, common):
            solution.insert(0, value)
            return True


def find_pair_set_wrapper(size):
    global solution, minsize
    for p in pair_dict:
        common = set(pair_dict[p])
        if len(common) < size - 1:
            continue
        for prime in common:
            if find_pair_set(size - 1, prime, common):
                solution.insert(0, p)
                print("Found solution of size %d: " % size, solution)
                if minsize == 0 or sum(solution) < minsize:
                    minsize = sum(solution)
    if minsize == 0:
        print("No luck!")
    else:
        print("Minsize: %d" % minsize)


def runtime(output=False):
    funcstart = time.perf_counter()
    # FUNCTION CALL
    find_pair_set_wrapper(5)
    functime = time.perf_counter() - funcstart
    filetime = time.perf_counter() - filestart
    if output:
        print(f"Time: {functime:.3}")
    record_time(60, functime, filetime)

runtime(True)
