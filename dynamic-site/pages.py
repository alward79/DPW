#superClass
class Page(object):
    def __init__(self):
        #html elements
        self.head = '''
<!DOCTYPE HTML>
<html>
	<head>
		<title>NBA Top Teams</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
	</head>
	<body>'''
        self.body = ''
        self.close = '''
    </body>
</html>'''

#subclass
class Content(Page):
    def __init__(self):
        #init subclass of superClass Page
        super(Content, self).__init__()

        #this will link the teams to buttons to return info
        self.links = '''
        <div id="team_links">
            <p>Eastern Conference</p>
        </div>

        <div id="team_links">
            <p>Western Conference</p>
        </div>
        '''
