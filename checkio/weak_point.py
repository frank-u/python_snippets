def weak_point(matrix):
    sumcols = [sum(i) for i in matrix]
    col_i = sumcols.index(min(sumcols))
    sumrows = [sum([matrix[i][j] for i in range(len(matrix[0]))]) for j
               in range(len(matrix))]
    row_i = sumrows.index(min(sumrows))
    return col_i, row_i  # [0, 0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]),
                      (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
