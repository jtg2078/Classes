# Reading Machine Minds 2
#
# We say that a finite state machine is "empty" if it accepts no strings.
# Similarly, we say that a context-free grammar is "empty" if it accepts no
# strings. In this problem, you will write a Python procedure to determine
# if a context-free grammar is empty.
#
# A context-free grammar is "empty" starting from a non-terminal symbol S 
# if there is no _finite_ sequence of rewrites starting from S that
# yield a sequence of terminals. 
#
# For example, the following grammar is empty:
#
# grammar1 = [ 
#       ("S", [ "P", "a" ] ),           # S -> P a
#       ("P", [ "S" ]) ,                # P -> S
#       ] 
#       
# Because although you can write S -> P a -> S a -> P a a -> ... that
# process never stops: there are no finite strings in the language of that
# grammar. 
#
# By contrast, this grammar is not empty: 
#
# grammar2 = [
#       ("S", ["P", "a" ]),             # S -> P a
#       ("S", ["Q", "b" ]),             # S -> Q b
#       ("P", ["P"]),                   # P -> P
#       ("Q", ["c", "d"]),              # Q -> c d 
#
# And ["c","d","b"] is a witness that demonstrates that it accepts a
# string.
#
# Write a procedure cfgempty(grammar,symbol,visited) that takes as input a
# grammar (encoded in Python) and a start symbol (a string). If the grammar
# is empty, it must return None (not the string "None", the value None). If
# the grammar is not empty, it must return a list of terminals
# corresponding to a string in the language of the grammar. (There may be
# many such strings: you can return any one you like.) 
#
# To avoid infinite loops, you should use the argument 'visited' (a list)
# to keep track of non-terminals you have already explored. 
#
# Hint 1: Conceptually, in grammar2 above, starting at S is not-empty with
# witness [X,"a"] if P is non-empty with witness X and is non-empty with
# witness [Y,"b"] if Q is non-empty with witness Y. 
#
# Hint 2: Recursion! A reasonable base case is that if your current
# symbol is a terminal (i.e., has no rewrite rules in the grammar), then
# it is non-empty with itself as a witness. 
#
# Hint 3: all([True,False,True]) = False
#         any([True,True,False]) = True

def cfgempty(grammar,symbol,visited):
	# Insert code here!
	proof = []
	isTerminal = True
	isMatch = True
	for rule in grammar:
		if rule[0] == symbol:
			isTerminal = False
			if rule[1] not in visited:
				visited.append(rule[1])
				for s in rule[1]:
					#proof.append(cfgempty(grammar, s, visited))
					cfgempty(grammar, s, visited)
			else:
				isMatch = False
	if isTerminal == True and isMatch == True:
		print symbol
		return symbol

def cfgempty(grammar,symbol,visited):
	#print symbol
	isTerminal = True
	repeat = False
	# check for terminal
	for name, rule in grammar:
		if name == symbol:
			witness = []
			isTerminal = False
			if rule not in visited:
				visited.append(rule)
				for s in rule:
					result = cfgempty(grammar, s, visited)
					if result is None:
						result = [None]
					witness += result
					#witness =  witness + cfgempty(grammar, s, visited)
				if None not in witness:
					return witness
				#print 'symbol: {0} witness: {1} '.format(symbol, witness)
			else:
				repeat = True
	if isTerminal == True:
		return [symbol]
	return None
		
# We have provided a few test cases for you. You will likely want to add
# more of your own. 

grammar1 = [ 
      ("S", [ "P", "a" ] ),           
      ("P", [ "S" ]) ,               
      ] 
                        
print cfgempty(grammar1,"S",[]) == None
#print cfgempty(grammar1,"S",[])

grammar2 = [
      ("S", ["P", "a" ]),             
      ("S", ["Q", "b" ]),             
      ("P", ["P"]), 
      ("Q", ["c", "d"]),              
      ] 

print cfgempty(grammar2,"S",[]) == ['c', 'd', 'b']
#print cfgempty(grammar2,"S",[])


grammar3 = [  # some Spanish provinces
        ("S", [ "Barcelona", "P", "Huelva"]),
        ("S", [ "Q" ]),
        ("Q", [ "S" ]),
        ("P", [ "Las Palmas", "R", "Madrid"]),
        ("P", [ "T" ]),
        ("T", [ "T", "Toledo" ]),
        ("R", [ ]) ,
        ("R", [ "R"]), 
        ]

print cfgempty(grammar3,"S",[]) == ['Barcelona', 'Las Palmas', 'Madrid', 'Huelva']


def can_rewrite(grammar, symbol, visited):
	isTerminal = True
	for s,r in grammar:
		if s == symbol:
			witness = []
			isTerminal = False
			if r not in visited:
				visited.append(r)
				for s1 in r:
					result = can_rewrite(grammar, s1, visited)
					witness += result
				if all(witness):
					return witness
	return [isTerminal]

print can_rewrite(grammar1,"S",[])
print can_rewrite(grammar2,"S",[])
print can_rewrite(grammar3,"S",[])
