'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 
steps at a time. Given N, write a function that returns the number of unique 
ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could 
climb any number from a set of positive integers X? For example, 
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''

def get_unique_ways(allowed_steps, n):

	combinations = set()

	#iteratively look for all solutions
	_combinations(allowed_steps, n, 0, (), combinations)

	print 'Combinations are:'
	for i in combinations: print i

def _combinations(allowed_steps, n, s, temp_comb, combinations):

	for step in allowed_steps:
		if s + step > n:
			continue
		elif s + step == n:
			combinations.add(temp_comb+(step,))
		else:
			temp_comb
			_combinations(allowed_steps, n, s+step, temp_comb+(step,), 
						  combinations)
	return


def get_number_of_ways(allowed_steps, n):
	cache = [0]*(n+1)
	cache[0]=0

	for i in range(n+1):
		cache[i] += sum(cache[i-x] for x in allowed_steps if i-x > 0)
		cache[i] += 1 if i in allowed_steps else 0

	return cache[-1]

if __name__ == '__main__':
	n=10
	allowed_steps=[3,4,5,2]
	get_unique_ways(allowed_steps, n)
	print get_number_of_ways(allowed_steps,n)