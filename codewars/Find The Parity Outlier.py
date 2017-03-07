"""
    You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely comprised
of even integers except for a single integer N. Write a method that takes the array as an argument
and returns N.

For example:
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160
"""


def find_outlier(integers):
    d = {0: 0, 1: 0}
    for n in integers:
        d[n % 2] += 1
        d[2 + n % 2] = n
    return d[2] if d[0] == 1 else d[3]


# test.assert_equals(find_outlier([2,6,8,10,3]), 3)

print(find_outlier([2, 6, 8, 10, 3]))
