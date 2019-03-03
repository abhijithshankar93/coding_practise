'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
'''
import random


def random_sampling(stream):
	'''
	Wrapper function that takes in a stream and calls the reservoir sampling
	function with a set number of sample size
	'''
	sample_size = 1
	print 'The random sample picked was {}'.format(reservoir_sampling(stream, 
																sample_size))

def reservoir_sampling(stream, sample_size):
	random_samples = [0]*sample_size

	for index, value in enumerate(stream):
		if index < sample_size:
			random_samples[index] = value
		else:
			random_value = random.randint(0, index)
			if random_value < sample_size:
				random_samples[random_value] = value

	return random_samples


if __name__ == '__main__':
	stream = [1,2,3,4,5,6,7,8,8,10,11,12,13,14,15,16,17,18,19,20,21,22]
	random_sampling(stream)