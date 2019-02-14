'''Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would 
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].

Follow-up: what if you can't use division?

'''


def first_sol_with_div(arr):
	''' Function takes in a list and returns resultant array which is prod
	of all other numbers in the array except arr[i]'''

	prod = []
	final_prod = 1

	#iterate through the list and find prod of all numbers
	for i in arr:
		final_prod *= int(i)

	#create the prod list to return
	for i in range (0, len(arr)):
		prod.append(final_prod/int(arr[i]))

	return prod


def second_sol_without_div(arr):
	'''Function takes in a list and returns resultant array which is prod 
	of all other elements except arr[i]. Additionally this approch does not
	use division
	This approch has O(n) complexity and O(1) space'''

	prod = [1] * len(arr)
	temp = 1

	#iterate forward storing value of list with product of all num < i
	for i in range (0, len(arr)):
		prod[i] *= temp
		temp *= arr[i]

	#set value of temp back to 1
	temp = 1

	#iterate back storing value of list with product of all num > i 
	for i in range(len(arr)-1,-1, -1):
		prod[i] *= temp
		temp *= arr[i]

	return prod



A = [1, 2, 3, 4, 5]
print('first_sol_with_div {}'.format(first_sol_with_div(A)))
print('second_sol_without_div {}'.format(second_sol_without_div(A)))
