"""
Problem Statement
    You are given an integer, N. Write a program to determine if N is an element
of the Fibonacci Sequence.
    The first few elements of fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13....
A fibonacci sequence is one where every element is a sum of the previous two
elements in the sequence. The first two elements are 0 and 1.

Formally:
    fib0 = 0
    fib1 = 1
    fibn = fibn-1 + fibn-2 ∀ n > 1

Input Format
    The first line contains T, number of test cases.
    T lines follows. Each line contains an integer N.

Output Format
    Display IsFibo if N is a fibonacci number and IsNotFibo if it is not a fibo-
nacci number. The output for each test case should be displayed on a new line.

Constraints
    1 <= T <= 10^5
    1 <= N <= 10^10

Sample Input

3
5
7
8

Sample Output

IsFibo
IsNotFibo
IsFibo

Explanation
5 is a Fibonacci number given by fib5 = 3 + 2
7 is not a Fibonacci number
8 is a Fibonacci number given by fib6 = 5 + 3

TimeLimit Time limit for this challenge is given here

"""
from datetime import datetime
import mpmath as mp


def is_perfect_square(x):
    s = mp.sqrt(x)
    return int(s)*int(s) == x

def calc_is_fib(n):
    """
        0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    # Decimal Precision
    mp.mp.dps = 100
    plus_seq = 5*n**2+4
    minus_seq = 5*n**2-4
    if is_perfect_square(plus_seq):
        return "IsFibo"
    if is_perfect_square(minus_seq):
        return "IsFibo"
    return "IsNotFibo"


if __name__ == '__main__':
    '''
    T = int(input())  # number of test cases
    tests = []
    for i in range(T):
        N = input()  # number of cycles in test scenario
        tests.append(N)
    '''
    tests = [233, 2584, 10946, 100000,
             0, 1, 2, 3, 4,
             117669030460994, 190392490709135,
             222232244629420445529739893461909967206666939096499764990979600]
    start_time = datetime.now()
    for i in tests:
        print(calc_is_fib(i))
    time_taken = datetime.now() - start_time
    print("--->\tAll Time taken: {0}".format(time_taken))
