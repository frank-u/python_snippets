def solveUtopian(n):
    height = 1
    for i in range(n):
        height = height + 1 if i % 2 else height * 2
    return height


# ---------------------------------------------------------------------------- #
T = int(input())  # number of test cases
tests = []
for i in range(T):
    N = int(input())  # number of cycles in test scenario
    tests.append(N)
for i in tests:
    print(solveUtopian(i))
