class Node:
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None


	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	def find_max_width(self, root, count=0, width_dict={}):
		if width_dict == {}:
			width_dict['min'] = width_dict['max'] = 0
		if root:
			if count < width_dict['min']:
				width_dict['min'] = count
			elif count > width_dict['max']:
				width_dict['max'] = count
			self.find_max_width(root.left, count=count-1, width_dict=width_dict)
			self.find_max_width(root.right, count=count+1, width_dict=width_dict)
		return int(width_dict['max']) - int(width_dict['min'])


	def find_max_width_queue(self, root):
		queue = []
		queue.insert(0,root)
		max_size=0

		while len(queue) > 0:
			if len(queue) > max_size:
				max_size = len(queue)

			for _ in range (0, len(queue)):
				node = queue.pop()
				if node.left is not None:
					queue.insert(0,node.left)
				if node.right is not None:
					queue.insert(0,node.right)
		return max_sizes


root = Node(4)
root.insert(6)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)


root.find_max_width(root)
root.find_max_width_queue(root)




