class Page(object):#class to collect data though input.
    def __init__(self):
        self.title = "Welcome Accessories and more"
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

        self.body = """
            <div id="form">
                    <form method="GET" action="">
                    <h1>Jewelry Choice</h1>
                    <p>Where you can find any type of handmade jewelry!</p>
                    <h3>Add your purchase</h3>
                    <p>If we don't have what you want we can make it for you.</p>
                    <label>Jewelry Type: </label><input type="text" name="jewel" class="input"/><br />
                    <label>Quantity: </label><input type="text" name="quantity" class="input"/><br />
                    <label>Price: </label><input type="text" name="price" class="input"/><br />
                    <label>Email: </label><input type="text" name="email" class="input"/><br /><br />
                    <input type="submit" value="Submit" class="submit" />
                </form>
                </div>

        """
        self.close = """
    </body>
</html> """

