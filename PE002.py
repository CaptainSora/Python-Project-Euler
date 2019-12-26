from _sequence_tools import Fibonacci


def even_fib(ceiling):
    """
    Returns the sum of all even Fibonacci numbers not exceeding ceiling.
    """
    total = 0
    fg = Fibonacci()
    n = next(fg)
    while n <= ceiling:
        if n % 2 == 0:
            total += n
        n = next(fg)
    return total


def solve(vol=0):
    return even_fib(4 * 10**6)
