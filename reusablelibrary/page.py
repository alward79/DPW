from lib import Jewelry

class Page(object):#class to collect data though input.
    def __init__(self):
        #default title and css link
        self.title = "Welcome Accessories and more"
        self.css = "css/style.css"
        #head of the html that will diplay title and css
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        #html the will store the form the user has to fill out
        self.body = '''
            <div id="form">
                <form method="GET" action="">
                    <h1>Jewelry Choice</h1>
                    <p>Where you can get handmade jewelry</p>
                    <h3>Add your purchase</h3>
                    <p>Necklaces are $10 <br/> Earrings are $5 <br/> Bracelets are $8</p>
                    <p>If we don't have what you want we can make it for you.</p>
                    <label>Jewelry Type: </label><input type="text" name="jewel" class="input"/><br />
                    <label>Quantity: </label><input type="text" name="quantity" class="input"/><br />
                    <label>Price: </label><input type="text" name="price" class="input"/><br />
                    <label>Email: </label><input type="text" name="email" class="input"/><br /><br />
                    <input type="submit" value="Submit" class="submit" />
                </form>
            </div>
        '''
        #closing section of html
        self.close = """
    </body>
</html> """

    #first view form class Page that will show head body and close and return the info.
    def print_out(self):
        result = self.head + self.body + self.close
        result = result.format(**locals())
        return result

#display second view with results depending on results from MainHandler.
class Results(object):
    def __init__(self):
        self.title = "Welcome Accessories and more"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        #passing variable values from input
        self.body = '''
            <div id="form">
                <h1>Jewelry Choice</h1>
                <form method="GET" action="">
                    <p>Where you can find any type of handmade jewelry!</p>
                    <h3>Add your purchase</h3>
                    <p>Necklace is $10 <br/> Earrings are $5 <br/> Bracelet is $8</p>
                    <p>If we don't have what you want we can make it for you.</p>
                    <label>Jewelry Type: </label><input type="text" name="jewel" class="input"/><br />
                    <label>Quantity: </label><input type="text" name="quantity" class="input"/><br />
                    <label>Price: </label><input type="text" name="price" class="input"/><br />
                    <label>Email: </label><input type="text" name="email" class="input"/><br /><br />
                    <input type="submit" value="Submit" class="submit" />
                </form>
            </div>

        '''
        #passing stored values to be viewed in browser
        self.info = Jewelry()
        self.display = '''
            <div id="response">
                {self.info.message}
                <ul>
                    <li><label>Jewelry Choice: </label></li><li id="result">{self.info.jewelry}</li>
                </ul>
                <ul>
                    <li><label>Quantity: </label></li><li id="result">{self.info.quantity}</li>
                </ul>
                <ul>
                    <li><label>Price: </label></li><li id="result">{self.info.price}</li>
                </ul>
                <ul>
                    <li><label>Email: </label></li><li id="result">{self.info.email}</li>
                </ul>
                <ul>
                    <li><label>Total: </label></li><li id="result">{self.info.total}</li>
                </ul>
            </div>
        '''
        self.close = """
    </body>
</html>"""
    #function to print results
    def print_out_results(self):#function to response the second view showing results, according to condition from MainHandler.
        result = self.head + self.display + self.close
        result = result.format(**locals())
        return result