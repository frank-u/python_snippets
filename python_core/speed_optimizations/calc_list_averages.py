"""
    Check speed calculating average values using different techniques:

    MacBook Pro Early 2015 Results:
        Lists of length 10
        mean1 1.8446930280001652
        mean2 1.0668987660001221
        mean3 0.529316690000087

        Lists of length 100
        mean1 12.732948584000042
        mean2 9.038075505999586
        mean3 1.4159731579998152

        Lists of length 1000
        mean1 167.52236727800027
        mean2 125.90510731099994
        mean3 11.059250855999835
"""
import timeit
import random

random.seed(1)

lengths = [10, 100, 1000]
lsts = [[random.randint(0, 100) for _ in range(length)] for length in lengths]


def mean1(lst):
    if lst:
        running_sum = 0
        running_count = 0
        for i in range(len(lst)):
            running_sum += lst[i]
            running_count += 1
        return running_sum / running_count


def mean2(lst):
    numer = 0
    denom = 0
    for num in lst:
        numer += num
        denom += 1
    return numer / denom


def mean3(lst):
    return sum(lst) / len(lst)


funcs = [mean1, mean2, mean3]  # , numpy, stats]

if __name__ == '__main__':
    for lst in lsts:
        print("\nLists of length", len(lst))
        for f in funcs:
            print(f.__name__, timeit.timeit('f(lst)', "from __main__ import f, lst"))
