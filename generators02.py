def gen(n):
    for i in range(n):
        yield i**2

g = gen(3)
print(next(g))
print(next(g))
print(next(g))
