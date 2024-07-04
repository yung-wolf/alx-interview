#!/usr/bin/python3
"""
module: 0-nqueens

Holds three main functions:
1. solve_nqueens()
     -->is_valid()
     -->solve()
2. print_solutions()
3. main()
"""


import sys


def solve_nqueens(n):
    """
        A function that returns all solutions for the given `n`.
    """
    def is_valid(board, row, col):
        """
            Checks if placing a queen at a given row and column is valid.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row):
        """
            Insert queens row by row.
            Adds valid solutions to the `solutions` list.
        """
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    board = [-1] * n
    solutions = []
    solve(0)
    return solutions


def print_solutions(solutions):
    """
        Format and print `solution` list.
    """
    for solution in solutions:
        print("[", end="")
        for i in range(len(solution)):
            print("[{}, {}]".format(i, solution[i]), end="")
            if i < len(solution) - 1:
                print(", ", end="")
        print("]")


def main():
    """Main function. Verify number of args passed."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
