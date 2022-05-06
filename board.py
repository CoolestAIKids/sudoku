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
        boxes (list[list[list[int]]]): List symbolising the state of the puzzle, but instead of the assignments,
                                       it contains the remaining legal values of each unassigned cell
    """
    def __init__(self, board) -> None:
        self.board = board

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

    def getNeighbors(self, cell) -> list[int]:
        """ Gets the assigned neighbors of a cell in the sudoku board
                Args:
                    cell: tuple with the row and column of the cell we want to find the neighbors of

                Returns:
                    a list of ints with the values of the neighbors
                """
        neighbors = []
        row = cell[0]
        col = cell[1]

        for i in range(9):
            if self.board[i][col] != 0:
                neighbors.append(self.board[i][col])
            if self.board[row][i] != 0:
                neighbors.append(self.board[row][i])

        box_row, box_col = row //3  * 3, col //3  * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if i == row or j == col:
                    continue
                if self.board[i][j] != 0:
                    neighbors.append(self.board[i][j])

        return neighbors


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


    def mrv(self) -> list[tuple[int]]:
        """ Calculates the minimum remaining values heuristic.

        Returns:
            int : The minimum remaining values heuristic.
        """
        minValue = 10
        returnList = []
        #Goes over the 3d boxes structure and appends the cells that have the smallest possible values
        for row in range(9):
            for col in range(9):
                if self.boxes[row][col] == None:
                    continue
                if len(self.boxes[row][col]) < minValue:
                    minValue = len(self.boxes[row][col])
                    returnList = [(row, col)]
                elif len(self.boxes[row][col]) == minValue:
                    returnList.append((row, col))
                else:
                    continue

        return returnList


    def degree(self, cells) -> list[tuple[int]]:
        """ Calculates the degree heuristic.

        Args:
            cells (list[tuple[int]]): List of tuples representing the cells with equal minimum values.

        Returns:
            list[tuple[int]] : Returns the cells with the highest amount of unasssigned neighbors
        """
        maxNeighborsCells = []
        maxNeighbors = 0 #initialize to 0 since it is the least amount of neighbors that a cell can have
        #This loop goes over the cells that were passed and checks which ones have the most unassigned neighbors
        for cell in cells: 
            numNeighbors = 20 - len(self.getNeighbors(cell)) #number of unassigned neighbors
            if numNeighbors > maxNeighbors:
                maxNeighbors = numNeighbors
                maxNeighborsCells = [cell]
            elif numNeighbors == maxNeighbors:
                maxNeighborsCells.append(cell)
            else:
                continue

        return maxNeighborsCells


    def assign(self, cell, assignment) -> bool:
        """ Puts the corresponding assignment in the given cell after checking if it is consistent with sudoku rules
                Args:
                    cell: tuple with the row and col where you want to put the assignment
                    assignment: int with value that we want to assign to a corresponsing cell

                Returns:
                    a bool indicating wether or not the assignment was consistent with sudoku rules
        """
        neighbors = self.getNeighbors(cell)

        if (assignment in neighbors):
            return False
        else:
            self.board[cell[0]][cell[1]] = assignment
            self.boxes[cell[0]][cell[1]] = None
            self.purge(assignment, cell)
            return True


    def purge(self, assignment, cell) -> None:
        """ Deletes the current assignment in all the neighbors of cell
            Args:
                cell: tuple with the row and column of the cell
                assignment: int that we want to delete from the possible values of cell's neighbors
             Returns:
                None
        """
        row = cell[0]
        col = cell[1]

        for i in range(9):
            if self.boxes[i][col] is None:
                continue

            if assignment in self.boxes[i][col]:
                self.boxes[i][col].remove(assignment)

            if self.boxes[row][i] is None:
                continue

            if assignment in self.boxes[row][i]:
                self.boxes[row][i].remove(assignment)

        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if self.boxes[i][j] is None:
                    continue
                if assignment in self.boxes[i][j]:
                    self.boxes[i][j].remove(assignment)

