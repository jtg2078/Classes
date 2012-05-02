class WrongNumberOfPlayersError < StandardError ; end 
class NoSuchStrategyError < StandardError ; end

def rps_game_winner(game)
	raise WrongNumberOfPlayersError unless game.length == 2 
	# your code here
	game.each do |item|
		item[1] = item[1].downcase
		raise NoSuchStrategyError unless (item[1] == 'r' || item[1] == 'p' || item[1] == 's')
	end
	# Rock beats Scissors, Scissors beats Paper, but Paper beats Rock
	p1 = game[0]
	p2 = game[1]
	if p1[1] == p2[1]
		return p1
	elsif p1[1] == 'r'
		if p2[1] == 'p'
			return p2
		elsif p2[1] == 's'
			return p1
		end
	elsif p1[1] == 'p'
		if p2[1] == 'r'
			return p1
		elsif p2[1] == 's'
			return p2
		end
	elsif p1[1] == 's'
		if p2[1] == 'r'
			return p2
		elsif p2[1] == 'p'
			return p1
		end
	end
end


#print rps_game_winner([ [ "Armando", "r" ], [ "Dave", "S" ] ])


def rps_round_winner(games)
	round = []
	match = []
	i = 0
	games.each do |game|
		# your code here
		#print rps_game_winner(game)
		match << rps_game_winner(game)
		i = i + 1
		if i % 2 == 0
			print 'match: '
			print match
			round << match
			match = []
		end
	end
	print 'round: '
	print round
	if round.length == 1
		return rps_round_winner(round[0])
	#else
	#	rps_round_winner(round)
	end
end

def rps_round_winner(games)
	# your code here
	if games == nil
		return
	end
	tmp1 = []
	games.each do |tournament|
		tmp2 = []
		tournament.each do |game|
			tmp2 << rps_game_winner(game)
		end
		tmp1 << tmp2
	end
	return [tmp1]
end

#def rps_tournament_winner(games)
#	while games.length > 1
#		games = rps_round_winner(games)
#	end
#	print games
#	final = rps_round_winner(games)
#	return rps_game_winner(final[0][0])
#end

def rps_tournament_winner2(games)
	tournment = games
	z = 0
	orz = []
	advanced = []
	tournment.each do |round|
		if round.length == 1 # only 1 game in the tournment
			#print 'only 1 game part'
			#print  round[0]
			advanced << rps_game_winner(round[0])
		else
			# so there are 2 or 2^n games in it
			# what should i do? drill down?
			stop = false
			left = []
			current = round
			winner = []
			i = 0
			while stop == false
				match = []
				current.each do |game|
					if game.length == 1
						winner << game[0]
						stop = true
						break
					end
					match << rps_game_winner(game)
					i = i + 1
					if i % 2 == 0
						left << match
						match = []
						i = 0
					end
				end
				current = left
			end
			advanced << winner[0]
		end
		if advanced.length >= 2
			orz << advanced
			advanced = []
		end
	end
	if orz.length == 0 # this means that final winner is already found
		return advanced[0]
	else
		return rps_tournament_winner([orz])
	end
end

def rps_tournament_winner(tournaments)
	if(tournaments[0][1].kind_of?(Array) == false) #k we dont this is down to minimum
		return rps_game_winner(tournaments)
	else
		return rps_game_winner([rps_tournament_winner(tournaments[0]), rps_tournament_winner(tournaments[1])])
	end
end


data = 
[
	[
		[ ["Armando", "P"], ["Dave", "S"] ],
		[ ["Richard", "R"], ["Michael", "S"] ],
		[ ["Armando", "P"], ["Dave", "S"] ],
				[ ["Richard", "R"], ["Michael", "S"] ],
				[ ["Armando", "P"], ["Dave", "S"] ],
						[ ["Richard", "R"], ["Michael", "S"] ],
						[ ["Armando", "P"], ["Dave", "S"] ],
								[ ["Richard", "R"], ["Michael", "S"] ],
								[ ["Armando", "P"], ["Dave", "S"] ],
										[ ["Richard", "R"], ["Michael", "S"] ],
										[ ["Armando", "P"], ["Dave", "S"] ],
												[ ["Richard", "R"], ["Michael", "S"] ],
	],
	[
		[ ["Allen", "S"], ["Omer", "P"] ],
		[ ["David E.", "R"], ["Richard X.", "P"] ]
	] 
]

data2 = [[[ ["Armando", "P"], ["Dave", "S"] ]]]
data3 = [["Cx", "P"], ["Dx", "S"]]

data4 = [
  [
    [
      [ ["A1", "P"], ["A2", "S"] ],
      [ ["A3", "R"],  ["A4", "S"] ],           
    ],
    [
      [ ["Armando", "P"], ["Dave", "S"] ],
      [ ["Richard", "R"],  ["Michael", "S"] ], 
    ]
  ],
  [
    [
      [ ["Armando", "P"], ["Dave", "S"] ],
      [ ["Richard", "R"],  ["Michael", "S"] ], 
    ],
    [
      [ ["Armando", "P"], ["Dave", "S"] ],
      [ ["Richard", "R"],  ["Michael", "S"] ], 
    ]
  ]
]

# print rps_tournament_winner(data2)
# print rps_tournament_winner(data)
# print ' ---test2: '
# print rps_tournament_winner(data4)

# print rps_tournament_winner(data4)
# print ' ---- '
# print rps_tournament_winner(data3)

#z1 = rps_round_winner(data)
#print z1
#print '-------'
#z2 = rps_round_winner(z1)
#print z2
#print '-------'
#z3 = rps_round_winner(z2)
#print z3
#print '-------'
#print rps_tournament_winner(data)
# print rps_round_winner([[ [ "zrmando", "r" ], [ "Dave", "S" ] ], [ ["Richard", "R"], ["Michael", "S"] ]])


# [ [
# [ ["Richard", "R"], ["Michael", "S"] ], ],
# [
# [ ["Allen", "S"], ["Omer", "P"] ],
# [ ["David E.", "R"], ["Richard X.", "P"] ]
# ] ]