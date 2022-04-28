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
    def __init__(self, board) -> None:
        self.board = board
        self.transposed = list(map(list, zip(*board)))
        fullSet = [1,2,3,4,5,6,7,8,9]
        block = []
        self.boxes = []

        for line in board:
            for cell in line:
                if cell == 0:
                    block.append(fullSet[:])
                else:
                    block.append(None)
            self.boxes.append(block[:][:])
            block = []



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
