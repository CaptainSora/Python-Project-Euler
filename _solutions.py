from importlib import import_module
from time import perf_counter
import json


def addsoln(qnum, vol=0):
    """
    Times and runs the question file, and adds the time and output to _solutions.json.
    """
    # Time file execution
    start = perf_counter()
    filename = f"PE{qnum:03}"
    mod = import_module(filename)
    soln = mod.solve()
    stop = perf_counter()

    # Add solution to file
    f = open('_solutions.json', 'r')
    timedict = json.load(f)
    f.close()

    timedict[filename] = (soln, round(stop - start, 1))
    print(f"Question {qnum} took {round(stop - start, 1)} seconds")

    f = open('_solutions.json', 'w')
    json.dump(timedict, f)
    f.close()


def checksoln():
    """
    Checks the runtimes of all question in _solutions.json.
    """
    f = open('_solutions.json', 'r')
    timedict = json.load(f)
    f.close()
    threshold = 60
    fail = []
    close = []

    for qnum in timedict:
        if timedict[qnum][1] >= threshold:
            fail += [qnum]
        elif timedict[qnum][1] >= threshold * 0.9:
            close += [qnum]

    if fail:
        print("These files take too long:", fail)
    if close:
        print("These files may take too long:", close)
    if not fail and not close:
        print("All questions run within time constraints.")


def addmultsoln(start, stop, vol=0):
    """
    Runs addsoln() for each number in start and stop inclusive, then runs checksoln()
    """
    for n in range(start, stop + 1):
        addsoln(n, vol=vol)
    checksoln()

#addmultsoln(41, 50)
addsoln(15, vol=3)
