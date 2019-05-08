import itertools, timeit, json

f = open('sieve-10k.txt', 'w')

def sieve(size):
    is_prime = [True] * (size)
    for i in range(2, size):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])
    f.write(json.dumps(list(itertools.compress(range(size), is_prime))[2:]))

print(timeit.timeit(setup='from __main__ import sieve', stmt='sieve(10**4)', number=1))