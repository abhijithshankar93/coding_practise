'''Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of 
each node holding next and prev fields, it holds a field named both, which is 
an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) 
which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you 
have access to get_pointer and dereference_pointer functions that converts 
between nodes and memory addresses.
'''


class XOR_linked_list_node:
	'''
	Imp take away: -1 can replace None as marker to signify end of LL
	'''
	def __init__(self, val, _next=-1, prev=-1):
		self.val = val
		self.both = _next ^ prev

	def next_node(self, prev=None):
		return self.both ^ prev

	def prev_node(self, _next=None):
		if _next is None:
			return -1
		else:
			return self.both ^ _next

	def curr_node(self, _next):
		'''
		Hacky way to get the id/address given the node. In a language that 
		supports pointers this would be equivalent of get_pointer func
		'''
		return (self.both ^ _next)+1

	def modify_both(self, prev, _next):
		'''
		To modify val of self.both when a new element is added to end
		'''
		self.both = prev ^ _next


class XOR_linked_list:
	def __init__(self, node):
		self.linked_list = []
		self.linked_list.append(node)
		self.len = len(self.linked_list)

	@property	
	def get_head(self):
		return self.linked_list[0]

	def add(self, element):
		'''
		Takes in a val and creates a node out of it and appends to linked list
		'''
		node = self.get_head
		prev_node = node.prev_node() #as it is head (will return -1)
		next_node = node.next_node(prev_node)

		while next_node != -1: #loop till we reach the end of LL
			prev_node = node.curr_node(next_node)
			node = self.linked_list[next_node]
			next_node = node.next_node(prev_node)

		#add the new node now since we reached he end
		new_node = XOR_linked_list_node(element, -1, node.curr_node(next_node))
		self.linked_list.append(new_node)

		#modify val of both of prev node as the next val has changed from -1
		node.modify_both(prev_node, new_node.curr_node(next_node))

		#just update the length of the LL to keep track
		self.len = len(self.linked_list)
		return self.linked_list

	def get(self, index):
		'''
		Takes an index, and moves corresponding number of nodes ahead in the 
		linked list.
		'''
		# if index is greater than equal to length of LL we return None
		if index >= self.len:
			return None

		node = self.get_head
		prev_node = node.prev_node()
		next_node = node.next_node(prev_node)
		cnt = 0 #counter to keep count of movements

		while cnt < index: #loop until we have jumped index num of nodes
			prev_node = node.curr_node(next_node)
			node = self.linked_list[next_node]
			next_node = node.next_node(prev_node)
			cnt += 1

		return node.val

	@property
	def print_l(self):
		return self.linked_list
	

if __name__ == '__main__':
	node = XOR_linked_list_node('a')
	l = XOR_linked_list(node)
	for i in xrange(15):
		l.add(i)

	print map(lambda x: x.val, l.print_l)

	for i in xrange(12):
		print l.get(i)

