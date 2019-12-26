from importlib import import_module
from time import perf_counter
import json
from _user_input import bool_ans, num_ans


def timesoln(qnum, vol=0):
    """
    Times and runs the question file, and returns [output, runtime].
    """
    # Helper for savesoln()
    start = perf_counter()
    filename = f"PE{qnum:03}"
    try:
        mod = import_module(filename)
        soln = mod.solve(vol=vol)
        stop = perf_counter()
        return [soln, round(stop - start, 1)]
    except ModuleNotFoundError:
        return [None, None]


def savesoln(last_qnum, skipto=0, vol=0):
    """
    Saves all solutions (from 1 to last_qnum) to file.
    """
    # Load file
    with open('_solutions.json', 'r') as f:
        solndict = json.load(f)
    # Safety checks
    if skipto <= 0:
        skipto = last_qnum
    # Loop through all questions
    for q in range(1, last_qnum + 1):
        skip = q < skipto
        filename = f"PE{q:03}"
        # For new question
        if filename not in solndict:
            solndict[filename] = {
                "solution": num_ans(
                    f"What is the known solution for question {q}? Enter 0 " +
                    f"for unsolved question."
                ),
                "output": None,
                "runtime": None
            }
        # For existing questions
        elif skip or not bool_ans(
            f'Would you like to solve question {q}? Est. runtime: ' +
            f'{solndict[filename]["runtime"]}s'
        ):
            if solndict[filename]["solution"] != solndict[filename]["output"]:
                print(f"Question {q}'s output does not match the solution.")
            continue
        # Update info
        solnlist = timesoln(q, vol=vol)
        solndict[filename]["output"] = solnlist[0]
        solndict[filename]["runtime"] = solnlist[1]
        if solndict[filename]["solution"] == solndict[filename]["output"]:
            bracket = '(correct)'
        else:
            bracket = f'(soln: {solndict[filename]["solution"]})'
        print(
            f'Question {q}: {solnlist[0]} {bracket}, {solnlist[1]}s runtime.'
        )
    # Only writes data if no errors
    with open('_solutions.json', 'w') as f:
        json.dump(solndict, f)


def checksoln():
    """
    Checks the runtimes of all question in _solutions.json.
    """
    with open('_solutions.json', 'r') as f:
        solndict = json.load(f)
    THRESHOLD = 60
    fail = []
    close = []

    for qnum in solndict:
        if solndict[qnum]["runtime"] >= THRESHOLD:
            fail += [qnum]
        elif solndict[qnum]["runtime"] >= THRESHOLD * 0.9:
            close += [qnum]

    if fail:
        print("These files take too long:", fail)
    if close:
        print("These files may take too long:", close)
    if not fail and not close:
        print("All questions run within time constraints.")


savesoln(1, skipto=1)
# savesoln(55, skipto=51)
# All questions starting from 51 need to be manually checked
