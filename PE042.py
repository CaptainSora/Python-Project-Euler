from _polygonal_tools import is_polygonal


def to_num(word):
    """
    Calculates the value of the word.
    """
    value = 0
    for char in word:
        value += ord(char) - ord("A") + 1
    return value


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
        if (is_polygonal(3, to_num(word.strip('"')))):
            count += 1
    if vol >= 1:
        print(f"There are {count} triangular number words.")
    return count


def solve(vol=0):
    return count_triangular("p042_words.txt", vol=vol)
