'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two neighboring
 houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to
build the nth house with kth color, return the minimum cost which achieves
this goal.
'''


def least_cost(cost):
	'''
	Time complexity O(nk) and space complexity O(1).
	Logic involves iterating through all paints of all the houses. Add the cost
	of current paint to the prev min till n-1'th house.
	When we encounter the cost of paint which is the least in prev house, then
	add the second least cost of the painting the previous house.
	
	After end of last house we have found the min cost of painting all the
	houses.
	'''
	pre_min = 0
	pre_second = 0
	pre_index = -1
	for i in range(len(cost)):
		cur_min = float('Inf')
		cur_second = float('Inf')
		cur_index = 0

		for j in range(len(cost[0])):
			if j != pre_index:
				cost[i][j] += pre_min
			else:
				cost[i][j] += pre_second

			if cost[i][j] < cur_min:
				cur_index = j
				cur_second = cur_min
				cur_min = cost[i][j]
			elif cost[i][j] < cur_second:
				cur_second = cost[i][j]

		pre_min = cur_min
		pre_second = cur_second
		pre_index = cur_index

	return pre_min


if __name__ == '__main__':
	cost = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
	print least_cost(cost)
