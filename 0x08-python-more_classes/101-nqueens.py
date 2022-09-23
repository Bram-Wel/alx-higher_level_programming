#!/usr/bin/python3
"""Solves the N-queens puzzle

Finds all the possible positions for N
non-attacking queens on an NxN board

Eg:
    $ ./101-nqueens.py N

N (Integer)
N >= 4
"""
import sys


def init_board(n):
    """Initialises nxn board"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    """Copy a chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_soln(board):
    """List rep of soved chess board"""
    soln = []
    for ro in range(len(board)):
        for col in range(len(board)):
            if board[ro][col] == 'Q':
                soln.append([ro, col])
                break
    return soln


def xout(board, row, col):
    """Crosses x's on a chessboard

    Args:
        board: operational board
        row: Last row occupied by queen
        col: Last column occupied by queen
    """
    # forward spots
    for i in range(col + 1, len(board)):
        board[row][i] = 'x'
    # backward spots
    for i in range(col - 1, -1, -1):
        board[row][i] = 'x'
    # spots below
    for j in range(row + 1, len(board)):
        board[j][col] = 'x'
    # spots above
    for j in range(row - 1, -1, -1):
        board[j][col] = 'x'
    # diagonal spots =>down to right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1
    # diagonal spots =>up to left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # diagonal spots =>up to right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = 'x'
        c += 1
    # diagonal spots =>down to left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = 'x'
        c -= 1


def rec_solve(board, row, queens, solns):
    """Solves n-queens puzzle recursively

    Args:
        board: operating board
        row: operating row
        queens: total placed queens
        solns: List of soln lists

    Return:
        Solns
    """
    if queens == len(board):
        solns.append(get_soln(board))
        return solns

    for c in range(len(board)):
        if board[row][c] == " ":
            temp = board_deepcopy(board)
            temp[row][c] == 'Q'
            xout(temp, row, c)
            solns = rec_solve(temp, row + 1, queens + 1, solns)
    return solns


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    elif sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solns = rec_solve(board, 0, 0, [])
    for s in solns:
        print(s)
