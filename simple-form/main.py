'''
Angelena Ward
May 14, 2015
Design Patterns for Web Programming
simple form
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
                    <label>Name: </label> <input type="text" name="user" />
                    <label>Email: </label> <input type="text" name="email"/>
                    <input type="submit" value="Submit"?>

                </form>'''
        page_close = '''
            </body>
        </html>
        '''

        self.response.write(page_head +page_body+page_close) #print

    def additional_function(self):
        pass

#nver touch this part of whats making python work within browser
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
