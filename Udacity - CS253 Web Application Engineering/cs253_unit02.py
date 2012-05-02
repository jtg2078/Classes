# -------------------- cs253 week 2 --------------------
# HTML Form
"""
<form>
	<input name="">
</form>
"""
# Enter the html for an input tag whos name parameter is q
# <input name="q">

# Put some text in the input box in your browser and prcess
# enter. what happen?
# Ans:
# the url changes with my text
# ....\cs253_unit02_form.html?q=asdasda

# Is clicking sumbit any different than pressing enter?
# Ans: No

# Associate the form element with an action
# <form action="/foo">
# when clicking the submit, the form will send the input data to that
# address
# e.g. file://localhost/foo?q=ddd

"""
<form action="http://www.google.com/search">
	<input name="q">
	<input type="submit">
</form>
"""
# e.g. http://www.google.com/search?q=diablo+3
#      http://www.google.com/search?q=better+flight+search
# what are the + in the url?
# because address cannot have spaces, so the broswer adds the +
# to replace space instead. this is called URL encoding or form
# encoding

# in google appengine, the default content type is text/html

# the default method in HTTP is GET, and the get parameters
# we can set it to POST

# Where did our q parameter go? (in HTTP POST)
# Ans: after the HTTP request headers

# GET vs POST
#
# GET
#	- parameters in URL
#	- used for fetching documents
#	- maximum URL length (not good for sending a lot of data to server)
#	- ok to cache
#	- shouldn't change the server
#
# POST
#	- parameters is in body
#	- used for updating data
#	- no max length (unless specifically set)
#	- not ok to cache
#	- ok to change the server

# for form's input, the default type is text
# types:
#	- text
#	- password
#	- checkbox (vale for checked is on e.g. /?q=on, but unchecked can be anything)

form="""
<form>
	<input type="checkbox" name="q">
	<input type="checkbox" name="r">
	<input type="checkbox" name="s">
	<br>
	<input type="submit">
</form>
"""
# When I select the first two checkboxes and click submit, what
# does the query section of the url look like?
#
# Ans: q=on&r=on

form="""
<form>
	<input type="radio" name="q" value="one">
	<input type="radio" name="q" value="two">
	<input type="radio" name="q" value="three">
	<br>
	<input type="submit">
</form>
"""

# What is the value of the q parameter when the form is submiited with the
# second radio button selected?
#
# Ans: q=two

# to group the radio buttons, make their name the same
# use the value attribute to tell which radio button in the given group is selected

form="""
<form>
	<label>
		One
		<input type="radio" name="q" value="one">
	</label>
	<label>
		Two
		<input type="radio" name="q" value="two">
	</label>
	<label>
		Three
		<input type="radio" name="q" value="three">
	</label>
	<br>
	<input type="submit">
</form>
"""

form="""
<form>
	<select name="q">
		<option>one</option>
		<option>two</option>
		<option>three</option>
	</select>
	<br>
	<input type="submit">
</form>
"""

# When we select two from the dropdown, what is the value of the
# q parameter?
#
# Ans: two

form="""
<form>
	<select name="q">
		<option value="1">the number one</option>
		<option>Two</option>
		<option>Three</option>
	</select>
	<br>
	<input type="submit">
</form>
"""
# What will q's value in the URL be when we submit with the number one
# selected?
#
# Ans: 1

# Validation
# your server can receive junk, you need to filter and verify stuff you
# recives

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)
          
def valid_month(month):
	valid = None
	for m in months:
		if m.lower() == month.lower():
			valid = m
			break
	return valid

def valid_month_prof(month):
	# ---- Prof's version
	if month:
		cap_month = month.capitalize()
		if cap_month in months:
			return cap_month

def valid_month_prof_abbvs(month):
	# ---- Prof's version
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)


def unit_02_30_valid_month():
	assert valid_month("january") == "January"
	assert valid_month("January") == "January"
	assert valid_month("foo") == None
	assert valid_month("") == None
	assert valid_month_prof("january") == "January"
	assert valid_month_prof("January") == "January"
	assert valid_month_prof("foo") == None
	assert valid_month_prof("") == None
	assert valid_month_prof_abbvs("feb") == "February"
	assert valid_month_prof_abbvs("febsddwww") == "February"
	print 'unit_02_30_valid_month - All tests passed'

# in python the dict.get(x) is the following
# This class method return a value for the given key. If key is not 
# available then return returns default value None.
#
# dict.get(key, default=None)

def valid_day(day):
	for i in range(1,32):
		if day == str(i):
			return i
	return None

def valid_day_prof(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day

def unit_02_31_valid_day():
	assert valid_day('0') == None
	assert valid_day('1') == 1
	assert valid_day('15') == 15
	assert valid_day('500') == None
	assert valid_day_prof('0') == None
	assert valid_day_prof('1') == 1
	assert valid_day_prof('15') == 15
	assert valid_day_prof('500') == None
	print 'unit_02_31_valid_day - All tests passed'

# -----------
# User Instructions
# 
# Modify the valid_year() function to verify 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year >= 1900 and year <= 2020:
			return year

def unit_02_31_valid_year():
	assert valid_year('0') == None
	assert valid_year('-11') == None
	assert valid_year('1950') == 1950
	assert valid_year('2000') == 2000
	print 'unit_02_31_valid_year - All tests passed'

unit_02_31_valid_year()

# validation
# 1. verify the user's input
# 2. on error, render form again
# 3. include error message

# string substitution
# <b> some bold text</b>
# <b>%s</b> % varaible

# User Instructions
# 
# Write a function 'sub1' that, given a 
# string, embeds that string in 
# the string: 
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given 
# string.
#

given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
	return given_string % s

def unit_02_35_string_substitution():
	assert sub1("running") == "I think running is a perfectly normal thing to do in public."
	assert sub1("sleeping") == "I think sleeping is a perfectly normal thing to do in public."
	print 'unit_02_35_string_substitution - All tests passed'

unit_02_35_string_substitution()

# Multiple string substitution
#
# "text %s text %s" %(var1, var2)

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
	return given_string2 %(s1, s2)

def unit_02_36_substituting_multiple_strings():
	assert sub2("running", "sleeping") == "I think running and sleeping are perfectly normal things to do in public."
	assert sub2("sleeping", "running") == "I think sleeping and running are perfectly normal things to do in public."
	print 'unit_02_36_substituting_multiple_strings - All tests passed'

unit_02_36_substituting_multiple_strings()

# String substitution with key-value
# "text %(NAME)s text" % {"NAME":value}

# User Instructions
# 
# Write a function 'sub_m' that takes a 
# name and a nickname, and returns a 
# string of the following format: 
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
# 

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
	return given_string2 % {"name": name, "nickname": nickname}

def unit_02_37_advanced_string_substitution():
	assert sub_m("Mike", "Goose") == "I'm Goose. My real name is Mike, but my friends call me Goose."
	print 'unit_02_37_advanced_string_substitution - All tests passed'

unit_02_37_advanced_string_substitution()

# Input values
# <input type="text" value="cool"> default value to cool

# Which of these if a correct <input> for preserving the user's month?
# Ans: <input name="month" value="%(month)s">

# Escaping
# <input value="%(month)s">			month="november"
#									month= '"foo">derp'
# <input value="foo">derp">
#
# " --> &quot;
# > --> &gt;
# < --> &lt;
# & --> &amp;

# what is the correct way to include the text &=&amp; in rendered html?
# Ans: &amp;=&amp;amp;

# User Instructions
# 
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

import re
def escape_html_regex(s):
	s = re.sub(r'&', '&amp;', s) # order matters
	s = re.sub(r'>', '&gt;', s)
	s = re.sub(r'<', '&lt;', s)
	s = re.sub(r'"', '&quot;', s)
	return s

def escape_html(s):
	s = s.replace('&', '&amp;')
	s = s.replace('>', '&gt;')
	s = s.replace('<', '&lt;')
	s = s.replace('"', '&quot;')
	return s

import cgi
def escape_html_built_in(s):
	return cgi.escape(s, quote = True)

def unit_02_44_implementing_html_escaping():
	assert escape_html_regex('<html>') == '&lt;html&gt;'
	assert escape_html('<html>') == '&lt;html&gt;'
	assert escape_html_built_in('<html>') == '&lt;html&gt;'
	print 'unit_02_44_implementing_html_escaping - All test passed'
	
unit_02_44_implementing_html_escaping()

# Redirect
# you ---------- Get ----------> servers
# you <------- form html ------> servers
# you ------ post answer ------> servers
# you <------- redirect -------> servers
# you ------ Get success ------> servers
# you <---- success html ------> servers

# why is it nice to redirect after a form submission?
# Ans: So that reloading the page doesn't resubmit the form
#	   so we can have distinct pages for forms and success pages


# redirect in google app engine
# self.redirect("/thanks")

tes_str = re.sub(r'[a-z]', 'b', 'hello')
print 'a'.isalpha()
print 'B'.isalpha()
print ord('h')
print ord('u')
print 'lets see'
print ord('a') + (ord('h')-ord('a')+13) % 26

def create_map_lower():
	letter = 'abcdefghijklmnopqrstuvwxyz'
	dict = {}
	for i in range(0, 26):
		dict[letter[i]] = letter[(i + 13) % 26]
	return dict

def create_map_upper():
	letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dict = {}
	for i in range(0, 26):
		dict[letter[i]] = letter[(i + 13) % 26]
	return dict

def rot13(s):
	i = 0
	map_lower = create_map_lower()
	map_upper = create_map_upper()
	r = []
	for c in s:
		r.append(c)
		if c.isalpha():
			r[i] = map_upper[c] if c.isupper() else map_lower[c]
		i += 1
	return cgi.escape(''.join(r), quote = True)

print rot13('h     Ello <html/>')
print rot13('234')
	
	