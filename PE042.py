f = open("p042_words.txt", "r")

words = f.read()

f.close()

triangle = [1]

def is_triangular(num):
    global triangle
    tri_len = len(triangle)
    while num > triangle[-1]:
        triangle.append(0.5 * (tri_len + 1) * (tri_len + 2))
        tri_len += 1
    if num in triangle:
        return True
    return False

def to_num(word):
    value = 0
    for char in word:
        value += ord(char) - ord("A") + 1
    return value

def count_triangular(wordlist):
    count = 0
    for word in wordlist:
        if (is_triangular(to_num(word.strip('"')))):
            count += 1
    print(count)

count_triangular(words.split(','))