import heapq
from puzzle import Puzzle, print_board, move_tile

def a_star(initial_state, goal_state, heuristic):
    """Performs A* search using the given heuristic."""
    open_list = []
    closed_list = set()
    nodes_generated = 0  # Counter for nodes generated
    nodes_expanded = 0    # Counter for nodes expanded

    start_cost = heuristic(initial_state, goal_state)
    heapq.heappush(open_list, Puzzle(initial_state, goal_state, None, None, 0, start_cost))
    nodes_generated += 1  # Count the initial state as generated
    
    print(f"Nodes Generated: {nodes_generated}")
    print(f"Nodes Expanded: {nodes_expanded}")
    while open_list:
        current_state = heapq.heappop(open_list)
        nodes_expanded += 1  # Count the node being expanded

        if current_state.is_goal():
            print(f"Solution found!")
            # print(f"Nodes Generated: {nodes_generated}")
            # print(f"Nodes Expanded: {nodes_expanded}")
            return current_state, nodes_generated, nodes_expanded  # Return counts along with the solution

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
            nodes_generated += 1  # Count the newly generated node

    print("No solution found.")
    # print(f"Nodes Generated: {nodes_generated}")
    # print(f"Nodes Expanded: {nodes_expanded}")
    return None, nodes_generated, nodes_expanded  # Return counts


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
