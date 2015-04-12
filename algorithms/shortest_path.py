"""
    A shortest path:

 [['>', 'v', ' ', ' ', ' ', ' '],
  [' ', '>', '>', '>', '>', 'v'],
  [' ', ' ', ' ', ' ', ' ', 'v'],
  [' ', ' ', ' ', ' ', ' ', 'v'],
  [' ', ' ', ' ', ' ', ' ', '*']]

"""

# Sample Test case
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

cost = 1


def search():
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    exnumber = 0
    graphpath = [[' ' for row in range(len(grid[0]))] for col in
                 range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]
    expand[x][y] = 0
    exnumber += 1

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
                graphpath[x][y] = '*'
                counter = expand[x][y]
                while counter > 0:
                    # moving backwards:
                    counter -= 1
                    # checking neigbor cells:
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                            if expand[x2][y2] == counter:
                                graphpath[x2][y2] = delta_name[(i + 2) % 4]
                                x = x2
                                y = y2
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            expand[x2][y2] = exnumber
                            exnumber += 1
                            closed[x2][y2] = 1

    for i in range(len(graphpath)):
        print(graphpath[i])
    return graphpath


search()