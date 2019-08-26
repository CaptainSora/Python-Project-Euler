from PE018 import maximum_path_sum


def MPS2():
    with open('p067_triangle.txt') as f:
        tri = f.read().split('\n')
    for i in range(len(tri)):
        tri[i] = list(map(int, tri[i].split()))
    return maximum_path_sum(tri)


def solve(vol=0):
    return MPS2()
