# IterWrapper

This is a wrapper for python iterators to give it a style like those in Rust among with other methods, to improve the consistency and code readablity of iterator manipulation.

A example for this is something like :

```python
from iterwrapper import IterWrapper as iw
l = (
    iw(range(0,10))
    .map(lambda x:x+1)
    .filter(lambda x:x%2==0)
    .fold(lambda c, x: c+x**2, d=0)
)

print(l) # 220 = 2^2 + 4^2 + 6^2 + 8^2 + 10^2
```

comparing to the equivalent representation in vanilla python :

```python
l = sum(map(lambda x: x**2, filter(lambda x:x%2==0, map(lambda x: x+1, range(0,10)))))
# or
r = range(0, 10)
m = map(lambda x: x+1, r)
f = filter(lambda x: x%2==0, m)
c = map(lambda x: x**2, f)
l = sum(c)
```

Another one:

```python
from iterwrapper import IterWrapper as iw
l = (
    iw(range(0,10))
    .map(lambda x: x+1)
    .filter(lambda x: x%2==0)
    .map(str)
    .collect(', '.join)
)

print(l) # "2, 4, 6, 8, 10"

# Comparing to

l = ', '.join(map(str, filter(lambda x: x%2==0, map(lambda x: x+1, range(0,10)))))

# or

r = range(0, 10)
m = map(lambda x: x+1, r)
f = filter(lambda x: x%2==0, m)
ms = map(str, f)
l = ', '.join(ms)

```

The main goal of this only is to be a convenient wrapper to manipulate iterators, so it comes with high compatibility since most of the method is done by accessing the wrapped iterator, and most of the method just use the wrapper as a container.
