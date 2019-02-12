# Depth First Search of a Tree
'''
Refer: https://www.tutorialspoint.com/python/python_graph_algorithms.htm

Also called depth first search (DFS),this algorithm traverses a graph in 
a depth ward motion and uses a stack to remember to get the next vertex to 
start a search, when a dead end occurs in any iteration. We implement DFS 
for a graph in python using the set data types as they provide the required 
functionalities to keep track of visited and unvisited nodes.



'''


class Graph:
	def __init__(self, graph_dict=None):
		if graph_dict is None:
			graph_dict = {}

		self.graph_dict = graph_dict


	def dfs(self, start, visited=None):
		if visited is None:
			visited = set()

		visited.add(start)
		print start
		for vertex in set(self.graph_dict[start]) - visited:
			self.dfs(vertex, visited)

		return visited

if __name__ == '__main__':
	g1 = { 	'a': ['b', 'c'],
			'b': ['a', 'd'],
			'c': ['a', 'd'],
			'd': ['e'],
			'e': ['a']
		}
	G1 = Graph(g1)
	nodes = G1.dfs('a')
	#for node in nodes: print node 