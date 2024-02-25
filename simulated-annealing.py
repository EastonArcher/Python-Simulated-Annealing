from datetime import datetime
import random
import math

class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.reset()

    def reset(self):
        """Reset the board with random queen positions."""
        self.queens = [-1 for _ in range(self.queen_count)]
        for i in range(self.queen_count):
            self.queens[i] = random.randint(0, self.queen_count - 1)

    def calculateCost(self):
        """Calculate the number of queen conflicts (threats) on the board."""
        threat = 0
        for queen in range(self.queen_count):
            for next_queen in range(queen + 1, self.queen_count):
                if self.queens[queen] == self.queens[next_queen] or abs(queen - next_queen) == abs(self.queens[queen] - self.queens[next_queen]):
                    threat += 1
        return threat

    @staticmethod
    def calculateCostWithQueens(queens):
        """Calculate the number of conflicts (threats) given a set of queen positions."""
        threat = 0
        queen_count = len(queens)
        for queen in range(queen_count):
            for next_queen in range(queen + 1, queen_count):
                if queens[queen] == queens[next_queen] or abs(queen - next_queen) == abs(queens[queen] - queens[next_queen]):
                    threat += 1
        return threat

    @staticmethod
    def toString(queens):
        """Convert queen positions to a string representation with 0s and 1s."""
        board_string = ""
        for row, col in enumerate(queens):
            for i in range(len(queens)):
                if i == col:
                    board_string += "1"
                else:
                    board_string += "0"
            board_string += "\n"
        return board_string

class SimulatedAnnealing:
    def __init__(self, board):
        self.elapsedTime = 0
        self.board = board
        self.temperature = 4.0  # Adjusted temperature value
        self.sch = 0.99
        self.startTime = datetime.now()

    def run(self):
        board = self.board
        board_queens = self.board.queens[:]
        solutionFound = False

        # Simulated Annealing loop
        for _ in range(170000):
            # Update temperature
            self.temperature *= self.sch
            # Reset board to random state
            board.reset()
            successor_queens = board.queens[:]
            # Calculate difference in cost between successor and current state
            dw = Board.calculateCostWithQueens(successor_queens) - Board.calculateCostWithQueens(board_queens)
            # Calculate acceptance probability
            exp = math.exp(-dw * self.temperature)
            # If better or accepted by probability, update current state
            if dw > 0 or random.uniform(0, 1) < exp:
                board_queens = successor_queens[:]
            # If solution found, print and exit loop
            if Board.calculateCostWithQueens(board_queens) == 0:
                print("Solution:")
                print(Board.toString(board_queens))
                self.elapsedTime = self.getElapsedTime()
                print("Success, Elapsed Time: %sms" % (str(self.elapsedTime)))
                solutionFound = True
                break

        # If no solution found, print elapsed time
        if not solutionFound:
            self.elapsedTime = self.getElapsedTime()
            print("Unsuccessful, Elapsed Time: %sms" % (str(self.elapsedTime)))

        return self.elapsedTime

    def getElapsedTime(self):
        endTime = datetime.now()
        elapsedTime = (endTime - self.startTime).microseconds / 1000
        return elapsedTime

if __name__ == '__main__':
    # Initialize board and print initial state
    board = Board()
    print("Board:")
    print(Board.toString(board.queens))
    # Run simulated annealing algorithm
    SimulatedAnnealing(board).run()

