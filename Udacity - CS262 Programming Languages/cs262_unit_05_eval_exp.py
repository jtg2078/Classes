# Quiz: Eval Exp

# Write an eval_exp procedure to interpret JavaScript arithmetic expressions.
# Only handle +, - and numbers for now.

def eval_exp(tree):
	# ("number" , "5")
	# ("binop" , ... , "+", ... )
	nodetype = tree[0]
	if nodetype == "number":
		return int(tree[1])
	elif nodetype == "binop":
		left_child = tree[1]
		operator = tree[2]
		right_child = tree[3]
		# QUIZ: (1) evaluate left and right child
		# (2) perform "operator"'s work
		if operator == '+':
			return eval_exp(left_child) + eval_exp(right_child)
		elif operator == '-':
			return eval_exp(left_child) - eval_exp(right_child)

		

test_tree1 = ("binop",("number","5"),"+",("number","8"))
print eval_exp(test_tree1) == 13

test_tree2 = ("number","1776")
print eval_exp(test_tree2) == 1776

test_tree3 = ("binop",("number","5"),"+",("binop",("number","7"),"-",("number","18")))
print eval_exp(test_tree3) == -6

# QUIZ : Variable Lookup

# Adding variable lookup to the interpreter!

def eval_exp(tree, environment):
	nodetype = tree[0]
	if nodetype == "number":
		return int(tree[1])
	elif nodetype == "binop":
		left_value = eval_exp(tree[1], environment)
		operator = tree[2]
		right_value = eval_exp(tree[3], environment)
		if operator == "+":
			return left_value + right_value
		elif operator == "-":
			return left_value - right_value
	elif nodetype == "identifier":
		# ("binop", ("identifier","x"), "+", ("number","2"))
		# QUIZ: (1) find the identifier name
		# (2) look it up in the environment and return it
		variable_name = tree[1]
		return environment.get(variable_name)


# Here's some code to simulate env_lookup for now. It's not quite what we'll be
# using by the end of the course.

def env_lookup(env,vname): 
		return env.get(vname,None)

environment = {"x" : 2}
tree = ("binop", ("identifier","x"), "+", ("number","2"))
print eval_exp(tree,environment) == 4

# QUIZ: Evaluating Statements

def eval_stmts(tree, environment):
	stmttype = tree[0]
	if stmttype == "assign":
		# ("assign", "x", ("binop", ..., "+",  ...)) <=== x = ... + ...
		variable_name = tree[1]
		right_child = tree[2]
		new_value = eval_exp(right_child, environment)
		env_update(environment, variable_name, new_value)
	elif stmttype == "if-then-else": # if x < 5 then A;B; else C;D;
		conditional_exp = tree[1] # x < 5
		then_stmts = tree[2] # A;B;
		else_stmts = tree[3] # C;D;
		# QUIZ: Complete this code
		# Assume "eval_stmts(stmts, environment)" exists
		if eval_exp(conditional_exp, environment) == True:
			eval_stmts(then_stmts, environment)
		else:
			eval_stmts(else_stmts, environment)

		
def eval_exp(exp, env): 
		etype = exp[0] 
		if etype == "number":
				return float(exp[1])
		elif etype == "string":
				return exp[1] 
		elif etype == "true":
				return True
		elif etype == "false":
				return False
		elif etype == "not":
				return not(eval_exp(exp[1], env))

def env_update(env, vname, value):
		env[vname] = value
		
environment = {"x" : 2}
tree = ("if-then-else", ("true", "true"), ("assign", "x", ("number", "8")), ("assign", "x", "5"))
eval_stmts(tree, environment)
print environment == {"x":8}
	

# QUIZ: Evaluating Statements

def eval_stmts(tree, environment):
	stmttype = tree[0]
	if stmttype == "assign":
		# ("assign", "x", ("binop", ..., "+",  ...)) <=== x = ... + ...
		variable_name = tree[1]
		right_child = tree[2]
		new_value = eval_exp(right_child, environment)
		env_update(environment, variable_name, new_value)
	elif stmttype == "if-then-else": # if x < 5 then A;B; else C;D;
		conditional_exp = tree[1] # x < 5
		then_stmts = tree[2] # A;B;
		else_stmts = tree[3] # C;D;
		# QUIZ: Complete this code
		# Assume "eval_stmts(stmts, environment)" exists
		if eval_exp(conditional_exp, environment) == True:
			eval_stmts(then_stmts, environment)
		else:
			eval_stmts(else_stmts, environment)

		
def eval_exp(exp, env): 
		etype = exp[0] 
		if etype == "number":
				return float(exp[1])
		elif etype == "string":
				return exp[1] 
		elif etype == "true":
				return True
		elif etype == "false":
				return False
		elif etype == "not":
				return not(eval_exp(exp[1], env))

def env_update(env, vname, value):
		env[vname] = value
		
environment = {"x" : 2}
tree = ("if-then-else", ("true", "true"), ("assign", "x", ("number", "8")), ("assign", "x", "5"))
eval_stmts(tree, environment)
print environment == {"x":8}

# QUIZ : Frames
# Return will throw an excception
# Function Calls: new environments, catch return values

def eval_stmt(tree,environment):
	stmttype = tree[0]
	if stmttype == "call": # ("call", "sqrt", [("number","2")])
		fname = tree[1] # "sqrt"
		args = tree[2] # [ ("number", "2") ]
		fvalue = env_lookup(fname, environment)
		if fvalue[0] == "function":
			# We'll make a promise to ourselves:
			# ("function", params, body, env)
			fparams = fvalue[1] # ["x"]
			fbody = fvalue[2]
			fenv = fvalue[3]
			if len(fparams) <> len(args):
				print "ERROR: wrong number of args"
			else:
				#QUIZ: Make a new environment frame
				new_frame = {}
				for i in range(len(args)):
					new_frame[fparams[i]] = eval_exp(args[i], environment)
				new_environment = (fenv, new_frame)
				try:
					# QUIZ : Evaluate the body
					eval_stmts(fbody, new_environment) #notice the plural
					return None
				except Exception as return_value:
					return return_value
		else:
			print  "ERROR: call to non-function"
	elif stmttype == "return":
		retval = eval_exp(tree[1],environment) 
		raise Exception(retval) 
	elif stmttype == "exp": 
		eval_exp(tree[1],environment) 
			
def env_lookup(vname,env):
	if vname in env[1]:
		return (env[1])[vname]
	elif env[0] == None:
		return None
	else:
		return env_lookup(vname,env[0])

def env_update(vname,value,env):
	if vname in env[1]:
		(env[1])[vname] = value
	elif not (env[0] == None):
		env_update(vname,value,env[0])
				
def eval_exp(exp,env):
	etype = exp[0]		
	if etype == "number":
		return float(exp[1])
	elif etype == "binop":
		a = eval_exp(exp[1],env)
		op = exp[2]
		b = eval_exp(exp[3],env)
		if op == "*":
			return a*b
	elif etype == "identifier":
		vname = exp[1]
		value = env_lookup(vname,env)
		if value == None: 
			print "ERROR: unbound variable " + vname
		else:
			return value

def eval_stmts(stmts,env): 
	for stmt in stmts:
		eval_stmt(stmt,env) 



sqrt = ("function",("x"),(("return",("binop",("identifier","x"),"*",("identifier","x"))),),{})

environment = (None,{"sqrt":sqrt})

print eval_stmt(("call","sqrt",[("number","2")]),environment)	
		
		

			 

	