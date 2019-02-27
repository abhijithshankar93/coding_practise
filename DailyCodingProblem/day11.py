'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set 
of all possible query strings, return all strings in the set that have s as 
a prefix.

For example, given the query string de and the set of strings 
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure 
to speed up queries.
'''


class TrieNode:
	def __init__(self):
		self.children = {}
		self.leaf_node = False


class Trie:
	def __init__(self):
		self.root = TrieNode()

	def create_trie(self, words):
		'''Function takes in a list of words and adds them in dictionary'''
		for word in words:
			self.add_word(word)
		return self.root

	def add_word(self, word, index=0):
		'''Function takes in a word and adds it to the trie'''
		node = self.root

		for letter in word:
			if not node.children.get(letter):
				node.children[letter] = TrieNode()
			
			node = node.children[letter]

		#set the last node as leaf
		node.leaf_node=True

		return self.root

	def _get_word_list(self, node, word_list=[], word=''):
		'''
		Private function. A recursive func that would go through all nodes
		getting the list of words stored in the dictionary.
		'''
		if node.leaf_node:
			word_list.append(word)

		for key, value in node.children.items():
			self._get_word_list(node.children[key], word_list, word+str(key))
		return word_list



	def check_prefix_present(self, prefix):
		'''
		Function that given a prefix would return back if the prefix is a part
		of the Trie and if it is returns the node with the last letter of 
		prefix was found
		'''
		isFound=True
		node = self.root

		for letter in prefix:
			if not node.children.get(letter):
				return False
			node=node.children[letter]

		return node


	def suggest(self, prefix):
		'''
		Function that takes a prefix and returns back a list of words in the 
		dictionary which have the same prefix.
		'''
		node = self.root

		#check if prefix is present in trie
		node = self.check_prefix_present(prefix)

		if node is False:
			return []

		#get word list if prefix is found in trie
		word_list = self._get_word_list(node, word_list=[], word=prefix)
		return word_list



if __name__ == '__main__':

	dictionary = Trie()
	words = ['dog', 'deer', 'deal']
	dictionary.create_trie(words)

	print 'Suggested words are: {}'.format(dictionary.suggest('de'))