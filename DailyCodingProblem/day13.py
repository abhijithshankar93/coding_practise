'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k 
distinct characters is "bcb".
'''

def longest_substring(s, k):
	'''
	Moving window concept. 
	We keep adding elements of word into the window, until the number of unique
	elements in the list is no longer lesser than k.

	Then, if num of unique char is equal to k, then we check if its the max 
	size that we have found so far; if yes, then we update our max substring 
	and continue adding elements to the temporary substring
	
	At any point if we find that the number of unique char are more than k, we
	start removing elements from the begining of the temporary array.

	This was we keep moving the window until the end_pointer reaches the end of
	the list   
	'''
	max_len = 0
	max_subs = []
	temp = []
	end_index = 0

	while end_index < len(s):
		if len(set(temp)) < k:
			temp.append(word[end_index])
			end_index += 1
		elif len(set(temp)) > k:
			temp.pop(0)
		else:
			if len(temp) > max_len:
				max_len = len(temp)
				# we cant just do max_subs = temp as it will sync with temp and
				# any changes in temp will reflect back on max_subs
				max_subs = []	
				max_subs.extend(temp)
			temp.append(word[end_index])
			end_index += 1


	return max_subs


if __name__ == '__main__':
	word = 'abcba'
	k = 2
	print longest_substring(word, k)