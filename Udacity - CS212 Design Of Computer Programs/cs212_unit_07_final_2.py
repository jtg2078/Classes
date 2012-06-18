"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools

def solve():
	"Return a list of the names of the people, in the order they arrive."
	## your code here; you are free to define additional functions if needed
	days = monday, tuesday, wednesday, thursday, friday = [1,2,3,4,5]
	orderings = list(itertools.permutations(days))
	return next([Hamming, Knuth, Minsky, Simon, Wilkes]
				for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderings
				if Simon == Knuth - 1 # 6. Knuth arrived the day after Simon.
				for (laptop, droid, tablet, iphone, _) in orderings
				if laptop == wednesday # 1. The person who arrived on Wednesday bought the laptop.
				if tablet != friday # 8. The person who arrived on Friday didn't buy the tablet.
				for (programmer, writer, manager, designer, _ ) in orderings
				if programmer != Wilkes # 2. The programmer is not Wilkes.
				if writer != Minsky # 4. The writer is not Minsky.
				and designer != thursday  # 7. The person who arrived on Thursday is not the designer.
				and designer != droid # 9. The designer didn't buy the droid.
				and manager == Knuth - 1 # 10. Knuth arrived the day after the manager.
				and manager != tablet and Knuth != tablet # 5. Neither Knuth nor the person who bought the tablet is the manager.
				if ((programmer == Wilkes and droid == Hamming) or (programmer == Hamming and droid == Wilkes))
				# 3. Of the programmer and the person who bought the droid, one is Wilkes and the other is Hamming.
				and ((laptop == monday and Wilkes == writer) or (laptop == writer and Wilkes == monday))
				# 11. Of the person who bought the laptop and Wilkes, one arrived on Monday and the other is the writer.
				and (iphone == tuesday or tablet == tuesday)
				# 12. Either the person who bought the iphone or the person who bought the tablet arrived on Tuesday.
				)
				
def logic_puzzle():
	days = solve()
	ans = [''] * 5
	ans[days[0]-1] = 'Hamming'
	ans[days[1]-1] = 'Knuth'
	ans[days[2]-1] = 'Minsky'
	ans[days[3]-1] = 'Simon'
	ans[days[4]-1] = 'Wilkes'
	return ans
	
print logic_puzzle()
	
    
