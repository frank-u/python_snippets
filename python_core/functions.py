def foo(p1, *p2):
    print(p1)
    print(p2)


def bar(p1, **p2):
    print(p1)
    print(p2)


foo(1, 2, 3, 4, 5)
bar(1, a=2, b=3)