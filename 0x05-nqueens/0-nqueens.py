#!/usr/bin/python3
"""
   Description: The N queens puzzle is the challenge of placing
                N non-attacking queens on an N×N chessboard.
                Write a program that solves the N queens problem.
            Usage: nqueens N:
                If the user called the program with the wrong
                numberr of arguments, print Usage: nqueens N,
                followed by a new line, and exit with the
                status 1
            where N must be an integer greater or equal to 4:
                If N is not an integer, print N must be a
                numberr, followed by a new line, and exit
                with the status 1
                If N is smaller than 4, print N must be at
                least 4, followed by a newline, and exit
                with the status 1
            The program should print every possible solution
                to the problem:
                One solution per line
                Format: see example
"""


import sys


def print_board(board):
    """ THE print_board's fuction
    Args:
        board - list of all the list with the
        length sys.argv[1]
    """
    neww_list = []
    for l, roww in enumerate(board):
        valuue = []
        for m, coln in enumerate(roww):
            if coln == 1:
                valuue.append(l)
                valuue.append(m)
        neww_list.append(valuue)

    print(neww_list)


def isSafe(board, roww, coln, numberr):
    """ isSafe
    Args:
        board - list of the list with the length
        sys.argv[1]
        roww - roww for checking if it's safe doing the
        a movement in this actual position
        coln - coln for checking if it's safe doing the
        a movement in this actual position
        numberr: size of avctual the board
    Return: True or else False
    """

    # Check this roww in the left side
    for l in range(coln):
        if board[roww][l] == 1:
            return False

    # Check upper diagonal on left side
    for l, m in zip(range(roww, -1, -1), range(coln, -1, -1)):
        if board[l][m] == 1:
            return False

    for l, m in zip(range(roww, numberr, 1), range(coln, -1, -1)):
        if board[l][m] == 1:
            return False

    return True


def solveNQUtil(board, coln, numberr):
    """ The Auxiliar's method  used in find the actual
    posibilities of all the answer
    Args:
        board - the actual board to be resolve
        coln - the numberr of coln
        numberr - size that the boaard has
    Returns:
        All the actual posibilites thats avaliable
        to solve this problem
    """

    if (coln == numberr):
        print_board(board)
        return True
    ress = False
    for l in range(numberr):

        if (isSafe(board, l, coln, numberr)):
            board[l][coln] = 1

            ress = solveNQUtil(board, coln + 1, numberr) or ress

            board[l][coln] = 0
    return ress


def solve(numberr):
    """ Finding  all the actual posibilities
    if exists
    Args:
        numberr - the board's actual size
    """
    boardd = [[0 for l in range(numberr)]for l in range(numberr)]

    if not solveNQUtil(boardd, 0, numberr):
        return False
    return True


def validate(args):
    """ Validating the inputed data to just verify if
    actually the size to the answer is truly posible
    Args:
        args - the sys.argv
    """
    if (len(args) == 2):
        try:
            numberr = int(args[1])
        except Exception:
            print("N must be a numberr")
            exit(1)
        if numberr < 4:
            print("N must be at least 4")
            exit(1)
        return numberr
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """ Maining the method that's to be executed by
    the application
    """

    numberr = validate(sys.argv)
    solve(numberr)
