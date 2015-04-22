"""
Problem Statement

    A point (x,y), on the cartesian plane, makes an angle theta with the
positive direction of the x-axis. Theta varies in the interval [0 ,2PI) radians,
i.e, greater than or equal to zero; but less than 2*PI radians.
    For example, the polar angle of the point (1,2) as marked in this plane
below, is (approximately) 63.4 degrees (multiply by PI/180 to convert to
radians)

    The Task

    Given a list of points in the 2D plane, sort them in ascending order of
their polar angle. In case multiple points share exactly the same polar angle,
the one with lesser distance from the origin (0,0) should occur earlier in the
sorted list.

    Input Format
    The first line contains an integer N.
    This is followed by N lines containing pairs of space separated integers, x
and y which represent the coordinates of the points in the cartesian plane.

    Constraints
    1 <= N <= 1000
    -100 <= x,y <= 100
    The point (0,0) will not be present in the list of points.

    Output Format
    The output should contain N lines. Each line should contain two integers x
and y, corresponding to a point in the original list. Display the points in
ascending order of their polar angle.

    Sample Input

        4
        1 0
        0 -1
        -1 0
        0 1
    Sample Output

        1 0
        0 1
        -1 0
        0 -1
    Explanation

    The point (0,1) has a polar angle of 90 degrees. The point (1,0) has a polar
angle of 0 degrees. (-1,0) has a polar angle of 180 degrees and (0,-1) has a
polar angle of 270 degrees.

"""

from math import atan2, degrees, sqrt

if __name__ == '__main__':
    '''
    T = int(input())  # number of test cases
    tests = []
    for i in range(T):
        N = input()  # number of cycles in test scenario
        tests.append(list(map(int,N.split())))
    '''
    '''
    tests = [
        [1, 0],
        [0, -1],
        [-1, 0],
        [0, 1],
    ]
    '''
    tests = [
        [-25, -99],
        [37, -100],
        [-80, 4],
        [-83, 11],
        [12, -28],
    ]
    tests.sort(key=lambda point: ((degrees(atan2(point[1], point[0]))) % 360,
                                  sqrt(point[0] ** 2 + point[1] ** 2)))

    for i in tests:
        print("{0} {1}".format(i[0], i[1]))
