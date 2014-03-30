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

from models import Responder

import json



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

        user = Responder(firstName = fName, lastName = lName, phoneNum = phNumber, email = Email, message = Message)
        user.put()

        querybutton = '/static/button.html' + "?code=" + str(user.key.urlsafe())
        #create simple blue button handler
        return webapp2.redirect(querybutton) #query parameter?

class Button(webapp2.RequestHandler):

    def get(self):
      self.response.write(BUTTON_HTML)

class GetLocation(webapp2.RequestHandler):

    def post(self):
      lon = self.request.get('lon')
      lat = self.request.get('lat')
      key = self.request.get('key')
      trouble = bool(self.request.get('assistance'))

      temp_key = ndb.Key(urlsafe=key)
      temp = temp_key.get();
      temp.lon = lon
      temp.lat = lat
      temp.trouble = trouble
      temp.put()

      # qry = ndb.gql("SELECT * FROM Responder")

      responders = Responder.query(Responder.key != temp_key).fetch()

      responders_list = list()
      for responder in responders:
        responder_dict = {
          'firstName' : responder.firstName,
          'lastName' : responder.lastName,
          'phoneNum' : responder.phoneNum,
          'email' : responder.email,
          'message' : responder.message,
          'lat' : responder.lat,
          'lon' : responder.lon,
          'trouble' : responder.trouble
        }
        responders_list.append(responder_dict)



      # qry = models.Responder.query("NO" != temp.key)

      self.response.write(json.dumps(responders_list))





app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', SignUp),
    ('/button', Button),
    ('/consumer', GetLocation)
], debug=True)

