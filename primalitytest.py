import json, math

f = open('sieve-1m.txt', 'r')

primes = json.load(f)

f.close()

# is_prime(num) tests the primality of num by trial division.
# requires: num < sqr(1000000)
# Int -> Bool
def is_prime(num):
    sqrt = math.sqrt(num)
    for a in primes:
        if a > sqrt:
            return True
        if num % a == 0:
            return False


def factor(num):
    factors = []
    while num not in primes:
        for a in primes:
            if num % a == 0:
                factors.append(a)
                num /= a
                break
    factors.append(int(num))
    return factors