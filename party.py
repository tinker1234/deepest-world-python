import js

class Party:
    def __init__(self):
        self.d = js.dw
    
    def accept(self, data):
        self.d.partyAccept(data.id)
    
    def decline(self, data):
        self.d.partyDecline(data.id)
    
    def invite(self, name: str):
        self.d.partyInvite(name)

    def kick(self, name: str):
        self.d.partyKick(name)
    
    def leave(self):
        self.d.partyLeave()
    
    def promote(self, name: str):
        self.d.partyPromote(name)