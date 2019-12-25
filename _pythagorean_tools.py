"""
This module contains functions which are related to Pythagorean triples and
right triangles.
"""

from math import sqrt


def find_pythag_trips(p):
    """
    Returns all integer sets {x, y, z} such that:
        x <= y < z and x + y + z = p

    Given that p = x + y + z
                 = x + y + sqrt(x^2 + y^2)
    We can derive y = (p*(p-2x))/(2(p-x))

    We also have that x < p + p/sqrt(2).
    """
    pythag_trips = []
    max_x = int(p - p/sqrt(2))
    for x in range(1, max_x + 1):
        y = int((p * (p - 2*x)) / (2 * (p - x)))
        z = int(sqrt(x**2 + y**2))
        if x + y + z == p:
            pythag_trips.append([x, y, z])
    return pythag_trips
