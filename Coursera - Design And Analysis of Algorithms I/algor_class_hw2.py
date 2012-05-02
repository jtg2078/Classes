def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def partition(a, l, r):
	pVal = a[l]
	i = l + 1
	for j in range(l + 1, r + 1):
		if a[j] < pVal:
			swap(a, j, i)
			i =  i + 1
	swap(a, l, i - 1)
	return i - 1

def choose_pivot(arr, l, r, mode):
	if mode == 'first':
		swap(arr, l, l)
	elif mode == 'last':
		swap(arr, l, r)
	elif mode == 'median':
		mid = int(l +(r-l) / 2)
		a = arr[l]
		b = arr[mid]
		c = arr[r]
		p = l;
		if a <= b <= c or c <= b <= a:
			p = mid
		elif b <= a <= c or b >= a >= c:
			p = l
		else:
			p = r
		swap(arr, l, p)

def quick_sort(a, l, r, mode):
	if l < r:
		choose_pivot(a, l, r, mode)
		p = partition(a, l, r)
		return (r - l) + quick_sort(a, l, p - 1, mode) + quick_sort(a, p + 1, r, mode)
	return 0

def hw2():
	print 'Reading hw2 input file into list'
	with open('QuickSort.txt', 'r') as f:
		m = list(f.read().splitlines())
	q1 = map(int, m)
	q2 = map(int, m)
	q3 = map(int, m)
	print 'Done reading the input file: QuickSort.txt'
	print 'Num of elements in the list m:', len(m)
	print '-----------'
	print 'Question 1, using first element as pivot...'
	count = quick_sort(q1, 0, len(q1) - 1, 'first')
	print 'Question 1 answer(num of comparison):', count
	print '-----------'
	print 'Question 2, using last element as pivot...'
	count = quick_sort(q2, 0, len(q2) - 1, 'last')
	print 'Question 2 answer(num of comparison):', count
	print '-----------'
	print 'Question 3, using median of the three element(first, middle, last) as pivot...'
	count = quick_sort(q3, 0, len(q3) - 1, 'median')
	print 'Question 3 answer(num of comparison):', count

hw2()

