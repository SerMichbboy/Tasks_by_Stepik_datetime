def starmap(func, iterable):
    for i in iterable:
        print(i)





pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))