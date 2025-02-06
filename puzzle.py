class Puzzle:
    def __init__(self, board, goal_state, parent, move, depth, cost):
        self.board = board  # 1D list of the puzzles configuration
        self.goal_state = goal_state # 1D list of the goal state
        self.parent = parent # Parent state
        self.move = move # Move that was made to get to this state
        self.depth = depth # Depth of the state g(n)
        self.cost = cost # Cost (f(n) = g(n) + h(n))

    # for priority queue
    def __lt__(self, other):
        return self.cost < other.cost
    
    # Check if the current state is the goal state
    def is_goal(self):
        return self.board == self.goal_state
    
def get_user_input():
    """Get initial board"""
    print("Enter the initial state of the board (use a zero to represent the blank): ")
    intial_state = list(map(int, input().split()))

    """Get goal state"""
    print("Enter the goal state of the board (use a zero to represent the blank): ")
    goal_state = list(map(int, input().split()))

    return intial_state, goal_state

def print_board(board):
    """Display the board in a 3x3 grid."""
    print("+---+---+---+")
    for row in range (0, 9, 3):
        row_view = "|"
        for tile in board[row:row + 3]:
            row_view += f" {tile if tile != 0 else ' '} |"
        print(row_view)
        print("+---+---+---+")

# Possible Moves
# UP, DOWN, LEFT, RIGHT

MOVES = {'UP': -3, "DOWN": 3, "LEFT": -1, "RIGHT": 1}

def move_tile(board, move, blank_index):
    """Return a new board with the blank tile moved."""
    new_board = board[:]
    new_blank_position = blank_index + MOVES[move]
    new_board[blank_index], new_board[new_blank_position] = new_board[new_blank_position], new_board[blank_index]

    return new_board