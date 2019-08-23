"""
This module contains functions related to integer formatting.
"""


def array_to_int(intarray):
    return int(''.join(intarray))


def int_to_int_array(num):
    return [int(str(num)[a]) for a in range(len(str(num)))]


def int_to_str_array(num):
    return [str(num)[a] for a in range(len(str(num)))]
