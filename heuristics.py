def manhattan_distance(board, goal_state):
    """ Calculates the manhattan distance of the board. """
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_state.index(board[i]), 3)
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def misplaced_tiles(board, goal_state):
    """ Calculates the number of misplaced tiles. """
    return sum([1 for i in range(9) if board[i] != goal_state[i]])