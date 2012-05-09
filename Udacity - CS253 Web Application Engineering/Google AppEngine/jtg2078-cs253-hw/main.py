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
import jinja2
jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from datetime import datetime
from google.appengine.ext import db

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
			self.redirect('/blog/%s' % post_id)
		else:
			error = 'subject and content cannot be blank'
			self.render_front(subject, content, error)
			

class HW3PostHandler(Handler):
	def render_front(self, post_id='', subject='', content='', created='', error=''):
		self.render('hw3_post.html', post_id = post_id, subject = subject, content = content, created = created, error = error)
		
	def get(self, post_id):
		post = Post.get_by_id(long(post_id))
		if post:
			self.render_front(post_id, post.subject, post.content, post.created, '')
		else:
			self.render_front(post_id, '', '', '', 'post does not exit ?.?')


class HW3BlogPageHandler(Handler):
	def get(self):
		posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
		self.render('hw3_blog.html', posts = posts)


app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/unit02_hw_1_rot13', Unit02HW1),
							   ('/unit02_hw_2_signup', Unit02HW2),
							   ('/welcome', WelcomeHandler),
							   ('/blog', HW3BlogPageHandler),
							   ('/blog/newpost', HW3NewPostHandler),
							   ('/blog/([0-9]+)', HW3PostHandler)],
                              debug=True)
