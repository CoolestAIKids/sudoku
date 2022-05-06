#!/usr/bin/python3

""" Driver code for the program.
    This is the file that you will invoke from 
    the command line like so:
    $ python3 sudoku.py <filename> <heuristic>

Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

import argparse
from copy import deepcopy

from board import Board

def makeFile(name : str, board : Board) -> None:
    """ Creates a file with the solution.

    Args:
        

    Returns:
        None.
        Just creates a file with the solution.
    """
    filename = name.lower().replace('input', 'output')

    with open(filename, 'w') as f:
        f.write(board.__str__())
        f.write("\n")


def backTrack(board):
    heur = board.mrv()
    if not heur:
        return board

    if len(heur) > 1:
        heur = board.degree(heur)

    cell = heur[0]
    row = cell[0]
    col = cell[1]
    for value in board.boxes[row][col]:
        newBoard = deepcopy(board)
        newBoard.assign(cell, value)
        backTrack(newBoard)






def main() -> None:
    """ Main function.

    Returns:
        None.
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description='Solve a sudoku problem using backtracking search.')
    parser.add_argument('filename', help='The txt file containing the initial state.')
    cmdline = parser.parse_args()

    # Read input file
    with open(cmdline.filename, 'r') as f:
        input = []
        for line in f:
            line = list(map(int, line.strip().split()))
            input.append(line)

    initial = Board(input)
    
    final = backTrack(initial)

    makeFile(cmdline.filename, final)


if __name__ == "__main__":
    main()
