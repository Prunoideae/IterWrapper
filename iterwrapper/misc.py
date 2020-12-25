
from typing import Iterable


def range_inf(start, step):
    while True:
        yield start
        start += step


def tail_inf(i: Iterable, d=None):
    yield from i
    while True:
        yield d


def all_eq(i: Iterable, n) -> bool:
    for a in i:
        if a != n:
            return False
    return True
