class Jewelry(object):
    def __init__(self):
        #public attributes to be accessed from mainhandler
        self.jewelry =''
        self.quantity = 0
        self.price = 0
        self.__total = 0
        self.email = ''
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.__body = "Welcome Accessories and more!"
        self.close = """
    </body>
</html>
        """