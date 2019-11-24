'''
Given a singly linked list and an integer k, remove the kth last element from 
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''


class Node:

	def __init__(self, val, next_node=None):
		self.value = val
		self._next = next_node

	@property
	def next(self):
		return self._next

	@next.setter	
	def next(self, next_node):
		self._next = next_node


class LinkedList:

	def __init__(self, first_node):
		self._head = first_node
		first_node.next = None
		self.tail = first_node

	def add_node(self, node):
		self.tail.next(node)
		self.tail = node

	@property
	def head(self):
		return self._head

	def print_list(self):
		temp_node = self.head
		while temp_node is not None:
			print temp_node.value
			temp_node = temp_node.next

	def append(self, val):
		new_node = Node(val)
		self.tail.next = new_node
		self.tail = new_node


def get_k_from_end(link_list, k):
	'''
	Takes a linked list and a integer k and removes the kth last element
	from the list.
	'''
	pointer_1 = link_list.head
	pointer_2 = link_list.head
	steps = 0

	while steps < k-1:
		pointer_1 = pointer_1.next
		steps += 1

	while pointer_1.next is not None:
		pointer_1 = pointer_1.next
		prev = pointer_2
		pointer_2 = pointer_2.next

	prev.next = pointer_2.next
	return link_list


node1 = Node(20)
llist = LinkedList(node1)
llist.append(4)
llist.append(15)
llist.append(35)

new_list = get_k_from_end(llist, 1)
new_list.print_list()
