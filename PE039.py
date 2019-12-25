from _pythagorean_tools import find_pythag_trips


def max_pythag_trips(ceiling):
    """
    Returns the number less than or equal to ceiling which has the most
    integer right triangles with perimeter equal the number.
    """
    max_pair = [0, 0]
    for a in range(1, ceiling + 1):
        num_triangles = len(find_pythag_trips(a))
        if num_triangles > max_pair[1]:
            max_pair = [a, num_triangles]
    return max_pair[0]


def solve(vol=0):
    return max_pythag_trips(1000)


print(solve())
