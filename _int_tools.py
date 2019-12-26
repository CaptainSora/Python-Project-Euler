"""
This module contains functions related to integer formatting and math.
"""
from functools import reduce
from math import gcd, prod


# ================ ARRAY FORMATTING FUNCTIONS ================

def str_array_to_int(intarray):
    return int(''.join(intarray))


def int_array_to_int(intarray):
    return str_array_to_int(map(str, intarray))


def int_to_int_array(num):
    """
    Deprecated, use int_to_digit_array(num)
    """
    return [int(str(num)[a]) for a in range(len(str(num)))]


def int_to_str_array(num):
    return [str(num)[a] for a in range(len(str(num)))]


def int_to_digit_array(num):
    return [int(str(num)[a]) for a in range(len(str(num)))]


# ================ CALCULATION FUNCTIONS ================

def product(numlist):
    """
    Deprecated since Python 3.8, use math.prod instead
    Also remove functools.reduce
    """
    return reduce(lambda x, y: x * y, numlist, 1)


def factorial(num):
    return prod(list(range(1, num + 1)))


def nCr(n, r):
    return int(prod(range(n-r+1, n+1)) / prod(range(1, r+1)))


def phi(n):
    """
    Returns the value of ϕ(n), or the Euler Totient function.
    """
    return len([x for x in range(1, n) if gcd(n, x) == 1])
