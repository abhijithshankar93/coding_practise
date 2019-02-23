'''Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?'''

from datetime import datetime

def find_max_sum(arr):
	return dp_helper(arr, 0, {})


def find_max_sum_v2(arr):
	return dp_helper_v2(arr)


def dp_helper(arr, index, memo={}):
	'''solution with O(n) time complexity and O(n) space complexity
	   top down approach'''
	#base cases
	#if index in memo:
	#	return memo[index]
	if index == len(arr)-2:
		memo[index] = max(arr[index], arr[index+1])
	elif index == len(arr)-3:
		memo[index] = max(arr[index]+arr[index+2], arr[index+1])
	else:
		memo[index] = max(arr[index]+dp_helper(arr, index+2,memo), 
			   dp_helper(arr, index+1,memo))
	return memo[index]


def dp_helper_v2(arr):
	''' Soltution with O(n) time complexity and constant space complexity
		a bottom up approach is followed
	'''
	prev_one, prev_two = 0,0

	for i in range(len(arr)):
		if i == 0:
			res = arr[i]
		elif i == 1:
			res = max(arr[i], arr[i-1])
		else:
			res = max(arr[i]+prev_two, prev_one)

		prev_two = prev_one
		prev_one = res

	return res


if __name__ == '__main__':
	a=[5,1,1,13,1]
	b=[2,4,6,2,5]
	c=[12,4,6,19,5]
	start = datetime.now()
	print find_max_sum(a)
	print find_max_sum(b)
	print find_max_sum(c)
	print 'Total time {}'.format(datetime.now()-start)
	print '-'*50+'\nAttempting next ver'+'\n'+'-'*50
	start = datetime.now()
	print find_max_sum_v2(a)
	print find_max_sum_v2(b)
	print find_max_sum_v2(c)
	print 'Total time {}'.format(datetime.now()-start)

