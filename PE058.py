import json
from Miller_Primality import miller_prime_test as mp_is_prime


def spiral_ratio(threshold):
    sp = 1
    prime_counter = 0
    while True:
        sp += 1
        prplist = [4*sp*sp-10*sp+7, 4*sp*sp-8*sp+5, 4*sp*sp-6*sp+3, (2*sp-1)**2]
        for a in prplist:
            if mp_is_prime(a):
                prime_counter += 1
        print(prime_counter, (4*sp-3), (prime_counter / (4*sp-3)))
        if (prime_counter / (4*sp-3)) < threshold:
            print(2*sp-1)
            break

spiral_ratio(0.1)