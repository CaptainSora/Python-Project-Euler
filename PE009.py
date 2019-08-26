def pythagorean_triplet(total):
    """
    Returns the product abc of a pythagorean triplet a^2 + b^2 = c^2 where
    a + b + c = total.
    """
    # Optimization: a <= b
    for a in range(1, total):
        for b in range(a, total):
            if a ** 2 + b ** 2 == (total - a - b) ** 2:
                return a * b * (total - a - b)
            elif a ** 2 + b ** 2 > (total - a - b) ** 2:
                break


def solve(vol=0):
    return pythagorean_triplet(1000)
