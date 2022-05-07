# 8puzzle
**Project 2**: Sudoku.

## Description
This program uses backtracking algorithm to solve a sudoku board. We programmed this project using Python due to it's syntactical simplicity.

You pass in a document with the initial state and it returns the solution of the sudoku board.  

The board class created for this project creates a 3d structure that represents the remaining legal values for all the unassigned cells. This was important in order to calculate the necessary heuristics.

Sudoku was defined as a constrain satisfaction problem, where each cell in the board is associated so a set of 10 different numbers that can be assigned to the cell. It is a constraint satisfaction problem because the value that you put in each cell will depend on the values that neighboring cells have.
Variables: cells in the sudoku board
Domain for variables: the set of numbers from 0 to 9
Constraints: each cell can't have the same number as any other cell in the same row or in the same column. Also, each cell has to have a different value from the block of 9 cells that it is located at in the board.

## Resources Used
We had to look at Python documentation. 


## Running the Project
It is recommended that you use a computer running Linux or macOS to run this code. Also ensure that the computer has a clean copy of `Python >3.10` installed. This project has been tested with all releases of Python till the latest one, `Python 3.10`.   

This code has been tested on Ubuntu, Arch, and macOS.   

Keep in mind that you need to have Python installed.   

You need to invoke this file from the terminal using two command line parameters:   
1. Path to input file   
```bash
python3 sudoku.py path/to/input/file.txt 
```
For example, if you wanted to call this file on `Input1.txt`, and both files were in the same directory, you would invoke:
```bash
python3 sudoky.py Input1.txt 1
```
If either argument is ignored, the file will throw an error.

## Files Submitted
As stated above, this project has been categorised into multiple module files that add layers of abstraction to better keep track of what is going on.
| File | Purpose |
|:----:|---|
|board.py|Holds the entire Board, including the heuristic functions.
|sudoku.py|The main file that you should run. This takes the path of the input file as an input and returns the final output as a file. It also has the code of the backtracking algorithm, which ultimately is what solves the sudoku board.


## Miscellaneous
Everything has been commented in [Google Docstings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).   

There are additional comments in the files to explain the obscure blocks of code, to help grade.   

Overall, this project was quite interesting to finish. We had fun.  

## Authors
Juan Jose Castano Moreno   
jc10536@nyu.edu   
[@juanjomoreno11](https://github.com/juanjomoreno11)   

Rishyak Panchal   
rishyak@nyu.edu   
[@rishyak](https://github.com/rishyak)   

## Course
NYU Tandon's CS-UY 4613 Intro to Artificial Intelligence.  
