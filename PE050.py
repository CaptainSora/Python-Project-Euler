import json

f = open('sieve-1m.txt', 'r')

primes = json.load(f)

f.close()

def consecutive_prime_sum(ceiling):
    # Requirement assertion
    if (ceiling > 1000000):
        print("Ceiling too high! Max value: 1 000 000")
        return
    
    len_primes = len([x for x in primes if x < ceiling])
    maxlen = 0
    primevalue = 0

    for a in range(len_primes):
        # Don't bother continuing if impossible to find longer consecutive sum
        if len_primes - a < maxlen:
            break
        # Start consecutive summation from primes[a]
        for b in range(maxlen + 1, len_primes):
            # Arry indexing assertion
            if a + b >= len_primes:
                # If true, primes[a+b] is greater than ceiling or invalid index
                break
            primesum = sum(primes[a:a+b])
            if primesum > ceiling:
                break
            if primesum in primes[:len_primes]:
                maxlen = b
                primevalue = primesum
    print("The prime is %d which is a sum of %d consecutive primes." % (primevalue, maxlen))

consecutive_prime_sum(1000000)