def find_initial(r, t):
	r = r / 2
	if r * r > t:
		return find_initial(r, t)
	else:
		return r
		
def slow_inverse(f, delta=1/128.):
	"""Given a function y = f(x) that is a monotonically increasing function on
	non-negatve numbers, return the function x = f_1(y) that is an approximate
	inverse, picking the closest value to the inverse, within delta."""
	def f_1(y):
		x = 0
		while f(x) < y:
			x += delta
		# Now x is too big, x-delta is too small; pick the closest to y
		return x if (f(x)-y < y-f(x-delta)) else x-delta
	return f_1

def inverse(f, delta=1/128.):
	def f_1(y):
		# binary search to find the initial
		x = y / 2
		while f(x) > y:
			#print x
			x /= 2
		# newton method for close in
		x = float(x)
		while abs(f(x)-y) > delta:
			#print x
			x = x - (f(x) - y) / (2 * x)
		return x
	return f_1

def find_initial_it(t):
	r = t / 2
	while r * r > t:
		r /= 2
	return r
	
def square(x): 
	return x*x

		
import math
def test_find_initial():
	n = 1000000000
	print 'n:{0} math.sqrt:{1} find_initial:{2}'.format(n, math.sqrt(n), find_initial(n,n))
	print 'n:{0} math.sqrt:{1} find_initial_it:{2}'.format(n, math.sqrt(n), find_initial_it(n))
	sqrt = inverse(square)
	print 'n:{0} math.sqrt:{1} sqrt:{2}'.format(n, math.sqrt(n), sqrt(n))

test_find_initial()