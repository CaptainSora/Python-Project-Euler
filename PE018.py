def maximum_path_sum(tri):
    """
    Returns the maximum total sum from top to bottom of the triangle.
    Must be formatted as a list of lists of ints.
    """
    tri.reverse()
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i-1][j], tri[i-1][j+1])
    return tri[-1][0]


def MPS1():
    """
    Returns the maximum total sum from top to bottom of a triangle saved to
    file.
    See PE067.py.
    """
    with open('p018_triangle.txt') as f:
        tri = f.read().split('\n')
    for i in range(len(tri)):
        tri[i] = list(map(int, tri[i].split()))
    return maximum_path_sum(tri)


def solve(vol=0):
    return MPS1()
