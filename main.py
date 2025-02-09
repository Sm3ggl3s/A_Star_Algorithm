from puzzle import get_user_input
from a_star import a_star, print_solution
from heuristics import manhattan_distance, misplaced_tiles

if __name__ == "__main__":
    initial_state, goal_state = get_user_input()
    
    print("\n Solving with Manhattan Distance heuristic...")
    solution, nodes_generated, nodes_expanded = a_star(initial_state, goal_state, manhattan_distance)

    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")
    print(f"Manhattan Distance - Nodes Generated: {nodes_generated}, Nodes Expanded: {nodes_expanded}")

    print("\n Solving with Misplaced Tiles heuristic...")
    solution, nodes_generated, nodes_expanded = a_star(initial_state, goal_state, misplaced_tiles)

    if solution:
        print("Solution found!")
        print_solution(solution)
    else:
        print("No solution found.")
    print(f"Misplaced Tiles - Nodes Generated: {nodes_generated}, Nodes Expanded: {nodes_expanded}")
