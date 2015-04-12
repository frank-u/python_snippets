import collections


def flatten1(l):
    res = str(l).replace('[', '').replace(']', '')
    return [int(x) for x in res.split(',') if x.strip()]


def flatten2(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, str):
            for sub in flatten1(el):
                yield sub
        else:
            yield el


if __name__ == '__main__':
    L = [[[1, 2, 3], [4, 5]], 6]
    print(L)
    print(flatten1(L))
    print([i for i in flatten2(L)])

