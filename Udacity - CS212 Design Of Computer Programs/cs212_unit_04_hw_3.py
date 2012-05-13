# -----------------
# User Instructions
# 
# Write a function, subway, that takes lines as input (read more about
# the **lines notation in the instructor comments box below) and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... } 
#
# For example, when calling subway(boston), one of the entries in the 
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}. 
# This means that foresthills only has one neighbor ('backbay') and 
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# Once you've defined your subway function, you can define a ride and 
# longest_ride function. ride(here, there, system) takes as input 
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given 
# subway system. 

# -------------
# Grading Notes
#
# The subway() function will not be tested directly, only ride() and 
# longest_ride() will be explicitly tested. If your code passes the 
# assert statements in test_ride(), it should be marked correct.


def find_neighbors(lines, lines_name, station_line, station_name):
	n = {}
	i = 0
	for line in lines:
		for station in line:
			if station == station_name:
				j = line.index(station)
				if j == 0:
					next_s = line[j + 1]
					n[next_s] = lines_name[i]
				elif j == len(line) - 1:
					prev_s = line[j - 1]
					n[prev_s] = lines_name[i]
				else:
					next_s = line[j + 1]
					n[next_s] = lines_name[i]
					prev_s = line[j - 1]
					n[prev_s] = lines_name[i]
		i += 1
	return n


def subway(**lines):
	"""Define a subway map. Input is subway(linename='station1 station2...'...).
	Convert that and return a dict of the form: {station:{neighbor:line,...},...}"""
	## your code here
	blue = lines['blue'].split()
	orange = lines['orange'].split()
	green = lines['green'].split()
	red = lines['red'].split()
	lines = [blue, orange, green, red]
	lines_name = ['blue', 'orange', 'green', 'red']
	map={}
	for line in lines:
		for station in line:
			map[station] = find_neighbors(lines, lines_name, line, station)
	return map
		

boston = subway(
	blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
	orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
	green='lechmere science north haymarket government park copley kenmore newton riverside',
	red='alewife davis porter harvard central mit charles park downtown south umass mattapan')


def ride(here, there, system=boston):
	"Return a path on the subway system from here to there."
	## your code here
	def successors(state):
		path = system[state]
		return path
	def is_goal(state, path = None):
		return state == there
	return shortest_path_search(here, successors, is_goal)
	
		
def longest_ride(system):
	"""Return the longest possible shortest path 
	ride between any two stops in the system."""
	## your code here
	paths = []
	def successors(state):
		path = system[state]
		return path
	def is_goal(state, path = None):
		return state == there
	for here in system.keys():
		for there in system.keys():
			path = shortest_path_search(here, successors, is_goal)
			paths.append(path)
	paths.sort(key = lambda path: len(path), reverse = True)
	return paths[0]


def longest_ride_between_two_station(here, there, system=boston):
	"""Return the longest possible shortest path 
	ride between any two stops in the system."""
	## your code here
	# oh, oh, oh oh, find the longest path, oh oh oh~
	paths = []
	def successors(state):
		path = system[state]
		return path
	def is_goal(state, path):
		if state == there:
			paths.append(path)
		return False
	shortest_path_search(here, successors, is_goal)
	paths.sort(key = lambda path: len(path), reverse=True)
	return paths[0]
	
	
def shortest_path_search(start, successors, is_goal):
	"""Find the shortest path from start state to a state
	such that is_goal(state) is true."""
	if is_goal(start):
		return [start]
	explored = set() # set of states we have visited
	frontier = [ [start] ] # ordered list of paths we have blazed
	while frontier:
		path = frontier.pop(0)
		s = path[-1]
		for (state, action) in successors(s).items():
			if state not in explored:
				explored.add(state)
				path2 = path + [action, state]
				if is_goal(state):
					return path2
				else:
					frontier.append(path2)
	return []

def path_states(path):
	"Return a list of states in this path."
	return path[0::2]
	
def path_actions(path):
	"Return a list of actions in this path."
	return path[1::2]

def test_ride():
	assert ride('mit', 'government') == [
		'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
	assert ride('mattapan', 'foresthills') == [
		'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
		'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
	assert ride('newton', 'alewife') == [
		'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
		'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
	assert (path_states(longest_ride(boston)) == [
		'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
		'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or 
		path_states(longest_ride(boston)) == [
				'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles', 
				'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
	assert len(path_states(longest_ride(boston))) == 16
	return 'test_ride passes'

print test_ride()


def my_test():
	blue = 'bowdoin government state aquarium maverick airport suffolk revere wonderland'.split()
	orange = 'oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills'.split()
	green = 'lechmere science north haymarket government park copley kenmore newton riverside'.split()
	red = 'alewife davis porter harvard central mit charles park downtown south umass mattapan'.split()
	lines = [blue, orange, green, red]
	lines_name = ['blue', 'orange', 'green', 'red']
	assert find_neighbors(lines, lines_name, 'orange', 'oakgrove') == {'sullivan':'orange'}
	assert find_neighbors(lines, lines_name, 'green', 'park') == {'downtown': 'red', 'charles': 'red', 'copley': 'green', 'government': 'green'}
	assert find_neighbors(lines, lines_name, 'red', 'mattapan') == {'umass': 'red'}
	print 'my_test all tests passed'

	