def even_fib(ceiling, vol=0):
    """
    Returns the sum of all even Fibonacci numbers not exceeding ceiling.
    """
    total = 0
    a = 1
    b = 1
    while b <= ceiling:
        b += a
        a = b - a
        if b % 2 == 0:
            total += b
    return total


def solve(vol=0):
    return even_fib(4 * 10**6)
