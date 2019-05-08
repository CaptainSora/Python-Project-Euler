import json, math

smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
ceilings = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 341550071728321, 3825123056546413051, 3825123056546413051, 3825123056546413051, 318665857834031151167461, 3317044064679887385961981]

f = open('sieve-100m.txt', 'r')
primes = set(json.load(f))
f.close()

# Works for n < 3.31 x 10 ^ 24

def miller_prime_test(n):
    # Quick trial division
    if n < 10 ** 8:
        if n in primes:
            return True
        return False
    print("Large number testing: %d" % n)
    # Size verification
    if n >= ceilings[-1]:
        print("Too big! Test failed.")
        return False
    # Prime testing setup
    index = 1
    while n > ceilings[index-1]:
        index += 1
    # Miller primality test with smallprimes[:index]
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = int(d/2)
        r += 1
    for a in smallprimes[:index]:
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        if x == n-1:
            continue
        # Composite
        return False
    # Prime
    return True