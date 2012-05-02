# -------------------- import ---------------------
import re
# -------------------- unit 01 --------------------
def unit_01_20_create_regexp():
	regexp = r'ab|[0-9]+'
	assert re.findall(regexp,'ab') == ['ab']
	assert re.findall(regexp,"1") == ["1"]
	assert re.findall(regexp,"123") == ["123"]
	assert re.findall(regexp,"a") != ["a"]
	assert re.findall(regexp,"abc") != ["abc"]
	assert re.findall(regexp,"abc123") != ["abc123"]
	print 'all tests passed'

# regex symbol + : one or more copies
# regex symbol * : zero or more copies
# regex symbol ? : zero or one copy
# e.g.	a+ is same as aa*

# in python back-slash \ is the escape
# which means treat the following character as
# part of the string, not end of it

def unit_01_22_escape_sequences():
	a = "P&P is Jane's Book."
	b = 'P&P is Jane\'s Book.'
	print a
	print b
	print a == b

def unit_01_23_hyphenation():
	regexp = r"[a-z]+-?[a-z]+"
	assert re.findall(regexp,"well-liked") == ["well-liked"]
	assert re.findall(regexp,"html") == ["html"]
	assert re.findall(regexp,"a-b-c") != ["a-b-c"]
	assert re.findall(regexp,"a--b") != ["a--b"]
	print 'all tests passed'

def unit_01_25_re_challenges():
	regexp = r"[a-z]+\([ ]*[0-9][ ]*\)"
	assert re.findall(regexp,"cos(0)") == ["cos(0)"]
	assert re.findall(regexp,"sqrt(   2     )") == ["sqrt(   2     )"]
	assert re.findall(regexp,"cos     (0)") != ["cos     (0)"]
	assert re.findall(regexp,"sqrt(x)") != ["sqrt(x)"]
	print 'all tests passed'

# regex symbol . : any characters except newline/return
# regex symbol ^ : not e.g.	[^ab] anything that is not a and not b
# in python grouping in regex is by using (?:   )
# e.g.	(?:xyz)+ would match xyz, xyzxyz, xyzxyzxyz ...
#		(?:do|re|mi) would match mimi, rere, midore

def unit_01_28_escaping_the_escape():
	regexp = r'"(?:[^\\]|(?:\\.))*"'
	assert re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""']
	assert re.findall(regexp,'"\\"') != ['"\\"']
	print 'all tests passed'

# explanation:
# regexp = r'"(?:[^\\]|(?:\\.))*"'
#			 1     2       3    4
# '"I say, \"hello.\""'
#  1222222233222222334

# ref: http://en.wikipedia.org/wiki/Complexity_of_songs
# ref: http://en.wikipedia.org/wiki/99_bottles_of_beer

# in python Tuple means "immutable list"
# e.g. t = (124,456)	t[0] = 124	t[1] = 456

def unit_01_30_fsm_simulator():
	edges = {(1, 'a') : 2,
	         (2, 'a') : 2,
	         (2, '1') : 3,
	         (3, '1') : 3}
	accepting = [3]
	assert fsmsim("aaa111", 1, edges, accepting) == True
	assert fsmsim("a1", 1, edges, accepting) == True
	assert fsmsim("a1a1a1", 1, edges, accepting) == False
	assert fsmsim("", 1, edges, accepting) == False
	print 'all tests passed'

def fsmsim(string, current, edges, accepting):
	if string == "":
		return current in accepting
	else:
		letter = string[0]
		if (current, letter) in edges:
			return fsmsim(string[1:], edges[(current, letter)], edges, accepting)
		else:
			return False

def unit_01_31_fsm_interpretation():
	# Define edges and accepting to encode r"q*". Name your start state 1.
	edges = {(1, 'q') : 2,
	         (2, 'q') : 2}
	accepting = [1, 2]
	assert fsmsim("", 1, edges,accepting) == True
	assert fsmsim("q", 1, edges,accepting) == True
	assert fsmsim("qq", 1, edges,accepting) == True
	assert fsmsim("p", 1, edges,accepting) == False
	print 'all tests passed'

def unit_01_32_more_fsm_encoding():
	# Define edges and accepting to encode r"[a-b][c-d]?". Name your start state 1.
	edges = {(1, 'a') : 2,
	         (1, 'b') : 2,
			 (2, 'c') : 3,
			 (2, 'd') : 3}
	accepting = [2, 3]
	assert fsmsim("a",1,edges,accepting) == True
	assert fsmsim("b",1,edges,accepting) == True
	assert fsmsim("ad",1,edges,accepting) == True
	assert fsmsim("e",1,edges,accepting) == False
	print 'all tests passed'
	
def unit_01_33_mis_msf():
	# Provide s1 and s2 that are both accepted, but s1 != s2.
	edges = {(1,'a') : 2,
	         (1,'b') : 3,
	         (2,'c') : 4,
	         (3,'d') : 5,
	         (5,'c') : 2,
	         (5,'f') : 6,
	         (5,'g') : 1}
	accepting = [6]
	s1 = "bdf"
	s2 = "bdgbdf"
	assert fsmsim(s1,1,edges,accepting) == True
	assert fsmsim(s2,1,edges,accepting) == True
	assert (s1 != s2) == True
	print 'all tests passed'

# python RE module uses something very similiar to fsmsim under the hood
# however our fsmsim does not handle epsilion(greedy) and abmiguity!
# HERE is the formal definition of FSM:
#	A FSM accepts a string s if THERE EXITS EVEN ONE PATH from the start
#	start state to ANY ACCEPTING STATE following s (a.k.a generous)

def unit_01_35_phone_it_in():
	regexp = r"[0-9]+(?:-[0-9]+)*"
	assert re.findall(regexp,"123-4567") == ["123-4567"]
	assert re.findall(regexp,"1234567") == ["1234567"]
	assert re.findall(regexp,"08-78-88-88-88") == ["08-78-88-88-88"]
	assert re.findall(regexp,"0878888888") == ["0878888888"]
	assert re.findall(regexp,"-6") != ["-6"]
	print 'all tests passed'

# Non-Deterministic FSM
# "easy-to-write" FSMs, like the one we are learning in class, with 
# EPSILON transitions or AMBIGUITY are known as
# 		non-deterministic finite state machine
# (which means you may not know exactly where to go!)
#
# A "lock-step" FSM with no epsilon edges or ambiguity is a
#		deterministic finite state machine
# (the fsmsim is one like this)
#
# every NON-DETERMINISTIC FSM has a corresponding DETERMINISTIC FSM
# that accepts exactly the same strings
#
# Non-deterministic FSMs are not more powerful, they are just more
# convenient

# Wrap Up~
# strings -  are sequence of characters
# regular expressions - concise notation for specifying sets of
#						strings. More flexible than fixed string
#						matching
# finite state machine - pictoral equivalance to regular expressions
# deterministic - every FSM can be converted to determonistic FSM
# FSM simulation - it is very easy, ~10 lines of recursive code to
#				   to see if a det FSM accepts a string

# -------------------- unit 01 homewoek --------------------
# Problem one
# 1.web pages can control their behavior and appearance through embedded Javascript (true)
# 2.while english sentences can be broken up into words, HTML and Javascript cannot (false)
# 3.for every python program that call re.findall(), there is another python program
#   that does not call re.findall() but still obtains the same results (true)
# 4.every regular expression that involves neither + or * matches a finite set of strings.
#   Only consider the regular expression syntax discussed in lecture (true)
#
# Problem two
def sumnums(sentence):
	regexp = r"[0-9]+"
	nums = map(int, re.findall(regexp, sentence))
	return sum(nums)

def unit_01_hw_2():
	assert sumnums("""The Act of Independence of Lithuania was signed 
	on February 16, 1918, by 20 council members.""") == 1954
	assert sumnums("hello 2 all of you 44") == 46
	assert sumnums("44") == 44
	assert sumnums("all your base are belong to us") == 0
	print 'all tests passed'
#
# Problem three
def unit_01_hw_3():
	regexp = r"[a-z]+(?:-[a-z]+)?"
	assert re.findall(regexp, "astronomy") == ["astronomy"]  
	assert re.findall(regexp, "near-infrared") == ["near-infrared"]
	assert re.findall(regexp, "x-ray") == ["x-ray"]
	assert re.findall(regexp, "-tricky") != ["-tricky"]
	assert re.findall(regexp, "tricky-") != ["tricky-"]
	assert re.findall(regexp, "large - scale") != ["large - scale"] 
	assert re.findall(regexp, "gamma-ray-burst") != ["gamma-ray-burst"] 
	assert re.findall(regexp, "") != [""]
	assert re.findall(regexp, """the wide-field infrared survey explorer is a nasa
	infrared-wavelength space telescope in an earth-orbiting satellite which
	performed an all-sky astronomical survey. be careful of -tricky tricky-
	hyphens --- be precise.""") == ['the', 'wide-field', 'infrared', 'survey', 'explorer',
	'is', 'a', 'nasa', 'infrared-wavelength', 'space', 'telescope', 'in', 'an',
	'earth-orbiting', 'satellite', 'which', 'performed', 'an', 'all-sky',
	'astronomical', 'survey', 'be', 'careful', 'of', 'tricky', 'tricky',
	'hyphens', 'be', 'precise']
	print 'all tests passed'

#
# Problem four
# (not programming question)
#
# Problem five
# Title: Simulating Non-Determinism
#
# Each regular expression can be converted to an equivalent finite state
# machine. This is how regular expressions are implemented in practice. 
# We saw how non-deterministic finite state machines can be converted to
# deterministic ones (often of a different size). It is also possible to
# simulate non-deterministic machines directly -- and we'll do that now!
#
# In a given state, a non-deterministic machine may have *multiple*
# outgoing edges labeled with the *same* character. 
#
# To handle this ambiguity, we say that a non-deterministic finite state
# machine accepts a string if there exists *any* path through the finite
# state machine that consumes exactly that string as input and ends in an
# accepting state. 
#
# Write a procedure nfsmsim that works just like the fsmsim we covered
# together, but handles also multiple outgoing edges and ambiguity. Do not
# consider epsilon transitions. 
# 
# Formally, your procedure takes four arguments: a string, a starting
# state, the edges (encoded as a dictionary mapping), and a list of
# accepting states. 
#
# To encode this ambiguity, we will change "edges" so that each state-input
# pair maps to a *list* of destination states. 
#
# For example, the regular expression r"a+|(?:ab+c)" might be encoded like
# this:
def unit_01_hw_5():	
	edges = { (1, 'a') : [2, 3],
	          (2, 'a') : [2],
	          (3, 'b') : [4, 3],
	          (4, 'c') : [5] }
	accepting = [2, 5] 
	# It accepts both "aaa" (visiting states 1 2 2 and finally 2) and "abbc"
	# (visting states 1 3 3 4 and finally 5).
	assert nfsmsim("aaa", 1, edges, accepting) == True
	assert nfsmsim("abbc", 1, edges, accepting) == True
	assert nfsmsim("abc", 1, edges, accepting) == True
	assert nfsmsim("aaa", 1, edges, accepting) == True
	assert nfsmsim("abbbc", 1, edges, accepting) == True
	assert nfsmsim("aabc", 1, edges, accepting) == False
	assert nfsmsim("z", 1, edges, accepting) == False
	assert nfsmsim("", 1, edges, accepting) == False
	print 'all tests passed'

def nfsmsim(string, current, edges, accepting):
	if string == "":
		return current in accepting
	else:
		letter = string[0]
		if (current, letter) in edges:
			routes = edges[(current, letter)]
			for r in routes:
				if nfsmsim(string[1:], r, edges, accepting) == True:
					return True
			return False
		return False
#
# Problem six
#
# Title: Reading Machine Minds
#
# It can be difficult to predict what strings a finite state machine will
# accept. A tricky finite state machine may not accept any! A finite state
# machine that accepts no strings is said to be *empty*. 
# 
# In this homework problem you will determine if a finite state machine is
# empty or not. If it is not empty, you will prove that by returning a
# string that it accepts. 
#
# Formally, you will write a procedure nfsmaccepts() that takes four
# arguments corresponding to a non-derministic finite state machine:
#   the start (or current) state
#   the edges (encoded as a mapping)
#   the list of accepting states
#   a list of states already visited (starts empty) 
#
# If the finite state machine accepts any string, your procedure must
# return one such string (your choice!). Otherwise, if the finite state
# machine is empty, your procedure must return None (the value None, not
# the string "None"). 
#
def unit_01_hw_6():
	# For example, this non-deterministic machine ...
	# ... accepts exactly one string: "abc". By contrast, this
	edges = { (1, 'a') : [2, 3],
	          (2, 'a') : [2],
	          (3, 'b') : [4, 2],
	          (4, 'c') : [5] }
	accepting = [5] 
	# non-deterministic machine:
	# ... accepts no strings (if you look closely, you'll see that you cannot
	# actually reach state 2 when starting in state 1). 
	edges2 = { (1, 'a') : [1],
	           (2, 'a') : [2] }
	accepting2 = [2]
	assert nfsmaccepts(1, edges, accepting, []) == "abc" 
	assert nfsmaccepts(1, edges, [4], []) == "ab"
	assert nfsmaccepts(1, edges2, accepting2, []) == None
	assert nfsmaccepts(1, edges2, [1], []) == ""
	print 'all tests passed'

# Hint #1: This problem is trickier than it looks. If you do not keep track
# of where you have been, your procedure may loop forever on the second
# example. Before you make a recursive call, add the current state to the
# list of visited states (and be sure to check the list of visited states
# elsewhere). 
#
# Hint #2: (Base Case) If the current state is accepting, you can return
# "" as an accepting string.  
# 
# Hint #3: (Recursion) If you have an outgoing edge labeled "a" that
# goes to a state that accepts on the string "bc" (i.e., the recursive call
# returns "bc"), then you can return "abc". 
#
# Hint #4: You may want to iterate over all of the edges and only consider
# those relevant to your current state. "for edge in edges" will iterate
# over all of the keys in the mapping (i.e., over all of the (state,letter)
# pairs) -- you'll have to write "edges[edge]" to get the destination list. 

def nfsmaccepts(current, edges, accepting, visited): 
	# write your code here
	if current in accepting:
		return ""
	else:
		if current in visited:
			return None
		visited.append(current)
		for edge,state in edges.items():
			if edge[0] == current:
				for s in state:
					r = nfsmaccepts(s, edges, accepting, visited)
					if r is not None:
						return edge[1] + r
		return None

	

					
				



	


	
	




	
