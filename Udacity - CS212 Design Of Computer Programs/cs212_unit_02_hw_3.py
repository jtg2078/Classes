# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
	"Return (i, j) such that text[i:j] is the longest palindrome in text."
	# Your code here
	text = text.upper()
	max_i = 0
	max_j = 0
	max_count = 0
	min = 0
	max = len(text)
	for m in range(len(text)):
		# probing: assuming pal is going to be odd
		i = m - 1
		j = m + 1
		count = 2
		while i >= min and j < max and text[i] == text[j]:
			count += 1
			if count > max_count:
				max_count = count
				max_i = i
				max_j = j
			i -= 1
			j += 1
		# probing: assuming pal is going to be even
		i = m
		j = m + 1
		count = 1
		while i >= min and j < max and text[i] == text[j]:
			count += 1
			if count > max_count:
				max_count = count
				max_i = i
				max_j = j
			i -= 1
			j += 1
	if len(text) > 0:
		max_j += 1
	return (max_i, max_j)
		
def test():
	L = longest_subpalindrome_slice
	assert L('racecar') == (0, 7)
	assert L('Racecar') == (0, 7)
	assert L('RacecarX') == (0, 7)
	assert L('Race carr') == (7, 9)
	assert L('') == (0, 0)
	assert L('something rac e car going') == (8,21)
	assert L('xxxxx') == (0, 5)
	assert L('Mad am I ma dam.') == (0, 15)
	return 'tests pass'
	

print test()