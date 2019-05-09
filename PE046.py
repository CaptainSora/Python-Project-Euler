import json

f = open('sieve.txt', 'r')

primes = json.load(f)

def generate(prev):
    prev += 2
    while (prev in primes):
        prev += 2
    return prev

def goldbach(candidate):
    while True:
        test = False
        index = 0
        while candidate > primes[index]:
            square = 1
            while candidate > primes[index] + 2 * square * square:
                square += 1
            if candidate == primes[index] + 2 * square * square:
                test = True
                break
            index += 1
        if test:
            print("%d failed" % candidate)
            candidate = generate(candidate)
        else:
            print("%d is a counterexample!" % candidate)
            break

goldbach(9)
