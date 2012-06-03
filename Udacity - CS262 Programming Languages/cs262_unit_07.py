# -------------------- cs262 unit 7 (last) --------------------
"""
Dave Herman, a researcher at Mozilla, talks about changes to JavaScript. JavaScript started as a simple language but has evolved into the language of the Web. One prominent feature under development is a a module system. 
"""

# Crafting Token Specifications

# Define a variable regexp that matches numbers with 1 or more leading digits
# and an optional . followed by 0 or more digits.

regexp = "[0-9]+(?:\.[0-9]*)?"

import re

tests = [("123", True), ("1.2", True), ("1.", True), (".5", False), (".5.6", False), ("1..2", False)]

for r, ans in tests:
	print (re.findall(regexp, r) == [r]) == ans


# Learning Regular Expressions

# Define a variable regexp that matches the left 3 strings but not the right 3.

#   Yes     No
#   aaa    aabbb
#   abb    aaccc
#   acc     bc


regexp = "(?:a(?:b|c)+|a+)"

import re 

tests = [("aaa", True), ("abb", True), ("acc", True), ("aabbb", False), ("aaccc", False), ("bc", False)]

for r, ans in tests:
	print (re.findall(regexp, r) == [r]) == ans

"""
For more information:

    Learning theory (i.e., a theory of how we learn) often comes up in education. The computer science equivalent is computational learning theory.
    Overfitting, in which one constructs a model that is very complex relative to the observations, is a problem in both statistics and also in machine learning. 
"""

"""
Dave Herman talks about security and languages at Mozilla. One key concept is the trusted computing base, which we want to be as small as possible. Languages like C++ admit buffer overflows, a source of security exploits. The halting problem prevents us from perfectly detecting malicious code or webpages statically.

For more information:

    Computer security is a critical area in computer science. 
"""
# List Comprehensions

# Write a short Python program that for all numbers x between 0 and 99 prints
# x^3 (x*x*x), but only if x is even and x^3 < 20.

print [x*x*x for x in range(100) if x % 2 == 0 and x*x*x  < 20]

"""
To spice up the quiz, we introduce the function reduce (also known as fold).

For more information:

    Sudoku is a number-placement puzzle. 
"""

# Fix the Bug

def count(number, row):
    return reduce(lambda acc, this: (1 + acc) if this == number else acc, row, 0)

def horiz_checker(board):
    size = len(board)
    for row in range(size):
        if not (all(map(lambda x : count(x, board[row]) <= 1, board[row]))): return False
    return True

board_good = [[1,2,3],
              [4,5,6],
              [7,8,9]]

board_bad = [[1,1,1],
             [4,5,6],
             [7,8,9]]

board_bug = [[1,2,3],
             [4,4,4],
             [7,8,9]]

print horiz_checker(board_good)
print horiz_checker(board_bad)
print horiz_checker(board_bug)