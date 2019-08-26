"""
This module contains functions related to integer formatting and math.
"""
from functools import reduce
from itertools import count


def array_to_int(intarray):
    return int(''.join(intarray))


def int_to_int_array(num):
    return [int(str(num)[a]) for a in range(len(str(num)))]


def int_to_str_array(num):
    return [str(num)[a] for a in range(len(str(num)))]


def int_to_digit_array(num):
    return [int(str(num)[a]) for a in range(len(str(num)))]


def product(numlist):
    return reduce(lambda x, y: x * y, numlist, 1)


def factorial(num):
    return product(list(range(1, num + 1)))


def nCr(n, r):
    return int(product(range(n-r+1, n+1)) / product(range(1, r+1)))


def Collatz(n):
    for i in count(0):
        if n == 1:
            return i
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
