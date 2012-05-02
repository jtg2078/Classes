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

form="""
<form method="post" action="/testform" >
	<input name="q">
	<input type="submit">
</form>
"""

form="""
<form>
	<input type="checkbox" name="q">
	<input type="checkbox" name="r">
	<input type="checkbox" name="s">
	<br>
	<input type="submit">
</form>
"""

form="""
<form>
	<input type="radio" name="q">
	<input type="radio" name="r">
	<input type="radio" name="s">
	<br>
	<input type="submit">
</form>
"""

form="""
<form>
	<input type="radio" name="q" value="one">
	<input type="radio" name="q" value="two">
	<input type="radio" name="q" value="three">
	<br>
	<input type="submit">
</form>
"""

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
		<option>One</option>
		<option>Two</option>
		<option>Three</option>
	</select>
	<br>
	<input type="submit">
</form>
"""

form="""
<form>
	<select name="q">
		<option value="1">the number one, very descriptive</option>
		<option>Two</option>
		<option>Three</option>
	</select>
	<br>
	<input type="submit">
</form>
"""

form="""
<form method="post" action="/">
	What is your birthday?
	<br>
	<label> Month
		<input type="text" name="month">
	</label>
	
	<label> Day
		<input type="text" name="day">
	</label>
		
	<label> Year
		<input type="text" name="year">
	</label>
	
	<div style="color: red">%(error)s</div>
	
	<br>
	<br>
	<input type="submit">
</form>
"""

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
	# ---- Prof's version
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day > 0 and day <= 31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year >= 1900 and year <= 2020:
			return year

form="""
<form method="post" action="/">
	What is your birthday?
	<br>
	<label> Month
		<input type="text" name="month" value="%(month)s">
	</label>
	
	<label> Day
		<input type="text" name="day" value="%(day)s">
	</label>
		
	<label> Year
		<input type="text" name="year" value="%(year)s">
	</label>
	
	<div style="color: red">%(error)s</div>
	
	<br>
	<br>
	<input type="submit">
</form>
"""

import cgi
def escape_html(s):
	return cgi.escape(s, quote = True)

class MainHandler(webapp2.RequestHandler):
	
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error,
										"month": escape_html(month),
										"day": escape_html(day),
										"year": escape_html(year)})
	
	def get(self):
		#self.response.out.write(form)
		self.write_form()

	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')
		
		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)
		
		if not (month and day and year):
			#self.response.out.write(form)
			self.write_form("That doesn't look valid to me, friend.",
							user_month, user_day, user_year)
		else:
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! That's a totally valid day!")

class TestHandler(webapp2.RequestHandler):
	def post(self):
		#q = self.request.get("q")
		#self.response.out.write(q)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write(self.request)

# via GET
# 	output from my chrome
# 	GET /testform?q=l33t HTTP/1.0
# 	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# 	Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
# 	Accept-Language: en-US,en;q=0.8
# 	Connection: keep-alive
# 	Host: localhost:8082
# 	Referer: http://localhost:8082/
# 	User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.165 Safari/535.19

# via POST
# 	POST /testform HTTP/1.0
# 	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# 	Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3
# 	Accept-Language: en-US,en;q=0.8
# 	Cache-Control: max-age=0
# 	Connection: keep-alive
# 	Content-Length: 11
# 	Content-Type: application/x-www-form-urlencoded
# 	Content_Length: 11
# 	Content_Type: application/x-www-form-urlencoded
# 	Host: localhost:8082
# 	Origin: http://localhost:8082
# 	Referer: http://localhost:8082/
# 	User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.165 Safari/535.19
# 	
# 	q=some+word

app = webapp2.WSGIApplication([('/', MainHandler), 
							   ('/thanks', ThanksHandler), 
							   ('/testform', TestHandler)]
							  , debug=True)
