import itertools

P = [0, 1, 2, set(), set(), set(), set(), set(), set()]

# figurate(n, type) returns the value of the nth term in the polytype sequence.
def figurate(n, type):
    if type == 3:
        return int(n * (n + 1) * 0.5)
    elif type == 4:
        return n ** 2
    elif type == 5:
        return int(n * (3 * n - 1) * 0.5)
    elif type == 6:
        return n * (2 * n - 1)
    elif type == 7:
        return int(n * (5 * n - 3) * 0.5)
    elif type == 8:
        return n * (3 * n - 2)

# update_P() populates P with 4-digit values.
def update_P():
    global P
    finished = [True, True, True, True, True, True]
    n = 1
    while True:
        for a in itertools.compress(range(3, 9), finished):
            num = figurate(n, a)
            if 1000 <= num < 10000:
                P[a].update([num])
            elif num >= 10000:
                finished[a-3] = False
        if True not in finished: break
        else: n += 1

update_P()

# cyclic(a, b) returns True if the last two digits of a are the first two digits of b.
# Example: cyclic(8128, 2882) -> True
def cyclic(a, b):
    return str(a)[2:] == str(b)[:2]

# find_cyclics(num, poly) returns a list of tuples of number and polytype which are cyclic with num.
def find_cyclics(num, poly):
    cyclics = []
    for a in (set(range(3, 9)) - set([poly])):
        for b in P[a]:
            if cyclic(num, b):
                cyclics.append((b, a))
    return cyclics

cyclic_dict = {}

# find_cyclic_pairs() populates cyclic_dict with the pairs of possible cyclic numbers.
def find_cyclic_pairs():
    global cyclic_dict
    for a in range(3, 9):
        for b in P[a]:
            cyclic_dict[(b, a)] = find_cyclics(b, a)

# find_next_cyclic(cyclic_tuple_list) recursively finds the next cyclic number by DFS.
# requires: all elements in cyclic_tuple_list exist in cyclic_dict.
def find_next_cyclic(cyclic_tuple_list):
    search_array = cyclic_dict[cyclic_tuple_list[-1]]
    for a in search_array:
        if a[1] in [x[1] for x in cyclic_tuple_list]:
            continue
        if len(cyclic_tuple_list) == 5:
            if cyclic(a[0], cyclic_tuple_list[0][0]):
                print("Sum: ", sum([x[0] for x in cyclic_tuple_list]) + a[0])
                return True
        elif a in cyclic_dict:
            next_list = list(cyclic_tuple_list)
            next_list.append(a)
            if find_next_cyclic(next_list):
                return True


def cyclic_figurate_loop():
    find_cyclic_pairs()
    for a in cyclic_dict:
        if find_next_cyclic([a]):
            return

cyclic_figurate_loop()