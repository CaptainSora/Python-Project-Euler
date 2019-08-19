def is_triangular(num):
    tri = [1]
    while num > tri[-1]:
        triangle.append(0.5 * (len(tri) + 1) * (len(tri) + 2))
    if num in triangle:
        return True
    return False


def to_num(word):
    value = 0
    for char in word:
        value += ord(char) - ord("A") + 1
    return value


def count_triangular():
    f = open("p042_words.txt", "r")
    words = f.read()
    f.close()
    wordlist = words.split(',')

    count = 0
    for word in wordlist:
        if (is_triangular(to_num(word.strip('"')))):
            count += 1
    return count


def solve(vol=0):
    return count_triangular()
