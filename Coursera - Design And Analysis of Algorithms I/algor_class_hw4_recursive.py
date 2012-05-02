t = 0
leader = None

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
			
def dfs_recursive_reversed(s):
	global t
	s.explored = True
	for v in s.incoming:
		if v.explored == False:
			dfs_recursive_reversed(v)
	t = t + 1
	s.fscore = t

def dfs_loop_1st(g):
	global t
	t = 0
	for v in reversed(g.vertices):
		if v != None:
			if v.explored == False:
				dfs_recursive_reversed(v)
			
def dfs_recursive(s):
	global leader
	global t
	s.explored = True
	s.leader = leader
	s.leader.minions = s.leader.minions + 1
	for v in s.outgoing:
		if v.explored == False:
			dfs_recursive(v)

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
			v.label = v.fscore
	for v in reversed(order):
		if v != None:
			if v.explored == False:
				leader = v
				dfs_recursive(v)
				
def test():
	file_name = 'SCC_test.txt'
	num_vertex = 9
	g = construct_graph(file_name, num_vertex)
	dfs_loop_1st(g)
	dfs_loop_2nd(g)
	for v in g.vertices:
		if v != None:
			print 'label:{0} t:{1} explored:{2} leader:{3} leader minions:{4}'.format(v.label, v.fscore, v.explored, v.leader.label, v.leader.minions)

def kosaraju():
	file_name = 'SCC.txt'
	num_vertex = 875714
	g = construct_graph(file_name, num_vertex)
	print '--------------------------------'
	print 'finding top five largest SCCs...'
	dfs_loop_1st(g)
	dfs_loop_2nd(g)
	# filler is just to make the sort function works
	# because g.vertices[0] is not used
	filler = Vertex()
	g.vertices[0] = filler
	top_scc_s = sorted(g.vertices, key = lambda vertex: vertex.minions, reverse = True)
	for i in range(5):
		v = top_scc_s[i]
		print 'label:{0} t:{1} minions:{2}'.format(v.label, v.fscore, v.minions)


# with the recursive way, two parameters need to be adjusted:
# (because the DFS recursive method can go really deep here)
# the default python recursive limit is 1000, which is not enough for the hw problem set
# the default thread stack size is 1mb? which is also not enough for the hw problem set
# (got the following code from the course's forum)
import sys, thread, threading, time
sys.setrecursionlimit(100000) 
thread.stack_size(2**27)
t1 = threading.Thread(target = kosaraju, args = ())

begin = time.clock()
t1.start()      # start the scc thread
t1.join()       # and wait for it to finish
print time.clock() - begin


