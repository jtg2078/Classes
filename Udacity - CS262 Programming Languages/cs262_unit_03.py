# Infinite Utterance is not the same as All Utterances

# syntactic structure

# Formal Grammer

#------------------------------
#			SENTENCE	-> 	SUBJECT VERB		
#			SUBJECT		->	teacher			#
# grammer	SUBJECT		-> 	studends	terminals
#			VERB		->	write			#
#			VERB		->	think			#
#			---- rewrite rule ------
# CAP = can be rewrite
# lower case = cannot be rewrite

# SENTENCE	->	SUBJECT	VERB	-> student	VERB
#			-> student think	-> (done)
# 3 rewrite rule used

# -> (the arrow can be called as derivation!)

# new rules!
#
# SENTENCE	->	SUBJ VERB
# SUBJ		->	students
# SUBJ		->	teachers
# SUBJ		->	SUBJ and SUBJ   (recursion!)
# VERB		->	think
# VERB		->	write
#
# 
# SENTENCE	->	SUBJ VERB	->	SUBJ and SUBJ VERB
# ->	students and SUBJ VERB	->	studends and SUBJ think
# ->	students and teachers think

# Even though there are an infinite number of strings in the language grammar
# every one of those strings has finite length

# Finite	->		Infinite
# grammer	->		utterances
#
# this means that although grammer is finite ser of rules, but it can
# create infinite possibilities!

# EXP -> EXP + EXP
# EXP -> EXP - EXP
# EXP -> number
#
# possibilities:
# 	number
#	number + number + number
# 	number - number + number
# 

# Lexical Analysis(aka Lexing)		=>		(string to token list)
# Syntactical Analysis(aka Parsing)	=>		(check if token list is valid in grammar)
#
# Lexing + Parsing = Expressive Power!
# word rules + sentence rules = creativity!

# Optional Parts of Languages
#
# "I think" vs "I think correctly"
#						(this is the optional adverb)
# Epilison => means the empty string or no input

# unit 3 10
# 2(subjects) * 2(verbs) * 2(opt adj) = 8

# Grammars can encode Regular Languages
# number = r'[0-9]+'
#
# NUMBER 		-> DIGIT MORE_DIGIT
# MORE_DIGIT	-> DIGIT MORE_DIGIT
# MORE_DIGIT	-> Episilon
# DIGIT			-> 0
# DIGIT			-> 1
# so on ....

# Grammer has more expressive power than Regexp!

# Regular Expression describe regular languages

# context free language means the replacing rule is not bound
# by nearby elements!
# grammars describe context free languages
#
# A (me dont matter) -> (me dont matter) B (me dont matter)

#	regex			grammar
#	ab				g -> ab
#	a*				g -> e(epsilion)
#					g -> a g
#	a|b				g -> a
#					g -> b

# A language L is a context-free language if there exists a 
# a context-free grammar G such that the set of strings 
# accepted by G is exactly L. Context-free languages are 
# strictly more powerful than regular languages 
# (i.e,. context-free grammars are strictly more powerful 
# than regular expressions.)

# Balanced Parantheses are not Regular!!
# zomg...
# so you cant use regular expression to check balanced parentheses
#

# Parse trees are a pictoral representation of the structure 
# of an utterance. A parse tree demonstrates that a string 
# is in the language of a grammar.

# I saw Jane Austen using binoculars
# what can it mean? it goes two ways
# I was using binoculars and through it i saw Jane Austen
# I saw Jane Austen and she was uing a binoculars
#
# confusing! ambuguity!

#
# Parentheses in programming languages allow programmers 
# (like you!) to control ambiguity by making the 
# desired interpretation explicit.
#
# Formally, a grammar is ambiguous if it contains at 
# least one string that has at least two different parse trees.
#

# Grammars for HTML and JavaScript
#
# <b> Welcome to <i>my</i> webpage! </b>
#
# 	HTML 		-> ELEMENT HTML
#	HTML 		-> (Epilison)
# 	ELEMENT 	-> word
#	ELEMENT		-> TAG_OPEN HTML TAG_OPEN
#	TAG_OPEN	-> < word >
#	TAG_OPEN	-> </ word >

# Revenge of JavaScript
# JavaScript is similiar to Python

# comparison of JavaScript and Python

# JavaScript
"""
function absval(x) {
	if x < 0 {
		return 0 - x;
	} else {
		return x;
	}
}
"""

def absval(x):
	if x < 0:
		return 0 - x
	else:
		return x

# in python you use print "hello" + "!"
# in JavaScript you use 
#		document.write("hello"+"!");
#		write("hello" + "!");

# Up to Ten
#
# Define a JavaScript function that embodies the same functionality as the
# following Python code:


def uptoten(x):
    if x < 10:
        return x
    else:
        return 10


javascriptcode="""
function uptoten(x) {
	if(x < 10) {
		return x;
	} else {
		return 10;
	}
}
"""

# Universal Meaning?
# def vs function
# meaning staged the same!, we can translate between python and
# JavaScript
#
# Universal Grammar

# python program is a list of statements and function definitions
# so is JavaScript program!

# Valid Statements

# Translate the following JavaScript code to Python:

#        function mymin(a, b){
#            if (a < b){
#                return a;
#            } else {
#                return b;
#            };
#        }
#        
#        function square(x){
#            return x * x;
#        }
#        
#        write(mymin(square(-2), square(3)));


def mymin(a,b):
	if a < b:
		return a
	else:
		return b

def square(x):
	return x * x

print mymin(square(-2), square(3))

def addtwo(x):
	return x+2

print addtwo(2) # 4

mystery = lambda(x): x+2
print mystery(5) # 7

pele = mystery

print pele(5)

# Lowercase lambda is a Greek letter. 
# In computer science it typically means "make me a function" 
# or "I am defining an anonymous function".

def mysquare(x):
	return x*x

print map(mysquare, [1,2,3,4,5])

print map(lambda(x): x*x, [1,2,3,4,5])

print [x*x for x in [1,2,3,4,5]]

"""
The function map transforms a list by doing work to each of its elements.

We can use lambda to make an anonymous function just when we need one.

A list comprehension defines a new list by transforming an old one.

For more information:

MapReduce is a programming framework based on map and another function, 
reduce (surprise!) or fold that we have not yet covered. 
Google's distributed computing is based on this paradigm.
The word "comprehension" in "list comprehension" relates to the set 
comprehension notation in Mathematics.
"""

def odd_only(numbers):
	for n in numbers:
		if (n % 2) == 1:
			yield n

print [x for x in odd_only([1,2,3,4,5,6,7])]

# Small Words

# Write a Python generator function called small_words 
# that accepts a list of strings as input and yields 
# those that are at most 3 letters long.
def small_words(strings):
	for str in strings:
		if len(str) <= 3:
			yield str

# Expanding Exp
# This is very, very difficult.

grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]


def expand(tokens, grammar):
	for pos in range(len(tokens)):
		for rule in grammar:
			# hmmmm
			#print 'token ',tokens[pos]
			#print 'rule ', rule
			if rule[0] == tokens[pos]:
				yield tokens[0:pos] + rule[1] + tokens[pos+1:]

            
            
depth = 1
utterances = [["a", "exp"]]
for x in range(depth):
    for sentence in utterances:
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    print sentence
    
#    ['exp']
#    ['exp', '+', 'exp']
#    ['exp', '-', 'exp']
#    ['(', 'exp', ')']
#    ['num']


