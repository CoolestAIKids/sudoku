#!/usr/bin/python3

""" Driver code for the program.
    This is the file that you will invoke from 
    the command line like so:
    $ python3 sudoku.py <filename>

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
        name (str): The filepath of the file.
        board (Board): The solved board.

    Returns:
        None.
        Just creates a file with the solution.
    """
    # Get output filename
    filename = name.lower().replace('input', 'output')

    # Create and write to output file
    with open(filename, 'w') as f:
        f.write(board.__str__())


def backTrack(board : Board) -> Board:
    """ Backtracking search. Loosely follows
    the algorithm outlined in the assignment document.

    Args:
        board (Board): The board to solve.

    Returns:
        Board: The solved board.
    """
    # Get MRV
    heur = board.mrv()

    # If MRV is empty, board is solved
    if not heur:
        return board

    # If MRV is more than one cell, call degree
    if len(heur) > 1:
        heur = board.degree(heur)
    
    # Choose the first from the heuristic
    cell = heur[0]

    row = cell[0]
    col = cell[1]

    # We iterate over all legal values
    for value in board.boxes[row][col]:
        # Make a deepcopy of the board for backtracking
        # purposes since python lists and objects are 
        # always passed by reference.
        newBoard = deepcopy(board)

        # Set the value, if successful, recurse
        # Otherwise, go to next value
        if(newBoard.assign(cell, value)):
            result = backTrack(newBoard)

            # If board is complete, return it
            if result is not False:
                return result
    
    # Failure represented by False
    return False


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

    # Create board
    initial = Board(input)
    
    # Solve and get final board
    final = backTrack(initial)

    # Make output file
    makeFile(cmdline.filename, final)


if __name__ == "__main__":
    main()
