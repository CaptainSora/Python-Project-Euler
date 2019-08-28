from _str_tools import to_num


def name_scores():
    """
    Returns the total score of all names as defined in the question.
    """
    with open('p022_names.txt') as f:
        namelist = f.read().split(',')
    namelist.sort()
    totalscore = 0
    for i in range(len(namelist)):
        totalscore += (i + 1) * to_num(namelist[i])
    return totalscore


def solve(vol=0):
    return name_scores()
