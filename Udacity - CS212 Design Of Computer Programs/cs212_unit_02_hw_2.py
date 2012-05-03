#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
	# Your code here
	floors = bottom, second, third, forth, top = [1, 2, 3, 4, 5]
	orderings = list(itertools.permutations(floors))
	return next([Hopper, Kay, Liskov, Perlis, Ritchie]
				for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
				if Hopper is not top
				and Kay is not bottom
				and (Liskov is not top and Liskov is not bottom)
				and Perlis > Kay
				and abs(Ritchie - Liskov) != 1
				and abs(Liskov - Kay) != 1
				)
	
print floor_puzzle()