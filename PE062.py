import math

# generate_cubes(len) generates a list of all cubes with len digits.
def generate_cubes(len):
    cubes = []
    start = math.floor((10 ** (len - 1)) ** (1/3))
    while start ** 3 < 10 ** len:
        if 10 ** (len - 1) <= start ** 3:
            cubes.append(start ** 3)
        start += 1
    return cubes

# find_permutations(size) returns the smallest cube for which 'size' of its permutations are also cubes.
def find_permutation(size):
    cubelen = 1
    while True:
        cubes = generate_cubes(cubelen)
        cubedict = {}
        for a in cubes:
            x = ''.join(sorted(str(a)[:]))
            if x in cubedict:
                cubedict[x].append(a)
            else:
                cubedict[x] = [a]
        for b in cubedict:
            if len(cubedict[b]) == size:
                print(min(cubedict[b]))
                return
        cubelen += 1

find_permutation(5)