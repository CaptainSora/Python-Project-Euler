from _int_tools import int_to_digit_array


def digit_sum(num):
    """
    Returns the sum of the digits of num.
    """
    return sum(int_to_digit_array(num))


def solve(vol=0):
    return digit_sum(2 ** 1000)
