'''
Angelena Ward
5/28/2015
Design Patterns for Web Programming
Dynamic Site
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
