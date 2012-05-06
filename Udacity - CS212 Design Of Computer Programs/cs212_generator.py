# generator

# xrange doesnt create list right away
print (x*x for x in xrange(11))
g = (x*x for x in xrange(11))

print next(g)
print next(g)
print next(g)
print next(g)

def gen_square(n):
	i = 0
	while i <= n:
		yield i * i
		i += 1

f = gen_square(11)

print next(f)
print next(f)
print next(f)