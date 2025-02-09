
# A* Search Algorithm for 8-Puzzle Solver

This project implements the A* search algorithm to solve the 8-puzzle problem using two different heuristics:

- **Manhattan Distance**
- **Misplaced Tiles**

## Table of Contents
- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Files Overview](#files-overview)
- [Code Explanation](#code-explanation)
  - [Main Script (`main.py`)](#main-script-mainpy)
  - [A* Algorithm (`a_star.py`)](#a-algorithm-a_starpy)
  - [Heuristics (`heuristics.py`)](#heuristics-heuristicspy)
  - [Puzzle Handling (`puzzle.py`)](#puzzle-handling-puzzlepy)
- [Example](#example)
- [Future Improvements](#future-improvements)
- [License](#license)

--- 

## Introduction

The 8-puzzle consists of a 3×3 grid with numbered tiles and one empty space (represented as 0). The goal is to rearrange the tiles to match a given goal state by sliding tiles into the empty space. The A* search algorithm is used to efficiently find the optimal solution.

--- 

## How it Works

1. The user provides:
    - An **initial state** (starting configuration of the board).
    - A **goal state** (desired configuration).
2. The A* algorithm searches for the optimal solution using two heuristics:
   - **Manhattan Distance**: The sum of the distances of each tile from its goal position.
   - **Misplaced Tiles**: The number of tiles not in their correct position.
3. If a solution exists, the program prints the sequence of moves and the board states leading to the goal.

---

## Usage

### Requirements

- Python 3.6 or greater

### Running the program

1. Clone this repository:
    ```bash
   git clone https://github.com/Sm3ggl3s/A_Star_Algorithm.git
   cd A_Star_Algorithm
    ```
2. Run the script:
    ```bash
    python main.py
    ```
3. Enter the board states as space-separated values (use `0` for the blank space).

Example input: 
```
Enter the initial state of the board (use a zero to represent the blank):1 2 3 4 0 5 6 7 8

Enter the goal state of the board (use a zero to represent the blank):1 2 3 4 5 6 7 8 0
```
---

### Files Overview

| File | Description |
| :---   | :---   |
| `main.py` | Entry point that runs A* search with different heuristics |
| `a_star.py` | Implements the A* search algorithm |
| `heuristics.py` | Defines heuristics functions (Manhattan Distance & Misplaced Tiles) |
| `puzzle.py` | Defines the puzzle state, board representation, and movement logic |

--- 

### Code Explanation

#### Main Script (`main.py`)

- `get_user_input()`: Prompts the user to enter the initial state and goal state.
- Calls the A algorithm* twice using:
    - **Manhattan Distance heuristics**
    - **Misplaced Tiles heuristic**
- `print_solution(solution)`: Displays the sequence of moves and the board states leading to the goal

#### A* Algorithm (`a_star.py`)
- `a_star(initial_state, goal_state, heuristic)`:
    - Implements the A* search algorithm.
    - Uses a **priority queue** (`heapq`) to explore the most promising nodes first.
    - Expands valid neighboring states based on possible moves.
    - Returns the **solution path** if the goal state is found.

#### Puzzle Handling (`puzzle.py`)
- `Puzzle` Class:
    - Represents the **current state** of the puzzle.
    - Stores information about:
        - `board` -> Current configuration of the puzzle.
        - `goal_state` -> Target configuration
        - `parent` -> Previous state (for backtracing)
        - `move` -> Action taken to reach this state.
        - `depth` -> Number of moves made so far
        - `cost` -> Evaluation function `f(n) = g(n) + h(n)`
- `get_user_input()`:
    - Asks the user to input the initial and goal states.
- `move_tile(board, move, blank_index)`:
    - Moves the blank tile(`0`) in a given direction (`UP`, `DOWN`, `LEFT`, `RIGHT`).
    - Returns a new board configuration.

---

### Example Output
```Bash
Solving with Manhattan Distance heuristic...
Solution found!
Move: None
+---+---+---+
| 1 | 2 | 3 |
| 4 |   | 5 |
| 6 | 7 | 8 |
+---+---+---+

Move: DOWN
+---+---+---+
| 1 | 2 | 3 |
| 4 | 7 | 5 |
| 6 |   | 8 |
+---+---+---+
...

```

---

### Future Improvements

- Add a Better GUI for cleaner visualization.
- Improve performance with optimized data structures.

## License

This project is open-source and available under the MIT License.

