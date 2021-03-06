from math import gcd
from math import prod
from _int_tools import int_array_to_int
from _int_tools import int_to_digit_array


def simplify(frac):
    """
    Takes a fraction a/b as [a, b] and returns it in simplest form.
    """
    GCD = gcd(frac[0], frac[1])
    return [int(frac[0] / GCD), int(frac[1] / GCD)]


def fake_simplify(frac):
    """
    Takes a fraction a/b as [a, b] and returns a fake simplification obtained
    by cancelling out one of the digits from a and b, in simplest form.

    Ignores trivial case where the common digit is 0.

    If no common digit exists, returns False.
    """
    frac = list(map(int_to_digit_array, frac))
    for d in frac[0]:
        if d == 0:
            continue
        elif d in frac[1]:
            frac[0].remove(d)
            frac[1].remove(d)
            return simplify(list(map(int_array_to_int, frac)))
    return False


def digit_cancelling_fractions():
    """
    Returns the denominator of the product of all digit cancelling fractions
    in simplest form. Fractions must have two-digit numerator and denominators
    and have 0 < a/b < 1.
    """
    fraclist = []
    for a in range(10, 100):
        for b in range(a+1, 100):
            f = fake_simplify([a, b])
            if not f and f == simplify([a, b]):
                fraclist.append([a, b])
    return prod([x[1] for x in fraclist])


def solve(vol=0):
    return digit_cancelling_fractions()
