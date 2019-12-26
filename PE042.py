from _polygonal_tools import is_polygonal
from _str_tools import to_num


def count_triangular():
    """
    Counts the number of words with triangular values in file.
    """
    with open('p042_words.txt', 'r') as f:
        wordlist = f.read().split(',')
    return len([w for w in wordlist if is_polygonal(3, to_num(w))])


def solve(vol=0):
    return count_triangular()
