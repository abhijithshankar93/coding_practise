'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you 
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the 
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, 
and right. You cannot move through walls. You cannot wrap around the edges 
of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum 
number of steps required to reach the end is 7, since we would need to go 
through (1, 2) because there is a wall everywhere else on the second row.
'''

from collections import deque

def shortest_path(board, start, end, memoize={}):
	'''
	DP soltuion. This solution keeps moving around in all possible directions.
	Until it meets the end point. Once there, it back tracks to find any
	shorter path
	'''
	if start == end:
		return 0
	if (start[0]<0 or start[0]>=len(board) or
	    start[1]<0 or start[1]>=len(board[-1]) or 
	   board[start[0]][start[1]] == 't'):
	   	return None

	if str(start[0])+','+str(start[1]) in memoize:
		if memoize[str(start[0])+','+str(start[1])] != -1:
			return memoize[str(start[0])+','+str(start[1])]
		else:
			return None
	else:
		memoize[str(start[0])+','+str(start[1])] = -1

	min_list=[]
	top = shortest_path(board, (start[0]-1,start[1]), end, memoize)
	if top is not None:
		min_list.append(top+1)
	right = shortest_path(board, (start[0],start[1]+1), end, memoize)
	if right is not None:
		min_list.append(right+1)
	down = shortest_path(board, (start[0]+1,start[1]), end, memoize)
	if down is not None:
		min_list.append(down+1)
	left = shortest_path(board, (start[0], start[1]-1), end, memoize)
	if left is not None:
		min_list.append(left+1)

	if len(min_list) == 0:
		return None

	memoize[str(start[0])+','+str(start[1])] = min(min_list)
	return memoize[str(start[0])+','+str(start[1])]

def is_valid(curr_row, curr_col, board):
	if (curr_row < 0 or curr_row >= len(board[0]) or 
	   curr_col < 0 or curr_col >= len(board)):
	   return False
	return True

def shortest_path_2(board, start, end):
	'''
	A better solution. Uses Lee Algorithm(usually used for finding the shortest
	path in a binary matrix)

	This approach will not look for all solutions. The first solution it
	finds is generally the shortest.
	
	Time Complexity: (m*n)
	'''
	row_val = [0, -1, 0, 1]
	col_val = [-1, 0, 1, 0]
	
	if board[start[0]][start[1]] != 'f' or board[end[0]][end[1]] != 'f':
		return None

	if start == end:
		return 0

	visited = {}

	q = deque()

	q.append((start,0))

	while len(q) > 0:
		curr_node = q.popleft()

		if curr_node[0] in visited:
			continue

		for i in range (0, 4):
			new_row = curr_node[0][0]+row_val[i]
			new_col = curr_node[0][1]+col_val[i]

			if (new_row, new_col) == end:
				return curr_node[1]+1

			if (is_valid(new_row, new_col, board) and 
			   (new_row, new_col) not in visited and
			   board[new_row][new_col] == 'f'):
			   q.append(((new_row, new_col), curr_node[1]+1))

	return None




if __name__ == '__main__':
	board = [['f', 'f', 'f', 'f'],
			 ['t', 't', 'f', 't'],
			 ['f', 'f', 'f', 'f'],
			 ['f', 'f', 'f', 'f']]

	start = (3,0)
	end = (0,0)
	print shortest_path(board, start, end)