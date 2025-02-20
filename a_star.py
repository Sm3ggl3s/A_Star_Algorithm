import heapq
from puzzle import Puzzle, print_board, move_tile

def a_star(initial_state, goal_state, heuristic):
    """Performs A* search using the given heuristic."""
    open_list = []
    closed_list = set()

    start_cost = heuristic(initial_state, goal_state)
    heapq.heappush(open_list, Puzzle(initial_state, goal_state, None, None, 0, start_cost))

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state # Solution found
        
        closed_list.add(tuple(current_state.board))
        blank_position = current_state.board.index(0)

        for move in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if move == "UP" and blank_position < 3:
                continue
            if move == "DOWN" and blank_position > 5:
                continue
            if move == "LEFT" and blank_position % 3 == 0:
                continue
            if move == "RIGHT" and blank_position % 3 == 2:
                continue

            new_board = move_tile(current_state.board, move, blank_position)

            if tuple(new_board) in closed_list:
                continue

            new_cost = current_state.depth + 1 + heuristic(new_board, goal_state)
            new_state = Puzzle(new_board, goal_state, current_state, move, current_state.depth + 1, new_cost)
            heapq.heappush(open_list, new_state)

    return None

def print_solution(solution):
    """Prints the solution to the puzzle."""
    moves = []
    current_state = solution
    while current_state:
        moves.append(current_state)
        current_state = current_state.parent
    moves.reverse()

    for move in moves:
        print(f"Move: {move.move}")
        print_board(move.board)