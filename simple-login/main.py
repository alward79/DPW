'''
Angelena Ward
May 7
Design Patterns for Web Programming
practice
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #funciton that starts everything
        self.response.write('Hello world!')

#nver touch this part of whats making python work within browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
