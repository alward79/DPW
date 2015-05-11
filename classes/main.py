'''
classes in python
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()


class Button(object):
    #contructor method init or setup method
    def __init(self):
        print "constructor method fo button ran"
        self.label ="" #public attribute
        self.__size = 60 #private attribute - 2 underscores
        self._color = "0x0000" #protected attribute - 1 underscore accessible inside class only
        #self.click()
        #self.on_roll_over("Hello!")

    #click method
    def click(self):
        print "I've been clicked"

    #rollover method
    def on_roll_over(self, message):
        print "You've rolled over my button" +message

    def show_label(self):
        print "My label is " + self.label

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
