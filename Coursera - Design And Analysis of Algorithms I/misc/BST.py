from random import randrange

class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.value = 0;
		
class BST:
	def __init__(self):
		self.root = None
	def search(self, node, key):
		if node == None:
			return None
		if key < node.key:
			return self.search(node.left, key)
		elif key > node.key:
			return self.search(node.right, key)
		else:
			return node.value
	def insert(self, key, value):
		if self.root == None:
			self.root = Node()
			self.root.key = key
			self.root.value = value 
			return
		node = self.root
		while node != None:
			if node.key == key:
				return
			elif node.key < key:
				if node.right == None:
					node.right = Node()
					node.right.key = key
					node.right.value = value
					return
				else:
					node = node.right
			else:
				if node.left == None:
					node.left = Node()
					node.left.key = key
					node.left.value = value
					return
				else:
					node = node.left
	def delete(self, key):
		if self.root == None:
			return
		node = self.root
		parent = None
		while node != None:
			if node.key == key:
				break
			elif node.key < key:
				parent = node
				node = node.right
			else:
				parent = node
				node = node.left
		if node == None: # key is not found
			return
		if node.left == None and node.right == None:
			if parent == None: # only one node in the tree
				self.root = None
			elif parent.right == node:
				parent.right = None
			else:
				parent.left = None
		elif node.left == None:
			if parent.right == node:
				parent.right = node.right
			else:
				parent.left = node.right
		elif node.right == None:
			if parent.right == node:
				parent.right = node.left
			else:
				parent.left = node.left
		else:
			# randomly choose a selection mode
			# 1. in-order successor
			# 2. in-order predecessor
			mode = randrange(1,3)
			if mode == 1:
				target = node.right
				while target.left != None:
					target = target.left
				self.delete(target.key)
				node.key = target.key
				node.value = target.value
			else:
				target = node.left
				while target.right != None:
					target = target.right
				self.delete(target.key)
				node.key = target.key
				node.value = target.value
	def traverse(self, node):
		if node ==  None:
			return
		self.traverse(node.left)
		print node.value
		self.traverse(node.right)
	def print_tree(self):
		self.traverse(self.root)

def	test_BST():
	bst = BST()
	input = [3,8,10,1,6,14,13,4,7]
	for n in input:
		key = n
		value = n
		bst.insert(key, value)
	print '---- printing the BST (in-order) ----'
	bst.print_tree()
	print '---- delete key(8) ----'
	bst.delete(8)
	print '---- printing the BST (in-order) ----'
	bst.print_tree()
	print '---- insert key(8) ----'
	bst.insert(8, 8)
	print '---- printing the BST (in-order) ----'
	bst.print_tree()
	

test_BST()
		
				
					
				
			
		
	
	
	



