'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear 
time and constant space. In other words, find the lowest positive integer that 
does not exist in the array. The array can contain duplicates and negative 
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
should give 3.

You can modify the input array in-place.
'''



def leftshift(arr):
	j = 0
	for i in range(0, len(arr)):
		if arr[i] < 1:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			j += 1
	return j

def _find_min_positive_num(arr, index):

	#first iterate through setting values to -ve if present
	for i in range(index, len(arr)):
		if arr[abs(i)] > len(arr)-index:
			continue
		else:
			arr[abs(arr[i])+index-1] *= -1

	#run through the array now checking if we left behind any positive
	for i in range(index, len(arr)):
		if arr[i] > 0:
			return i-index+1
	return len(arr)-index+1

def find_min_posistive_num(arr):
	'''
	Crux of problem: move all -ve to left and then set a[i] to -ve if i is 
	present in a. 
	For eg: 
	if A = [3, 4, -1, 1] first move all -ve num to left and calculate
	the num of -ve num. (here [-1, 4, 3, 1] and index returned is 1)

	Now set A[abs(i)+index-1] to -ve num if i is present in A.
	Here we would end up with this array A = [-1, -4, 3, -1]

	Now we can easilly iterate through A (after index) and determining index of
	A where A[i] > 0. If we do not find any then we send back len-index+1
	'''

	#shift all -ve numbers to left
	index_shift = leftshift(arr)
	#find the min num
	val = _find_min_positive_num(arr, index_shift)

	return val

if __name__ == '__main__':
	A = [3, 4, -1, 1]
	print (find_min_posistive_num(A))
	B = [1, 2, 0]
	print (find_min_posistive_num(B))









