def selfpowers(d, stop, vol=0):
    """
    Returns the last d digits of 1^1 + 2^2 + ... + stop ^ stop
    """
    sum = 0
    for a in range(1, stop + 1):
        sum += a**a
        sum %= 10**d
    if vol >= 1:
        print(f"The last {d} digits are {sum}")
    return sum


def solve(vol=0):
    return selfpowers(10, 1000, vol=vol)
