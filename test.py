from iters.iters import IterWrapper as iw

l = (
    iw(range(0, 10))
    .map(lambda x: x + 1)
    .filter(lambda x: x % 2 == 0)
    .skip(2)
    .take(2)
    .mutate(list)
    .repeat(3)
    .collect(list)
)

print(l)
