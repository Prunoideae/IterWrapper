from iterwrapper import IterWrapper as iw
from iterwrapper.misc import *

l = (
    iw(range(0, 10))
    .map(lambda x: x + 1)
    .filter(lambda x: x % 2 == 0)
    .skip(2)
    .take(2)
    .mutate(list)
    .repeat(3)
    .map(str)
    .collect(lambda x: ".".join(x))
)

print(l)
