#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import cgi
import re
import hmac
import random
import string
import hashlib
import jinja2
import json
import time
import calendar
import logging
jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from datetime import datetime
from google.appengine.ext import db
from google.appengine.api import memcache

unit02_hw1_form = """
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>

</html>
"""
unit02_hw2_form = """

<!DOCTYPE html>

<html>
  <head>
    <title>Sign Up</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>

  </head>

  <body>
    <h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(username_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
            %(password_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
            %(verify_error)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(email_error)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
  </body>

</html>
"""

def escape_html(s):
	return cgi.escape(s, quote = True)

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
	return ''.join(r)
	

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(unit02_hw1_form % {'text': ''})
		
	def post(self):
		text = self.request.get('text')
		text = rot13(text)
		text = escape_html(text)
		self.response.out.write(unit02_hw1_form % {'text': text})

class Unit02HW1(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(unit02_hw1_form % {'text': ''})
		
	def post(self):
		text = self.request.get('text')
		text = rot13(text)
		text = escape_html(text)
		self.response.out.write(unit02_hw1_form % {'text': text})

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


class Unit02HW2(webapp2.RequestHandler):
	
	def valid_username(self, username):
		return USER_RE.match(username)
	
	def valid_password(self, password):
		return PWD_RE.match(password)
	
	def valid_password_verify(self, password, verify):
		if self.valid_password(password):
			if password == verify:
				return verify
		return None
	
	def valid_email(self, email):
		return EMAIL_RE.match(email)
	
	def write_form(self, info = None):
		self.response.out.write(unit02_hw2_form % 
				{"username": info.get('username') if info else "",
				 "username_error": info.get('username_error') if info else "",
				 "password": info.get('password') if info else "",
				 "password_error": info.get('password_error') if info else "",
				 "verify": info.get('verify') if info else "",
				 "verify_error": info.get('verify_error') if info else "",
				 "email": info.get('email') if info else "",
				 "email_error": info.get('email_error') if info else ""})
				
	def get(self):
		self.response.out.write(self.write_form())
		
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		user_verify = self.request.get('verify')
		user_email = self.request.get('email')
		
		info = {}
		
		info['username'] = ""
		info['password'] = ""
		info['verify'] = ""
		info['email'] = ""
		
		info['username_error'] = ""
		info['password_error'] = ""
		info['verify_error'] = ""
		info['email_error'] = ""
		
		info['username'] = escape_html(user_username)
		info['password'] = escape_html(user_password)
		info['verify'] = escape_html(user_verify)
		info['email'] = escape_html(user_email)
		
		username = self.valid_username(user_username)
		password = self.valid_password(user_password)
		
		is_valid = True
		
		if not username:
			info['username_error'] = escape_html("That's not a valid username.")
			is_valid = False;
		
		if not password:
			info['password_error'] = escape_html("That wasn't a valid password.")
			is_valid = False;
		else:
			verify = self.valid_password_verify(user_password, user_verify)
			if not verify:
				info['verify_error'] = escape_html("Your passwords didn't match.")
				is_valid = False;
		
		info['password'] = ""
		info['verify'] = ""
		
		if user_email:
			email = self.valid_email(user_email)
			if not email:
				info['email_error'] = escape_html("That's not a valid email.")
				is_valid = False;
		
		if is_valid:
			self.redirect("/welcome?username=%s" % user_username)
		else:
			self.response.out.write(self.write_form(info))
			
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		self.response.out.write("Welcome, %s" % username)
		
# -------------------- hw3 --------------------

"""
----------------
Including CSS as static files
http://forums.udacity.com/cs253-april2012/questions/14052/including-css-as-static-files
These two lines need to bee the last for the handlers, because it satisfies every path.

- url: .*
  script: main.app
----------------
datetime.datetime and strftime()
http://forums.udacity.com/cs253-april2012/questions/13099/datetimedatetime-and-strftime
I think it might be because you have an extra % before the :.

Should be just:

{{entry.date.strftime("%b %d, %Y %I:%M %p")}}

Related: http://docs.python.org/library/time.html#time.strftime


"""

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)
	
	def render_str(self, template, **params):
		t = jinja_environment.get_template(template)
		return t.render(params)
	
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		
		
class Post(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	
		
class HW3NewPostHandler(Handler):
	def render_front(self, subject='', content='', error=''):
		self.render('hw3_new_post.html', subject = subject, content = content, error = error)
		
	def get(self):
		self.render_front()
		
	def post(self):
		subject = self.request.get('subject')
		content = self.request.get('content')
		
		if subject and content:
			post = Post(subject = subject, content = content)
			post.put()
			post_id = str(post.key().id())
			HW6_update_all_posts()
			self.redirect('/blog/%s' % post_id)
		else:
			error = 'subject and content cannot be blank'
			self.render_front(subject, content, error)
			

class HW3PostHandler(Handler):
	def render_front(self, post_id='', subject='', content='', created='', age='', error=''):
		self.render('hw3_post.html', post_id = post_id, subject = subject, content = content, created = created, age = age, error = error)
		
	def get(self, post_id):
		post = HW6_get_post(post_id)
		if post:
			self.render_front(post_id, post.subject, post.content, post.created, HW6_get_single_post_query_age(post_id), '')
		else:
			self.render_front(post_id, '', '', '', 'post does not exit ?.?')


class HW3BlogPageHandler(Handler):
	def get(self):
		posts = HW6_get_all_posts()
		self.render('hw3_blog.html', posts = posts, age = HW6_get_all_posts_query_age())


# -------------------- hw4 --------------------
"""
In order to be graded correctly for this homework, there are a few things to keep in mind. 
We'll be grading your web app by POSTing new users to your signup form and checking that we 
correctly get redirected and a cookie gets set. 
There are a few main issues you need to keep in mind in order for this to work:

    - We assume your form to signup new users is at a path of '/signup' from the url you enter. That is, 
      if you enter 'www.myblog.com/blog' in the text field above, then the form is at 'www.myblog.com/blog/signup'.
    - The form method must be POST, not GET.
    - The form input boxes must have the names 'username', 'password', 'verify', and 'email' in order for the 
	  grading script to correctly post to them.
    - Don't forget to escape your output!

Also, the basic methods you'll use to set and get cookies are as follows: In order to get 
a cookie you receive from the user, you can use 'self.request.cookies.get(name)', where name 
is the name of the cookie you are looking for. In order to send a cookie to a user, you simply 
add the header to your response. For example, 'self.response.headers.add_header('Set-Cookie', 'name=value; Path=/')', 
where name is the name of the cookie, and value is the value you're setting it to. The Path section of the 
header should be left as is for our purposes.

If you're interested in the css styling file we use for the example page, the link is here.

"""

class User(db.Model):
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	user_email = db.StringProperty(required = False)
	created = db.DateTimeProperty(auto_now_add = True)
	
SECRET = 'imsosecret'
def hash_str(s):
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
	val = h.split('|')[0]
	return h == make_secure_val(val)
	
def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = make_salt()):
	h = hashlib.sha256(name + pw + salt).hexdigest()
	return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
	return h == make_pw_hash(name, pw, h.split(',')[1])

class HW4SignUpHandler(Handler):
	def render_front(self, username='', password='', verify='', email='', username_error='', password_error='', verify_error='', email_error=''):
		self.render('hw4_sign_up.html', username = username, 
										password = password, 
										verify = verify, 
										email = email, 
										username_error = username_error,
										password_error = password_error,
										verify_error = verify_error,
										email_error = email_error)
			
	def get(self):
		self.render_front()
			
	def post(self):
		user_username = escape_html(self.request.get('username'))
		user_password = escape_html(self.request.get('password'))
		user_verify = escape_html(self.request.get('verify'))
		user_email = escape_html(self.request.get('email'))
		
		username_error = ''
		password_error = ''
		verify_error = ''
		email_error = ''
		
		username = self.valid_username(user_username)
		password = self.valid_password(user_password)
		
		is_valid = True
		
		if not username:
			username_error = escape_html("That's not a valid username.")
			is_valid = False;
		
		if not password:
			password_error = escape_html("That wasn't a valid password.")
			is_valid = False;
		else:
			verify = self.valid_password_verify(user_password, user_verify)
			if not verify:
				verify_error = escape_html("Your passwords didn't match.")
				is_valid = False;
		
		password = ''
		verify = ''
		
		if user_email:
			email = self.valid_email(user_email)
			if not email:
				email_error = escape_html("That's not a valid email.")
				is_valid = False;
				
		if is_valid:
			query = db.GqlQuery("SELECT * FROM User WHERE username = :1", user_username)
			user = query.get()
			if user:
				username_error = escape_html("That user already exists.")
				is_valid = False;
				
		
		if is_valid:
			user = User(username = user_username, password = make_pw_hash(user_username, user_password), email = user_email)
			user.put()
			user_id = str(user.key().id())
			hash = make_secure_val(user_id)
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % (hash))
			self.redirect("/blog/welcome")
		else:
			self.render_front(user_username, '', '', user_email, username_error, password_error, verify_error,  email_error)
	
	def valid_username(self, username):
		return USER_RE.match(username)
		
	def valid_password(self, password):
		return PWD_RE.match(password)
	
	def valid_password_verify(self, password, verify):
		if self.valid_password(password):
			if password == verify:
				return verify
		return None
	
	def valid_email(self, email):
		return EMAIL_RE.match(email)

class HW4WelcomeHandler(Handler):
	def render_front(self, username=''):
		self.render('hw4_welcome.html', username = username)
	
	def get(self):
		hash = self.request.cookies.get('user_id')
		check = check_secure_val(hash)
		if check == True:
			user_id = hash.split('|')[0]
			user = User.get_by_id(long(user_id))
			self.render_front(user.username)
		else:
			self.redirect("/blog/signup")
			
class HW4SignInHandler(Handler):
	def render_front(self, username='', error=''):
		self.render('hw4_sign_in.html', username = username, error = error)
	
	def get(self):
		self.render_front()
		
	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')
		
		error = 'Invalid login'
		
		if username and password:
			query = db.GqlQuery("SELECT * FROM User WHERE username = :1", username)
			user = query.get()
			if user:
				hash = user.password
				check = valid_pw(username, password, hash)
				if check:
					user_id = str(user.key().id())
					hash = make_secure_val(user_id)
					self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % (hash))
					self.redirect("/blog/welcome")
				else:
					self.render_front(username, error)
			else:
				self.render_front(username, error)
		else:
			self.render_front(username, error)

class HW4SignOutHandler(Handler):
	def get(self):
		self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % (''))
		self.redirect("/blog/signup")

# -------------------- hw5 --------------------
'''
In order to be graded correctly for this homework, there are a few things to keep in mind. 
We\'ll be grading your web app by checking the JSON output on both the front page and permalink pages. 
Note that we still require all the functionality from previous homeworks.

    We assume your frontpage JSON is at a location of "/.json from the URL you enter. 
	That is, if you enter \'www.myblog.com/blog\' in the text field above, then your frontpage JSON 
	is at \'www.myblog.com/blog/.json\'. We assume your permalink JSON is at ".json" from your permalink URLs.
	
	signup_url = url + "/signup"
	login_url = url + "/login"
	logout_url = url + "/logout"
	post_url = url + "/newpost"
	json_url = url + "/.json"
	permalink_json_url = permalink_url + ".json

Sample output:
{"content": "again", "created": "Tue May  8 23:04:17 2012", "last_modified": "Tue May  8 23:04:17 2012", "subject": "the suit is back!"}

'''

class HW5BlogPageJSONHandler(Handler):
	def get(self):
		posts = HW6_get_all_posts()
		l = []
		for post in posts:
			p = {
				'content': post.content,
				'created': post.created.strftime("%a %b %d, %Y %I:%M %p"), #May 09, 2012 04:35 PM
				'subject': post.subject }
			l.append(p)
		self.response.headers['Content-Type'] = "application/json; charset=utf-8"
		self.response.out.write(json.dumps(l))

class HW5PostJSONHandler(Handler):
	def get(self, post_id):
		post = Post.get_by_id(long(post_id))
		if post:
			p = {
				'content': post.content,
				'created': post.created.strftime("%a %b %d, %Y %I:%M %p"), #May 09, 2012 04:35 PM
				'subject': post.subject }
			self.response.headers['Content-Type'] = "application/json; charset=utf-8"
			self.response.out.write(json.dumps(p))


# -------------------- hw6 --------------------

CACHE = {}
AGE = {}

KEY = 'ALLPOSTS'

def HW6_get_all_posts():
	key = 'ALLPOSTS'
	result = gets(key)
	if result:
		posts, hash = result
		logging.error('cache hit for get all posts')
		return posts
	else:
		posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
		posts = list(posts)
		set(key, posts)
		set('AGE-ALLPOSTS', datetime.now())
		logging.error('db hit for get all posts')
		return posts

def HW6_update_all_posts():
	key = 'ALLPOSTS'
	result = gets(key)
	if result:
		posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
		posts = list(posts)
		set(key, posts)
		set('AGE-ALLPOSTS', datetime.now())
		logging.error('db hit for get all posts')
		
def HW6_get_query_age(key):
	query_time = get(key)
	now = datetime.now()
	diff = now - query_time
	return diff.seconds
	
def HW6_get_all_posts_query_age():
	key = 'AGE-ALLPOSTS' 
	return HW6_get_query_age(key)

def HW6_get_post(post_id):
	key = 'POST-%s' %  post_id
	result = gets(key)
	if result:
		post, hash = result
		logging.error('cache hit for get single post for id %s' % post_id)
		return post
	else:
		post = Post.get_by_id(long(post_id))
		set(key, post)
		set('AGE-POST-%s' %  post_id, datetime.now())
		logging.error('db hit for get single post for id %s' % post_id)
		return post

def HW6_get_single_post_query_age(post_id):
	key = 'AGE-POST-%s' %  post_id
	return HW6_get_query_age(key)

def HW6_clear_all_cache():
	flush()
		

#return True after setting the data
def set(key, value):
	#CACHE[key] = value
	memcache.set(key, value)
	return True

#return the value for key
def get(key):
	#return CACHE.get(key)
	return memcache.get(key)

#delete key from the cache
def delete(key):
	if key in CACHE:
		del CACHE[key]

#clear the entire cache
def flush():
	#CACHE.clear()
	memcache.flush_all()

#return a tuple of (value, h), where h is hash of the value. a simple hash
#we can use here is hash(repr(val))
def gets(key):
	val = get(key)
	if val:
		return val, hash(repr(val))

# set key = value and return True if cas_unique matches the hash of the value
# already in the cache. if cas_unique does not match the hash of the value in
# the cache, don't set anything and return False.
def cas(key, value, cas_unique):
	r = gets(key)
	if r is None:
		return set(key, value)
	else:
		v, h = r
		if h == cas_unique:
			return set(key, value)
		else:
			return False
			
class HW6ClearCacheHandler(Handler):
	def get(self):
		HW6_clear_all_cache()
		self.redirect("/blog")
	

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/unit02_hw_1_rot13', Unit02HW1),
							   ('/unit02_hw_2_signup', Unit02HW2),
							   ('/welcome', WelcomeHandler),
							   ('/blog', HW3BlogPageHandler),
							   ('/blog/newpost', HW3NewPostHandler),
							   ('/blog/([0-9]+)', HW3PostHandler),
							   ('/blog/signup', HW4SignUpHandler),
							   ('/blog/welcome', HW4WelcomeHandler),
							   ('/blog/login', HW4SignInHandler),
							   ('/blog/logout', HW4SignOutHandler),
							   ('/blog/.json', HW5BlogPageJSONHandler),
							   ('/blog/([0-9]+).json', HW5PostJSONHandler),
							   ('/blog/flush', HW6ClearCacheHandler)],
                              debug=True)
