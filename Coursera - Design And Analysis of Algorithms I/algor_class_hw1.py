def sort_and_countSplitInv(left, right):
	# print 'left=', left
	# print 'right=', right
	sorted = []
	count = 0
	# find out the total number of element
	n = len(left) + len(right)
	i = 0
	j = 0
	
	
	# loop through left and right list and
	# fill them into result array in order
	# and record the count if right is smaller than left
	for z in range(n):
		if i < len(left) and j < len(right):
			if left[i] <= right[j]:
				sorted.append(left[i])
				i+=1
			else:
				sorted.append(right[j])
				j+=1
				# the number of inversion are precisely the num of elements remain in left list
				count+=(len(left)-i)
		elif i < len(left): # right list is used up
			sorted.append(left[i])
			i+=1
		elif j < len(right): #left list is used up
			sorted.append(right[j])
			j+=1
	# print 'count=', count
	return [sorted, count]
	

def sort_and_count(m):
	# print 'm=', m
	if len(m) == 1:
		return [m, 0]
	else:
		x = sort_and_count(m[:len(m)/2])
		# print 'x=', x
		y = sort_and_count(m[len(m)/2:])
		# print 'y=', y
		z = sort_and_countSplitInv(x[0], y[0])
		# print 'z=', z
		count = x[1] + y[1] + z[1]
		# print 'count=', count
		# print '-------'
		return [z[0], count]
		
def hw1():
	print 'Reading hw1 input file into list'
	with open('IntegerArray.txt', 'r') as f:
		m = list(f.read().splitlines())
	m = map(int, m)
	print 'done reading the input file: IntegerArray.txt'
	print 'num of element in list m:', len(m)
	# print 'm: ', m
	print '-----------'
	print 'finding num of inversion....'
	result = sort_and_count(m)
	print 'num of inversion: ', result[1]
	# print 'sorted: ', result[0]

hw1()

# try1:2397819672 (was not correct because i did not convert input list into number properly)
# try2:2407905288 (correct answer)

