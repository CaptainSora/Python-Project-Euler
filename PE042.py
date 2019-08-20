def is_triangular(num):
    """
    Checks if num is a triangular number.
    """
    tri = [1]
    while num > tri[-1]:
        tri.append(0.5 * (len(tri) + 1) * (len(tri) + 2))
    if num in tri:
        return True
    return False


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
        if (is_triangular(to_num(word.strip('"')))):
            count += 1
    if vol >= 1:
        print(f"There are {count} triangular number words.")
    return count


def solve(vol=0):
    return count_triangular("p042_words.txt", vol=vol)
