'''Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular 
expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your 
function should return true. The same regular expression on the string 
"raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function 
should return true. The same regular expression on the string "chats" should 
return false.
'''

def reg_ex(string,pattern):

	#Bottom up aproach

	#1.Create a 2D list of size len(pattern)+1 X len(string)+1
	dp = [[False]*(len(pattern)+1) for _ in range(len(string)+1)]

	dp[0][0] = True
	#2.Fill the 2D list
	for i in range(0, len(string)+1):
		for j in range(1, len(pattern)+1):
			if i == 0:
				if j>0 and pattern[j-1]=='*':
					dp[i][j] = dp[i][j-2]
			else:
				if pattern[j-1] in {string[i-1], '.'}:
					dp[i][j]=dp[i-1][j-1]
				if j>1 and pattern[j-1]=='*':
					dp[i][j] = dp[i][j-2]
					if pattern[j-2] in {string[i-1], '.'}:
						dp[i][j] = dp[i][j] or dp[i-1][j]
	return dp[-1][-1]


if __name__ == '__main__':
	assert reg_ex("aa","a*") == True, 'Test1 failed'
	assert reg_ex("aaa","ab*a*c*a") == True, 'Test2 failed'
	assert reg_ex(".*at","chats") == False, 'Test3 failed'
	print 'All tests have passed!!'
