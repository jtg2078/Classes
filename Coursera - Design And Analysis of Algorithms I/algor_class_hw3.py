def update_graph(m, a_key, b_key):
	for k, v in m.items():
		if(k != b_key):
			for i in range(len(v)):
				if v[i] == a_key:
					v[i] = b_key
			m[k] = v

def contract(m, a_key, b_key):
	# a: to be eaten
	# b: the eater
	a = m[a_key]
	b = filter (lambda v: v != a_key, m[b_key])
	for v in a:
		if v != b_key:
			b.append(v)
	m[b_key] = b;
	del m[a_key]
	update_graph(m, a_key, b_key)

from random import randrange
def karger(m):
	while len(m) > 2:
		b_key = 0
		while True:
			b_key = randrange(1, 41)
			if b_key in m:
				break
		b = m[b_key]
		a_key = b[randrange(len(b))]
		contract(m, a_key, b_key)
	for k, v in m.items():
		return len(v)
	
import copy
def hw3():
	print 'Reading hw3 input file into list'
	with open('kargerAdj.txt', 'r') as f:
		m = {}
		for line in f:
			e = map(int, line.split())
			m[e[0]] = [e[v] for v in range(1,len(e))]
	print 'Done reading the input file: kargerAdj.txt'
	print '-----------'
	smallest = 40 * (40 - 1) / 2
	for i in range(100):
		m1 = copy.deepcopy(m)
		cut = karger(m1)
		if cut < smallest:
			smallest = cut
			print 'cut:', cut
			print 'm1:', m1
	print 'smallest cut:', smallest

hw3()


	