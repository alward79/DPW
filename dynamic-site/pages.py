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
            <a href="?team=golden_state">Golden State Warriors</a>
            <a href="?team=houston">Houston Rockets</a>
            <a href="?team=clippers">Los Angeles Clippers</a>
            <a href="?team=portland">Portland Trail Blazers</a>
            <a href="?team=memphis">Memphis Grizzlies</a>
        </div>
        '''
        #static elements that will show before a team is clicked on
        self.info = '''
            <div id="info">
                <h1>NBA TOP TEAMS</h1>
                <h3>Choose Conference From Above</h3>
            </div>
        '''
        #will contain html
        self._results = ''
        self._close_results = '''</div>'''#close results div

    @property
    def results(self):
        pass

     #calculate teams Percent
	def __calc_pct(self, perc):
        pct = float(perc.wins) / float(perc.wins + perc.losses)#divide wins by wins+losses(total games)
        win_percentage = round(pct, 3)#round results 3 places
        return win_percentage#returns value of ptc to printed
