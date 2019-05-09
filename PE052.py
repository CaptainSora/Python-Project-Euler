import itertools

def is_permutation(num):
    perm_gen = itertools.permutations(str(num))
    perm_array = []
    for p in perm_gen:
        perm_array.append(int(''.join(p)))
    for mult in range(2, 7):
        if mult * num not in perm_array:
            return False
    return True

i = 142857 # Notice how this is 999999/7: something about the fractions of 7 makes this interesting
while not is_permutation(i):
    i += 1
print(i)