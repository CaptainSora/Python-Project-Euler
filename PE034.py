from itertools import combinations_with_replacement
from _int_tools import factorial
from _int_tools import int_array_to_int
from _int_tools import int_to_digit_array


def digit_factorials():
    """
    Returns the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note that single digit numbers are not included as they are not sums.
    """
    max_digits = 2
    while max_digits * factorial(9) > 10 ** max_digits:
        max_digits += 1
    sumtotal = 0
    for n in range(2, max_digits + 1):
        for x in combinations_with_replacement(range(10), n):
            if int_array_to_int(x) >= max_digits * factorial(9):
                break
            total = 0
            for digit in x:
                total += factorial(int(digit))
            if sorted(int_to_digit_array(total)) == sorted(x):
                sumtotal += total
    return sumtotal


def solve(vol=0):
    return digit_factorials()
