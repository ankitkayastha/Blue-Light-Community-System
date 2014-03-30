import webapp2
from google.appengine.ext import db

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>')
    greetings = db.GqlQuery("SELECT * "
                            "FROM Greeting "
                            "ORDER BY date DESC LIMIT 10")