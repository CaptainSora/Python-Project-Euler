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
            if vol >= 3:
                print("%d failed" % candidate)
            candidate = generate(candidate)
        else:
            if vol >= 1:
                print("%d is a counterexample!" % candidate)
            break


def solve(vol=0):
    return goldbach(9, vol=vol)
