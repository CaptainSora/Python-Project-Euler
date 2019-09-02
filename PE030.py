from _int_tools import int_to_int_array


def digit_powers(p):
    """
    Returns the sum of all numbers which can be written as the sum of pth
    powers of their digits.
    """
    total = 0
    sum_digits = 2
    # While the number of digits is still plausible:
    while sum_digits * 9**p > 10 ** (sum_digits - 1):
        for i in range(10 ** (sum_digits - 1), 10 ** sum_digits):
            # Remove implausible sums
            if i > sum_digits * 9**p:
                break
            elif i == sum(map(lambda x: x ** p, int_to_int_array(i))):
                total += i
        sum_digits += 1
    return total


def solve(vol=0):
    return digit_powers(5)
