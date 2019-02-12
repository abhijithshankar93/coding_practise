'''
Question: Given a million number print out the max n elements


Solution: Use a max heap with n elements and insert and pop out smallest 
		  numbers from the list as we read
'''

import heapq

def find_max(arr, n):

	#create a min heap with first n elements
	heap = arr[:int(n)]
	heapq.heapify(heap)

	#Iterate through the rest of the array replacing max
	for i in range(int(n), len(arr)):
		heapq.heappushpop(heap,arr[i])

	return heap

def find_min(arr, n):

	#create a max heap with first n elements
	heap = map(lambda x: -1*x, arr[:int(n)])
	heapq.heapify(heap)

	#Iterate through the rest of the array replacing max
	for i in range(int(n), len(arr)):
		heapq.heappushpop(heap,-1*arr[i])

	return map(lambda x: -1*x, heap)



H = [21,1,45,78,3,5,0]

print(find_max(H,2))

print(find_min(H,2))



