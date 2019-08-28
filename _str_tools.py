"""
This module contains functions related to string formatting and math.
"""


def to_num(word, case="upper"):
    """
    Calculates the value of the word.

    "upper": all letters are uppercase
    "lower": all letters are lowercase
    """
    if case == "upper":
        base = ord("A") - 1
    elif case == "lower":
        base = ord("a") - 1

    value = 0
    for char in word.strip('"'):
        value += ord(char) - base
    return value
