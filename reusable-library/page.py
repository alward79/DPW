class Page(object):#class to collect data though input.
    def __init__(self):
        self.title = "Accessories and More"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = '''
            <div id = "page">
                <div id="form">
                    <form method="GET" action="">
                    <h1>Book Choice</h1>
                    <p>Where you can find every book your heart desires!</p>
                    <h3>Add your book purchase</h3>
                    <label>Title: </label><input type="text" name="title" class="input"/><br />
                    <label>Author: </label><input type="text" name="author" class="input"/><br />
                    <label>Year: </label><input type="text" name="year" class="input"/><br />
                    <label>Price: </label><input type="text" name="price" class="input"/><br />
                    <label>Quantity: </label><input type="text" name="quantity" class="input"/><br />
                    <label>Email: </label><input type="text" name="email" class="input"/><br /><br />
                    <input type="submit" value="Submit" class="submit" />
                </form>
                </div>
            </div>
        '''
        self.close = """
    </body>
</html> """
