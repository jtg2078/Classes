# Implementing RE
# Challenge Problem 
#
# Focus: All Units
#
#
# In this problem you will write a lexer, parser and interpreter for
# strings representing regular expressions. Your program will output 
# a non-deterministic finite state machine that accepts the same language
# as that regular expression. 
#
# For example, on input 
#
# ab*c
#
# Your program might output
# 
# edges = { (1,'a')  : [ 2 ] ,
#           (2,None) : [ 3 ] ,    # epsilon transition
#           (2,'b')  : [ 2 ] ,
#           (3,'c')  : [ 4 ] } 
# accepting = [4]
# start = 1
#
# We will consider the following regular expressions:
#
#       single characters       #       a       
#       regexp1 regexp2         #       ab
#       regexp *                #       a*
#       regexp1 | regexp2       #       a|b
#       ( regexp )              #       (a|b)* -- same as (?:a|b) 
#
# That's it. We won't consider [a-c] because it's just a|b|c, and we won't
# consider a+ because it's just aa*. We will not worry about escape
# sequences. Single character can be a-z, A-Z or 0-9 -- that's it. No need
# to worry about strange character encodings. We'll use ( ) for regular
# expression grouping instead of (?: ) just to make the problem simpler.
#
# Don't worry about precedence or associativity. We'll fully parenthesize
# all regular expressions before giving them to you. 
#
# You will write a procedure re_to_nfsm(re_string). It takes as input a
# single argument -- a string representing a regular expression. It returns
# a tuple (edges,accepting,start) corresponding to an NSFM that accepts the
# same language as that regular expression.
#
# Hint: Make a lexer and a paser and an interpreter. Your interpreter may
# find it handy to know the current state and the goal state. Make up as
# many new states as you need. 
#
import ply.lex as lex
import ply.yacc as yacc

# Fill in your code here.
tokens = (
	'CHAR',
	'STAR',
	'OR',
	'RPAREN',
	'LPAREN')

def t_CHAR(token):
	r'[a-zA-Z0-9]'
	return token

def t_STAR(token):
	r'\*'
	return token
	
def t_OR(token):
	r'\|'
	return token

def t_RPAREN(token):
	r'\)'
	return token

def t_LPAREN(token):
	r'\('
	return token

t_ignore = ' \t\v\r'

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1)

start = 'r'    # the start symbol in our grammar

def p_r(p):
	'r : regex'
	p[0] = p[1]

def p_regex(p):
	'regex : regex regex'
	p[0] = p[1] + p[2]

def p_regex_empty(p):
	'regex : '
	p[0] = [ ]

def p_regex_char(p):
	'regex : CHAR'
	p[0] = [('char', p[1])]

def p_regex_star(p):
	'regex : regex STAR'
	p[0] = [('star', p[1])]

def p_regex_or(p):
	'regex : regex OR regex'
	p[0] = [('or', p[1], p[3])]

def p_regex_paran(p):
	'regex : LPAREN regex RPAREN'
	p[0] = p[2]

def interpret(trees): # Hello, friend
	print 'tree:', trees


lexer = lex.lex() 
parser = yacc.yacc()



def reverse(edges,accepting,start):
	new_accepting = start
	new_start = accepting
	new_edges = {}
	for edge,nodes in edges.items():
		for node in nodes:
			key = (node,edge[1])
			if key in new_edges:
				new_edges[key] += [edge[0]]
			else:
				 new_edges[key] = [edge[0]]

	result = (new_edges, new_accepting, new_start)
	return result

"""
edges = { (1,'a')  : [ 2 ] ,
	  (2,None) : [ 3 ] ,    # epsilon transition
	  (2,'b')  : [ 2 ] ,
	  (3,'c')  : [ 4 ] } 
accepting_state = [4]
start_state = 1
"""

def re_to_nfsm(re_string):
	print  're_string:', re_string
	# Feel free to overwrite this with your own code. 
	lexer.input(re_string)
	parse_tree = parser.parse(re_string, lexer=lexer)
	print 'abc',parse_tree
	accept = 1
	start = []
	edges = {}
	state = accept
	for e in parse_tree:
		if e[0] == 'char':
			key = (state, e[1]))
			state += 1
			if key in edges:
				edges[key] += [state]
			else:
				edges[key] = [state]
		elif e[0] == 'star':
			key = 
	
	
	
	
	

# We have included some testing code ... but you really owe it to yourself
# to do some more testing here.

def nfsmaccepts(edges, accepting, current, string, visited): 
	# If we have visited this state before, return false. 
	if (current, string) in visited:
		return False
	visited.append((current, string))       

	# Check all outgoing epsilon transitions (letter == None) from this
	# state. 
	if (current, None) in edges:
		for dest in edges[(current, None)]:
			if nfsmaccepts(edges, accepting, dest, string, visited):
				return True

	# If we are out of input characters, check if this is an
	# accepting state. 
	if string == "":
		return current in accepting

	# If we are not out of input characters, try all possible
	# outgoing transitions labeled with the next character. 
	letter = string[0]
	rest = string[1:]
	if (current, letter) in edges:
		for dest in edges[(current, letter)]:
			if nfsmaccepts(edges, accepting, dest, rest, visited):
				return True
	return False

def test(re_string, e, ac_s, st_s, strings):
  my_e, my_ac_s, my_st_s = re_to_nfsm(re_string) 
  print my_e
  for string in strings:
      print nfsmaccepts(e,ac_s,st_s,string,[]) == \
	    nfsmaccepts(my_e,my_ac_s,my_st_s,string,[]) 

edges = { (1,'a')  : [ 2 ] ,
	  (2,None) : [ 3 ] ,    # epsilon transition
	  (2,'b')  : [ 2 ] ,
	  (3,'c')  : [ 4 ] } 
accepting_state = [4]
start_state = 1

test("a(b*)c", edges, accepting_state, start_state, 
  [ "", "ab", "cd", "cddd", "c", "", "ad", "abcd", "abbbbbc", "ac" ]  ) 

edges = { (1,'a')  : [ 2 ] ,
	  (2,'b') :  [ 1 ] ,    
	  (1,'c')  : [ 3 ] ,
	  (3,'d')  : [ 1 ] } 
accepting_state = [1]
start_state = 1

test("((ab)|(cd))*", edges, accepting_state, start_state, 
  [ "", "ab", "cd", "cddd", "c", "", "ad", "abcd", "abbbbbc", "ac" ]  ) 
	