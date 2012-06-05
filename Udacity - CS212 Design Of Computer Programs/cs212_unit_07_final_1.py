"""
UNIT 1: Bowling:

You will write the function bowling(balls), which returns an integer indicating
the score of a ten-pin bowling game.  balls is a list of integers indicating 
how many pins are knocked down with each ball.  For example, a perfect game of
bowling would be described with:

	>>> bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
	300

The rules of bowling are as follows:

(1) A game consists of 10 frames. In each frame you roll one or two balls,
except for the tenth frame, where you roll one, two, or three.  Your total
score is the sum of your scores for the ten frames.
(2) If you knock down fewer than ten pins with your two balls in the frame,
you score the total knocked down.  For example, bowling([8, 1, 7, ...]) means
that you knocked down a total of 9 pins in the first frame.  You score 9 point
for the frame, and you used up two balls in the frame. The second frame will
start with the 7.
(3) If you knock down all ten pins on your second ball it is called a 'spare'
and you score 10 points plus a bonus: whatever you roll with your next ball.
The next ball will also count in the next frame, so the next ball counts twice
(except in the tenth frame, in which case the bonus ball counts only once).
For example, bowling([8, 2, 7, ...]) means you get a spare in the first frame.
You score 10 + 7 for the frame; the second frame starts with the 7.
(4) If you knock down all ten pins on your first ball it is called a 'strike'
and you score 10 points plus a bonus of your score on the next two balls.
(The next two balls also count in the next frame, except in the tenth frame.)
For example, bowling([10, 7, 3, ...]) means that you get a strike, you score
10 + 7 + 3 = 20 in the first frame; the second frame starts with the 7.

"""
def bowling(balls):
	"Compute the total score for a player's game of bowling."
	## bowling([int, ...]) -> int
	## your code here
	frames = [0] * 10
	i = 0
	f = 0
	while f < 9:
		score = balls[i]
		if score == 10:
			frames[f] = (10, 'strike')
			f += 1
			i += 1
		else:
			s1 = balls[i]
			i += 1
			s2 = balls[i]
			frames[f] = (s1, s2)
			i += 1
			f += 1
	# last frame
	last = 0
	if balls[i] == 10 or balls[i] + balls[i+1] == 10:
		frames[f] = (balls[i],  balls[i+1])
		last = balls[i+2]
	else:
		frames[f] = (balls[i], balls[i+1])
	f = 0
	score  = 0
	while f < 9:
		if frames[f] == (10, 'strike'):
			if frames[f + 1] == (10, 'strike'):
				score += (10 + 10 + frames[f + 2][0])
			else:
				score += (10 + frames[f + 1][0] + frames[f + 1][1])
			f += 1
		else:
			s1, s2 = frames[f]
			if s1 + s2 == 10:
				score += (10 + frames[f + 1][0])
			else:
				score += (s1 + s2)
			f += 1
	return score + sum(frames[f]) + last
		
		
def test_bowling():
	assert   0 == bowling([0] * 20)
	assert  20 == bowling([1] * 20)
	assert  80 == bowling([4] * 20)
	assert 190 == bowling([9,1] * 10 + [9])
	assert 300 == bowling([10] * 12)
	assert 200 == bowling([10, 5,5] * 5 + [10])
	assert  11 == bowling([0,0] * 9 + [10,1,0])
	assert  12 == bowling([0,0] * 8 + [10, 1,0])
	

z = [0,0] * 9 + [10,1,0]
print z
print bowling(z)
test_bowling()
	
   