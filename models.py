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
  email = ndb.StringProperty

  @classmethod
  def query_book(cls, ancestor_key):
    return cls.query(ancestor=ancestor_key).order(-cls.date)

class Event(ndb.Model):
	"""BLUE BUTTON PUSH INFORMATION"""
	location = GeoPtProperty
	datetime = DateTimeProperty
	


