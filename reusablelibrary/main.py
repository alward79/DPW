'''
Angelena Ward
Reusable Library
Design Patterns for Web Programming
5/21/2015
'''


import webapp2
from lib import Jewelry, Jewels
from page import Page, Results

#lunches application
class MainHandler(webapp2.RequestHandler):
    #defines variables to hold values
    def get(self):

        #variable referencing the classes from lib.py and page.py
        j = Jewelry()
        js = Jewels()
        page = Page()
        results = Results()

        #if statement to show data that's collected from the Jewlery() and Jewls() classes from lib.py
        if self.request.GET:
            #will collect user input from Jewlery() 
            j.jewelry = self.request.GET['jewel']
            j.price = self.request.GET['price']
            j.quantity = self.request.GET['quantity']
            j.email = self.request.GET['email']
            #will get info from Jewels class from user and run question_answer() function 
            j.question = js.question_answer()
            #will calculate the user input from Jewelry() and calculate it using the total_price() function 
            j.total = js.total_price(j.price, j.quantity)
            #once submit is hit the message from the messages() function will run and show a message
            j.message = js.messages()
            results.info = j #assign data from view
            #response will write function print_out_results from class Result
            self.response.write(results.print_out_results())

        else:
            #will write print_out from class Page if not satisfied
            self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)