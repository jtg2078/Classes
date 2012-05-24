# -------------------- cs253 unit 6 --------------------
import time

# complex_computation() simulates a slow function. time.sleep(n) causes the
# program to pause for n seconds. In real life, this might be a call to a
# database, or a request to another web service.
def complex_computation(a, b):
	time.sleep(.5)
	return a + b

# QUIZ - Improve the cached_computation() function below so that it caches
# results after computing them for the first time so future calls are faster
cache = {}
def cached_computation(a, b):
	if (a,b) not in cache:
		cache[(a,b)] = complex_computation(a, b)
	return cache[(a,b)]
		

def sect_05_cache():
	start_time = time.time()
	print cached_computation(5, 3)
	print "the first computation took %f seconds" % (time.time() - start_time)

	start_time2 = time.time()
	print cached_computation(5, 3)
	print "the second computation took %f seconds" % (time.time() - start_time2)


#Various methods on (dictionaries)
#[http://docs.python.org/release/2.5.2/lib/typesmapping.html], including clear().

#Note that you should always use clear() to empty a dictionary 
#rather than setting the dictionary empty directly, i.e:
"""
	d.clear()

	not

	d = {}

	The reason for this is that it can be the source of some subtle bugs.
"""


#handy link
#http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them
#maybe a link to itertools

SERVERS = ['SERVER1', 'SERVER2', 'SERVER3', 'SERVER4']

# QUIZ - implement the function get_server, which returns one element from the
# list SERVERS in a round-robin fashion on each call. Note that you should 
# comment out all your 'print get_server()' statements before submitting 
# your code or the grading script may fail. For more info see:
# http://forums.udacity.com/cs253-april2012/questions/22327/unit6-13-quiz-problem-with-submission

n = -1
def get_server():
	global n
	n += 1
	if n == len(SERVERS):
		n = 0
	return SERVERS[n]

print get_server()
print get_server()
print get_server()
print get_server()
print get_server()
print get_server()
print get_server()
print get_server()

# >>> SERVER1
# >>> SERVER2
# >>> SERVER3
# >>> SERVER4
# >>> SERVER1
# >>> SERVER2
# >>> SERVER3
# >>> SERVER4




