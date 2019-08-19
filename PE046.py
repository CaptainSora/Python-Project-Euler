from Miller_Primality import is_prime


def generate(prev):
    prev += 2
    while not is_prime(prev):
        prev += 2
    return prev


def goldbach(candidate):
    while True:
        test = False
        index = 0
        while candidate > primes[index]:
            square = 1
            while candidate > primes[index] + 2 * square**2:
                square += 1
            if candidate == primes[index] + 2 * square**2:
                test = True
                break
            index += 1
        if test:
            print("%d failed" % candidate)
            candidate = generate(candidate)
        else:
            print("%d is a counterexample!" % candidate)
            break


def solve():
    return goldbach(9)
