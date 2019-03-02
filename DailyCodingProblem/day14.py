'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as (pie)r^2. Estimate pie to 3 decimal places 
using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

'''
import random

def monte_carlo():
	'''
	Wrapper function that iterates over the calc_pie function and reports
	back values of pie
	'''
	n = 1000000
	interval = 1000

	for value in calc_pie(n,interval):
		print 'Value of pie is {}'.format(value)



def calc_pie(n, interval):
	'''
	Formula for area of cicle = pie*r^2
	Formula of a circle is x^2+y^2=r^2

	So assuming a square of sides=2units centered at the origin (0,0).
	We now plot the biggest circle possible that can be inscribed within the
	circle.
	The radius of such a circle must be of diemension (side of circle)/2, this
	case of dimension 1 unit.
	We now randomly generate numbers in the range of -1 to 1 using random
	function. And check weather it liew within the circle of outside it.

	If we sample enough times we can fairly assume that the area of cicle can
	be given by the number of points we have generated that lie inside(or even
	on) the circle.
	Also since our range was -1 to 1 all points generated would definitely lie
	within or on the square.
	With simple mathamatics we can assume:
		area of circle             num of points within(or on) the circle
		--------------   =        -----------------------------------------
		are of square              num of points within(or on) the square

	We know in above case area of sqaure would be side^2 = 2^2 = 4
	Also r in above case reduces to 1, reducing RHS to pie/4

	So value of pie can be given by the formula:
						num of points within(or on) the circle
		pie   =   4 *  -----------------------------------------
		                num of points within(or on) the square
	'''
	circle_pt, square_pt = 0, 0

	for _ in range(n+1):
		x_pt = float(float(random.randint(-1000,1000))/1000)
		y_pt = float(float(random.randint(-1000,1000))/1000)
		if x_pt ** 2 + y_pt ** 2 <= 1:
			circle_pt += 1
		square_pt += 1

		#every inteval times we report back value of pie
		if n%interval == 0:
			yield (4*float(circle_pt)/square_pt)


if __name__ == '__main__':
	monte_carlo()
