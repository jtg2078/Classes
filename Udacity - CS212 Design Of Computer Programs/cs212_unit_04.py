# week 4 ---------------------------------

# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
	"""Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the 'light', and t is a number indicating the elapsed time. Action is represented
	as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
	'<-' for there to here."""
	here, there, t = state
	# your code here 
	dict  = {}
	# from here to there
	for p1 in here:
		if p1 == 'light': continue
		for p2 in here:
			if p2 == 'light': continue
			new_t = max(p1, p2) + t
			new_here = set(here)
			new_here.remove(p1)
			if p1 is not p2: new_here.remove(p2)
			new_here.remove('light')
			new_there = set(there)
			new_there.add(p1)
			if p1 is not p2: new_there.add(p2)
			new_there.add('light')
			dict[(frozenset(new_here), frozenset(new_there), new_t)] = (p1, p2, '->')
	# from there to here
	for p1 in there:
		if p1 == 'light': continue
		for p2 in there:
			if p2 == 'light': continue
			new_t = max(p1, p2) + t
			new_there = set(there)
			new_there.remove(p1)
			if p1 is not p2: new_there.remove(p2)
			new_there.remove('light')
			new_here = set(here)
			new_here.add(p1)
			if p1 is not p2: new_here.add(p2)
			new_here.add('light')
			dict[(frozenset(new_here), frozenset(new_there), new_t)] = (p1, p2, '<-')
	# we're all done
	return dict

def bsuccessors_prof_version(state):
	here, there, t = state
	result = {}
	if 'light' in here:
		result = dict(((here - frozenset([p1, p2, 'light']), there | frozenset([p1, p2, 'light']), t + max(p1, p2)), (p1, p2, '->')) for p1 in here if p1 is not 'light' for p2 in here if p2 is not 'light')
	else:
		result = dict(((here | frozenset([p1, p2, 'light']), there - frozenset([p1, p2, 'light']), t + max(p1, p2)), (p1, p2, '<-')) for p1 in there if p1 is not 'light' for p2 in there if p2 is not 'light')
	return result
		
def unit_8_bridge_successors():

	assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
				(frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

	assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
				(frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
				
	assert bsuccessors_prof_version((frozenset([1, 'light']), frozenset([]), 3)) == {
					(frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

	assert bsuccessors_prof_version((frozenset([]), frozenset([2, 'light']), 0)) =={
				(frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
	
	print 'unit_8_bridge_successors all tests passed'

unit_8_bridge_successors()

# ----------------
# User Instructions
#
# Write two functions, path_states and path_actions. Each of these
# functions should take a path as input. Remember that a path is a 
# list of [state, action, state, action, ... ]
# 
# path_states should return a list of the states. in a path, and 
# path_actions should return a list of the actions.

def path_states(path):
	"Return a list of states in this path."
	states =  [state for state in path if isinstance(state[0], frozenset)]
	return states

def path_actions(path):
	"Return a list of actions in this path."
	actions = [action for action in path if isinstance(action[2], str)]
	return actions
	
def path_states_prof_version(path): #orz... wtf am i doing...
	"Return a list of states in this path."
	return path[::2]

def path_actions_prof_version(path): 
	"Return a list of actions in this path."
	return path[1::2]

def unit_9_paths_actions_states():
	testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
				(5, 2, '->'),										# action 1
				(frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
				(2, 1, '->'),										# action 2
				(frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
				(5, 5, '->'), 
				(frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
				(5, 10, '->'), 
				(frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
				(2, 2, '->'), 
				(frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
				(10, 1, '->'), 
				(frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
				(10, 10, '->'), 
				(frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
				(10, 2, '->'), 
				(frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
				(5, 1, '->'), 
				(frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
				(1, 1, '->')]
	assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
				(frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
				(frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
				(frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
				(frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
				(frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
				(frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
				(frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
				(frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
				(frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
	assert path_actions(testpath) == [(5, 2, '->'), # action 1
									  (2, 1, '->'), # action 2
									  (5, 5, '->'), 
									  (5, 10, '->'), 
									  (2, 2, '->'), 
									  (10, 1, '->'), 
									  (10, 10, '->'), 
									  (10, 2, '->'), 
									  (5, 1, '->'), 
									  (1, 1, '->')]
	assert path_states_prof_version(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
					(frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
					(frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
					(frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
					(frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
					(frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
					(frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
					(frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
					(frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
					(frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
	assert path_actions_prof_version(testpath) == [(5, 2, '->'), # action 1
									  (2, 1, '->'), # action 2
									  (5, 5, '->'), 
									  (5, 10, '->'), 
									  (2, 2, '->'), 
									  (10, 1, '->'), 
									  (10, 10, '->'), 
									  (10, 2, '->'), 
									  (5, 1, '->'), 
									  (1, 1, '->')]
	
	print 'unit_9_paths_actions_states all tests passed' 

unit_9_paths_actions_states()

# -----------------
# User Instructions
# 
# Modify the bridge_problem(here) function so that it 
# tests for goal later: after pulling a state off the 
# frontier, not when we are about to put it on the 
# frontier. 

def bsuccessors(state):
	"""Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the light, and t is a number indicating the elapsed time."""
	here, there, t = state
	if 'light' in here:
		return dict(((here  - frozenset([a,b, 'light']),
					  there | frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '->'))
					for a in here if a is not 'light'
					for b in here if b is not 'light')
	else:
		return dict(((here  | frozenset([a,b, 'light']),
					  there - frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '<-'))
					for a in there if a is not 'light'
					for b in there if b is not 'light')
		
def elapsed_time(path):
	return path[-1][2]

def bridge_problem(here):
	"""Modify this to test for goal later: after pulling a state off frontier,
	not when we are about to put it on the frontier."""
	## modify code below
	here = frozenset(here) | frozenset(['light'])
	explored = set() # set of states we have visited
	# State will be a (people-here, people-there, time-elapsed)
	frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
	if not here:
		return frontier[0]
	while frontier:
		path = frontier.pop(0)
		# check the goal state here
		here = path[-1][0]
		if not here or here == set(['light']):
			return path
		for (state, action) in bsuccessors(path[-1]).items():
			if state not in explored:
				here, there, t = state
				explored.add(state)
				path2 = path + [action, state]
				frontier.append(path2)
				frontier.sort(key=elapsed_time)
	return []

def unit_14_modify_code():
	assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2 # the [-1][-1] grabs the total elapsed time
	assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17
	print 'unit_14_modify_code all tests passed'

unit_14_modify_code()

# -----------------
# User Instructions
# 
# Add a few new test cases to begin familiarizing yourself 
# with doctest. 


import doctest

def bsuccessors(state):
	"""Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the light, and t is a number indicating the elapsed time."""
	here, there, t = state
	if 'light' in here:
		return dict(((here  - frozenset([a,b, 'light']),
					 there | frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '->'))
					for a in here if a is not 'light'
					for b in here if b is not 'light')
	else:
		return dict(((here  | frozenset([a,b, 'light']),
					  there - frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '<-'))
					for a in there if a is not 'light'
					for b in there if b is not 'light')  
		
def elapsed_time(path):
	return path[-1][2]

def bridge_problem(here):
	"Find the fastest (least elapsed time) path to the goal in the bridge problem."
	here = frozenset(here) | frozenset(['light'])
	explored = set() # set of states we have visited
	# State will be a (peoplelight_here, peoplelight_there, time_elapsed)
	# E.g. ({1, 2, 5, 10, 'light'}, {}, 0)
	frontier = [ [(here, frozenset(), 0)] ] # ordered list of paths we have blazed
	while frontier:
		path = frontier.pop(0)
		here1, there1, t1 = state1 = path[-1]
		if not here1 or here1 == set(['light']):  ## Check for solution when we pull best path off frontier
			return path
		for (state, action) in bsuccessors(state1).items():
			if state not in explored:
				here, there, t = state
				explored.add(state)
				path2 = path + [action, state]
				# Don't check for solution when we extend a path
				frontier.append(path2)
				frontier.sort(key=elapsed_time)
	return Fail

def path_states(path):
	"Return a list of states in this path."
	return path[0::2]
	
def path_actions(path):
	"Return a list of actions in this path."
	return path[1::2]

class TestBridge: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (1, 2, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

>>> path_actions(bridge_problem([1,2,11,19,26,30]))
[(2, 1, '->'), (1, 1, '<-'), (11, 19, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (30, 26, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,3,4]))
[(2, 1, '->'), (1, 1, '<-'), (3, 1, '->'), (1, 1, '<-'), (4, 1, '->')]

"""

def unit_15_adding_tests():
	#print doctest.testmod()
	print 'unit_15_adding_tests all tests passed'
	
unit_15_adding_tests()

# -----------------
# User Instructions
# 
# write a function, bsuccessors2 that takes a state as input
# and returns a dictionary of {state:action} pairs.
# 
# The new representation for a path should be a list of 
# [state, (action, total time), state, ... , ], though this 
# function will just return {state:action} pairs and will
# ignore total time. 
#
# The previous bsuccessors function is included for your reference.

def bsuccessors2(state):
	"""Return a dict of {state:action} pairs. A state is a
	(here, there) tuple, where here and there are frozensets
	of people (indicated by their travel times) and/or the light."""
	# your code here
	here, there = state
	if 'light' in here:
		return dict(((here  - frozenset([p1,p2, 'light']), there | frozenset([p1, p2, 'light'])), (p1, p2, '->')) for p1 in here if p1 is not 'light' for p2 in here if p2 is not 'light')
	else:
		return dict(((here  | frozenset([p1,p2, 'light']), there - frozenset([p1, p2, 'light'])), (p1, p2, '->')) for p1 in there if p1 is not 'light' for p2 in there if p2 is not 'light')

def bsuccessors(state):
	"""Return a dict of {state:action} pairs.  A state is a (here, there, t) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the light, and t is a number indicating the elapsed time."""
	here, there, t = state
	if 'light' in here:
		return dict(((here  - frozenset([a,b, 'light']),
					  there | frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '->'))
					for a in here if a is not 'light'
					for b in here if b is not 'light')
	else:
		return dict(((here  | frozenset([a,b, 'light']),
					  there - frozenset([a, b, 'light']),
					  t + max(a, b)),
					 (a, b, '<-'))
					for a in there if a is not 'light'
					for b in there if b is not 'light')  


def unit_16_refactoring_paths():
	here1 = frozenset([1, 'light']) 
	there1 = frozenset([])

	here2 = frozenset([1, 2, 'light'])
	there2 = frozenset([3])
	
	assert bsuccessors2((here1, there1)) == {
			(frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
	assert bsuccessors2((here2, there2)) == {
			(frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'), 
			(frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'), 
			(frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}
	print 'unit_16_refactoring_paths all tests passed'

unit_16_refactoring_paths()

# -----------------
# User Instructions
# 
# Write a function, path_cost, which takes a path as input 
# and returns the total cost associated with that path. 
# Remember that paths will obey the convention
# path = [state, (action, total_cost), state, ...] 
#
# If a path is less than length 3, your function should
# return a cost of 0.

def path_cost(path):
	"""The total cost of a path (which is stored in a tuple
	with the final action."""
	# path = [state, (action, total_cost), state, ... ]
	if len(path) < 3:
		return 0
	else:
		return path[-2][1]
		
def bcost(action):
	"""Returns the cost (a number) of an action in the
	bridge problem."""
	# An action is an (a, b, arrow) tuple; a and b are 
	# times; arrow is a string. 
	a, b, arrow = action
	return max(a, b)

def unit_17_calculating_costs():
	assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
	assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6
	assert bcost((4, 2, '->'),) == 4
	assert bcost((3, 10, '<-'),) == 10
	print 'unit_17_calculating_costs all tests passed'

unit_17_calculating_costs()

# this kind of search problem is tricky
# how to deal with it!
#
# - lots of tests
# - use (re-use) tools, meaning existed algorithm

"""
Example Generalization

problems:
	missionaries and cannibals
	- m and c, both are trying to cross the bridge
	- 2 max on boat
	- num of c cannot be greater at num of m on either side of the river
"""

# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
	"""Find successors (including those that result in dining) to this
	state. But a state where the cannibals can dine has no successors."""
	M1, C1, B1, M2, C2, B2 = state
	# your code here
	r = {}
	if (C1 > M1 and M1 != 0) or (C2 > M2 and M2 != 0):
		return r
	r[(M1-2, C1, B1-1, M2+2, C2, B2+1)] = 'MM->'
	r[(M1-1, C1-1, B1-1, M2+1, C2+1, B2+1)] = 'MC->'
	r[(M1, C1-2, B1-1, M2, C2+2, B2+1)] = 'CC->'
	r[(M1-1, C1, B1-1, M2+1, C2, B2+1)] = 'M->'
	r[(M1, C1-1, B1-1, M2, C2+1, B2+1)] = 'C->'
	r[(M1+2, C1, B1+1, M2-2, C2, B2-1)] = '<-MM'
	r[(M1+1, C1+1, B1+1, M2-1, C2-1, B2-1)] = '<-MC'
	r[(M1, C1+2, B1+1, M2, C2-2, B2-1)] = '<-CC'
	r[(M1+1, C1, B1+1, M2-1, C2, B2-1)] = '<-M'
	r[(M1, C1+1, B1+1, M2, C2-1, B2-1)] = '<-C'
	for k in r.keys():
		if any(v < 0 for v in k):
			r.pop(k)
	return r
	 
			
def unit_22_Csuccessors():
	assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
											   (1, 2, 0, 1, 0, 1): 'M->', 
											   (0, 2, 0, 2, 0, 1): 'MM->', 
											   (1, 1, 0, 1, 1, 1): 'MC->', 
											   (2, 0, 0, 0, 2, 1): 'CC->'}
	assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
											   (2, 1, 1, 3, 3, 0): '<-M', 
											   (3, 1, 1, 2, 3, 0): '<-MM', 
											   (1, 3, 1, 4, 1, 0): '<-CC', 
											   (2, 2, 1, 3, 2, 0): '<-MC'}
	assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
	print 'unit_22_Csuccessors all tests passed'

unit_22_Csuccessors()

"""
			GENERALIZE!

	shortest-path-search(...)->path
inventory
-paths			[state, action, state]
-states			atomic
-actions		atomic
-successors		a function(state) -> {state:action}
-start			atomic
-goal			a function(state) -> bool
"""

# -----------------
# User Instructions
# 
# Write a function, shortest_path_search, that generalizes the search algorithm
# that we have been using. This function should have three inputs, a start state,
# a successors function, and an is_goal function.
#
# You can use the solution to mc_problem as a template for constructing your 
# shortest_path_search. You can also see the example is_goal and successors
# functions for a simple test problem below.

def shortest_path_search(start, successors, is_goal):
	"""Find the shortest path from start state to a state
	such that is_goal(state) is true."""
	# your code here
	if is_goal(start) ==  True:
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
	return Fail
	


def mc_problem1(start=(3, 3, 1, 0, 0, 0), goal=None):
	"""Solve the missionaries and cannibals problem.
	State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
	Find a path that goes from the initial state to the goal state (which, if
	not specified, is the state with no people or boats on the start side."""
	if goal is None:
		goal = (0, 0, 0) + start[:3]
	if start == goal:
		return [start]
	explored = set() # set of states we have visited
	frontier = [ [start] ] # ordered list of paths we have blazed
	while frontier:
		path = frontier.pop(0)
		s = path[-1]
		for (state, action) in csuccessors(s).items():
			if state not in explored:
				explored.add(state)
				path2 = path + [action, state]
				if state == goal:
					return path2
				else:
					frontier.append(path2)
	return Fail

Fail = []

def csuccessors(state):
	"""Find successors (including those that result in dining) to this
	state. But a state where the cannibals can dine has no successors."""
	M1, C1, B1, M2, C2, B2 = state
	## Check for state with no successors
	if C1 > M1 > 0 or C2 > M2 > 0:
		return {}
	items = []
	if B1 > 0:
		items += [(sub(state, delta), a + '->')
				  for delta, a in deltas.items()]
	
	if B2 > 0:
		items += [(add(state, delta), '<-' + a)
				  for delta, a in deltas.items()]
	return dict(items)

def add(X, Y):
	"add two vectors, X and Y."
	return tuple(x+y for x,y in zip(X, Y))

def sub(X, Y):
	"subtract vector Y from X."
	return tuple(x-y for x,y in zip(X, Y))

deltas = {(2, 0, 1,	-2,  0, -1): 'MM',
		  (0, 2, 1,	 0, -2, -1): 'CC',
		  (1, 1, 1,	-1, -1, -1): 'MC',
		  (1, 0, 1,	-1,  0, -1): 'M',
		  (0, 1, 1,	 0, -1, -1): 'C'}
Fail = []


# --------------
# Example problem
#
# Let's say the states in an optimization problem are given by integers.
# From a state, i, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to the integer 8. 
#
# This is an overly simple example of when we can use the 
# shortest_path_search function. We just need to define the appropriate
# is_goal and successors functions.

def is_goal(state):
	if state == 8:
		return True
	else: 
		return False
	
def successors(state):
	successors = {state + 1: '->',
				  state - 1: '<-'}
	return successors

def unit_25_sps_function():
	assert shortest_path_search(5, successors, is_goal) == [5, '->', 6, '->', 7, '->', 8]
	print 'unit_25_sps_function all tests passed' 
	
unit_25_sps_function()

# -----------------
# User Instructions
# 
# Write a function, mc_problem2, that solves the missionary and cannibal
# problem by making a call to shortest_path_search. Add any code below
# and change the arguments in the return statement's call to the 
# shortest_path_search function.

def is_goal(state):
	return state[:3] == (0,0,0)

def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
	# your code here if necessary
	return shortest_path_search(start, csuccessors, is_goal) # <== insert arguments here
	
def mc_problem2_prof_version(start=(3, 3, 1, 0, 0, 0), goal=None):
	"""Solve the missionaries and cannibals problem.
	State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
	Find a path that goes from the initial state to the goal state (which, if
	not specified, is the state with no people or boats on the start side."""
	if goal is None:
		def goal_fn(state): return state[:3] == (0, 0, 0)
	else:
		def goal_fn(state): return state == goal
	return shortest_path_search(start, csuccessors, goal_fn)

def shortest_path_search(start, successors, is_goal):
	"""Find the shortest path from start state to a state
	such that is_goal(state) is true."""
	if is_goal(start):
		return [start]
	explored = set()
	frontier = [ [start] ] 
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
	return Fail
Fail = []

def csuccessors(state):
	"""Find successors (including those that result in dining) to this
	state. But a state where the cannibals can dine has no successors."""
	M1, C1, B1, M2, C2, B2 = state
	## Check for state with no successors
	if C1 > M1 > 0 or C2 > M2 > 0:
		return {}
	items = []
	if B1 > 0:
		items += [(sub(state, delta), a + '->')
				  for delta, a in deltas.items()]
	if B2 > 0:
		items += [(add(state, delta), '<-' + a)
				  for delta, a in deltas.items()]
	return dict(items)

def add(X, Y):
	"add two vectors, X and Y."
	return tuple(x+y for x,y in zip(X, Y))

def sub(X, Y):
	"subtract vector Y from X."
	return tuple(x-y for x,y in zip(X, Y))

deltas = {(2, 0, 1,	-2,  0, -1): 'MM',
		  (0, 2, 1,	 0, -2, -1): 'CC',
		  (1, 1, 1,	-1, -1, -1): 'MC',
		  (1, 0, 1,	-1,  0, -1): 'M',
		  (0, 1, 1,	 0, -1, -1): 'C'}

def unit_26_cleaning_up_mc_problem():
	assert mc_problem2(start=(1, 1, 1, 0, 0, 0)) == [
							 (1, 1, 1, 0, 0, 0), 'MC->',
							 (0, 0, 0, 1, 1, 1)]
	assert mc_problem2() == [(3, 3, 1, 0, 0, 0), 'CC->', 
							 (3, 1, 0, 0, 2, 1), '<-C', 
							 (3, 2, 1, 0, 1, 0), 'CC->', 
							 (3, 0, 0, 0, 3, 1), '<-C', 
							 (3, 1, 1, 0, 2, 0), 'MM->', 
							 (1, 1, 0, 2, 2, 1), '<-MC', 
							 (2, 2, 1, 1, 1, 0), 'MM->', 
							 (0, 2, 0, 3, 1, 1), '<-C', 
							 (0, 3, 1, 3, 0, 0), 'CC->', 
							 (0, 1, 0, 3, 2, 1), '<-C', 
							 (0, 2, 1, 3, 1, 0), 'CC->', 
							 (0, 0, 0, 3, 3, 1)]
	print 'unit_26_cleaning_up_mc_problem all tests passed'

unit_26_cleaning_up_mc_problem()
	 
"""
			GENERALIZE!(lowest_cost)

	shortest-path-search(...)->path
inventory
-paths			[state, action, state]
-states			atomic
-actions		atomic
-successors		a function(state) -> {state:action}
-start			atomic
-goal			a function(state) -> bool
-action_cost	a function(action) -> cost
"""

# -----------------
# User Instructions
# 
# In this problem, you will generalize the bridge problem 
# by writing a function bridge_problem3, that makes a call
# to lowest_cost_search.

def bridge_problem3(here):
	"""Find the fastest (least elapsed time) path to 
	the goal in the bridge problem."""
	# your code here
	start = (frozenset(here) | frozenset(['light']), frozenset())
	return lowest_cost_search(start, bsuccessors2, is_goal, bcost) # <== your arguments here

# your code here if necessary
def is_goal(state):
	here, there = state
	if not here or (len(here)==1 and 'light' in here):
		return True
	else:
		return False

## Now there is still a problem to deal with.
def bridge_problem2(here):
	here = frozenset(here) | frozenset(['light'])
	explored = set() # set of states we have visited
	# State will be a (peoplelight_here, peoplelight_there) tuple
	# E.g. ({1, 2, 5, 10, 'light'}, {})
	frontier = [ [(here, frozenset())] ] # ordered list of paths we have blazed
	while frontier:
		path = frontier.pop(0)
		here1, there1 = state1 = final_state(path)
		if not here1 or (len(here1)==1 and 'light' in here1):  
			return path
		explored.add(state1)
		pcost = path_cost(path)
		for (state, action) in bsuccessors2(state1).items():
			if state not in explored:
				total_cost = pcost + bcost(action)
				path2 = path + [(action, total_cost), state]
				add_to_frontier(frontier, path2)
	return Fail

def lowest_cost_search(start, successors, is_goal, action_cost):
	"""Return the lowest cost path, starting from start state,
	and considering successors(state) => {state:action,...},
	that ends in a state for which is_goal(state) is true,
	where the cost of a path is the sum of action costs,
	which are given by action_cost(action)."""
	explored = set() # set of states we have visited
	frontier = [ [start] ] # ordered list of paths we have blazed
	while frontier:
		path = frontier.pop(0)
		state1 = final_state(path)
		if is_goal(state1):  
			return path
		explored.add(state1)
		pcost = path_cost(path)
		for (state, action) in successors(state1).items():
			if state not in explored:
				total_cost = pcost + action_cost(action)
				path2 = path + [(action, total_cost), state]
				add_to_frontier(frontier, path2)
	return Fail

def final_state(path): return path[-1]

def path_cost(path):
	"The total cost of a path (which is stored in a tuple with the final action)."
	if len(path) < 3:
		return 0
	else:
		action, total_cost = path[-2]
		return total_cost
	
def add_to_frontier(frontier, path):
	"Add path to frontier, replacing costlier path if there is one."
	# (This could be done more efficiently.)
	# Find if there is an old path to the final state of this path.
	old = None
	for i,p in enumerate(frontier):
		if final_state(p) == final_state(path):
			old = i
			break
	if old is not None and path_cost(frontier[old]) < path_cost(path):
		return # Old path was better; do nothing
	elif old is not None:
		del frontier[old] # Old path was worse; delete it
	## Now add the new path and re-sort
	frontier.append(path)
	frontier.sort(key=path_cost)

def bsuccessors2(state):
	"""Return a dict of {state:action} pairs.  A state is a (here, there) tuple,
	where here and there are frozensets of people (indicated by their times) and/or
	the light."""
	here, there = state
	if 'light' in here:
		return dict(((here  - frozenset([a, b, 'light']),
					  there | frozenset([a, b, 'light'])),
					 (a, b, '->'))
					for a in here if a is not 'light'
					for b in here if b is not 'light')
	else:
		return dict(((here  | frozenset([a, b, 'light']),
					  there - frozenset([a, b, 'light'])),
					 (a, b, '<-'))
					for a in there if a is not 'light'
					for b in there if b is not 'light')

def bcost(action):
	"Returns the cost (a number) of an action in the bridge problem."
	# An action is an (a, b, arrow) tuple; a and b are times; arrow is a string
	a, b, arrow = action
	return max(a, b)

def unit_28_back_to_bridge_problem():
	here = [1, 2, 5, 10]
	assert bridge_problem3(here) == [
			(frozenset([1, 2, 'light', 10, 5]), frozenset([])), 
			((2, 1, '->'), 2), 
			(frozenset([10, 5]), frozenset([1, 2, 'light'])), 
			((2, 2, '<-'), 4), 
			(frozenset(['light', 10, 2, 5]), frozenset([1])), 
			((5, 10, '->'), 14), 
			(frozenset([2]), frozenset([1, 10, 5, 'light'])), 
			((1, 1, '<-'), 15), 
			(frozenset([1, 2, 'light']), frozenset([10, 5])), 
			((2, 1, '->'), 17), 
			(frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
	print 'unit_28_back_to_bridge_problem all tests passed'

unit_28_back_to_bridge_problem()
	
"""
		LESSON LEARNED
- search
- different kinds
	shortest_path
	least_cost
- subtle
- bugs
	counter with tests
	counter with tools
- generalize
- two parts
	this problem
	general
"""




