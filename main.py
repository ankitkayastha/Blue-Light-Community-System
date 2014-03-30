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
"""import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)"""


import cgi

from google.appengine.api import users

import webapp2


MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sign" method="post">
      <html><body>name
      <div><textarea name="fName" rows="1" cols="15"></textarea> <textarea name="lName" rows="1" cols="15"></textarea> </div>
      <html><body>phone number 
      <div><textarea name="number" rows="1" cols="30"></textarea></div>
      <html><body>email
      <div><textarea name="email" rows="1" cols="30"></textarea></div>
      <div><input type="submit" value="Submit"></div>
    </form>
  </body>
</html>
"""


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class SignUp(webapp2.RequestHandler):

    def post(self):
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('fName')))
        self.response.write(' ')
        self.response.write(cgi.escape(self.request.get('lName')))
        self.response.write('\n')
        self.response.write(cgi.escape(self.request.get('number')))
        self.response.write('\n')
        self.response.write(cgi.escape(self.request.get('email')))
        self.response.write('</pre></body></html>')


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', SignUp),
], debug=True)

