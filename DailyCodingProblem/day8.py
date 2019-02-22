'''Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes 
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_unival(root):
	count, _ = dp_helper(root, root.value)
	return count

def dp_helper(root, value):

	if root is None:
		return (0, True)

	is_unival = True

	left_cnt, is_left_unival = dp_helper(root.left, root.value)
	right_cnt, is_right_unival = dp_helper(root.right, root.value)

	if is_left_unival and is_right_unival:
		count = left_cnt+right_cnt+1
	else:
		count = left_cnt+right_cnt
		is_unival = False

	if root.value != value:
		is_unival = False

	return (count, is_unival)


if __name__ =='__main__':
	root = Node(5) 
	root.left = Node(4) 
	root.right = Node(5) 
	root.left.left = Node(4) 
	root.left.right = Node(4) 
	root.right.right = Node(5) 
	print count_unival(root) 