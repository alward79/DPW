'''
Angelena Ward
Reusable Library
Design Patterns for Web Programming
5/21/2015
'''
import webapp2
from lib import Jewelry
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #calling Jewelry() class from lib.py
        j = Jewelry()
        p = Page()
        self.head ="""
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link href="css/styles.css" rel="stylesheet">
     </head>
    <body>
    </body>
</html>
        """

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
