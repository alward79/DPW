'''
Angelena Ward
May 7
Design Patterns for Web Programming
simple login
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #funciton that starts everything
        page_head = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Simple Form</title>
            </head>
            <body>'''

        page_body =  '''<form method="GET">

                </form>'''
        page_close = '''
            </body>
        </html>
        '''

#nver touch this part of whats making python work within browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
