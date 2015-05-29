'''
Angelena Ward
5/28/2015
Design Patterns for Web Programming
Dynamic Site
'''

import webapp2
from pages import Content #imports from pages.py the Content() class
from data import Data #import from data.py the Data() class

#MainHandler() receives and handles request
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #refencing the subclasses from pages.py and data.py
        page = Content()
        data = Data()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
