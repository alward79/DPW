'''
Angelena Ward
5/15/2015
Design Patterns for Web Programming - Online
Reusable Library
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
