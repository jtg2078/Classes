#cs252 week 4
import hashlib

def test_sha_256(str):
	return hashlib.sha256(str).hexdigest()
	
print test_sha_256('udacity')


def hash_str(s):
	return hashlib.md5(s).hexdigest()

# -----------------
# User Instructions
# 
# Implement the function make_secure_val, which takes a string and returns a 
# string of the format: 
# s,HASH

def make_secure_val(s):
	return '{0},{1}'.format(s, hash_str(s))
	
print make_secure_val('udacity')


def hash_str(s):
	return hashlib.md5(s).hexdigest()

def make_secure_val(s):
	return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
	###Your code here
	str = h.split(',')
	if hash_str(str[0]) == str[1]:
		return str[0]
	else:
		return None

s = 'udacity'
input = make_secure_val(s)
print 'input: ', input


print check_secure_val(input) == s
print check_secure_val('udacIty,1497d98baea787eb6a8a676145c44212') == None

import hmac

print hmac.new('secert', 'udacity').hexdigest()

import hmac

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'
def hash_str(s):
	###Your code here
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
	val = h.split('|')[0]
	if h == make_secure_val(val):
		return val
	
x = make_secure_val('hello')
print x

print check_secure_val(x + 'abc')

print make_secure_val('jason')
print make_secure_val('jason')
print make_secure_val('jason')

import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
	###Your code here
	x = list(string.ascii_lowercase)
	random.shuffle(x)
	return ''.join(x[:5])

def make_salt_prof():
	return ''.join([random.choice(string.letters) for x in xrange(5)])
	
print make_salt()
print make_salt_prof()

import random
import string
import hashlib

def make_salt():
	return ''.join(random.choice(string.letters) for x in xrange(5))

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

def make_pw_hash(name, pw):
	###Your code here
	salt =  make_salt()
	return '%s,%s' % (hashlib.sha256(name + pw +salt).hexdigest(), salt)

print make_pw_hash('jason', 'stonybrook')

import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# Implement the function valid_pw() that returns True if a user's password 
# matches its hash. You will need to modify make_pw_hash.

def make_pw_hash(name, pw):
	salt = make_salt()
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
	###Your code here
	h = h.split(',')
	salt = h[1]
	h1 = hashlib.sha256(name + pw + salt).hexdigest()
	return h[0] == h1
	
def make_pw_hash(name, pw, salt = make_salt()):
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
	###Your code here
	return h == make_pw_hash(name, pw, h.split(',')[1])

h = make_pw_hash('spez', 'hunter2')
print valid_pw('spez', 'hunter2', h)





    



	