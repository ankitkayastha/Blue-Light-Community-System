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


import cgi

from google.appengine.api import users

from google.appengine.ext import ndb

import webapp2

import models



MAIN_PAGE_HTML = """\
<html>
  <body>
    <!--if localStorage.get("userid") != null, redirect to Button_HTML-->
    <form action="/sign" method="post">
      
      <div>first name: <input type="text" name="fName"></div> 
      <div>last name: <input type="text" name="lName"></div>
      <div>phone number: <input type="tel" name="number"></div>
      <div>email: <input type="email" name="email"></div>
      <div><input type="submit" value="Submit"></div>

    </form>
  </body>
</html>
"""

BUTTON_HTML = """\

"""



class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write(MAIN_PAGE_HTML)


class SignUp(webapp2.RequestHandler):

    def post(self):

        fName = self.request.get('fName')
        lName = self.request.get('lName')
        phNumber = self.request.get('number')
        Email = self.request.get('email')

        user = models.Responder(firstName = fName, lastName = lName, phoneNum = phNumber, email = Email)
        user.put()

        querybutton = '/static/button.html' + "?code=" + str(user.key)
        #create simple blue button handler
        return webapp2.redirect(querybutton) #query parameter?

class Button(webapp2.RequestHandler):

  def get(self):
    self.response.write(BUTTON_HTML)





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', SignUp),
    ('/button', Button)
], debug=True)

