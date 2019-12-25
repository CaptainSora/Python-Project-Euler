from _palindrome_tools import is_palindrome


def sum_double_base_palindromes(ceiling):
    """
    Returns the sum of all numbers below ceiling which are palindromic in both
    base 10 and base 2.
    """
    return sum(
        [a for a in range(ceiling)
            if is_palindrome(a) and is_palindrome(bin(a)[2:])]
    )


def solve(vol=0):
    return sum_double_base_palindromes(1000000)


print(solve())
