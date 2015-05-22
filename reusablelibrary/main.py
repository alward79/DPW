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

        #variables to hold values.
        j = Jewelry()
        js = Jewels()
        page = Page()
        results = Results()

        #if statement to show data that's collected
        if self.request.GET:
            j.jewelry = self.request.GET['jewel']
            j.price = self.request.GET['price']
            j.quantity = self.request.GET['quantity']
            j.email = self.request.GET['email']
            j.question = js.question_answer()
            j.total = js.total_price(j.price, j.quantity)
            j.message = js.messages()
            results.info = j #assign data from view
            #response will write function print_out_library from class PageResult
            self.response.write(results.print_out_results())

        else:
            #will write print_out from class Page if not satisfied
            self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)