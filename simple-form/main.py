'''
Angelena Ward
May 14, 2015
Design Patterns for Web Programming
simple form
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #funciton that starts everything

        #html for page_head, page_body, and page_close.
        page_head = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Simple Form</title>
            </head>
            <body>'''
        #page body is the form where the user inputs information into the fields
        page_body =  '''<form method="GET">
                    <label>Full Name </label> <input type="text" name="first" placeholder="First Name"/><input type="text" name="last" placeholder="Last Name"/></br>
                    <label>Email </label> <input type="text" name="email"/></br>
                    <label>Address </label>
                        <input type="text" name="address" placeholder="Street Address"/>
                        <input type="text" name="address" placeholder="Street Address Line 2"/>
                        <input type="text" name="city" placeholder="City" /></br>
                    <label>State </label>
                    <select class="half-size" name="address_state" id="state" required>
					<option value="AL">AL</option>
					<option value="AK">AK</option>
					<option value="AZ">AZ</option>
					<option value="AR">AR</option>
					<option value="CA">CA</option>
					<option value="CO">CO</option>
					<option value="CT">CT</option>
					<option value="DE">DE</option>
					<option value="DC">DC</option>
					<option value="FL">FL</option>
					<option value="GA">GA</option>
					<option value="HI">HI</option>
					<option value="ID">ID</option>
					<option value="IL">IL</option>
					<option value="IN">IN</option>
					<option value="IA">IA</option>
					<option value="KS">KS</option>
					<option value="KY">KY</option>
					<option value="LA">LA</option>
					<option value="ME">ME</option>
					<option value="MD">MD</option>
					<option value="MA">MA</option>
					<option value="MI">MI</option>
					<option value="MN">MN</option>
					<option value="MS">MS</option>
					<option value="MO">MO</option>
					<option value="MT">MT</option>
					<option value="NE">NE</option>
					<option value="NV">NV</option>
					<option value="NH">NH</option>
					<option value="NJ">NJ</option>
					<option value="NM">NM</option>
					<option value="NY">NY</option>
					<option value="NC">NC</option>
					<option value="ND">ND</option>
					<option value="OH">OH</option>
					<option value="OK">OK</option>
					<option value="OR">OR</option>
					<option value="PA">PA</option>
					<option value="RI">RI</option>
					<option value="SC">SC</option>
					<option value="SD">SD</option>
					<option value="TN">TN</option>
					<option value="TX">TX</option>
					<option value="UT">UT</option>
					<option value="VT">VT</option>
					<option value="VA">VA</option>
					<option value="WA">WA</option>
					<option value="WV">WV</option>
					<option value="WI">WI</option>
					<option value="WY">WY</option>
				</select></br>

                <label for="range">Gender</label>
				<input type="radio" name="gender" value="female"> Female
				<input type="radio" name="gender" value="male"> Male </br>

                <input type="checkbox" name="option1" value="terms" required> I agree to the terms and conditions<br>
			    <input type="checkbox" name="option2" value="terms" required> I agree all the information above is correct<br>

                <input type="submit" value="Submit"?>

                </form>'''
        #closing for page
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
