# IterWrapper

This is a wrapper for python iterators to give it a style like those in Rust.

A example for this is something like :

```python
from iters.iters import IterWrapper as iw
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

among with other methods, to improve the consistency and code readablity of iterator manipulation.
