import json
from Miller_Primality import miller_prime_test as mp_is_prime

f = open('sieve-10m.txt', 'r')

primes = json.load(f)

f.close()

searchlen = len([x for x in primes if x < 10**4])

# pairwise(a, b) determines if "ab" and "ba" are both prime.
# requires: a, b are positive integers.
# example: pairwise(3, 7) -> True (both 37 and 73 are prime)
def pairwise(a, b):
    if mp_is_prime(int(str(b) + str(a))) and mp_is_prime(int(str(a) + str(b))):
        return True
    return False


pair_dict = {}

for a in range(searchlen):
    for b in range(a+1, searchlen):
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
    if len(common) < depth-1:
        return False
    if depth == 2:
        if len(common) >= 1:
            solution.extend(list(common))
            solution.insert(0, value)
            return True
        return False
    for prime in common:
        if find_pair_set(depth-1, prime, common):
            solution.insert(0, value)
            return True

def find_pair_set_wrapper(size):
    global solution, minsize
    print("Starting wrapper")
    for p in pair_dict:
        common = set(pair_dict[p])
        if len(common) < size-1:
            continue
        for prime in common:
            if find_pair_set(size-1, prime, common):
                solution.insert(0, p)
                print("Found solution of size %d: " % size, solution)
                if minsize == 0 or sum(solution) < minsize:
                    minsize = sum(solution)
    if minsize == 0:
        print("No luck!")
    else:
        print("Minsize: %d" % minsize)

find_pair_set_wrapper(5)