from datetime import date, timedelta


def count_weekday(start, stop, wd_target=0):
    """
    Returns the number of days between start and stop inclusive which is the
    first day of the month and is the specified weekday, with 0 being Monday.
    """
    day = timedelta(days=1)
    counter = 0
    while start != stop + day:
        if start.weekday() == wd_target and start.day == 1:
            counter += 1
        start += day
    return counter


def solve(vol=0):
    return count_weekday(date(1901, 1, 1), date(2000, 12, 31), wd_target=6)
