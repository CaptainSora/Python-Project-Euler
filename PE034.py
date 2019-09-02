from _int_tools import factorial, int_to_digit_array


def digit_factorials():
    """
    Returns the sum of all numbers which are equal to the sum of the factorial
    of their digits.

    Note that single digit numbers are not included as they are not sums.
    """
    total = 0
    max_digits = 2
    while max_digits * factorial(9) > 10 ** max_digits:
        max_digits += 1
    a = 10
    while a < 10 ** max_digits:
        x = sum(map(factorial, int_to_digit_array(a)))
        if x > a:
            p = 0
            while a % (10 ** p) == 0:
                p += 1
            a += 10 ** p - a % (10 ** p)
            continue
        elif x == a:
            total += a
        a += 1
    return total


def solve(vol=0):
    return digit_factorials()
