import itertools

def sieve(size):
    is_prime = [True] * (size)
    for i in range(2, size):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])
    f.write(json.dumps(list(itertools.compress(range(size), is_prime))[2:]))
