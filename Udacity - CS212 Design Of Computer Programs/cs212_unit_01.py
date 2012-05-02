# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.

def poker(hands):
	"Return the best hands: poker([hand,...]) => hand"
	return max(hands, key=hand_rank)
	
def poker_all_max(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
	"Return a list of all items equal to the max of the iterable."
	# prof's method
	result, maxval = [], None
	key = key or (lambda x: x)
	for x in iterable:
		xval = key(x)
		if not result or xval > maxval:
			result, maxval = [x], xval
		elif xval == maxval:
			result.append(x)
	return result
	# Your code here.
	max_hand = max(iterable, key=hand_rank)
	a = []
	for hand in iterable:
		if hand_rank(hand) == hand_rank(max_hand):
			a.append(hand)
	return a

def hand_rank(hand):
	"Return a value indicating the ranking of a hand"
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):            # straight flush
		return (8, max(ranks)) # 2 3 4 5 6 (8,6)  6 7 8 9 T (8, 10)
	elif kind(4, ranks):                           # 4 of a kind
		return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 (7, 9, 3)
	elif kind(3, ranks) and kind(2, ranks):        # full house
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):                              # flush
		return (5, ranks)                          # (5, [10,8,7,5,3])
	elif straight(ranks):                          # straight
		return (4, max(ranks))                     # (4, 11)
	elif kind(3, ranks):                           # 3 of a kind
		return (3, kind(3, ranks), ranks)          # (3, 7, [7,7,7,5,2])
	elif two_pair(ranks):                          # 2 pair
		return (2, two_pair(ranks), ranks)         # (2, 11, 3, [13,11,11,3,3])
	elif kind(2, ranks):                           # kind
		return (1, kind(2, ranks), ranks)          # (1, 2, [11,6,3,2,2])
	else:                                          # high card
		return (0, ranks)                          # (0, [7,5,4,3,2])

def card_ranks(cards):
	"Return a list of the ranks, sorted with higher first."
	method_to_use = 2
	if method_to_use == 1:
		# ---- method 1 ----
		ranks = [r for r,s in cards]
		rank_map = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
		ranks = [int(x) if x not in rank_map.keys() else rank_map[x] for x in ranks]
		ranks.sort(reverse = True)
		return ranks
	else:
		# ---- method 2 ----
		ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
		ranks.sort(reverse = True)
		# ---- prof's method for handing 1,2,3,4,5
		return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks
		# ---- my attemps ----
		special = [5, 4, 3, 2, 14]
		if len(set(ranks) - set([5, 4, 3, 2, 14])) == 0:
			return [5, 4, 3, 2, 1]
		else:
			return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) # Should output [14, 13, 4, 3]


def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight."
	# Your code here.
	return ranks[0] == ranks[1] + 1 == ranks[2] + 2 == ranks[3] + 3 == ranks[4] + 4
	# prof's version
	return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
	"Return True if all the cards have the same suit."
	# Your code here.
	suite = [s for r,s in hand]
	return suite[0] == suite[1] == suite[2] == suite[3] == suite[4]
	# prof's version
	suits = [s for r,s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n of.
	Return None if there is no n-of-a-kind in the hand."""
	# Your code here.
	current = -1
	counter = 0
	for r in ranks:
		if current != r:
			if counter == n:
				return current
			current = r
			counter = 1
		else:
			counter = counter + 1
	if counter == n:
		return current
	return None
	# prof's version
	for r in ranks:
		if ranks.count(r) == n:
			return r

def two_pair(ranks):
	"""If there are two pair, return the two ranks as a
	tuple: (highest, lowest); otherwise return None."""
	# Your code here.
	s = set()
	for r in ranks:
		if ranks.count(r) == 2:
			s.add(r)
	if len(s) == 2:
		return (max(s), min(s))
	else:
		return None

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
	# prof's code
	random.shuffle(deck)
	return [deck[n*i:n*(i+1)] for i in range(numhands)]
	# Your code here.
	for i in range(len(deck)-1, 0, -1):
		j = random.randint(0, i)
		tmp = deck[i]
		deck[i] = deck[j]
		deck[j] = tmp
	hands = []
	idx = 0
	for i in range(0, numhands):
		hand =[]
		for j in range(0, n):
			hand.append(deck[idx])
			idx = idx + 1
		hands.append(hand)
	return hands

def test():
	"Test cases for the functions in poker program."
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
	sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	tp = "5D 5C AS AH 4S".split() # Two pairs
	s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
	s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
	ah = "AS 2S 3S 4S 6C".split() # A high
	sh = "2S 3S 4S 6C 7D".split() # y high
	assert poker([sf, fk, fh]) ==  sf
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	# Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
	assert poker([fh]) == fh
	assert poker([fh] * 99 + [sf]) == sf
	assert hand_rank(sf) == (8, 10)
	#assert hand_rank(fk) == (7, 9, 7)
	#assert hand_rank(fh) == (6, 10, 7)
	assert card_ranks(sf) == [10, 9, 8, 7, 6]
	assert card_ranks(fk) == [9, 9, 9, 9, 7]
	assert card_ranks(fh) == [10, 10, 10, 7, 7]
	assert straight([9, 8, 7, 6, 5]) == True
	assert straight([9, 8, 8, 6, 5]) == False
	assert flush(sf) == True
	assert flush(fk) == False
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
	assert kind(4, fkranks) == 9
	assert kind(3, fkranks) == None
	assert kind(2, fkranks) == None
	assert kind(1, fkranks) == 7
	#assert two_pair(tpranks) == (14, 5)
	#assert two_pair(fkranks) == None
	srank = card_ranks(s1)
	assert straight(srank) == True
	assert poker_all_max([sf1, sf2, fk, fh]) == [sf1, sf2]
	return "tests pass"

print test()

print deal(5)

cards = [r+s for r in '23456789TJQKA' for s in 'SC']
print cards

x = [1, 2, 3]
y = [4, 5, 6]
print x+y
zipped = zip(x, y)
#print zipped

x = ['6C','7C','8C','9C','TC','5C','?B']
x.remove('?B')
y = [r+s for r in '23456789TJQKA' for s in 'SC']
z = [(a,b) for a in [x] for b in y ]
z = [x+[b] for b in y]
print z