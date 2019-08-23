"""
This module contains functions related in some way to palindromes.
"""


def is_palindrome(num):
    """
    Returns true if num is a palindrome.
    """
    return str(num) == str(num)[::-1]
