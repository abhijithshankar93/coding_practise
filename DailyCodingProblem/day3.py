'''Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string 
back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:

	def __init__(self, val, left=None, right=None):

		self.val = val
		self.left = left
		self.right = right

	def print_tree(self, root):
		'''Pre-order'''
		if root:
			print root.val
			self.print_tree(root.left)
			self.print_tree(root.right)


def serialize(root, s=[]):
	'''
	Crux of problem: How to identify the edges of the tree

	We serealize by following the pre-order traversal (actually any will work
	as long as same technique is used while deserializing) technique
	When we hit the end of the tree(when we hit None) we add a special
	MARKER (this case '/') to the list. This way, when we try reconstructing
	back the tree we can exactly figure out the edges of the tree. 
	'''

	if root is None:
		s.append('/')
		return

	s.append(root.val)
	serialize(root.left, s)
	serialize(root.right, s)

	return s


def deserialize(s):
	'''
	Crux of problem: Same as above; key is to figure out the edges

	As we serialized, we run through the list and removing each element as we
	construct the tree. 
	Every time we hit the marker('/' in this case) we return bactrack as this 
	signifies an edge of the tree
	'''

	val = s.pop(0)
	if len(s) < 1 or val == '/':
		return None

	node = Node(val)
	node.left = deserialize(s)
	node.right = deserialize(s)
	return node


node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'
