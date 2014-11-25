"""
Problem Statement
    Shashank likes strings in which consecutive characters are different. For
example, he likes ABABA, while he doesn't like ABAA. Given a string containing
characters A and B only, he wants to change it into a string he likes. To do
this, he is allowed to delete the characters in the string.
    Your task is to find the minimum number of required deletions.

Input Format
    The first line contains an integer T i.e. the number of test cases.
    Next T lines contain a string each.

Output Format
    Print minimum number of required steps for each test case.

Constraints
    1≤T≤10
    1≤lengthofString≤10^5

Sample Input
    5
    AAAA
    BBBBB
    ABABABAB
    BABABA
    AAABBB

Sample Output
    3
    4
    0
    0
    4

Explanation
    AAAA⟹A, 3 deletions
    BBBBB⟹B, 4 deletions
    ABABABAB⟹ABABABAB, 0 deletions
    BABABA⟹BABABA, 0 deletions
    AAABBB⟹AB, 4 deletions
"""
from datetime import datetime


def timedcall(fn):
    """
        Call function, print the time taken and return result.
    """
    def wrapper(*args):
        t0 = datetime.now()
        result = fn(*args)
        t1 = datetime.now() - t0
        print("Time taken:\t{0}".format(t1))
        return result
    return wrapper


def kill_duplicates(startpos, data_list):
    dist = 0
    l = len(data_list)
    while (startpos+dist+1 < l) and (data_list[startpos] == data_list[startpos+dist+1]):
        dist += 1
    del data_list[startpos:startpos+dist]
    return dist


@timedcall
def calc_alternate_distance(s):
    if len(s) <= 1:
        return 0
    slist = list(s)
    idx = 0
    dist = 0

    while idx < len(slist)-1:
        dist += kill_duplicates(idx, slist)
        idx += 1
    return dist

# ---------------------------------------------------------------------------- #
'''
T = int(input())  # number of test cases
tests = []
for i in range(T):
    N = input()  # number of cycles in test scenario
    tests.append(N)
'''
tests = ['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB']
test = ""
for i in range(50000):
    test += "BBBCC"
tests.append(test)
start_time = datetime.now()
for i in tests:
    print(calc_alternate_distance(i))
time_taken = datetime.now() - start_time
print("--->\tAll Time taken: {0}".format(time_taken))
