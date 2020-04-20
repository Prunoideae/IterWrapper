
from iterwrapper import IterWrapper as iw

range_iw = iw(range(0, 9))


def test_map():
    assert range_iw.map(lambda x: x + 1).take(3).collect(list) == [1, 2, 3]

def test_filter():
    assert range_iw.filter(lambda x:x%2==0).take(2).collect(list)==[0,2]

def test_foreach():
    assert (iw([[1,2,3],[1,2],[1]]).foreach(list.pop).collect(list))==[[1,2],[1],[]]