def knapsack_problem_1():
	print '----- knapsack problem one -----'
	file = 'hw3_input_knapsack1.txt'
	print 'Reading input file: {0}'.format(file)
	with open(file, 'r') as f:
		m = list(f.read().splitlines())
	print 'done reading the input file: {0}'.format(file)
	print 'num of element in list m:', len(m)
	s = 0
	c = 0
	v = []
	w = []
	index = 0
	for l in m:
		elements = l.split()
		a = int(elements[0])
		b = int(elements[1])
		if index == 0:
			c = a
			s = b
		else:
			v.append(a)
			w.append(b)
		index = index + 1
	print 'capacity: {0}'.format(c)
	print 'num items:{0}'.format(s)
	print 'items:'
	for i in range(len(v)):
		print '{0}. ${1} - {2}kg'.format(i, v[i],w[i])
	a = find_optimal_knapsack_linear(v,w,c)
	print 'maximum packing value: ${0}'.format(a[len(v)-1][c])
	print 'now trying 2nd implementation'
	a = {}
	a[(0,0)] = 0
	ans = find_optimal_knapsack_recursive(a,v,w,len(v) - 1, c)
	print 'done 2nd'
	print 'maximum packing value: ${0}'.format(ans)

def knapsack_problem_2():
	print '----- knapsack problem two -----'
	file = 'hw3_input_knapsack2.txt'
	print 'Reading input file: {0}'.format(file)
	with open(file, 'r') as f:
		m = list(f.read().splitlines())
	print 'done reading the input file: {0}'.format(file)
	print 'num of element in list m:', len(m)
	s = 0
	c = 0
	v = []
	w = []
	index = 0
	for l in m:
		elements = l.split()
		a = int(elements[0])
		b = int(elements[1])
		if index == 0:
			c = a
			s = b
		else:
			v.append(a)
			w.append(b)
		index = index + 1
	print 'capacity: {0}'.format(c)
	print 'num items:{0}'.format(s)
	print 'items:'
	for i in range(len(v)):
		print '{0}. ${1} - {2}kg'.format(i, v[i],w[i])
	a = {}
	a[(0,0)] = 0
	ans = find_optimal_knapsack_recursive(a,v,w,len(v) - 1, c)
	print 'done 2nd'
	print 'maximum packing value: ${0}'.format(ans)

def find_optimal_knapsack_linear(v,w,c):
	l = len(v)
	a = [[0 for x in range(c + 1)] for y in range(l)]
	for i in range(1,l):
		for x in range(c+1):
			a[i][x] = max(a[i-1][x], a[i-1][x-w[i]] + v[i] if x > w[i] else a[i-1][x])
	return a

def find_optimal_knapsack_recursive(m,v,w,i,c):
	if i == 0:
		return 0
	# case 1
	key = (i-1,c)
	if key not in m:
		m[key] = find_optimal_knapsack_recursive(m,v,w,i-1,c)
	case1 = m[key]
	# case 2
	if w[i] > c:
		case2 = case1
	else:
		key = (i-1,c-w[i])
		if key not in m:
			m[key] = find_optimal_knapsack_recursive(m,v,w,i-1,c-w[i])
		case2 = m[key] + v[i]
	# compare
	m[(i,c)] = max(case1, case2)
	return m[(i,c)]

knapsack_problem_1() #maximum packing value: $2493893
knapsack_problem_2()