import js


class Mission:
    def __init__(self):
        self.d = js.dw
    
    def abandon(self):
        self.d.abandonMission()
    
    def getMissions(self, mission_type):
        return self.d.fetchMissions(mission_type)

    def join(self, id):
        self.d.joinMission(id)
    
    def setPrivate(self):
        self.d.makeMissionPrivate()
    
    def setPublic(self):
        self.d.makeMissionPublic()
    
    def start(self, mission_type: str, mission_level: int):
        self.d.tartMission(mission_type, mission_level)


    
