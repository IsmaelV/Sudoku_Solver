import numpy as np


def possible(y, x, n, my_grid):
	"""
	Check to see if a given cell in the given grid can possibly put a given number

	Author: Professor Thorsten Altenkirch
	Source: https://www.youtube.com/watch?v=G_UYXzGuqvM

	:param y: y-coordinate of grid
	:param x: x-coordinate of grid
	:param n: number to be checked
	:param my_grid: grid to be checked
	:return: Boolean of whether the number can possibly be placed
	"""
	# Check column rule
	for i in range(0, 9):
		if my_grid[y][i] == n:
			return False

	# Check row rule
	for i in range(0, 9):
		if my_grid[i][x] == n:
			return False

	# Check box rule
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0, 3):
		for j in range(0, 3):
			if my_grid[y0 + i][x0 + j] == n:
				return False
	return True


def my_solve(my_grid):
	"""
	Recursive function that checks to gives all solutions to a sudoku grid

	Author: Professor Thorsten Altenkirch
	Source: https://www.youtube.com/watch?v=G_UYXzGuqvM

	:param my_grid: Sudoku grid to check
	:return: Nothing really
	"""
	for y in range(9):  								# Check columns
		for x in range(9):  							# Check rows
			if my_grid[y][x] == 0:  					# Empty cell found
				for n in range(1, 10):  				# Check every number for the cell
					if possible(y, x, n, my_grid):  	# Number is possible in empty cell
						my_grid[y][x] = n  				# Set the number to empty cell
						my_solve(my_grid)  				# RECURSION to solve puzzle
						my_grid[y][x] = 0  				# Number was possible but wrong, set as empty again
				return

	# Finished puzzle and show
	print(np.matrix(my_grid))
	input("Above is one possible solution. Press enter and we will look for any other possible solution :)")


def construct_row(x):
	"""
	Construct a row for the grid

	Author: Ismael Villegas Molina
	Source: Original

	:param x: row number
	:return: constructed row as a list
	"""
	print("We are constructing row number", x)
	tmp_row = []
	valid_num = True
	while len(tmp_row) < 9:
		if valid_num:
			tmp_input = input("What is the next number in the row? ")
		else:
			tmp_input = input("You did not input a valid number. Please repeat that number. ")
		if tmp_input.isdigit() and 0 <= int(tmp_input) <= 9:
			valid_num = True
			tmp_row.append(int(tmp_input))
		else:
			valid_num = False
	return tmp_row


def construct_grid():
	"""
	Constructing the full grid row-by-row

	Author: Ismael Villegas Molina
	Source: Original

	:return: constructed grid as list of lists
	"""
	full_grid = []
	while len(full_grid) < 9:
		my_row = construct_row(len(full_grid) + 1)
		print("Below is the row you constructed\n" + str(my_row))
		good_row = input("Is this the correct row? (y/n) ")
		if good_row.lower()[0] == 'y':
			full_grid.append(my_row)
		else:
			print("Let's retry to make that row!")
	print("---------------------")
	print("You constructed the following grid:")
	print(np.matrix(full_grid))
	print("---------------------")
	return full_grid


if __name__ == "__main__":
	print("Hello there! We are going to construct your sudoku grid")
	print("We will go ROW BY ROW! That is the first line on top first and we work our way down")
	print("If you make an error, don't worry! We will ask you at the end if the row is correct.")
	print("If a row is not correct, let us know and we will restart!")
	grid = construct_grid()
	my_solve(grid)
