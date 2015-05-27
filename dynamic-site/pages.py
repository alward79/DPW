#superClass
class Page(object):
    def __init__(self):
        #html elements
        self.head = '''
<!DOCTYPE HTML>
<html>
	<head>
		<title>NBA Top 5 Teams</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
	</head>
	<body>'''
	    self.body = ''
	    self.close = '''
	</body>
</html>'''