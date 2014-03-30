import cgi
import urllib
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

class Responder(ndb.Model):
  """USER INFORMATION ENTITY"""
  firstName = ndb.StringProperty()
  lastName = ndb.StringProperty()
  phoneNum = ndb.StringProperty()
  email = ndb.StringProperty()
  message = ndb.StringProperty()
  lat = ndb.StringProperty()
  lon = ndb.StringProperty()
  trouble = ndb.BooleanProperty()

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)


	


