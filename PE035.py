from _prime_tools import is_prime


def gen_rotation_list(num):
    """
    Returns a list of all digit rotations of num (excluding itself).
    """
    return [int(str(num)[a:] + str(num)[:a]) for a in range(1, len(str(num)))]


def count_circular_primes(ceiling):
    """
    Counts the number of circular primes below ceiling.
    A circular prime is a prime for which all rotations of the digits is also
    prime.
    """
    counter = 0
    for a in range(ceiling):
        if is_prime(a) and all([is_prime(a) for a in gen_rotation_list(a)]):
            counter += 1
    return counter


def solve(vol=0):
    return count_circular_primes(1000000)
