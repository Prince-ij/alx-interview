#!/usr/bin/python3
"""
Solves the N Queens puzzle.
"""

import sys


def is_safe(board, row, col, N):
    """
    Checks if it's safe to place a queen at board[row][col].
    :param board: Current state of the board.
    :type board: list
    :param row: Row index.
    :type row: int
    :param col: Column index.
    :type col: int
    :param N: Size of the board (N x N).
    :type N: int
    :return: True if it's safe to place the queen, otherwise False.
    :rtype: bool
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solves the N Queens problem and prints all possible solutions.

    :param N: Size of the board (N x N).
    :type N: int
    """
    def backtrack(row):
        """
        Uses backtracking to place queens and find all solutions.

        :param row: Current row to place the queen.
        :type row: int
        """
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    backtrack(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_nqueens(N)
