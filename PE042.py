from _polygonal_tools import is_polygonal
from _str_tools import to_num


def count_triangular(file, vol=0):
    """
    Counts the number of words with triangular values in file.
    """
    f = open(file, "r")
    words = f.read()
    f.close()
    wordlist = words.split(',')

    count = 0
    for word in wordlist:
        if is_polygonal(3, to_num(word)):
            count += 1
    if vol >= 1:
        print(f"There are {count} triangular number words.")
    return count


def solve(vol=0):
    return count_triangular("p042_words.txt", vol=vol)
