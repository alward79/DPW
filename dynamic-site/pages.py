#superClass
class Page(object):
    def __init__(self):
        #html elements
        self._head = '''
<!DOCTYPE HTML>
<html>
	<head>
		<title>NBA Top Teams</title>
		<link href="css/style.css" rel="stylesheet" type="text/css" >
	</head>
	<body>'''
        self._body = ''
        self._close = '''
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
            <a href="?team=atlanta">Atlanta Hawks</a>
            <a href="?team=cleveland">Cleveland Cavaliers</a>
            <a href="?team=chicago">Chicago Bulls</a>
            <a href="?team=toronto">Toronto Raptors</a>
            <a href="?team=washington">Washington Wizards</a>
        </div>

        <div id="team_links">
            <p>Western Conference</p>
        </div>
        '''
