
import webapp2
from pages import Page #from package import Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My page!"
        p.css = "css/style.css"
        p.body = "Miss Piggy likes Kermit De Frog"

        self.response.write(p.whole_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
