# -------------------- cs262 unit 6 --------------------
"""
A JavaScript program may contain zero, one or many calls to write(). We will use environments to capture the output of a JavaScript program. 
"""

"""
A good test case gives us confidence that a program implementation adheres to its specification. In this situation, a good test case reveals a bug. 
"""

"""
We use testing to gain confidence that an implementation (a program) adheres to it specification (the task at hand). If a program accepts an infinite set of inputs, testing alone cannot prove that program's correctness. Software maintenance (i.e., testing, debugging, refactoring) carries a huge cost. 
"""

"""
Steve Fink of Mozilla talks about testing in the real world. The "range error" example he mentions is related to array bounds checking, a critical language feature for both correctness and security. He argues for simple test cases with obvious control flow, and talks about removing parts of a test case to help localize the fault. 
"""

"""
My old job localizing compiler bugs by shrinking test cases is now almost completely automated by Delta Debugging, Andreas Zeller's scientific approach to debugging.
On a personal note, Udacity will be offering a course on debugging by Andreas Zeller in a bit. I highly recommend that you take it — Andreas is a great guy and he explains things clearly.
"""

"""
Steve Fink of Mozilla talks about optimization in the real world. Mozilla's JavaScript interpreter is called SpiderMonkey, and it has gone through a number of different just-in-time (JIT) optimization architectures. He reminds us that you must always be aware of the cost of an optimization. He also notes that it is rare that a software engineer spends the entire day writing new code — looking over old code is very important and time-consuming. 
"""

"""
In this class we will optionally perform optimization after parsing but before interpreting. Our optimizer takes a parse tree as input and returns a (simpler) parse tree as output. 
"""

# Optimization Phase

def optimize(tree): # Expression trees only
	etype = tree[0]
	if etype == "binop":
		a = tree[1]
		op = tree[2]
		b = tree[3]
		if op == "*" and b == ("number","1"):
			return a
		# QUIZ: It only handles A * 1
		# Add in support for A * 0  and A + 0
		if op == '*' and b == ('number', '0'):
			return b
		if op == '+' and b == ('number', '0'):
			return a

		return tree
    

print optimize(("binop",("number","5"),"*",("number","1"))) == ("number","5")
print optimize(("binop",("number","5"),"*",("number","0"))) == ("number","0")
print optimize(("binop",("number","5"),"+",("number","0"))) == ("number","5")

"""
We desire an optimizer that is recursive. We should optimize the child nodes of a parse tree before optimizing the parent nodes. 
"""

# Optimization Phase

def optimize(tree): # Expression trees only
	etype = tree[0]
	if etype == "binop":
		# Fix this code so that it handles a + ( 5 * 0 )
		# recursively! QUIZ!
		a = optimize(tree[1])
		op = tree[2]
		b = optimize(tree[3])
		if op == "*" and b == ("number","1"):
			return a
		elif op == "*" and b == ("number","0"):
			return ("number","0")
		elif op == "+" and b == ("number","0"):
			return a
	return tree
	

print optimize(("binop",("number","5"),"*",("number","1"))) == ("number","5")
print optimize(("binop",("number","5"),"*",("number","0"))) == ("number","0")
print optimize(("binop",("number","5"),"+",("number","0"))) == ("number","5")
print optimize(("binop",("number","5"),"+",("binop",("number","5"),"*",("number","0")))) == ("number","5")

"""
A fuller answer would replace return tree with return (etype, a, op, b) at the end. The question only asked you to handle a+(5*0), but we would really like to be more general as well. 
"""

"""
Genetic Programming uses evolutionary algorithms inspired by biological notions to find computer programs that have certain properties. It is possible to use such evolutionary computation to automatically repair defects in programs. 
"""
