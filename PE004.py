from _palindrome_tools import is_palindrome


def largest_palindrome(d, vol=0):
    """
    Returns the largest palindrome made from the product of two d digit
    numbers.
    """
    largest = 0
    for a in range(10 ** (d-1), 10 ** d):
        for b in range(10 ** (d-1), 10 ** d):
            if a * b > largest and is_palindrome(a * b):
                largest = a * b
    return largest


def solve(vol=0):
    return largest_palindrome(3, vol=vol)
