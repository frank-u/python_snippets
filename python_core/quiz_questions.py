import functools


def describe_func(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("/-[ {0:10} ]--------------\\".format(func.__name__))
        func(*args, **kwargs)
        print("\-----------------------------/\n\n")

    return wrapped


# ---------------------------------------------------------------------------- #

@describe_func
def q1():
    list = []

    for i in range(100):
        list.append(lambda x, i=i: x + i)

    print(list[42](3))


@describe_func
def q2():
    try:
        qwe = 'qwe'
        qwe[0] = 'a'
        print(qwe)
    except TypeError as e:
        print("TYPE ERROR: {0}".format(e))


@describe_func
def q3():
    text = 'hello'
    print(text[4:100])


@describe_func
def q4():
    """
        Выражение с использованием тернарного оператора условной подстановки
    ("ifTrue if condition else ifFalse")
    """
    a = 3
    a = "foo" if a / 2 == 1 else 2
    a = a + a
    print(a)


@describe_func
def q5():
    print(int(7).__floordiv__(-3))


if __name__ == '__main__':
    q1()
    q2()
    q3()
    q4()
    q5()