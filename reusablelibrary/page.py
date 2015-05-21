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

        """
        self.close = """
    </body>
</html> """

