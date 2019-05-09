import json, itertools

f = open('sieve.txt', 'r')

primes = json.load(f)
print(primes[0])

f.close()

four_digit_primes = [a for a in primes if 1000 < a < 10000]

permutations = {}

for prime in four_digit_primes:
    x = itertools.permutations(str(prime))
    p = []
    for perm in x:
        value = int(''.join(perm))
        if value > 1000:
            p.append(value)
    p = list(dict.fromkeys(p))
    p.sort()
    if p[0] not in permutations:
        common = list(set(p) & set(four_digit_primes))
        common.sort()
        if len(common) > 2:
            permutations[p[0]] = common

for a in permutations:
    for b in permutations[a]:
        for c in [x for x in permutations[a] if x > b]:
            if 2 * c - b in permutations[a]:
                print("Found %d%d%d" % (b, c, 2*c-b))
