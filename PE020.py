from _int_tools import factorial
from _int_tools import int_to_digit_array


def factorial_digit_sum(n):
    """
    Returns the sum of the digits in the number n!
    """
    return sum(int_to_digit_array(factorial(n)))


def solve(vol=0):
    return factorial_digit_sum(100)
