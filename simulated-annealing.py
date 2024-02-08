from datetime import datetime
import random
import math
import decimal

class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.reset()

    def reset(self):
        """Reset the board with random queen positions."""
        self.queens = [random.randint(0, self.queen_count - 1) for _ in range(self.queen_count)]

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
        """Convert queen positions to a printable string."""
        board_string = ""
        for row, col in enumerate(queens):
            board_string += "(%s, %s)\n" % (row, col)
        return board_string

class SimulatedAnnealing:
    def __init__(self, board):
        self.elapsedTime = 0
        self.board = board
        self.temperature = 4000
        self.sch = 0.99
        self.startTime = datetime.now()

    def run(self):
        board_queens = self.board.queens[:]  # Make a copy of initial board state
        solutionFound = False

        for k in range(170000):  # Reduced range to improve efficiency
            self.temperature *= self.sch
            board = deepcopy(self.board)  # Create a new board instance
            board.reset()
            successor_queens = board.queens[:]
            dw = Board.calculateCostWithQueens(successor_queens) - Board.calculateCostWithQueens(board_queens)
            exp = math.exp(-dw * self.temperature)  # Removed unnecessary decimal.Decimal
            if dw > 0 or random.uniform(0, 1) < exp:
                board_queens = successor_queens[:]
            if Board.calculateCostWithQueens(board_queens) == 0:
                print("Solution:")
                print(Board.toString(board_queens))
                self.elapsedTime = self.getElapsedTime()
                print("Success, Elapsed Time: %sms" % (str(self.elapsedTime)))
                solutionFound = True
                break

        if not solutionFound:  # Simplified condition
            self.elapsedTime = self.getElapsedTime()
            print("Unsuccessful, Elapsed Time: %sms" % (str(self.elapsedTime)))

        return self.elapsedTime

    def getElapsedTime(self):
        endTime = datetime.now()
        elapsedTime = (endTime - self.startTime).microseconds / 1000
        return elapsedTime

if __name__ == '__main__':
    board = Board()
    print("Board:")
    print(board)
    SimulatedAnnealing(board).run()
