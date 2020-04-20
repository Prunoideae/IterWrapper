import pytest
from iterwrapper import IterWrapper as iw

range_iw = iw(range(0, 9))


def test_filter():
    assert (range_iw
            .filter(lambda x: x % 2 == 0)
            .take(2)
            .collect(list)
            ) == [0, 2]


def test_foreach():
    assert (
        iw([[1, 2, 3], [1, 2], [1]])
        .foreach(list.pop)
        .collect(list)
    ) == [[1, 2], [1], []]


def test_flat():
    assert (
        iw([[1, 2], [2, 3], [3, 4]])
        .flat()
        .collect(list)
    ) == [1, 2, 2, 3, 3, 4]


def test_take():
    assert (
        iw([1, 2, 3, 4])
        .take(2)
        .collect(list)
    ) == [1, 2]


def test_skip():
    assert (
        iw([1, 2, 3, 4])
        .skip(2)
        .collect(list)
    ) == [3, 4]


def test_step():
    assert (
        iw([1, 2, 3, 4, 5, 6])
        .step(3)
        .collect(list)
    ) == [1, 4]


def test_mutate():
    assert (
        iw([1, 2, 3, 4])
        .mutate(tuple)
        .unwrap()
    ) == (1, 2, 3, 4)

    # Map test
    assert (
        iw([1, 2, 3, 4])
        .map(str)
        .mutate(''.join)
        .unwrap()
    ) == '1234'


def test_chain():
    assert (
        iw([1, 2])
        .chain((3, 4))
        .chain({5: -1, 6: -1})
        .collect(list)
    ) == [1, 2, 3, 4, 5, 6]


def test_repeat():
    assert (
        iw([1, 2])
        .repeat(3)
        .collect(list)
    ) == [1, 2, 1, 2, 1, 2]


def test_chunk():
    assert (
        iw([1, 2, 3, 4, 5])
        .chunk(2)
        .collect(list)
    ) == [(1, 2), (3, 4), (5, None)]


def test_zip():
    assert (
        iw([1, 1])
        .zip([2, 2])
        .collect(list)
    ) == [(1, 2), (1, 2)]


def test_inf():
    assert (
        iw([1, 2])
        .inf()
        .chunk(2)
        .take(100)
        .collect(list)
    ) == [(1, 2) for _ in range(100)]

    # Exhaustion check
    assert (
        iw([1, 2, 1, 2])
        .filter(lambda x: x == 1)
        .inf()
        .collect(list)
    ) == [1, 1]


def test_fold():
    assert (
        iw([1, 2, 3, 4])
        .fold(lambda c, x: c + x ** 2, d=0)
    ) == 30


def test_unwrap():
    assert (
        iw([1, 2, 3, 4])
        .unwrap()
    ) == [1, 2, 3, 4]

    # Mutate test
    i = iw([3, 1, 4, 2])
    ref = i.unwrap()
    ref.sort()
    assert i.unwrap() == [1, 2, 3, 4]


def test_collect():
    assert (
        iw([1, 2, 3, 4])
        .collect(tuple)
    ) == (1, 2, 3, 4)

    # Pipe test
    assert (
        iw([1, 2, 3, 4])
        .collect(sum)
    ) == 10


def test_pipe():
    piped = []
    assert (
        iw([1, 2, 3, 4])
        .pipe(piped.append)
    ) == None

    assert piped == [1, 2, 3, 4]


def test_apply():
    assert (
        iw([1, 3, 2, 4])
        .apply(list.sort)
        .collect(list)
    ) == [1, 2, 3, 4]


def test_exhaust():
    piped = []
    assert (
        iw([1, 2, 3, 4])
        .foreach(piped.append)
        .exhaust()
    ) == None

    assert piped == [1, 2, 3, 4]


def test_count():
    assert (
        iw([1, 2, 3, 4, 5, 6])
        .count(lambda x: x % 2 == 0)
    ) == len(iw([1, 2, 3, 4, 5, 6])
             .filter(lambda x: x % 2 == 0)
             .collect(list))


def test_contains():
    assert iw([1, 2, 3]).contains(1)
    assert not iw([1, 2, 3]).contains(4)


def test_rev():
    assert iw([1, 2, 3]).rev().unwrap() == [3, 2, 1]


def test_override():

    # iter
    for idx, i in enumerate(iw([0, 1, 2, 3])):
        assert idx == i

    # in
    assert 1 in iw([1, 2, 3])
    assert 2 in iw(range(40)).filter(lambda x: x % 2 == 0)

    # + -> chain
    assert (iw([1, 2]) + [3, 4]).collect(list) == [1, 2, 3, 4]
    assert ([1, 2] + iw([3, 4])).collect(list) == [1, 2, 3, 4]

    # x -> repeat
    assert (iw([1, 2]) * 3).collect(list) == [1, 2, 1, 2, 1, 2]

    # len
    assert len(iw([1, 2])) == len([1, 2])

    # | (pipe) -> map
    assert (iw([1, 2]) | str | ord).collect(list) == [49, 50]

    # >> (write) -> mutate
    assert (iw([1, 2]) >> tuple).unwrap() == (1, 2)

    # indexing
    assert iw([1, 2])[1] == 2
    assert iw({5: 6})[5] == 6
    assert iw(range(6))[2] == 2

    # slicing
    assert iw(range(10))[::3].collect(list) == [0, 3, 6, 9]
    assert iw(range(10))[5::].collect(list) == [5, 6, 7, 8, 9]
    assert iw(range(10))[:5:].collect(list) == [0, 1, 2, 3, 4]

    # most types supports slicing so...
    assert iw(range(10)).take(10)[2:2:2].collect(list) == [2, 4]

    assert (
        iw(range(10))
        .mutate(list)[1:2:-1]
        .unwrap()
    ) == list(range(10))[1:2:-1]
