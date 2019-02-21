'''Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count 
the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not 
allowed.'''


def memoize(f):
	memo={}
	def cache(*args, **kwargs):
		if args[1] not in memo:
			memo[args[1]] = f(*args)
		return memo[args[1]]
	return cache

@memoize
def dp_helper(msg, num):

	if num  == 0:
		return 1

	v = len(msg) - num

	if msg[v] == '0':
		return 0

	res = dp_helper(msg, num-1)

	if num >= 2 and int(msg[v:v+2]) < 27:
		res += dp_helper(msg, num-2)

	return res


def find_max_encoded_msg(message):
	return dp_helper(message, len(message))


if __name__ == '__main__':
	print find_max_encoded_msg('10224')