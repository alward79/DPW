'''
Angelena Ward
Reusable Library
Design Patterns for Web Programming
5/21/2015
'''
import webapp2
from lib import Jewelry

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #calling Jewelry() class from lib.py
        j = Jewelry()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
