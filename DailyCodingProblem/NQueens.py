'''The N queens puzzle is the classic backtracking problem. The question 
is this:

You have an N by N board. Write a function that returns the number of 
possible arrangements of the board where N queens can be placed on the 
board without threatening each other, i.e. no two queens share the same
row, column, or diagonal.
'''


def is_valid(board):
	'''
	Util that will return if the current placement of the queen is valid
	'''
	current_queen_row = len(board)-1
	current_queen_column = board[-1]

	for row, column in enumerate(board[:-1]):
		abs_diff = abs(column - current_queen_column)
		if abs_diff == 0 or (current_queen_row - row) == abs_diff: 
			return False
	return True


def n_queens(size, board=[], solutions=[]):
	'''
	Bactracking solution that keeps building the board over each iteration

	In addition to getting the sum. This algorithm also returns the position
	of the queens also.
	'''
	#when the size of board is equal to the provided size we know we have a
	#completed solution
	if len(board) == size:
		solutions.append(board[:])
		return (1 , solutions)

	count = 0
	#iterate through every possible value that wwe can put for a row
	for column in range(size):
		board.append(column)
		#only if the given column num is valid do we need to continue
		if is_valid(board):
			count += n_queens(size, board, solutions)[0]
		board.pop()

	return (count, solutions)



if __name__ == '__main__':
	count, solutions = n_queens(8)
	print count, solutions

