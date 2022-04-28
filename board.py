#!/usr/bin/python3

""" Object file for the 
    TODO

Authors:
    Juan Jose Castano Moreno
    jc10536@nyu.edu

    Rishyak Panchal
    rishyak@nyu.edu
"""

class Board:
    """ Board Class
    
    Attributes:
        board (list[list[int]]): List symbolising state of the puzzle.
    """
    def __init__(self, board : list[list[int]]) -> None:
        self.board = board
        self.transposed = list(map(list, zip(*board)))


    def __str__(self):
        """ Print method mainly for debugging purposes.

        Returns:
            str : String representation of the board.
        """
        output = ""
        for line in self.board:
            for num in line:
                output += str(num) + " "
            output += "\n"
        
        return output


    def mrvHeuristic(self) -> int:
        """ Calculates the minimum remaining values heuristic.

        Returns:
            int : The minimum remaining values heuristic.
        """
        # TODO
        return 0


    def degreeHeuristic(self) -> int:
        """ Calculates the degree heuristic.

        Returns:
            int : The degree heuristic.
        """
        # TODO
        return 0
