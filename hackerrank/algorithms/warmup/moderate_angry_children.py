"""


"""
from datetime import datetime


def calc_unfairness(n, k, data):
    data.sort()
    min_unfairness = data[k-1] - data[0]
    for i in range(1, n-k+1):
        current_unfainess = data[i+k-1] - data[i]
        if current_unfainess < min_unfairness:
            min_unfairness = current_unfainess
    return min_unfairness

if __name__ == '__main__':
    '''
    N = int(input())  # number of test cases
    K = int(input())  # number of test cases
    tests = []
    for i in range(N):
        ITEM = input()  # number of cycles in test scenario
        tests.append(ITEM)
    '''
    tests = [10, 20, 30, 301, 302, 303, 1000]
    k = 3
    start_time = datetime.now()
    print(calc_unfairness(n=len(tests), k=k, data=tests))
    time_taken = datetime.now() - start_time
    print("--->\tAll Time taken: {0}".format(time_taken))