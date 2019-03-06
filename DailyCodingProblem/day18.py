'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the 
array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should 
get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place 
and you do not need to store the results. You can simply print them out as 
you compute them.
'''
from __future__ import print_function
from collections import deque

def max_window_subarray(array, k):
	Dq = deque()

	#add first k elements of the array
	for i in range(k):
		while Dq and array[Dq[-1]] <= array[i]:
			Dq.pop()

		Dq.append(i)

	#now start from k to end of array
	for i in range(k, len(array)):
		print(array[Dq[0]], sep = ',', end=' ')
		while Dq and Dq[0] <= i-k:
			Dq.popleft()

		while Dq and array[Dq[-1]] <= array[i]:
			Dq.pop()

		Dq.append(i)
	print(array[Dq[0]])


if __name__ == '__main__':
	a = [10, 5, 2, 7, 8, 7]
	b=[1, -2, 5, 6, 0, 9, 8, -1, 2, 0]
	k = 3
	max_window_subarray(a, k)
	max_window_subarray(b, k)