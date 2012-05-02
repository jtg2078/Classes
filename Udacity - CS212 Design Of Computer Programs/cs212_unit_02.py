def compile_word(word):
	ten = 1
	result = []
	for c in reversed(word):
		if c.isalpha() and c.isupper():
			if ten > 1:
				result.append('+')
			result.append(str(ten))
			result.append('*')
			result.append(c)
			ten *= 10
		else:
			result.append(c)
	return ''.join(result)

print compile_word('YOU') #1*U+10*O+100*Y

# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????. 

import string, re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    

def all_ints():
	"Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
	# Your code here.
	yield 0
	for i in ints(1):
		yield i
		yield -i

limit = 10
i = 0
for z in all_ints():
	if i > limit:
		break
	print z
	i += 1
