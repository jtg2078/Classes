import sys
import string

def floyd_warshall_1(v,n):
	a = [[[999999 for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
	for i in range(1,n):
		a[i][i][0] = 0
	for i,j,cij in v:
		a[i][j][0] = cij
	for i in range(1,n):
		for j in range(1,n):
			print a[i][j] 
	print 'lalal'
	for k in range(1,n):
		for i in range(1,n):
			for j in range(1,n):
				case1 = a[i][j][k-1]
				case2 = a[i][k][k-1] + a[k][j][k-1]
				a[i][j][k] = min(case1, case2)
	return a

def floyd_warshall_2(v,n):
	n = n + 1 #realign n
	a = [["x" for i in range(n)] for j in range(n)]
	for i in range(1,n):
		a[i][i] = 0
	for i,j,cij in v:
		a[i][j] = cij
	for k in range(1,n):
		for i in range(1,n):
			for j in range(1,n):
				case1 = a[i][j]
				if type(a[i][k]) == int and type(a[k][j]) == int:
					case2 = a[i][k] + a[k][j]
				else:
					case2 = 'x'
				if type(case1) == int and type(case2) == int:
					a[i][j] = min(case1, case2)
				elif type(case1) == int:
					a[i][j] = case1
				else:
					a[i][j] = case2
	trim_a = [["x" for i in range(n-1)] for j in range(n-1)]
	for i in range(1,n):
		for j in range(1, n):
			trim_a[i-1][j-1] = a[i][j]
	return trim_a

def floyd_warshall_3(v,n):
	n = n + 1 #realign n
	a = [[None for i in range(n)] for j in range(n)]
	for i in range(1,n):
		a[i][i] = 0
	for i,j,cij in v:
		a[i][j] = cij
	print 'about to do triple nested loop'
	for k in xrange(1,n):
		for i in xrange(1,n):
			for j in xrange(1,n):
				case1 = a[i][j]
				if a[i][k] != None and a[k][j] != None:
					case2 = a[i][k] + a[k][j]
				else:
					case2 = None
				if case1 != None and case2 != None:
					a[i][j] = min(case1, case2)
				elif case1 != None:
					a[i][j] = case1
				else:
					a[i][j] = case2
	print 'done running triple nested loop'
	trim_a = [[None for i in range(n-1)] for j in range(n-1)]
	for i in range(1,n):
		for j in range(1, n):
			trim_a[i-1][j-1] = a[i][j]
	return trim_a

def floyd_warshall_4(v,n):
	n = n + 1 #realign n
	a = [[float('inf') for i in range(n)] for j in range(n)]
	for i in range(1,n):
		a[i][i] = 0
	for i,j,cij in v:
		a[i][j] = cij
	print 'about to do triple nested loop'
	for k in xrange(1,n):
		for i in xrange(1,n):
			for j in xrange(1,n):
				a[i][j] = min(a[i][j], a[i][k] + a[k][j])
	print 'done running triple nested loop'
	trim_a = [[None for i in range(n-1)] for j in range(n-1)]
	for i in range(1,n):
		for j in range(1, n):
			trim_a[i-1][j-1] = a[i][j]
	return trim_a


def check_negative_cycle(a):
	for i in range(len(a)):
		if a[i][i] < 0:
			return True
	return False
	
	
def search_shortest(a):
	# check for negative cycle
	if check_negative_cycle(a):
		return None
	else:
		shortest = sys.maxint
		for i in range(len(a)):
			for j in range(len(a)):
				if a[i][j] != None:
					shortest = min(shortest, a[i][j])
		return shortest

def load_data(filename, debug):
	if debug:
		print '----- loading file: {0} -----'.format(filename)
	num_vertex = 0
	num_edge = 0
	v = []
	with open(filename, 'r') as f:
		data = list(f.read().splitlines())
		for line in data:
			e = line.split()
			if num_edge == num_vertex == 0:
				num_vertex = int(e[0])
				num_edge = int(e[1])
			else:
				v.append((int(e[0]), int(e[1]), int(e[2])))
	if debug:
		print '----- done reading the file -----'
	if debug:
		print '{0} {1}'.format(num_vertex, num_edge)
		for i,j,cij in v:
			print '{0} {1} {2}'.format(i,j,cij)
	return (num_vertex, num_edge, v)
	
def run_test1():
	debug = True
	n,_,v = load_data('test1.txt', debug)
	a = floyd_warshall_2(v, n)
	for i in range(1,n):
		print a[i]

def run_test2():
	debug = True
	n,_,v = load_data('test2.txt', debug)
	a = floyd_warshall_2(v, n)
	if debug:
		print '----- matrix a -----'
		print "\n".join(["\t".join(map(str, r)) for r in a])
	print 'shortest path: {0}'.format(search_shortest(a))

def run_test3():
	debug = False
	n,_,v = load_data('test3.txt', debug)
	a = floyd_warshall_2(v, n)
	if debug:
		print '----- matrix a -----'
		print "\n".join(["\t".join(map(str, r)) for r in a])
	print 'shortest path for test3.txt: {0}'.format(search_shortest(a))
	
def run_test(file, debug):
	n,_,v = load_data(file, debug)
	a = floyd_warshall_2(v, n)
	if debug:
		print '----- matrix a -----'
		print "\n".join(["\t".join(map(str, r)) for r in a])
	print 'shortest path for {0}: {1}'.format(file, search_shortest(a))

def run_test2(file, debug):
	n,_,v = load_data(file, debug)
	a = floyd_warshall_4(v, n)
	if debug:
		print '----- matrix a -----'
		print "\n".join(["\t".join(map(str, r)) for r in a])
	print 'shortest path for {0}: {1}'.format(file, search_shortest(a))
	

run_test2('g1.txt', False)
run_test2('g2.txt', False)
run_test2('g3.txt', False)
		
