'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the 
intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same node 
objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and 
constant space.
'''
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, node=None):
		self.head = node
		self.tail = node

	def add_value(self, value):
		temp = Node(value)
		self.tail.next = temp
		self.tail = temp
	
	def add_node(self, node):
		self.tail.next = node
		self.tail = node


def get_length(node):
	length = 0
	while node:
		node = node.next
		length += 1
	return length



def find_intersecting_node_1(ll1, ll2):
	'''
	Approach 1:
	Run through the two LinkedLists(LL) and find the length of both

	Next, iterate through the larger LL up until a point where the 2
	LL are now of equal lengths

	Now iterate through the 2 LLs and look when the nodes are equal.
	Though the time and space complexity is O(m+n) and O(1) respectively, it
	involves multiple iterations through the LL
	'''
	node1 = ll1.head
	node2 = ll2.head
	length1 = get_length(node1)
	length2 = get_length(node2)
	if length1 > length2:
		for _ in range(length1-length2):
			node1 = node1.next
	elif length1 < length2:
		for _ in range(length2-length1):
			node2 = node.next

	while node1 and node2:
		if node1.value == node2.value:
			return node1
		else:
			node1 = node1.next
			node2 = node2.next
	return None

def find_intersecting_node_2(ll1, ll2):
	'''
	Approach 2:
	Iterate through the first LinkedList(LL) and make it circular by setting
	the next attribute of the last node as the first node.

	Now iterate through the second LL and find the point at which the second LL
	becomes cyclic.
	The point of cyclicity in the second LL eventually turns out to be the
	point of intersection of the two LL
	Time Complexity: O(n+m)
	Space Complexity: O(1) 
	'''
	node1 = ll1.head
	node2 = ll2.head
	
	#make LL1 cyclic
	while node1.next:
		node1 = node1.next
	node1.next = ll1.head

	#now look for point of cyclicity in ssecond LL

	#First check if LL is cyclic
	ptr1 = ll2.head.next
	ptr2 = ll2.head.next.next
	while ptr1.value != ptr2.value:
		ptr1 = ptr1.next
		ptr2 = ptr2.next.next

	#now that we know it is cyclic start looking for point of cyclicity
	ptr1 = ll2.head
	while ptr1.value != ptr2.value:
	    ptr1 = ptr1.next
	    ptr2 = ptr2.next

	return ptr1



if __name__ == '__main__':
	#create A
	A1 = Node(3)
	A = LinkedList(A1)
	A.add_value(7)
	A.add_value(234)
	A.add_value(4)
	A.add_value(9)
	
	#point of intersection
	I1 = Node(8)
	I = LinkedList(I1)
	I.add_value(189)
	A.add_node(I1)
	
	#create B
	B1 = Node(99)
	B = LinkedList(B1)
	B.add_value(1)
	B.add_value(5)
	B.add_node(I1)
	print find_intersecting_node_1(A,B).value
	print find_intersecting_node_2(A,B).value