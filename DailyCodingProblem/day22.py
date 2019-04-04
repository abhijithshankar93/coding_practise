'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
or ['bedbath', 'and', 'beyond'].
'''
import time

def recursive_solution(words, string):
	'''
	Basic bactracking+recursive solution. Will check if a substring is in
	dictionary. As soon as it finds a match it looks for next substring from
	the end of the current substring.
	When it reaches the end of string without finding a valid word, it 
	backtracks and removes the last word and looks for a larger word which
	contains the prev substring.
	If it reaches the end without finding any valid word. It returns None

	Time complexity = 2^n (where n is size of string)
 	Space complexity = constant
	'''
	sentence = []
	index = 1
	start_index = 0
	while True:
		if string[start_index:index] in words:
			if index == len(string):
				sentence.append(string[start_index:index])
				return sentence
			sentence.append(string[start_index:index])
			start_index = index
			index += 1
		else:
			if index == len(string):
				if len(sentence) == 0:
					return None
				else:
					index = start_index+1
					start_index -= len(sentence[-1])
					sentence.pop()
					continue
			index += 1
			continue

def dp_solution(words, string):
	'''
	Similar solution to above with the addition of caching faulty strings in
	a memoized dict(faulty strings are string which we have previously seen to 
	have no valid word combinations) and looking up in the memoized dict before 
	starting to look in the words dictionary. 
	This way we do not duplicate lookup of valid words once found to be invalid

	Time Complexity(n^2)
	Space Complexity(n)
	where n is size of string
	'''
	sentence = []
	index = 1
	start_index = 0
	memoized={}
	while True:
		if not memoized.get(string[start_index:]):
			if string[start_index:index] in words:
				if index == len(string):
					sentence.append(string[start_index:index])
					return sentence
				sentence.append(string[start_index:index])
				start_index = index
				index += 1
			else:
				if index == len(string):
					if len(sentence) == 0:
						return None
					else:
						memoized[string[start_index:]]=1
						index = start_index+1
						start_index -= len(sentence[-1])
						sentence.pop()
						continue
				index += 1
				continue
		else:
			if start_index == 0:
				return None
			else:
				index = start_index+1
				start_index -= len(sentence[-1])
				sentence.pop()
				continue





if __name__ == '__main__':
	words = ['the', 'quick', 'brown', 'fox']
	string = "thequickbrownfox"
	print recursive_solution(words, string)

	words = ['bed', 'bedbath', 'and', 'beyond']
	string = "bedbathandbeyond"
	print dp_solution(words, string)

	words = ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa']
	string='aaaaaaaaaab'
	print dp_solution(words, string)