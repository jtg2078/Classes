# -------------------- unit 02 --------------------

# specify HTML + JavaScript using regular expression
# HTML: Hyper Text Markup Language

# Lexical Analysis
#
# lexicon 	break down into words
# (using regular expression)

# Token		smallest unit of lexical analysis outputs:
#			words, strings, number, punctuation
#			(white spaces are omitted)
#
# string -> Lexical Analysis -> list of tokens

# Some HTML Tokens
# LANGLE		<
# LANGLESLASH	</
# RANGLE		>
# EQUAL			=
# STRING		"google.com"
# WORD			(anything else, e.g. Welcome!)

# def t_RANGLE(token):
#   (token)(name)
#
#	r'>' (regexp matching this token)
#
#	return token

# We use regular expressions to specify tokens. In this class we will use a 
# particular Python syntax for defining tokens.
#
# For more information:
#
# The particular syntax we'll use to define tokens comes from 
# PLY, the Python Lex-Yacc project.
# http://www.dabeaz.com/ply/
#
def t_LANGLESLASH(token):
	r"</"
	return token

def t_NUMBER(token):
	r"[0-9]+"
	token.value = int(token.value)
	return token

# input "1368"  => output 1368

def t_STRING(token):
	r'"[^"]*"'
	return token

def t_WHITESPACE(token):
	r' '
	pass

# print re.findall('[^<> ]+', "ast ro no my") ['ast', 'ro', 'no', 'my']
def t_WORD(token):
	r'[^<> ]+'
	return token

# a lexical analyzer is a collection of token definitions
# a.k.a lexer

# use ordering of lexer to resolve ambiguity

# whitespace string word

def t_STRING(token):
	r'"[^"]*"'
	token.value = token.value[1:-1] #snipping off ""
	return token

def t_newline(token):
	r'\n'
	token.lexer.lineno += 1
	pass


# Crafting Input
#
# Define a variable called webpage that holds a string that causes our
# lexical
# analyzer to produce the exact output below
#
# LexToken(WORD,'This',1,0)
# LexToken(WORD,'is',1,5)
# LexToken(LANGLE,'<',2,11)
# LexToken(WORD,'b',2,12)
# LexToken(RANGLE,'>',2,13)
# LexToken(WORD,'webpage!',2,14)
def unit_02_20_crafting_input():
	webpage = "This is   \n<b>webpage!"
	tokens = ('LANGLE', # <
	          'LANGLESLASH', # </
	          'RANGLE', # >
	          'EQUAL', # =
	          'STRING', # "hello"
	          'WORD', # Welcome!
	          )
	t_ignore = ' ' # shortcut for whitespace
	htmllexer = lex.lex()
	htmllexer.input(webpage)
	while True:
	    tok = htmllexer.token()
	    if not tok: break
	    print tok

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token

# in HTML, comment starts with 
# <!-- comments -->

# Identifier

# Identifiers are textual string descriptions that refer to program elements,
# such as variables and functions. Write a indentifier token rule for Javascript identifiers.

# The token rule should match:

#   factorial
#   underscore_separated
#   mystery
#   ABC

# The token rule should not match:

#   _starts_wrong
#   123


def t_IDENTIFIER(token):
    r'[a-zA-Z]+[_a-zA-Z]*'
    return token

# Numbers

# Write a indentifier token rule for Javascript numbers that converts the value
# of the token to a float.

# The token rule should match:

#    12
#    5.6
#    -1.
#    3.14159
#    -8.1
#    867.5309

# The token rule should not match:

#    1.2.3.4
#    five
#    jenny

def t_NUMBER(token):
    r'-?[0-9]+(?:\.?[0-9]*)?'
    return token

# in python end-of-line ia #
# in JavaScript end-of-line is //

# unit 02 hw 01
# see the file cs262_unit_02_hw_1.py