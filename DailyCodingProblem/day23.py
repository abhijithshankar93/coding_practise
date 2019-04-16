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



if __name__ == '__main__':
	board = [['f', 'f', 'f', 'f'],
			 ['t', 't', 'f', 't'],
			 ['f', 'f', 'f', 'f'],
			 ['f', 'f', 'f', 'f']]

	start = (3,0)
	end = (0,0)
	print shortest_path(board, start, end)