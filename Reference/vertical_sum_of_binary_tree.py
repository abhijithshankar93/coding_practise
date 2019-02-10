'''
Question: Given a binary tree find the Vertical sum of Binary Tree

Ex:         1
        2       
    4       5   3    
            7       6


Answer:
    4   2   13  3   6

'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
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

    def VerticalSum(self, root, count=0, sum_dict={}):
        '''
        Logic was simple. Calculate the Horizontal Distance between the root
        and the subsequest nodes.
        Start the count with 0 and as we go left subt 1 (count-1) and when we
        move right add 1 (count+1).
        Store the sums in a Dictionary with the HD(count) as the key and the
        sum as value. Return the dictionary.
        '''
        res = []
        if root:
            if count in sum_dict:
                sum_dict[count] += root.data
            else:
                sum_dict[count] = root.data
            self.VerticalSum(root.left, count=count-1, sum_dict=sum_dict)
            self.VerticalSum(root.right, count=count+1, sum_dict=sum_dict)
        return sum_dict


root = Node(4)
root.insert(6)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(5)
root.insert(7)

print root.VerticalSum(root)
