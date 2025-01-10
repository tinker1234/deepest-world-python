import js

class Entity:
    def __init__(self):
        self.d = js.dw
    
    def findOne(self, f):
        self.d.findOneEntity(f)

    def findClosest(self, f):
        self.d.findClosest(f)
    
    def findAll(self, f):
        self.d.findAllEntities(f)
