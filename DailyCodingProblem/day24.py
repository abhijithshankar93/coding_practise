'''
Implement locking in a binary tree. A binary tree node can be locked or
unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked

lock, which attempts to lock the node. If it cannot be locked, then it 
should return false. Otherwise, it should lock it and return true.

unlock, which unlocks the node. If it cannot be unlocked, then it should
 return false. Otherwise, it should unlock it and return true.


You may augment the node to add parent pointers or any other property 
you would like. You may assume the class is used in a single-threaded 
program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.
'''



class Node:
	def __init__(self, val, left, right, parent):
		self.value = val
		self.left = left
		self.right = right
		self.parent = parent
		self.is_locked = False
		self.locked_descendants = 0


	def is_locked(self):
		return self.is_locked

	def can_lock_unlock(self):
		if self.locked_descendants != 0:
			return False

		#check if any ancestors are locked
		parent = self.parent
		while parent != None:
			if parent.is_locked == True:
				return False
			else:
				parent = parent.parent

		return True

	def lock(self):
		if not can_lock_unlock() or self.is_locked == True:
			return False

		#lock the node
		self.is_locked = True

		#increment the value locked_descendants on all the ancestors
		parent = self.parent
		while parent != None:
			parent.locked_descendants += 1
			parent=parent.parent

		return True

	def unlock(self):
		if not can_lock_unlock() or self.is_locked == False:
			return False

		#unlock the node
		self.is_locked = False

		#Decrement the value locked_descendants on all the ancestors
		parent = self.parent
		while parent != None:
			parent.locked_descendants -= 1
			parent=parent.parent

		return True


if __name__ == '__main__':
	

