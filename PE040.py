def champernowne(p):
    """
    The fraction created by concatenating the positive integers
    0.1234567891011121314... is called Champernowne's constant (in base 10).
    This function returns the product d_10^0 * d_10^1 * ... * d_10^(p-1), where
    d_n represents the nth digit of the fractional part.
    """
    index = 1
    num = 1
    product = 1
    power = 0
    while True:
        if index <= 10 ** power <= index + len(str(num)) - 1:
            product *= int(str(num)[10 ** power - index])
            power += 1
            if power == p:
                break
        index += len(str(num))
        num += 1
    return product


def solve(vol=0):
    return champernowne(7)
