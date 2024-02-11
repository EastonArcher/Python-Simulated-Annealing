# 8 Queens Simulated Annealing
This code implements the Simulated Annealing algorithm to solve the Eight Queens Puzzle. The puzzle involves placing eight chess queens on an 8×8 chessboard such that no two queens threaten each other; they cannot share the same row, column, or diagonal.

## Problem Description 
The Eight Queens Puzzle requires finding a configuration of queen placements on the chessboard where no queen can capture another. This code provides a solution to this problem using the Simulated Annealing algorithm.

### 'Board'
* Initializes and represents the chessboard.
* 'reset()': Resets the board with random queen positions.
* 'calculateCost()': Calculates the number of queen conflicts (threats) on the board.
* 'calculateCostWithQueens(queens)': Static method to calculate the number of conflicts given a set of queen positions.
* 'toString(queens)': Static method to convert queen positions to a string representation.
  
### 'SimulatedAnnealing'
* Initializes and runs the Simulated Annealing algorithm.
* 'run()': Runs the Simulated Annealing loop to find a solution.
* 'getElapsedTime()': Calculates and returns the elapsed time during execution.

## Running the Code
To run the code:
```
python <simulated-annealing.py>
```
The initial board state and the solution (if found) will be printed along with the elapsed time.
