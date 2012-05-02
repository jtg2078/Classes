class Node:
	def __init__(self):
		self.value = 0
		self.next = None
		self.original_key = 0

class SimpleHashTable:
	def __init__(self):
		# choose n to be a prime (with constant actor of # of objects in table)
		# not too close to a power of 2
		# not too close to a power of 10
		# input range:	 	1 to 1 million
		# num of objects:	100k
		# 2^17 = 131 072
		# 2^16 = 65 536 
		# 10^5 = 100 000
		# some primes between 100k to 110k: 100 417, 101 771, 103 291, ...
		# ok lets pick 103291 as n
		self.n = 103291
		self.buckets = [None] * self.n
		self.keys = []
	
	def ghetto_hash_function(self, input):
		return input % self.n
	
	def get_bucket_for_key(self, key):
		hash = self.ghetto_hash_function(key)
		bucket = self.buckets[hash]
		return bucket
	
	def get_object_for_key(self, key):
		bucket = self.get_bucket_for_key(key)
		while bucket != None:
			if bucket.original_key == key:
				return bucket.value
			else:
				bucket = bucket.next
		return None
	
	def set_object_for_key(self, object, key):
		bucket = self.get_bucket_for_key(key)
		if bucket == None:
			bucket = Node()
			bucket.value = object
			hash = self.ghetto_hash_function(key)
			self.buckets[hash] = bucket
		else:
			while bucket.next != None:
				if bucket.original_key == key:
					bucket.value = object
					return
				else:
					bucket = bucket.next
			new_node = Node()
			new_node.value = object
			new_node.original_key = key
			bucket.next = new_node
			self.keys.append(key)
			
def hw5_using_custom_hashtable():
	file_name = 'HashInt.txt'
	print 'Reading hw5 input file {0} into a custom hashtable'.format(file_name)
	myHashTable = SimpleHashTable()
	with open(file_name, 'r') as f:
		for line in f:
			tokens = line.split()
			number = int(tokens[0])
			myHashTable.set_object_for_key(number, number)
	print 'Done reading the input file: ', file_name
	print '-----------------------------------------'
	print 'Solving the two-sum problem set...'
	target_sums = [231552, 234756, 596873, 648219, 726312, 981237, 988331, 1277361, 1283379];
	result = [0] * len(target_sums)
	i = 0
	for sum in target_sums:
		for key in myHashTable.keys:
			num1 = key
			num2 = sum - num1
			obj = myHashTable.get_object_for_key(num2)
			if obj != None:
				result[i] = 1
				break
		i = i + 1
	
	print 'target sums: '
	pprint(target_sums)
	print 'result: '
	pprint(result)
	print 'formatted result: ' + ''.join(map(str, result))


from pprint import pprint
def hw5_using_built_in_hashtable():
	file_name = 'HashInt.txt'
	print 'Reading hw5 input file {0} into a hashtable'.format(file_name)
	hashtable = {}
	with open(file_name, 'r') as f:
		for line in f:
			tokens = line.split()
			number = int(tokens[0])
			hashtable[number] = number
	print 'Done reading the input file: ', file_name
	print '-----------------------------------------'
	print 'Solving the two-sum problem set...'
	target_sums = [231552, 234756, 596873, 648219, 726312, 981237, 988331, 1277361, 1283379];
	result = [0] * len(target_sums)
	i = 0
	for sum in target_sums:
		for key in hashtable.keys():
			num1 = key
			num2 = sum - num1
			if num2 in hashtable:
				result[i] = 1
				break
		i = i + 1
	
	print 'target sums: '
	pprint(target_sums)
	print 'result: '
	pprint(result)
	print 'formatted result: ' + ''.join(map(str, result))

hw5_using_built_in_hashtable()
hw5_using_custom_hashtable() # wow this is almost 10 times slower....haha