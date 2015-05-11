'''
classes in python
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_buttod44
        #contact_button = Button()

class Button(object):
    #contructor method init or setup method
    def __init(self):
        print "constructor method fo button ran"
        #self.click()
        #self.on_roll_over("Hello!")

    #click method
    def click(self):
        print "I've been clicked"

    #rollover method
    def on_roll_over(self, message):
        print "You've rolled over my button" +message

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
