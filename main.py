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
      
      <div>First Name: <input type="text" name="fName"></div> 
      <div>Last Name: <input type="text" name="lName"></div>
      <div>Phone Number: <input type="tel" name="number"></div>
      <div>Email: <input type="email" name="email"></div>
      <div>Additional Info: <input type="text" name="Additional Info"></div>
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
        Message = self.request.get('Additional Info')

        user = models.Responder(firstName = fName, lastName = lName, phoneNum = phNumber, email = Email, message = Message)
        user.put()

        querybutton = '/static/button.html' + "?code=" + str(user.key)
        #create simple blue button handler
        return webapp2.redirect(querybutton) #query parameter?

class GetLocation(webapp2.RequestHandler):

    def post(self):
      lon = self.request.get('lon')
      lat = self.request.get('lat')
      key = self.request.get('key')
      trouble = self.request.get('trouble')

      temp = key.get(key)
      temp.lon = lon
      temp.lat = lat
      temp.trouble = trouble

      qry = Responder.query(Responder.key != temp.key)

      return qry





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', SignUp),
    ('/button', Button)
], debug=True)

