'''
Angelena Ward
Reusable Library
Design Patterns for Web Programming
05/21/2015
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
