"""
    Klotski Puzzle solver
"""

N = 8


def solve_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple 
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""
    return shortest_path_search(start, successors, is_goal)


def is_goal(puzzle):
    goal_cell = 0
    for x in puzzle:
        if x[0] == "@":
            goal_cell = x[1][0]
    for x in puzzle:
        if x[0] == "*":
            if goal_cell in x[1]:
                return True
            else:
                return False


def not_free_cell(cell, block, puzzle):
    for x in puzzle:
        if (x[0] != "@") and (x[0] != block):
            for pos in x[1]:
                if pos == cell:
                    return True
    return False


def next_state(state, action):
    result = []
    for x in state:
        if x[0] == action[0]:
            delta = x[1][len(x[1]) - 1] - x[1][len(x[1]) - 2]
            moveto = []
            for act in x[1]:
                new_cell = act + delta * action[1]
                if not_free_cell(new_cell, action[0], state):
                    return False
                moveto.append(new_cell)
            result.append(tuple([x[0], tuple(moveto)]))
        else:
            result.append(x)
    return tuple(result)


def successors(state):
    successors_list = {}
    for block in state:
        if (block[0] != "@") and (block[0] != "|"):
            n = 1
            nxt = next_state(state, (block[0], n))
            while nxt:
                delta = block[1][len(block[1]) - 1] - block[1][
                    len(block[1]) - 2]
                successors_list[nxt] = (block[0], n * delta)
                n += 1
                nxt = next_state(state, (block[0], n))
            n = -1
            nxt = next_state(state, (block[0], n))
            while nxt:
                delta = block[1][len(block[1]) - 1] - block[1][
                    len(block[1]) - 2]
                successors_list[nxt] = (block[0], n * delta)
                n -= 1
                nxt = next_state(state, (block[0], n))
    return successors_list


def locs(start, n, incr=1):
    """Return a tuple of n locations, starting at start and incrementing by
    incr."""
    return tuple([start + i * incr for i in range(n)])


def grid(blocks, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to 
    indicate there are walls all around the NxN grid, except at the goal 
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this. The variable 'blocks'  is a
    tuple of pairs like ('*', (26, 27)). The return result is a big tuple
    of the 'blocks' pairs along with the walls and goal pairs."""
    result = []
    goal_place = N * N / 2 - 1
    goal_tuple = ('@', (goal_place,))
    result.append(goal_tuple)
    for block in blocks:
        result.append(block)
    wall_places = []
    for i in range(1, 1 + N - 2):
        wall_places.append(i * N)
        if (i * N + 7) != goal_place:
            wall_places.append(i * N + 7)
    wall_places = [x for x in range(N)] + wall_places + \
                  [x for x in range(N * (N - 1), N * (N - 1) + N)]
    walls_tuple = ('|', (tuple(wall_places)))
    result.append(walls_tuple)
    return tuple(result)


def show(state, N=N):
    """Print a representation of a state as an NxN grid."""
    # Initialize and fill in the board.
    board = ['.'] * N ** 2
    for (c, squares) in state:
        for s in squares:
            board[int(s)] = c
    # Now print it out
    lines = ""
    for i, s in enumerate(board):
        lines += s
        if i % N == N - 1:
            lines += "\n"
    print(lines)

# Here we see the grid and locs functions in use:

puzzle1 = grid((
    ('*', locs(26, 2)),
    ('G', locs(9, 2)),
    ('Y', locs(14, 3, N)),
    ('P', locs(17, 3, N)),
    ('O', locs(41, 2, N)),
    ('B', locs(20, 3, N)),
    ('A', locs(45, 2))))

puzzle2 = grid((
    ('*', locs(26, 2)),
    ('B', locs(20, 3, N)),
    ('P', locs(33, 3)),
    ('O', locs(41, 2, N)),
    ('Y', locs(51, 3))))

puzzle3 = grid((
    ('*', locs(25, 2)),
    ('B', locs(19, 3, N)),
    ('P', locs(36, 3)),
    ('O', locs(45, 2, N)),
    ('Y', locs(49, 3))))


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []


def path_actions(path):
    """Return a list of actions in this path."""
    return path[1::2]


print(path_actions(shortest_path_search(puzzle3, successors, is_goal)))
show(puzzle3)
show(shortest_path_search(puzzle3, successors, is_goal)[-1])
