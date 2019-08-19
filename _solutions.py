from importlib import import_module
from time import perf_counter
import json


def addsoln(qnum, primesieve=False):
    # Time file execution
    filename = f"PE{qnum:03}"
    mod = import_module(filename)
    start = perf_counter()
    soln = mod.solve()
    stop = perf_counter()

    # Add solution to file
    f = open('_solutions.json', 'r')
    timedict = json.load(f)
    f.close()

    if filename not in timedict:
        timedict[filename] = {}
    timedict[filename]["solution"] = soln
    timedict[filename]["time"] = round(stop - start, 1)
    timedict[filename]["primesieve"] = primesieve

    f = open('_solutions.json', 'w')
    json.dump(timedict, f)
    f.close()


def checksoln():
    f = open('_solutions.json', 'r')
    timedict = json.load(f)
    f.close()
    threshold = 60
    fail = []
    close = []
    sieve = []

    for qnum in timedict:
        if timedict[qnum]["time"] >= threshold:
            fail += qnum
        elif timedict[qnum]["time"] >= threshold * 0.9:
            close += qnum
        elif timedict[qnum]["primesieve"]:
            sieve += qnum

    if fail:
        print("These files take too long:", fail)
    if close:
        print("These files may take too long:", close)
    if sieve:
        print("These files rely on a prime sieve:", sieve)
    if not fail and not close and not sieve:
        print("All questions run within time constraints.")

addsoln(45)
addsoln(46)
checksoln()
