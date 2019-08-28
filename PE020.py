from PE016 import digit_sum
from _int_tools import factorial


def factorial_digit_sum(n):
    """
    Returns the sum of the digits in the number n!
    """
    return digit_sum(factorial(n))


def solve(vol=0):
    return factorial_digit_sum(100)
