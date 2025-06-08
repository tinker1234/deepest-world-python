import js

class Entity:
    def __init__(self):
        self.d = js.dw
    
    def findOne(self, f):
        return self.d.findOneEntity(f)

    def findClosest(self, f):
        return self.d.findClosestEntity(f)
    
    def findAll(self, f):
        return self.d.findAllEntities(f)
