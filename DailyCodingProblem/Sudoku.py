'''
Solve a well-posed sudoku puzzle
'''
EMPTY = 0

def is_complete(board):
	for row in board:
		for val in row:
			if val == EMPTY:
				return False
	return True

def get_next_empty(board):
	for r, row in enumerate(board):
		for c, val in enumerate(row):
			if board[r][c] == EMPTY:
				return (r,c)

def row_valid(board):
	for row in board:
		if is_duplicate(row):
			print 'Is duplicate is telling there are invalid'
			print row
			print '-'*10
			return False
	return True

def col_valid(board):
	for row in range(len(board[0])):
		if is_duplicate([board[row][col] for col in range(len(board))]):
			return False
	return True

def block_valid(board):
	for r in range(0, 9, 3):
		for c in range(0, 9, 3):
			block = []
			for row in range(3):
				for col in range(3):
					block.append(board[r+row][c+col])
			if is_duplicate(block):
				return False
	return True

def is_duplicate(array):
	key = {}
	for val in array:
		print '*'*10
		print val
		print key
		print '*'*10
		if val in key and val != EMPTY:
			print 'Val is in key'
			return True
		key[val] = True
	return False


def is_valid(board):
	if not row_valid(board):
		print 'Row is invalid'
		return False
	elif not col_valid(board):
		print 'Col is invalid'
		return False
	elif not block_valid(board):
		print 'Block is invalid'
		return False
	return True

def solve_sudoku(board):
	if is_complete(board):
		return board

	#get next Empty cell to fill
	r, c = get_next_empty(board)
	print r,c

	for val in range(1,10):
		board[r][c] = val
		print board
		if is_valid(board):
			print 'Found board to be valid'
			result = solve_sudoku(board)
			if is_complete(result):
				return board
		print 'Looks like board is no longer valid'
		board[r][c] = EMPTY
	return board


if __name__ =='__main__':
	row = [0]*9
	board = []
	for _ in range(9):
		board.append(list(row))
	board[0][5] = 1
	print board
	print solve_sudoku(board)

