#class with attributes for the teams info
class TopTeams(object):
    def __init__(self):
        self.__team_name = ''
        self.__img = ''
        self.__wins = 0
        self.__losses = 0
        self.__home_game = 0
        self.__road_game = 0

#class with instances of objects
class Data(object):
    def __init__(self):
        #eastern team instance
        atlanta = TopTeams() #attribute that will store values of atlanta

        cleveland = TopTeams() #attribute to store values for cleveland

        chicago = TopTeams() #attribute to store values for chicago

        toronto = TopTeams() #attribute to store values for toronto

        washington = TopTeams() #attribute to store values for washington

        #western team instance
        golden_state = TopTeams()#attribute to store values for golden state

        houston = TopTeams() #attribute to store values for houston

        clippers = TopTeams() #attribute to store values for LA clippers

        portland = TopTeams() #attribute to store values for portland

        memphis = TopTeams() #attribute to store values for memphis

        #array containing team instances
        self.eteam_array = [atlanta, cleveland, chicago, toronto, washington]

        #array containing team instances
        self.wteam_array = [golden_state, houston, clippers, portland, memphis]