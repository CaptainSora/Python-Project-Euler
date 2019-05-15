import os
import json
import math


def record_time(qnum, functime, filetime):
    """Record the runtime of the function.

    qnum: the question number as an int
    time: runtime as a float
    """
    f = open('runtime.json', 'r')
    timedict = json.load(f)
    f.close()
    rdict = {
        "functime": functime,
        "filetime": filetime
    }
    for atime in rdict:
        if rdict[atime] < 0.9:
            rdict[atime] = "PASS"
        elif rdict[atime] < 1.1:
            rdict[atime] = "CONDITIONAL PASS"
        elif rdict[atime] < 10:
            rdict[atime] = f"CONDITIONAL FAIL: TIME = {rdict[atime]:.3f}"
        else:
            rdict[atime] = f"FAIL: ORDER {math.ceil(math.log10(rdict[atime]))}"
    timedict[f'{qnum:03}'] = rdict
    f = open('runtime.json', 'w')
    json.dump(timedict, f)
    f.close()
