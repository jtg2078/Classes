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
import webapp2
import cgi
import re

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


app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/unit02_hw_1_rot13', Unit02HW1),
							   ('/unit02_hw_2_signup', Unit02HW2),
							   ('/welcome', WelcomeHandler)],
                              debug=True)
