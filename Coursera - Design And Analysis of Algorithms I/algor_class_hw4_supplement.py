t = 0
leader = None
import sys
import resource
 
# Increase max stack size from 8MB to 512MB
#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
#sys.setrecursionlimit(10**6)

class Vertex:
	def __init__(self):
		self.outgoing = []
		self.incoming = []
		self.label = -1
		self.explored = False
		self.leader = None
		self.fscore = -1
		self.minions = 0
	def description(self):
		outs = []
		for v in self.outgoing:
			outs.append(str(v.label))
			outs.append(' ')
		ins = []
		for v in self.incoming:
			ins.append(str(v.label))
			ins.append(' ')
		return '\nlabel: ' + str(self.label) + '\noutgoing: ' + ''.join(outs) + '\nincoming: ' + ''.join(ins)
		
class Graph:
	def __init__(self, vertex_count):
		self.vertices = [None] * (vertex_count + 1)
	def add_edge(self, vf, vt):
		from_vertex = self.vertices[vf]
		to_vertex = self.vertices[vt]
		# create from vertex if it hasnt been initialized yet
		if from_vertex == None:
			from_vertex = Vertex()
			from_vertex.label = vf
			self.vertices[vf] = from_vertex
		# create to vertex if it hasnt been initialized yet
		if to_vertex == None:
			to_vertex = Vertex()
			to_vertex.label = vt
			self.vertices[vt] = to_vertex
		# setting up each vertex's from and to
		from_vertex.outgoing.append(to_vertex)
		to_vertex.incoming.append(from_vertex)

def construct_graph(file_name, num_of_vertex):
	print 'Reading hw4 input file {0} into Graph Object'.format(file_name)
	g = Graph(num_of_vertex)
	with open(file_name, 'r') as f:
		for line in f:
			tokens = line.split()
			fromvertex = int(tokens[0])
			tovertex =  int(tokens[1])
			g.add_edge(fromvertex, tovertex)
	print 'Done reading the input file: ', file_name
	return g

def dfs_stack(s):
	stack = []
	stack.append(s)
	while len(stack) > 0:
		v = stack.pop()
		if(v.explored == False):
			v.explored = True
			print v.label
			for next in reversed(v.outgoing):
				stack.append(next)
				
def dfs_stack_reversed(s):
	stack = []
	stack.append(s)
	while len(stack) > 0:
		v = stack.pop()
		if(v.explored == False):
			v.explored = True
			print v.label
			for next in reversed(v.incoming):
				stack.append(next)
		else:
			print '-- backtracked? {0}'.format(v.label)

def dfs_stack_reversed_order(s):
	stack = []
	stack.append(s)
	order = []
	while len(stack) > 0:
		v = stack.pop()
		if(v.explored == False):
			v.explored = True
			for next in reversed(v.incoming):
				stack.append(next)
			

def dfs_recursive_reversed(s):
	global t
	s.explored = True
	for v in s.incoming:
		if v.explored == False:
			dfs_recursive_reversed(v)
	t = t + 1
	s.fscore = t



def test():
	file_name = 'SCC_test.txt'
	num_vertex = 9
	g = construct_graph(file_name, num_vertex)
	dfs_stack_reversed(g.vertices[num_vertex])

def test2():
	file_name = 'SCC.txt'
	num_vertex = 875714
	g = construct_graph(file_name, num_vertex)
	dfs_stack_reversed(g.vertices[3])

def test3():
	file_name = 'SCC.txt'
	num_vertex = 875714
	g = construct_graph(file_name, num_vertex)
	dfs_recursive_reversed(g.vertices[3])
	
def dfs_loop_1st(g):
	global t
	t = 0
	for v in reversed(g.vertices):
		if v != None:
			if v.explored == False:
				dfs_recursive_reversed(v)
			


def dfs_loop_2nd(g):
	# construct a dictionary of vertices which the key is
	# the vertex's fscore
	global leader
	global t
	leader = None
	order = [None] * (len(g.vertices) + 1)
	for v in g.vertices:
		if v != None:
			v.explored = False
			order[v.fscore] = v
	for v in reversed(order):
		if v != None:
			if v.explored == False:
				leader = v
				dfs_recursive(v)

def dfs_recursive(s):
	global leader
	global t
	s.explored = True
	s.leader = leader
	s.leader.minions = s.leader.minions + 1
	for v in s.outgoing:
		if v.explored == False:
			dfs_recursive(v)				

			
def kosaraju():
	file_name = 'SCC.txt'
	num_vertex = 875714
	#file_name = 'SCC_test.txt'
	#num_vertex = 9
	g = construct_graph(file_name, num_vertex)
	dfs_loop_1st(g)
	dfs_loop_2nd(g)
	filler = Vertex()
	g.vertices[0] = filler
	#for v in g.vertices:
	#	if v.leader == None:
	#		print 'label:{0} has no leader'.format(v.label)
	#	else:
	#		print 'label:{0} leader:{1} t:{2}'.format(v.label, v.leader.label, v.fscore, v.minions)
	#print '-------------------------'
	#max = 0
	#for v in g.vertices:
	#	if v == None:
	#		print 'found None in g.vertices'
	#	else:
	#		if v.minions > max:
	#			max = v.minions
	#print max
			
	
	
	top_scc_s = sorted(g.vertices, key = lambda vertex: vertex.minions, reverse = True)
	for i in range(5):
		v = top_scc_s[i]
		print 'label:{0} t:{1} minions:{2}'.format(v.label, v.fscore, v.minions)


import sys, thread, threading, time
sys.setrecursionlimit(100000)   # don't know what I actually needed here
thread.stack_size(2**27)      # largest power of 2 that didn't give me an error, don't know what I needed
t1 = threading.Thread( target = kosaraju, args = () )   #  creates a thread to call my function   scc(graph)

begin = time.clock()
t1.start()      # start the scc thread
t1.join()       # and wait for it to finish
print time.clock() - begin

# correct answer is 434821,968,459,313,211


class Vertex:
	def __init__(self):
		self.outgoing = []
		self.incoming = []
		self.label = -1
		self.visited = False
		self.leader = None
		self.fscore = -1
		self.minions = 0
	def description(self):
		outs = []
		for v in self.outgoing:
			outs.append(str(v.label))
			outs.append(' ')
		ins = []
		for v in self.incoming:
			ins.append(str(v.label))
			ins.append(' ')
		return '\nlabel: ' + str(self.label) + '\noutgoing: ' + ''.join(outs) + '\nincoming: ' + ''.join(ins)
	
class Edge:
	def __init__(self):
		self.fromvertex = None
		self.tovertex = None

class Graph:
	def __init__(self):
		self.vertices = {}
		self.edges = []
	def mark_all_unvisited(self):
		for e in self.edges:
			e.fromvertex.visited = False
			e.tovertex.visited = False
	def add_edge(self, vf, vt):
		from_vertex = None
		to_vertex = None
		# getting or creating from vertex
		if vf in self.vertices:
			from_vertex = self.vertices[vf]
		else:
			from_vertex = Vertex()
			from_vertex.label = vf
			self.vertices[vf] = from_vertex
		# getting for creating to vertex
		if vt in self.vertices:
			to_vertex = self.vertices[vt]
		else:
			to_vertex = Vertex()
			to_vertex.label = vt
			self.vertices[vt] = to_vertex
		# setting to/from attributes
		from_vertex.outgoing.append(to_vertex)
		to_vertex.incoming.append(from_vertex)
		# creating and adding the edge to Graph
		edge = Edge()
		edge.fromvertex = from_vertex
		edge.tovertex = to_vertex
		self.edges.append(edge)
		
def construct_graph(file_name):
	print 'Reading hw4 input file {0} into Graph Object'.format(file_name)
	g = Graph()
	with open(file_name, 'r') as f:
		for line in f:
			tokens = line.split()
			fromvertex = int(tokens[0])
			tovertex =  int(tokens[1])
			g.add_edge(fromvertex, tovertex)
			#e = map(int, line.split())
			# e is an edge e[0]: from  e[1]: to
			#g.add_edge(e[0], e[1])
	print 'Done reading the input file: ', file_name
	print '-----------'
	print 'printing input file content:'
	#for key in g.vertices:
	#	print 'key:{0} vertex:{1}'.format(key, g.vertices[key].description())
	#for edge in g.edges:
	#	print '[{0}, {1}]'.format(edge.fromvertex.label, edge.tovertex.label)
	print '-----------'
	return g

from collections import deque
def bfs(g, s, reset_state):
	if reset_state == True:
		g.mark_all_unvisited()
	s.visited = True
	queue = deque()
	queue.append(s)
	while len(queue) > 0:
		v = queue.popleft()
		print 'just visited: ', v.label
		for w in v.outgoing:
			if w.visited == False:
				w.visited = True
				queue.append(w)

def dfs(g, s, reset_state, reverse, count_minions):
	global t
	global leader
	if reset_state == True:
		g.mark_all_unvisited()
	s.visited = True
	s.leader = leader
	if count_minions == True:
		leader.minions = leader.minions + 1
	stack = []
	stack.append(s)
	while len(stack) > 0:
		v = stack.pop()
		v.visited = True
		v.leader = leader
		if count_minions == True:
			leader.minions = leader.minions + 1
		print 'just visited: ', v.label
		edges = v.outgoing
		if reverse == True:
			edges = v.incoming
		end = True
		for w in edges:
			if w.visited == False:
				end = False
				stack.append(w)
		#if end == True:
		#	t = t + 1
		#	v.fscore = t

def dfs_1st(g, s):
	global t
	global leader
	s.visited = True
	s.leader = leader
	for v in s.incoming:
		if v.visited == False:
			dfs_1st(g, v)
	t = t + 1
	s.fscore = t

def dfs_2nd(g, s):
	global t
	global leader
	s.visited = True
	s.leader = leader
	leader.minions = leader.minions + 1
	for v in s.outgoing:
		if v.visited == False:
			dfs_2nd(g, v)

def dfs_2nd_ex(g, s):
	global t
	global leader
	stack = []
	stack.append(s)
	while len(stack) > 0:
		v = stack.pop()
		v.visited = True
		v.leader = leader
		leader.minions = leader.minions + 1
		for w in v.outgoing:
			if w.visited == False:
				stack.append(w)

				
t = 0
leader = None
def dfs_loop_1st(g):
	global t
	global leader
	t = 0
	leader = None
	# since the input for this problem is well defined
	# so lets just take the assumption
	for i in range(len(g.vertices), 0, -1):
		v = g.vertices[i]
		if v.visited == False:
			leader = v
			#dfs(g, v, False, True, False)
			dfs_1st(g, v)
			


def dfs_loop_2nd(g):
	# construct a dictionary of vertices which the key is
	# the vertex's fscore
	global t
	global leader
	t = 0
	leader = None
	fscore_dict = {}
	for i in range(1, len(g.vertices) + 1, 1):
		v = g.vertices[i]
		v.visited = False
		v.label = v.fscore
		fscore_dict[v.fscore] = v
	for i in range(len(g.vertices), 0, -1):
		v = fscore_dict[i]
		#print '2nd loop processed label:{0} f:{1}'.format(v.label, v.fscore)
		if v.visited == False:
			leader = v
			#dfs(g, v, False, True, True)
			#dfs_2nd(g, v)
			dfs_2nd_ex(g,v)
			
def kosaraju(g):
	dfs_loop_1st(g)
	#for k,v in g.vertices.items():
	#		print 'label:{0} leader:{1} t:{2}'.format(k, v.leader.label, v.fscore)
	#print '-------------------------'
	dfs_loop_2nd(g)
	top_scc_s = sorted(g.vertices.itervalues(), key = lambda vertex: vertex.minions, reverse = True)
	for i in range(5):
		v = top_scc_s[i]
		print 'label:{0} leader:{1} t:{2} minions:{3}'.format(v.label, v.leader.label, v.fscore, v.minions)
	
	#for k,v in g.vertices.items():
	#	print 'label:{0} leader:{1} t:{2} minions:{3}'.format(k, v.leader.label, v.fscore, v.minions)
	
	
	
def hw4():
	file_name = 'SCC_test.txt'
	#file_name = 'SCC.txt'
	g = construct_graph(file_name)
	#print '---- Breath first search ----'
	#for s in g.vertices.keys():
	#	print 'starting from: ', s
	#	bfs(g, g.vertices[s], True)
	#print '---- Depth first search ----'
	#for s in g.vertices.keys():
	#	print 'starting from: ', s
	#	dfs(g, g.vertices[s], False, False, False)
	kosaraju(g)

hw4()

	

