def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	if n == 2: return 1
	return fib(n-1) + fib(n-2)
	
def unit_5_recursive_definition():
	assert fib(6) == 8
	assert fib(1) <= fib(2) == True
	assert fib(1) == fib(2) == True
	assert fib(20) > 1000
	print 'unit_5_recursive_definition all tests passed'
	
unit_5_recursive_definition()

# Memofibo

# Submit via the interpreter a definition for a memofibo procedure that uses a
# chart. You are going to want the Nth value of the chart to hold the Nth
# fibonacci number if you've already computed it and to be empty otherwise.

chart = {}

def memofibo(n):
	if n == 0: return 0
	if n == 1: return 1
	if n == 2: return 1
	if n-1 not in chart.keys():
		chart[n-1] = memofibo(n-1)
	if n-2 not in chart.keys():
		chart[n-2] = memofibo(n-2)
	return chart[n-1] + chart[n-2]

def memofibo2(n):
	if n <= 2: return 1
	if n in chart: return chart[n]
	else: chart[n] = memofibo2(n-1) + memofibo2(n-2)
	return chart[n]
		
    
    
print memofibo(24)
print memofibo2(24)

import timeit
t = timeit.Timer(stmt = 
"""
chart = {}
def memofibo2(n):
	if n <= 2: return 1
	if n in chart: return chart[n]
	else: chart[n] = memofibo2(n-1) + memofibo2(n-2)
	return chart[n]
memofibo2(24)
""")
print t.timeit(number=100)

"""
a PARSING STATE is a rewrite rule from the grammar augmented
with 1 red dot on the right-rhand side
"""
# Addtochart

# Let's code in Python! Write a Python procedure addtochart(chart,index,state)
# that ensures that chart[index] returns a list that contains state exactly
# once. The chart is a Python dictionary and index is a number. addtochart
# should return True if something was actually added, False otherwise. You may
# assume that chart[index] is a list.


def addtochart(chart, index, state):
	# Insert code here!
	s = set(chart[index])
	a = len(s)
	s.add(state)
	b = len(s)
	if b == a + 1:
		chart[index].append(state)
		return True
	else:
		return False
		
def addtochart_prof(chart, index, state):
	# Insert code here!
	if state in chart[index]:
		return False
	else:
		chart[index] += [state]
		return True

# Writing Closure

# We are currently looking at chart[i] and we see x => ab . cd from j

# Write the Python procedure, closure, that takes five parameters:

#   grammar: the grammar using the previously described structure
#   i: a number representing the chart state that we are currently looking at
#   x: a single nonterminal
#   ab and cd: lists of many things

# The closure function should return all the new parsing states that we want to
# add to chart position i

# Hint: This is tricky. If you are stuck, do a list comphrension over the grammar rules.

def closure (grammar, i, x, ab, cd):
	# Insert code here!
	return [(name,[],rule,i) for name,rule in grammar if len(cd[0]) and name == cd[0]]


grammar = [ 
	("exp", ["exp", "+", "exp"]),
	("exp", ["exp", "-", "exp"]),
	("exp", ["(", "exp", ")"]),
	("exp", ["num"]),
	("t",["I","like","t"]),
	("t",[""])
	]

print closure(grammar,0,"exp",["exp","+"],["exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",[],["exp","+","exp"]) == [('exp', [], ['exp', '+', 'exp'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['num'], 0)]
print closure(grammar,0,"exp",["exp"],["+","exp"]) == []

z = 10

print [[a,z] for a in [9,8,7,6]]
print [name for name,rule in grammar]
print closure(grammar,0,"exp",["exp","+"],["exp"])
    
# Writing Shift

# We are currently looking at chart[i] and we see x => ab . cd from j. The input is tokens.

# Your procedure, shift, should either return None, at which point there is
# nothing to do or will return a single new parsing state that presumably
# involved shifting over the c if c matches the ith token.

def shift (tokens, i, x, ab, cd, j):
	# Insert code here
	if len(cd) == 0:
		return None
	c = cd[0]
	token = tokens[i]
	if c == token:
		return (x, ab + [c], cd[1:], j)
	else:
		return None

	

print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) == ('exp', ['exp'], ['+', 'exp'], 0)
print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None
print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) == None

print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0)

# Writing Reductions

# We are looking at chart[i] and we see x => ab . cd from j.

# Hint: Reductions are tricky, so as a hint, remember that you only want to do
# reductions if cd == []

# Hint: You'll have to look back previously in the chart. 

def reductions(chart, i, x, ab, cd, j):
	# Insert code here!
	if cd == []:
		return [(name, bef + aft[:1], aft[1:], j) for name,bef,aft,frn in chart[j] if len(aft) > 0 and aft[0] == x]
	else:
		return None
	
	
	
chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)], 1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]

print reductions(chart,2,'exp',['exp','+','exp'],[],0)

# Rama's Journey

# Suppose we input "Rama's Journey" to our parser. Define a variable ptree that
# holds the parse tree for this input.

ptree = [("word-element","Rama's"), ("word-element","Journey")] # Change this variable!




	