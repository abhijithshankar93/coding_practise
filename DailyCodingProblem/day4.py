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









