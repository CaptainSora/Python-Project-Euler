from _prime_tools import sieve
from itertools import permutations


def four_digit_prime_permutations(vol=0):
    """
    Finds the second arithmetic sequence made of three 4-digit primes.
    """
    four_digit_primes = sieve(10**4, floor=10**3)
    ppdict = {}

    for prime in four_digit_primes:
        permstrs = permutations(str(prime))
        prime_perms = []
        for perm in permstrs:
            value = int(''.join(perm))
            if value in four_digit_primes:
                prime_perms.append(value)
        if len(prime_perms) >= 3:
            prime_perms.sort()
            if prime_perms[0] not in ppdict:
                ppdict[prime_perms[0]] = prime_perms

    for cand_pp in ppdict:
        if cand_pp == 1487:
            continue
        for a in ppdict[cand_pp]:
            for b in [x for x in ppdict[cand_pp] if x > a]:
                if 2 * b - a in ppdict[cand_pp]:
                    solution = int(f"{a}{b}{2 * b - a}")
                    if vol >= 1:
                        print(f"Found solution {solution}")
                    return solution


def solve(vol=0):
    return four_digit_prime_permutations(vol=vol)
