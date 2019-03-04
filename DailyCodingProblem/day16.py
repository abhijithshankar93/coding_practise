'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a 
log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be 
smaller than or equal to N.
You should be as efficient with time and space as possible.
'''


class CircularQueue:
	'''
	Implementation of a circular Queue using Python lists
	'''
	def __init__(self, max_len):
		self.buffer = [0]*max_len
		self.index = 0
		self.max_len = max_len

	def record(self, data):
		'''
		Function to record the data that is to be added to the Circular Queue
		Complexity here is O(1) as we just replace old values by overwritting 
		the oldest data by index
		'''
		self.buffer[self.index] = data
		self.index = (self.index + 1)%self.max_len

	def get_last(self, i):
		'''
		Function to get the last i values in the Queue.
		Complexity here would O(i) where i is the number of records from the
		end that need to retrieved.
		Complexity is O(i) as slicing in python requires it to iterate over the
		values that it needs to return. eg. a[i:j] will require python to
		iterate from a[i] to a[j] for it to return the values in between 
		'''
		start_index = self.index - i
		if start_index < 0:
			return self.buffer[start_index:]+self.buffer[:self.index]
		else:
			return self.buffer[:start_index]

if __name__ == '__main__':
	c1 = CircularQueue(10)

	for i in range(23):
		c1.record(i)
		
	print c1.get_last(5)