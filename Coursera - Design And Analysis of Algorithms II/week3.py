def max_independent_set_problem():
	print '----- max independent set problem -----'
	w = [1,4,5,4]
	print 'vertices are: {0}'.format(w)
	a = find_max_is_weight(w)
	print 'max IS weight: {0}'.format(a[-1])
	s = find_max_is_set(w, a)
	print 'max IS: {0}'.format(s)

def find_max_is_weight(w):
	a = [0] * len(w)
	a[0] = 0
	a[1] = w[1]
	for i in range(2, len(w)):
		a[i] = max(a[i-1], a[i-2]+w[i])
	return a
		
def find_max_is_set(w, a):
	s = []
	i = len(a) - 1
	while i >= 1:
		if a[i-1] >= a[i-2] + w[i]:
			i = i - 1
		else:
			s.append(w[i])
			i = i - 2
	return s

max_independent_set_problem()

def knapsack_problem():
	print '----- knapsack problem -----'
	b = ['green','gray','yellow','blue', 'orange']
	v = [4,2,10,2,1]
	w = [12,1,4,2,1]
	c = 15
	print 'capacity:{0}'.format(c)
	print 'boxes:'
	for i in range(len(b)):
		print '{0} - ${1} - {2}kg'.format(b[i],v[i],w[i])
	a = find_optimal_knapsack(v,w,c)
	print 'maximum packing value: ${0}'.format(a[len(b)-1][c])
	

def find_optimal_knapsack(v,w,c):
	l = len(v)
	a = [[0 for x in range(c + 1)] for y in range(l)]
	for i in range(1,l):
		for x in range(c+1):
			a[i][x] = max(a[i-1][x], a[i-1][x-w[i]] + v[i] if x > w[i] else a[i-1][x])
	return a
		
	

knapsack_problem()

