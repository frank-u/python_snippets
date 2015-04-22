from datetime import datetime


def solve(n):
    (x0, y0, x1, y1) = n
    sx = x1 + (x1 - x0)
    sy = y1 + (y1 - y0)
    return "{0} {1}".format(sx, sy)


if __name__ == '__main__':
    '''
    T = int(input())  # number of test cases
    tests = []
    for i in range(T):
        N = input()  # number of cycles in test scenario
        tests.append(map(int,N.split()))
    '''
    tests = [
        [0, 0, 1, 1],
        [1, 1, 2, 1]
    ]
    start_time = datetime.now()
    for i in tests:
        print(solve(i))
    time_taken = datetime.now() - start_time
    print("--->\tAll Time taken: {0}".format(time_taken))