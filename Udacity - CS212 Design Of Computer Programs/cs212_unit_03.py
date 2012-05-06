'cs212 week 3'

# Python
# - statements
# - expressions
# - format
# - class: operator overloading
# - domain specific langauge

# the main scope of this unit, we will learn about
# - language
# - grammer
# - compiler
# - interpreter
# - design tool

"""
First, a literal of some string 's'. For example, if we say lit('a') then that describes the language consisting of just the character string "a" and nothing else.

We have the API call seq(x, y). We could say seq(lit('a'), lit('b')), and that would consist of just the string "ab." So far not very interesting.

Then we could say alt(x, y). Similarly, alt(lit('a'), lit('b')), and that would consist of two possibilities -- either the string "a" or the string "b." We'll use the standard notation for the name of our API call here.

star(x) stands for any number of repetitions -- zero or more. star(lit('a')) would be the empty string or "a" or "aa" and so on.

We can say oneof(c) and then string of possible characters. That's that same as the alternative of all the individual characters. oneof('abc') matches "a" or "b" or "c." It's a constrained version of the alt function.

We'll use the symbol "eol," standing for "end of line" to match only the end of a character string and nowhere else. What matches is the empty string, but it matches only at the end. The only example we can give is "eol" itself, and we can give an example of seq(lit('a'), eol), and that matches exactly the "a" and nothing else at the end.

Then we'll add dot, which matches any possible character -- a, b, c, any other character in the alphabet.

			API
Grammar				Example						Language
lit(s)				lit('a')					{a}
seq(x,y)			seq(lit('a'), lit('b'))		{ab}
alt(x,y)			alt(lit('a'),lit('b'))		{a,b}
star(x)				star(lit('a'))				{'',a,aa,aaa,...}
oneof(c)			oneof('abc')				{a,b,c}
eol					eol							{''}
					seq(lit('a'), eol)			{a}
dot					dot							{a,b,c,....}

But what if we're matching with the pattern -- let's say we have the expression 'a*b+' -- any number of a's followed by one or more b's?

In our API notation, we would write that as seq(star(lit('a')), plus(lit('b'))).


"""

'Regular Expression'

# API: application programming interface
# lit(s): consist of string and nothing else
# seq(x,y): {ab}
# alt(x,y): either a or b: {a,b}
# star(x): any number of x
# eol: end of line ....

'We are going to build something similiar to Regular Expression'

# pattern
# text - result
# partial result
# control over iteration

#----------------
# User Instructions
#
# The function, matchset, takes a pattern and a text as input
# and returns a set of remainders. For example, if matchset 
# were called with the pattern star(lit(a)) and the text 
# 'aaab', matchset would return a set with elements 
# {'aaab', 'aab', 'ab', 'b'}, since a* can consume one, two
# or all three of the a's in the text.
#
# Your job is to complete this function by filling in the 
# 'dot' and 'oneof' operators to return the correct set of 
# remainders.
#
# dot:   matches any character.
# oneof: matches any of the characters in the string it is 
#		called with. oneof('abc') will match a or b or c.
def matchset(pattern, text):
	"Match pattern at start of text; return a set of remainders of text."
	op, x, y = components(pattern)
	if 'lit' == op:
		return set([text[len(x):]]) if text.startswith(x) else null
	elif 'seq' == op:
		return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
	elif 'alt' == op:
		return matchset(x, text) | matchset(y, text)
	elif 'dot' == op:
		return set([text[1:]]) if text else null
	elif 'oneof' == op:
		# correct version, it means any of character in x
		return set([text[1:]]) if text.startswith(x) else null # startswith accepts tuple
		# i guess i got the meaning wrong
		#return set(t2 for t1 in x for t2 in matchset(('lit', t1), text))
	elif 'eol' == op:
		return set(['']) if text == '' else null
	elif 'star' == op:
		return (set([text]) |
				set(t2 for t1 in matchset(x, text)
					for t2 in matchset(pattern, t1) if t1 != text))
	else:
		raise ValueError('unknown pattern: %s' % pattern)
		
null = frozenset()

def components(pattern):
	"Return the op, x, and y arguments; x and y are None if missing."
	x = pattern[1] if len(pattern) > 1 else None
	y = pattern[2] if len(pattern) > 2 else None
	return pattern[0], x, y
   
def unit_3_6_matchset():
	assert matchset(('lit', 'abc'), 'abcdef') == set(['def'])
	assert matchset(('seq', ('lit', 'hi '),
					 ('lit', 'there ')), 
				   'hi there nice to meet you')	== set(['nice to meet you'])
	assert matchset(('alt', ('lit', 'dog'), 
					('lit', 'cat')), 'dog and cat') == set([' and cat'])
	assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
	assert matchset(('oneof', 'a'), 'aabc123') == set(['abc123'])
	assert matchset(('eol',),'') == set([''])
	assert matchset(('eol',),'not end of line') == frozenset([])
	assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])
	
	return 'unit_3_6_matchset tests pass'

print unit_3_6_matchset()

#---------------
# User Instructions
#
# Fill out the API by completing the entries for alt, 
# star, plus, and eol.


def lit(string):  return ('lit', string)
def seq(x, y):    return ('seq', x, y)
def alt(x, y):    return ('alt', x, y)
def star(x):      return ('star', x)
def plus(x):      return seq(x, star(x))
def opt(x):       return alt(lit(''), x)
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def unit_3_7_filling_out_the_api():
    assert lit('abc')         == ('lit', 'abc')
    assert seq(('lit', 'a'), 
               ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
    assert alt(('lit', 'a'), 
               ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
    assert star(('lit', 'a')) == ('star', ('lit', 'a'))
    assert plus(('lit', 'c')) == ('seq', ('lit', 'c'), 
                                  ('star', ('lit', 'c')))
    assert opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
    assert oneof('abc')       == ('oneof', ('a', 'b', 'c'))
    return 'unit_3_7_filling_out_the_api tests pass'

print unit_3_7_filling_out_the_api()

"""
Let's just review what we've defined in terms of our API. We have a function match and a function search, and they both take a pattern and a text, and they both return a string representing the earliest longest match.


match(p, t) -> '...'
search(p, t) -> '...'
But for match the string would only return if it's at the start of the string. For search, it'll be anywhere within the string. If they don't match, then they return None.

We've also defined an API of functions to create patterns -- a literal string, an alternative between two patterns x and y, a sequence of two patterns x and y, and so on. That's sort of the API that we expect the programmer to program to. You create a pattern on this side and then you use a pattern over here against a text to get some result. Then below the line of the API -- sort of an internal function -- we've defined matchset, which is not really designed for the programmer to call it. It was designed for the programmer to go through this interface (match and search), but this function is there. It also takes a pattern and a text. Instead of returning a single string, which is a match, it returns a set of strings, which are remainders. For any remainder we have the constraint that the match plus the remainder equals the original text. Here I've written versions of search and match. We already wrote matchset. The one part that we missed out was this component that pulls out the x, y and op components out of a tuple. I've left out two pieces of code here that I want you to fill in.
"""

#---------------
# User Instructions
#
# Complete the search and match functions. Match should
# match a pattern only at the start of the text. Search
# should match anywhere in the text.

def search(pattern, text):
	"Match pattern anywhere in text; return longest earliest match or None."
	for i in range(len(text)):
		m = match(pattern, text[i:])
		#if m: # wrong, cant use this, since ' ' would be false
		if m is not None:
			return m
        
def match(pattern, text):
	"Match pattern against start of text; return longest match found or None."
	remainders = matchset(pattern, text)
	if remainders:
		shortest = min(remainders, key=len)
		# prof's version
		return text[:len(text)-len(shortest)]
		# my quiz answer
		return text[:text.index(shortest)] if text.index(shortest) else text
    
def components(pattern):
    "Return the op, x, and y arguments; x and y are None if missing."
    x = pattern[1] if len(pattern) > 1 else None
    y = pattern[2] if len(pattern) > 2 else None
    return pattern[0], x, y

def matchset(pattern, text):
    "Match pattern at start of text; return a set of remainders of text."
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
    elif 'dot' == op:
        return set([text[1:]]) if text else null
    elif 'oneof' == op:
        return set([text[1:]]) if text.startswith(x) else null
    elif 'eol' == op:
        return set(['']) if text == '' else null
    elif 'star' == op:
        return (set([text]) |
                set(t2 for t1 in matchset(x, text)
                    for t2 in matchset(pattern, t1) if t1 != text))
    else:
        raise ValueError('unknown pattern: %s' % pattern)
    
null = frozenset()

def lit(string):  return ('lit', string)
def seq(x, y):    return ('seq', x, y)
def alt(x, y):    return ('alt', x, y)
def star(x):     return ('star', x)
def plus(x):      return seq(x, start(x))
def opt(x):       return alt(lit(''), x)
def oneof(chars): return ('oneof', tuple(chars))
dot = ('dot',)
eol = ('eol',)

def unit_3_8_search_and_match():
    assert match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
    assert match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
    assert match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
    assert search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'
    return 'unit_3_8_search_and_match tests pass'

print unit_3_8_search_and_match()

"""
12. 9 Compiling
Let's quickly summarize how a language interpreter works.

For regular expressions we have patterns like (a|b)+, which define languages. A language is a set of strings like {a, b, ab, ba, ...} and so on, defined by that pattern.

Then we have interpreters like matchset, which in this case takes a pattern and a text and returns a list of strings or a set of strings.

So we saw that matchset is an interpreter because it takes a description of the language, namely a pattern as a data structure, and operates over that pattern. Here's the definition of matchset.

You see it looks at the pattern, breaks out its components, and then the first thing it does is this big case statement to figure out what type of operator we have and to do the appropriate thing.

There's an inherent inefficiency here in that the pattern is defined once, and it's always the same pattern over a long string of text and maybe over many possible texts.

We want to apply the same pattern to many texts. Yet every time we get to that pattern, we're doing this same process of trying to figure out what operator we have when, in fact, we should already know that, because the pattern static, is constant.

So this is kind of repeated work. We're doing this over and over again for no good reason.

There's another kind of interpreter called a "compiler" which does that work all at once. The very first time when the pattern is defined we do the work of figuring out which parts of the pattern are which so we don't have to repeat that every time we apply the pattern to a text.

Where an interpreter takes a pattern and a text and operates on those, a compiler has two steps. In the first step, there is a compilation function, which takes just the pattern and returns a compiled object, which we'll call c. Then there's the execution of that compiled object where we take c and we apply that to the text to get the result.

Here work can be done repeatedly every time we have a text.

Here the work is split up. Some of it is done in the compilation stage to get this compiled object. Then the rest of it is done every time we get a new text. Let's see how that works.

Here is the definition of the interpreter. Let's focus just on this line here:


Toggle line numbers
   1 def matchset(pattern, text):
   2     "Match pattern at start of text; return a set of remainders of text."
   3     op, x, y = components(pattern)
   4     if 'lit' == op:
   5         return set([text[len(x):]]) if text.startswith(x) else null
This says if the op is a literal, then we return this result.

The way I'm going to change this interpreter into a compiler is I'm going to take the individual statements like this that were in the interpreter, and I'm going to throw them into various parts of a compiler, and each of those parts is going to live in the constructor for the individual type of pattern.

We have a constructor -- literal takes a string as input and let's return a tuple that just represents what we have, and then the interpreter deals with that.

Now, we're going to have literal act as a compiler. What it's going to do is return a function that's going to do the work.


Toggle line numbers
   1 def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null
What is this saying?

We have the exact same expression here as we had before, but what we're saying is that as soon as we construct a literal rather than having that return a tuple, what it's returning is a function from the text to the result that matchset would have given us.

"""

"""
13. 10 Lower Level Compilers
We can define a pattern -- let's say pattern is lit('a').


Toggle line numbers
   1 >>> pat = lit('a')
Now what is a pattern? Well, it's a function. It's no longer a tuple.


Toggle line numbers
   1 >>> pat
   2 <function <lambda> at 0x101b7bd70>
We can apply that pattern to a string and we get back the set of the remainders.


Toggle line numbers
   1 >>> pat('a string')
   2 set([' string'])
It says, yes, we were able to successfully parse a off of a string, and the remainder is a string.

We can define another pattern. Let's say pattern 2 equals plus(pat).


Toggle line numbers
   1 >>> pat2 = plus(pat)
   2 >>> pat2
   3 <function <lambda> at 0x101b7bcf8>
Pattern 2 is also a function, and we can call pattern 2 of let's say the string of five a's followed by a b.


Toggle line numbers
   1 >>> pat2('aaaaab')
   2 set(['b', 'ab', 'aaab', 'aaaab', 'aab'])
Now we get back this set that says we can break off any number of a's because we're asking for a and the plus of that and the closure of a. These are the possible remainders if we break off all of the a's or all but one or all but three, and so on. Essentially we're doing the same computation that in the previous incarnation with an interpreter we would have done with:

Toggle line numbers
   1 >>> matchset(pat2, 'aaaab')
Now we don't have to do that. Now we're calling the pattern directly. So we don't have matchset, which has to look at the pattern and figure out, yes, the top-level pattern is a plus and the embedded pattern is a lit. Instead the pattern is now a composition of functions, and each function does directly what it wants to do. It doesn't have to look up what it should do.

In interpreter we have a way of writing patterns that describes the language that the patterns below to. In a compiler there are two sets of descriptions to deal with. There's a description for what the patterns look like, and then there's a description for what the compiled code looks like.

Now, in our case -- the compiler we just built -- the compile code consists of Python functions. They're good target representations because they're so flexible. You can combine them in lots of different ways. You can call each other and so on. That's the best unit that we have in Python for building up compiled code.

There are other possibilities. Compilers for languages like C generate code that's the actual machine instructions for the computer that you're running on, but that's a pretty complicated process to describe a compiler that can go all the way down to machine instructions. It's much easier to target Python functions.

Now there's an intermediate level where we target a virtual machine, which has its own set of instructions, which are portable across different computers. Java uses that, and in fact Python also uses the virtual machine approach, although it's a little bit more complicated to deal with. But it is a possibility, and we won't cover it in this class, but I want you to be aware of the possibility.

Here is what the so-called byte code from the Python virtual machine looks like. I've loaded the module dis for disassemble and dis.dis takes a function as input and tells me what all the instructions are in that function.

Here's a function that takes the square root of x-squared plus y-squared.


Toggle line numbers
   1 >>> import dis
   2 >>> import math
   3 >>> sqrt = math.sqrt
   4 >>> dis.dis(lambda x, y: sqrt(X ** 2 + y ** 2))
   5   1           0 LOAD_GLOBAL              0 (sqrt)
   6               3 LOAD_GLOBAL              0 (x)
   7               6 LOAD_CONST               1 (2)
   8               9 BINARY_POWER        
   9              10 LOAD_FAST                1 (y)
  10              13 LOAD_CONST               1 (2)
  11              16 BINARY_POWER        
  12              17 BINARY_ADD          
  13              18 CALL_FUNCTION            1
  14              21 RETURN_VALUE        
This is how Python executes that. It loads the square root function. It loads the x and the 2, and then does a binary power, loads the y and the 2, does a binary power, adds the first two things off the top of the stack, and then calls the function, which is the square root function with that value, and then returns it.

This is a possible target language, but much more complicated to deal with this type of code than to deal with composition of functions.

"""

#import dis
#import math
#sqrt = math.sqrt
#print dis.dis(lambda x, y: sqrt(X ** 2 + y ** 2))


# 14. 11 Alt
"""
Let's get back to our compiler.

   1 def matchset(pattern, text)
   2     ...
   3     elif 'seq' == op:
   4         return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))

Again, in matchset I pulled out one more clause. This is a clause for sequence, and this is what we return. If I want to write the compiler for that sequence clause, I would say let's define seq(x, y).

   1 def seq(x, y): return lambda text: set().union(*map(y, x(text))

It's a compiler so it's going to return a function that operates on x and y, take as input a text and then returns as result. We could take exactly that result. While I'm moving everything to this more functional notation, I decided let's just show you a different way to do this. This way to do it would be fine, but I could have the function return that. But instead, let's have it say what we're really trying to do is form a union of sets. What are the sets? The sets that we're going to apply union to. First we apply x to the text, and that's going to give us a set of remainders. For each of the remainders, we want to apply y to it. What we're saying is we're going to map y to each set of remainders. Then we want to union all those together. Now, union, it turns out, doesn't take a collection. It takes arguments with union a, b, c. So we want to turn this collection into a list of arguments to union. We do that using this apply notation of saying let's just put a star in there. Now, we've got out compiler for sequence. It's the function from text to the set that results from finding all the remainders for x and then finding all the remainders from each of those after we apply y. Unioning all those together in union will eliminate duplicates.

Now it's your turn to do one. This was the definition of alt in the interpreter matchset. Now I want you to write the definition of the compiler for alt, take a pattern for (x, y), and return the function that implements that.
"""

#----------------
# User Instructions
#
# Write the compiler for alt(x, y) in the same way that we 
# wrote the compiler for lit(s) and seq(x, y). 

'''
def matchset(pattern, text):
    op, x, y = components(pattern)
    if 'lit' == op:
        return set([text[len(x):]]) if text.startswith(x) else null
    elif 'seq' == op:
        return set(t2 for t1 in matchset(x, text) for t2 in matchset(y, t1))
    elif 'alt' == op:
        return matchset(x, text) | matchset(y, text)
'''

def lit(s): return lambda text: set([text[len(s):]]) if text.startswith(s) else null

def seq(x, y): return lambda text: set().union(*map(y, x(text)))

def alt(x, y): return lambda text: set().union(x(text), y(text))
        
null = frozenset([])

def unit_3_11_alt():
    g = alt(lit('a'), lit('b'))
    assert g('abc') == set(['bc'])
    return 'unit_3_11_alt test passes'

print unit_3_11_alt()

"""
The structure is exactly the same. It's the union of these two sets. The difference is that with a compiler the calling convention is pattern gets called with the text as argument. In the interpreter the calling convention is matchset calls with the pattern and the text.
"""

# --------------
# User Instructions
#
# Fill out the function match(pattern, text), so that 
# remainders is properly assigned. 

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text)-len(shortest)]
    
def lit(s): return lambda t: set([t[len(s):]]) if t.startswith(s) else null
def seq(x, y): return lambda t: set().union(*map(y, x(t)))
def alt(x, y): return lambda t: x(t) | y(t)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else null
dot = lambda t: set([t[1:]]) if t else null
eol = lambda t: set(['']) if t == '' else null
def star(x): return lambda t: (set([t]) | 
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))

null = frozenset([])

def unit_3_12_simple_compilers():
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    assert match(oneof('xyz'), '   x is here!') == None
    return 'unit_3_12_simple_compilers tests pass'

print unit_3_12_simple_compilers()

"""
Now, compilers have a reputation as being difficult and more complicated than interpreters, but notice here that the compilers is actually in many ways simpler than the interpreter.

It's fewer lines of code over all. One reason is because we didn't have to duplicate effort here of saying first we need constructors to build up a literal and then within matchset have an interpreter for that literal. Rather we did it just once. Just once! We said the constructor for literal returns a function which is going to be the implementation of the compiler for that type of pattern. It's very concise. Most of these are one-liners. Maybe I cheated a little bit and I replaced the word "text" with the word "t" to make it a little bit shorter and fit on one line.

There's only one that's complicated. That's the star of x, because it's recursive. The ones I haven't listed here is because they're all the same as before. Before we get into star(x) let me note that.

I didn't have to put down search here, because search is exactly the same as before.

I didn't have to put down plus, because plus is exactly the same as before. It's defined in terms of star.

What is the definition of star? One thing we could return is the remainder could be the text itself. Star of something -- you could choose not to take any of it and return the entire text as the remainder. That's one possibility. The other possibility is we could apply the pattern x. From star(x) apply the pattern x to the text and take those sets as remainders. For every remainder that's not the text itself -- because we already took care of that. We don't need to take care of it again. For all the remainders that are different from the whole text then we go through and we apply star(x) to that remainder. We get a new remainder and that's the result. That's all we need for the compiler result.

Oh, one piece that was missing is how do interface the match function, which takes a pattern and a text, with this compiler where a pattern is applied to the text. That's one line, which is slightly different. Here before we called matchset. In the previous implementation we had
"""

# 18. 13 Recognizers and Generators
"""
So far what we've done is call the recognizer task. We have a function match which takes a pattern and a text, and that returns back a substring of text if it matches or None.

It's called a recognizer, because we're recognizing whether the prefix of text is in the language defined by the pattern.

There's a whole other task called the generator in which we generate from a pattern a complete language defined by that pattern.

For example, the pattern a or b sequenced with a or b -- (a|b)(a|b). That defines a language of four different strings -- {aa, ab, ba, bb}, and we could define a function that takes a pattern and generates out that language. That all seems fine.

One problem, though. If we have a language like a* then the answer of that should be the empty string or a or aa or aaa and so on -- {'', a, aa, aaa, ...}. It's an infinite set. That's a problem. How are we going to represent this infinite set?

Now, it's possible, we could have a generator function that generates the items one at a time. That's a pretty good interface, but instead I'm going to have one where we limit the sizes of the strings we want. If we say we want all strings up to n characters in length, then that's always going to be a finite set.

I'm going to take the compiler approach. Rather than write a function "generate," I'm going to have the generator be compiled into the patterns. What we're going to write is a pattern, which is a compiled function, and we're going to apply that to a set of integers representing the possible range of lengths that we want to retrieve. That's going to return a set of strings.


pat({int}) --> {str}
So for example, if we define pattern to be a* -- we did that appropriately -- and then we asked for pattern, and we gave it the set {1, 2, 3},


pat = a*
pat({1,2,3}) --> {a, aa, aaa}
then that should return all strings which are derived from the pattern that have a length 1, 2, or 3. So that should be the set {a, aa, aaa}. Now let's go ahead and implement this.
"""

"""
Now, remember the way the compiler works is the constructor for each of the patterns takes some arguments -- a string, and x and y pattern, or whatever -- and it's going to return a function that matches the protocol that we've defined for the compiler.

The protocol is that each pattern function will take a set of numbers where the set of numbers is a list of possible lengths that we're looking for. Then it will return a set of strings.

What have I done for lit(s)? I've said we return the function which takes a set of numbers as input, and if the length of the string is in that set of number -- if the literal string was "hello" and if hello has five letters and if 5 is one of the numbers we're trying to look for -- then return the set consisting of a single element -- the string itself. Otherwise, return the null set.

star I can define in terms of other things.

plus I've defined in terms of a function sequence that we'll get to in a minute. It's a little bit complicated. It's really the only complicated one here. We can reduce all the other complications down to calling plus, which calls genseq(). seq does that too.

I've introduced epsilon, which is the standard name in language theory for the empty string. So it's the empty string. It's the same as just the literal of the empty string, which matches just itself if we're looking for strings of length 0.

For dot -- dot matches any character. I've decided to just return a question mark to indicate that. You could return all 256 characters or whatever you want. Your results would start to get bigger and bigger. You can change that if you want to.

I left space for you to do some work.

Give me the definitions for oneof(chars).

If we ask for oneof('abc') , what should that match?

What it should match is if 1 is an element of Ns then it should be abc. Otherwise, it shouldn't be anything.

Similarly for alt. Give me the code for that.
"""

# --------------
# User Instructions
#
# Complete the code for the compiler by completing the constructor
# for the patterns alt(x, y) and oneof(chars). 

def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
def oneof(chars):   return lambda Ns: set([s for s in chars if len(s) in Ns])
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.

null = frozenset([])

def unit_3_14_oneof_and_alt():
    
    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null 
    
    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])
    
    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null
    
    return 'unit_3_14_oneof_and_alt tests pass'

print unit_3_14_oneof_and_alt()

# 21. 15 Avoiding Repetition
"""
21. 15 Avoiding Repetition
That's the whole compiler. I want to show you just a little bit of the possibility of doing some compiler optimizations. Notice this sort of barrier here where we introduce lambda, where we introduce a function. Remember I said that there's two parts to a compiler. There's the part where we're first defining a language. When we call lit and give it a string, then we're doing some work to build up this function that's going to do the work every time we call it again. Anything that's on the right of the lambda is stuff that gets done every time. Anything that's to the left is stuff that gets done only once.

Notice that there is a part here building up this set of s that I'm doing every time, but that's wasteful because s doesn't depend on the input. s is always going to be the same.

I can pull this out and do it at compile time rather than do it every time we call the resulting function.

I'll make this set of s and I'll give that a name -- set_s. Over here I'll do set_s equals that value. It looks like I'd better break this up into multiple lines.

Now I pulled out that precomputation so it only gets done once rather than gets done every time. You could look around for other places to do that.

I could pull out the computation of this set of characters and do that only once as well.

That's a lifting operation that stops us from repeating over and over again what we only need to do once. That's one of the advantages of having a compiler in the loop. There is a place to do something once rather than to have to repeat it every time.
"""

"""
22. 16 Genseq
Now there's only one bit left -- this generate sequence. Let's talk about that. Now sequence in this formulation is a function that takes x and y, two patterns, and what it returns is a function, and that function takes a list of numbers and returns a set of text that match. So sequence is delaying the calculation. It's computing a function which can do the calculation later on. Genseq does the calculation immediately. It takes x and y and a set of numbers, and it immediately calculates the set of possible text. Now the question is what do we know about genseq in terms of the patterns x and y and the set of possible numbers. We know at some point we're going to have to call the pattern x with some set of numbers. We're not yet quite sure what. That's going to return a list of possible text. Then we're going to have to call y with some other set of numbers. Then we're going to have to concatenate them together and see if they make sense, if the concatenation of some x and some y, if that length is within this allowable set. Now, what do we know about what these Ns should be in terms of this set of possible numbers here regardless of what this set is. This could be a dense set, so we could have Ns equals 0, 1, 2, all the way up to 10 or something. Or it could be a sparse set. It could be, say, only the number 10. But either way, the restriction on x and y is such that they have to add up to no more than 10. But x could be anything. If the list of possible numbers that we want to add up to is only 10, that doesn't constrain x at all other than to be less than 10. This N should be everything up to the maximum of N sub s. Then what should y be? Well, we have two choices. One, we could for each x that comes back we could generate the y's. Or we could generate the y's all at once and then try to combine them together and see if they match up. I think that's actually easier. So for the y's also, they can be any size up to the maximum. Then we take the two together, add up the x match and the y match and see if that length is within N. In this example, if Ns is equal to 10, here we want to have the Ns be everything from 0 up to 10 inclusive in both cases, and we get back some results like, say, a, abb, acde, and so on, and some other result over here -- ab, bcd. Then for each of them we add them up, and if we say abb plus ab and check to see if that's in Ns. If it is, we keep it. If it's not, we don't keep it. Here is candidate solution for genseq. We take x, y, and a set of numbers, and then we define Ns as being everything up to the largest number, including the largest number. We have to add 1 to the maximum number in order to get a range going from 0 up to and including the largest number. Now that we know the possible values of the numbers that we're looking for for the sizes of the two components-the x and the y components -- then we can say m1 is all the possible matches for x, m2 is all the possible matches for y. If the length of m1 plus m2 is in the original set of numbers that we're looking for, then return m1 plus m2. This seems reasonable. It looks like it's doing about what we're looking for to generate all sequences of x and y concatenated together. But I want you to think about it and say, have we really gotten this right? The choices are is this function correct for all inputs? Or is in incorrect for some? Does it return incorrect results? Or is it correct when it returns, but doesn't doesn't always return? Think about that. Think about is there any result that looks like it's incorrect that's being formed. Think about does it infinite loop or not. Think about base cases on recursion and saying is there any case where it looks like it might not return. This is a tricky question, so I want you to try it, but it may be difficult to get this one right.

23. 16 Genseq (Answer)
The answer is that it is correct when it returns. All the values it builds up are correct, but unfortunately it doesn't always return. Let's try to figure out why. In think about this, we want to think about recursive patterns. Let's look at the pattern x+. We've definec x+ as being the sequence of x followed by x*. And now for most instances of x that's not a problem. If we had plus(lit('a')), it not going to be a problem. That's going to generate a, aa, aaa, and so on. But consider this -- let's define a equals lit('a'), pat equals plus(opt('a')). Now, this should be the same. This should also generate a, aa, aaa. The way we can see that is we have a plus so that generates any number of these. If we pick a once, we get this. It we pick a twice we get this. If we pick a three times we get this. But the problem is there's all these other choices in between. Opt(a) means we we can either be picking a or the empty string. As we go through the loop for plus, we could pick empty string, empty string, empty string. We could pick empty string an infinite number of times. Even though our N is finite -- at some point we're going to ask for pattern of some N -- let's say the set {1, 2, 3} -- we won't have a problem with having an infinite number of a's, but we will have a problem of choosing from the opt(a) the empty part. If an infinite number of times we choose the empty string rather than choosing a, then we're never going to get past three as the highest value. We're going to keep going forever. That's the problem. We've got to somehow say I don't want to keep choosing the empty string. I want to make progress and choose something each time through. So how can we make sure that happens?
"""

# 25. 18 Testing genseq
"""
Here's what gensequence looks like. We have a recursive base case that says, if there are no numbers that we're looking for, we can't generate anything of those lengths, and so return the empty set. Then we say the xmatches we get by applying x to any number up to the maximum of Ns, including the maximum of Ns, but then we got to do some computation to figure out what can be the allowable sizes for y, and we do that by saying, let's take all the possible values that came back from the xmatches and then for each of those values and for each of the original values for the lengths that we're looking for, subtract those off and say, total is going to be one of the things we got from x and one of the things we got from y, that better add up to one of the things in Ns. Then we call y with that set of possible ends for y and then we do the same thing that we were going to do before. We go through those matches, but this is going to be with a reduced set of possibilities and count those up, and now, the thing that makes it all work is this optional argument here, saying the number that we're going to start at for the possible sizes, for x in the default case, that's 0, and so we start the range at 0. But in the case where we're calling from +, we're going to set that to 1. Let's see what that looks like. Here's the constructors, the compilers for sequence and plus. For a regular sequence, there is no constraint on this start for x. X can be any size up to the maximum of the N's. But for plus, we're going to always ask that the x part have a length of at least 1, and then the y part will be whatever is left over. That's how we break the recursion, and we make sure that genseq will always terminate. Now this language generation program is a little bit complex. So I wanted to make sure that I wrote a test suite for it to test the generation. So here I've just defined some helper functions and then wrote a whole bunch of statements here. If we check one of 'ab' and limit that to size 2, that should be equal to this set. It's gone off the page. Let's put it back where it belongs. One element of size 0, 2 elements of size 1, and 4 elements of size 2, just what you would expect. Here are sequences of a star, b star, c star of size exactly 4. Here they are and so on and so on. We've made all these tests. I should probably make more than these, but this will give you some confidence that the program is doing the right thing if it passes at least this minimal test suite.
"""

# 26. 19 Theory and Practice
"""
This is a good time to pause and summarize what we've learned so far. We've learned some theory and some practice. In theory, we've learned about patterns, which are grammars which describe languages, where a language is a set of strings. We've learned about interpreters over those languages, and about compilers, which can do the same thing only faster. In terms of practice, we've learned that regular expressions are useful for all sorts of things, and they're a concise language for getting work done. We've learned that interpreters, including compilers, can be valuable tools, and that they can be more expressive and more natural to describe a problem in terms of a native language that makes sense for the problem rather than in terms of Python code that doesn't necessarily make sense. We learned functions are more composable than other things in Python. For example, in Python we have expressions, and we have statements. They can only be composed by the Python programmer whereas functions can be composed dynamically. We can take 2 functions and put them together. We can take f and call g with that and then apply that to some x. We can do that for any value of f and g. We can pass those into a function and manipulate them and have different ones applying to x. We can't do that with expressions and statements. We can do it with the values of expressions, but we can't do it with expressions themselves. Functions provide a composability that we don't get elsewhere. Functions also provide control over time, so we can divide up the work that we want to do into do some now and do some later. A function allows us to do that. Expressions and statements don't do that because they just get done at 1 time when they're executed. Functions allow us to package up computation that we want to do later.
"""

# 27. 20 Changing seq
"""
Now one thing I noticed as I was writing all those test patterns is that functions like seq and alt are binary, which means if I want a sequence of 4 patterns, I have to have a sequence of (a, followed by the sequence of (b, followed by sequence of (c,d), and then I have to count the number of parens and get them right. It seems like it'd be much easier if I could just write sequence of (a, b, c, d). And we talked before about this idea of refactoring, that is changing your code to come up with a better interface that makes the program easier to use, and this looks like a good example. This would be a really convenient thing to do. Why did I write seq this way? Well, it was really convenient to be able to define sequence of (x,y) and only have to worry about exactly 2 cases. If I had done it like this, and I had to define sequence of an arbitrary number of arguments, then the definition of sequence would have been more complex. So it's understandable that I did this. I want to make a change, so let's draw a picture. Imagine this is my whole program and then somewhere here is the sequence part of my program. Now, of course, this has connections to other parts of the program. Sequence is called by and calls other components, and if we make a change to sequence, then we have to consider the effects of those changes everywhere else in which it's used. When we consider these changes, there are 2 factors we would like to break out. One is, is the change backward compatible? That is, if I make some change to sequence, am I guaranteed that however it was used before, that those uses are still good, and they don't have to be changed? If so, then my change will be local to sequence, and I won't have to be able to go all over the program changing it everywhere else. So that's a good property to have. So for example, in this case, if I change sequence so that it still accepted than that would be a backwards compatible change as long as I didn't break anything else. And then the second factor is whether the change is internal or external. So am I changing something on the inside of sequence that doesn't effect all the callers, than that's okay. In general, that's going to be backwards compatible. Or am I changing something on the outside -- changing the interface to the rest of the world? In this case, going from the binary version to this n_ary version, I can make it backwards compatible if I'm careful. It's definitely going to be both an internal and external change. So I'm going to have to do something to the internal part of sequence. And then I'm also changing the signature of the function, so I'm effecting the outside as well. I can make that effect in a backwards compatible way. Thinking about those 2 factors, what would be the better way to implement this call? Let's say we're dealing with the match-set version where we're returning a tuple, would it be better to return the tuple sequence (a, b, c, d) or the tuple sequence of (a, sequence of (b, sequence of (c, d)? Tell me which of these do you prefer from these criteria.

28. 20 Changing seq (Answer)
The answer is this approach is much better because now from the external part everybody else sees exactly the same thing. But internally, I can write the calls to the function in a convenient form and they still get returned in a way that the rest of the program can deal with, and I don't have to change the rest of the program.
"""

# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        # your code here
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

# 30. 22 Function Mapping
"""
What's the best way to do that? How can I map from function f to a function f prime? One possibility would be to edit the bytecode of f. Another possibility would be to edit the source string of f and concatenate some strings together. Another possibility would be to use an assigment statement to say f = some function g of f to give us a new version of f. Which of these would be the best solution?
"""

# 31. 22 Function Mapping
"""
I think it's pretty clear that this one is the best because we know how to do this quite easily. We know how to compose functions together, and that's simple, but editing the bytecode or the source code, that's going to be much trickier and not quite as general, so let's go for the solution.
"""

# 32. 23 n_ary Function
"""
What I want to do is define a function, and let's call it n_ary, and it takes (f), which should be a binary function, that is a function that takes exactly 2 arguments, and n_ary should return a new function that can take any number of arguments. We'll call this one f2, so that f2 of (a, b, c) is = f(a, f(b, c)), and that will be true for any number of arguments -- 2 or more. It doesn't have to just be a, b, c. So let's see if you can write this function n_ary. Here's a description of what it should do. It takes a binary function (f) as input, and it should return this n_ary function, that when given more than 2 arguments returns this composition of arguments. When given 2 arguments, it should return exactly what (f) returns. We should also allow it to take a single argument and return just that argument. That makes sense for a lot of functions (f), say for sequence. The sequence of 1 item is the item. For alt, the alternative of 1 item is the item. I mentioned addition and multiplication makes sense to say the addition of a number by itself is that number or same with multiplication. So that's a nice extension for n_ary. See if you can put your code here. So what we're doing is, we're passed in a function. We're defining this new n_ary function, putting the code in there, and then we're returning that n_ary function as the value of that call.
"""

# 33. 23 n_ary Function (Answer)
"""
Here's the answer. It's pretty straight forward. If there's only 1 argument, you return it. Otherwise, you call the original f that was passed in with the first argument as the first argument, and the result of the n-ary composition as the other argument.
"""

# 34. 24 Update Wrapper
"""
Now how do we use this? Well, we take a function we define, say seq of x, y, and then we can say sequence is redefined as being an n_ary function of sequence. Oops -- I guess I got to fix this typo here. From now on, I can call sequence and pass in any number of numbers, and it will return the result that looks like that. So that looks good. In fact, this pattern is so common in Python that there's a special notation for it. The notation is called the decorator notation. It looks like this. All we have to do is say, @ sign, then the name of a function, and then the definition. This is the same as saying sequence = n_ary of sequence. It's just an easier way to write it. But there is one problem with the way we specified this particular decorator, which is if I'm in an interactive session, and I ask for help on sequence, I would like to see the argument list and if there is a doc string, I want to see the documentation here. I didn't happen to put in any documentation for sequence. But when I ask for help, what I get is this. I'm told that sequence is called n_ary function. Well, why is that? Because this is what we returned when we define sequence = n_ary of sequence. We return this thing that has the name n_ary function. So we would like to fix n_ary up so that when the object that it returns has the same function name and the same function documentation -- if there is any documentation -- and have that copied over into the n_ary f function. Now it turns out that there is a function to do exacty that, and so I'm going to go get it. I'm going to say from the functools -- the functional tools package. I want to import the function called update_wrapper. Update_wrapper takes 2 functions, and it copies over the function name and the documentation and several other stuff from the old function to the new function, and I can change n_ary to do that, so once I've defined the n_ary function, then I can go ahead and update the wrapper of the n_ary function -- the thing I'm going to be returning from the old function. So this will be the old sequence, which has a sequence name, a list of arguments, maybe some documentation string, and this will be the function that we were returning, and we're copying over everything from f into n_ary f. Now when I ask for help -- when I define n_ary sequence, and I ask for help on sequence, what I'll see is the correct name for sequence, and if there was any documentation string for sequence, that would appear here as well. So update_wrappers is a helpful tool. It helps us when we're debugging. It doesn't really help us in the execution of the program, but in doing debugging, it's really helpful to know what the correct names of your functions are. Notice that we may be violating the Don't Repeat Yourself principle here. So this n_ary function is a decorator that I'm using in this form to update the definition of sequence. I had to -- within my definition of n_ary -- I had to write down that I want to update the wrapper. But it seems like I'm going to want to update the wrapper for every decorator, not just for n_ary, and I don't want to repeat myself on every decorator that I'm going to define.
"""

# 35. 25 Decorated Wrappers
"""
So here's an idea. Let's get rid of this line, and instead, let's declare that n_ary is a decorator. We'll write a definition of what it means to be a decorator in terms of updating wrappers. Then we'll be done, and we've done it once and for all. We can apply it to n_ary, and we can apply it to any other decorator that we define. This is starting to get a little bit confusing because here we're trying to define decorator, and decorator is a decorator. Have we gone too far into recursion? Is that going to bottom out? Let's draw some pictures and try to make sense of it. So we've defined n_ary, and we've declared that as being a decorator, and that's the same as saying n_ary = decorator of n_ary. Then we've used n_ary as a decorator. We've defined sequence to be an n_ary function. That's the same as saying sequence = n_ary of sequence. Now we wanted to make sure that there's an update so that the documentation and the name of sequence gets copied over. We want to take it from this function, pass it over to this function because that's the one we're going to keep. While we're at it, we might as well do it for n_ary as well. We want to have the name of n_ary be n_ary and not something arbitrary that came out of decorator. So we've got 2 updates that we want to do for the function that we decorated and for the decorator itself. Now let's see if we can write decorator so that it does those 2 updates. So let's define decorator. It takes an argument (d), which is a function. Then we'll call the function we're going to return _d, and that takes a function as input. So it returns the update wrapper from applying the decorator to the function and copying over onto that decorated function, the contents of the original function's documentation and name, and then we also want to update the wrapper for the decorator itself. So from (d) the decorated function, we want to copy that over into _d and then return _d. Now which update is which? Well, this one here is the update of _d with d, and this one is the update of the decorated function from the function. So here we're saying the new n_ary that we're defining gets the name from the old n_ary, the name in the documentation string, and here we're saying the new sequence, the new n_ary sequence, gets its name from the old sequence. Here's what it all looks like. If you didn't quite follow that the first time, don't worry about it. This is probably the most confusing thing in the entire class because we've got functions pointing to other functions, pointing to other functions. Try to follow the pictures. If you can't follow the pictures, that's okay. Just type it into the interpreter. Put these definitions in. Decorate some functions. Decorate some n_ary functions. Take a look at them and see how it works.
"""

"""
def decorator(d):
	"Make function d a decorator: d wraps a function fn"
	def _d(fn):
		return update_wrapper(d(fn), fn)
	update_wrapper(_d, d)
	return _d

def decorator(d):
	"make function d a decorator: d wraps a function fn"
	return lambda fn:update_wrapper(d(fn), fn)

decorator = decorator(decorator)
"""

"""
   1 @decorator
   2 def memo(f):
   3     '''Decorator that caches the return value for each call to f(args).
   4     Then when called again with same args, we can just look it up.'''
   5     cache = {}
   6     def _f(*args):
   7         try:
   8             return cache[args]
   9         except KeyError:
  10             cache[args] = result = f(*args)
  11             return result
  12         except TypeError:
  13             # some element of args can't be a dict key
  14             return f(args)
  15     return _f

The guts of it is the same as what I sketched out previously.

If we haven't computed the result already, we compute the result by applying the function f to the arguments. It gives us the result. We cache that result away, then we return it for this time. It's ready for next time. Next time we come through, we try to look up the arguments in the cache to see if they're there. If they are, we return the result.

And now I've decided to structure this one as a try-except statement rather than an if-then statement. In Python, you always have 2 choices. You can first ask for permission to say are the args in the cache, and if so, return cache or args, or you can use the try-except pattern to ask for forgiveness afterwards to say, I'm first going to try to say, if the args are in the cache, go ahead and return it. If I get a keyError, then I have to fill in the cache by doing the computation and then returning the result.

The reason I use the try structure here rather than the if structure is because I knew I was going to need it anyways for this third case. Either the args are in the cache, or they aren't, but then there's this third case which says that the args are not even hashable.

What does that mean?

Start out with a dictionary d being empty, and then I'm going to have a variable x, and let's say x is a number. If I now ask, is x in d? That's going to tell me false. It's not in the dictionary yet. But now, let's say I have another variable, which is y, which is the list [1, 2, 3] and now if I ask is y in d? You'd think that would tell me false, but in fact, it doesn't. Instead, it gives me an error, and what it's going to tell me is type error: unhashable type: list.

What does that mean?

That means we were trying to look up y in the dictionary, and a dictionary is a hash table -- implemented as a hash table. In order to do that, we have to compute the hash code for y and then look in that slot in the dictionary. But this error is telling us that there is no hash code for a list.

Why do you think that is?

Are lists unhashable because:

lists can be arbitrarily long?
lists can hold any type of data as the elements, not just integers?
lists are mutable?
Now I recognize this might be a hard problem if you're not up on hash tables. This might not be a question you can answer. But give it a shot and give me your one best response.
"""

# 39. 27 Cache Management (Answer)
"""
The answer is because lists are mutable. That makes them unlikely candidates to put into hash tables. Here's why. Let's suppose we did allow lists to be hashable. Now we're trying to compute the hash function for y, and let's say we have a very simple hash function -- not a very good one -- that just says add up the values of the elements. Let's also say that the hash of an integer is itself, so the hash code for this list would be equal to 6, the sum of the elements. But now the problem is, because these lists are mutable, I could go in, and I could say, y[0] = 10. Y would be the list [10, 2, 3]. Now when we check and say, is y in d? We're going to compute the hash value 10 + 2 + 3 = 15. That's a different hash value than we had before. So if we stored y into the dictionary when it had the value 6, and now we're trying to fetch it when it has the value 15, you can see how Python is going to be confused. Now, there's 2 ways you could handle that. One -- the way that Python does take is to disallow putting the list into the hash table in the first place because it potentially could lead to errors if it was modified. The other way is Python could allow you to put it in, but then recognize that it's the programmers fault, and if you go ahead and modify it, then things are not going to work anymore, and Python does not take that approach, although some other languages do.
"""

# golden ration:  (1 + sqrt(5)) / 2
from functools import update_wrapper


def decorator(d):
	"Make function d a decorator: d wraps a function fn."
	def _d(fn):
		return update_wrapper(d(fn), fn)
	update_wrapper(_d, d)
	return _d

@decorator
def memo(f):
	"""Decorator that caches the return value for each call to f(args).
	Then when called again with same args, we can just look it up"""
	cache = {}
	def _f(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = result = f(*args)
			return result
		except TypeError:
			return f(args)
	return _f

@decorator
def countcalls(f):
	"Decorator that makes the function count calls to it, in callcounts[f]"
	def _f(*args):
		callcounts[_f] += 1
		return f(*args)
	callcounts[_f] = 0
	return _f

callcounts = {}

@countcalls
@memo
def fib(n): return 1 if n <= 1 else fib(n-1) + fib(n-2)

# Type of Tools
"""
DEBUG				PERF			EXPRESSINESS
countcalls			memo			n_ary
trace
disabled
"""
# ---------------
# User Instructions
#
# Modify the function, trace, so that when it is used
# as a decorator it gives a trace as shown in the previous
# video. You can test your function by applying the decorator
# to the provided fibonnaci function.
#
# Note: Running this in the browser's IDE will not display
# the indentations.

from functools import update_wrapper


def decorator(d):
	"Make function d a decorator: d wraps a function fn."
	def _d(fn):
		return update_wrapper(d(fn), fn)
	update_wrapper(_d, d)
	return _d

@decorator
def trace(f):
	indent = '   '
	def _f(*args):
		signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
		print '%s--> %s' % (trace.level*indent, signature)
		trace.level += 1
		try:
			result = f(*args)
			print '%s<-- %s == %s' % ((trace.level-1)*indent, signature, result)
		finally:
			trace.level -= 1
		return result
	trace.level = 0
	return _f

@trace
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print fib(6)

# ---------------
# User Instructions
#
# Modify the parse function so that it doesn't repeat computations.
# You have learned about a tool in this unit that prevents 
# repetitive computations. Try using that!
#
# For this question, the grader will be looking for a specific 
# solution. Hint: it should only involve adding one line of code
# (and that line should only contain 5 characters).

from functools import update_wrapper
import re

def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text
    @memo
    def parse_atom(atom, text):
        if atom in grammar:  # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem  
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])
    
    # Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

# The following decorators may help you solve this question. HINT HINT!

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

# summary!!!!
"""
Tools - components

Langauge		grammar
				interpreter
				compilers

Function	vs	statements
compose
object
decorator
pattern and objects


"""