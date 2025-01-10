import js
import asyncio
import math
import time
import events
import random
import party
import mission
import building
import misc
import entity
class Bot:
    def __init__(self):
        self.d = js.dw
        self.ignore = []
        self.party = party.Party()
        self.mission = mission.Mission()
        self.building = building.Building()
        self.misc = misc.Misc()
        self.entity = entity.Entity()
        events.Event(self)

    def random_xy(self):
        try:
            start_x = int(self.d.character.x)
            start_y = int(self.d.character.y)
            end_x = start_x + 5
            end_y = start_y + 5
            return (random.randint(start_x, abs(end_x)), random.randint(start_y, abs(end_y)))
        except Exception as e: print('error', e)
        

    def getId(self):
        return self.d.targetId
    
    def canGather(self, target) -> bool:
        return self.d.canGather(target['object'])
    
    def findResource(self, name: str, level: int = 1):
        n = []
        target = self.entity.findClosest(lambda ent: ent.name.lower() == name.lower() and ent.level == level)
        if target:
            return {"found": True, "object": target, "id": target.id, "name": target.name}

        return {"found": False}

    async def gather(self, name: str = 'tree', level: int = 1):
        target = self.findResource(name, level)
        if not target['found']:
            self.log("<span style='color: yellow; background-color: black;'>Can't find resource</span>")
            x, y = self.random_xy()
            self.move(x,y)
            self.log(f"<span style='color: gray; background-color: black;'>moving character randomly ({x}, {y})")
            return
        if not self.canGather(target):
            return
        if not self.inRange(target=target, resource=True):
            self.log(f"<span style='color: red; background-color: black;'>found {target['name']}#{target['id']} moving to it..</span>")
            self.moveToTarget(target)
            return
        self.log(f"<span style='color: blue; background-color: black;'>gathering{target['name']}#{target['id']}...</span>")
        self.d.gather(target['id'])

    def findClosestTarget(self, type: str) -> dict:
        target = self.entity.findClosest(lambda ent: type == ent.classMd)
        if target:
            return {"found": True, "id": target.id, "object": target, "name": target.name}
        else:
            return {"found": False}
            
    def move(self, x:int, y:int) -> None:
        self.d.move(x, y)
    
    def moveToTarget(self, target):
        target = target['object']
        self.move(target.x, target.y)
    
    def log(self, text: str):
        self.d.log(text)
    
    def getSkills(self) -> list: return self.d.character.skills
    
    def checkSkillToUse(self) -> int:
        
        skill_md = "dmg1"
        # Check main-hand weapon type and adjust skill_md
        if self.d.character.gear.mainHand:
            if self.d.character.gear.mainHand.type in [self.d.enums.Type.BOW]:
                skill_md = "dmg2"
            elif self.d.character.gear.mainHand.type in [self.d.enums.Type.WAND]:
                skill_md = "dmg3"
        return next((i for i, skill in enumerate(self.getSkills()) if skill and skill.md == skill_md), 00   -1)

    def inRange(self,  skill: int = None,  pos: tuple = None, target: any = None, id: int = None, resource: bool = False) -> bool:
        if not resource:
            if pos:
                x,y = pos
                return self.d.isInRange(skill, x, y)
            elif target:
                return self.d.isInRange(skill, target)
            elif id:
                return self.d.isInRange(skill, id)
        else:
            return self.d.isInGatherRange(target['object'])
    
    def canPayCost(self, skill_index: int) -> bool:
        return self.d.canPayCost(skill_index)
    
    def setTarget(self, target) -> None:
        self.d.setTarget(target['id'])

    def canUseSkill(self, skill: int,  pos: tuple = None, target: any = None, id: int = None) -> bool:
        if pos:
            x,y = pos
            return self.d.canUseSkill(skill, x, y)
        elif target:
            return self.d.canUseSkill(skill, target)
        elif id:
            return self.d.canUseSkill(skill, id)

    async def useSkill(self, skill_index: int, pos: tuple = None, target: any = None, id: int = None)->None:
        if pos:
            x,y = pos
            await self.d.useSkill(skill_index, x, y)
        elif target:
            await self.d.useSkill(skill_index, target)
        elif id:
            await self.d.useSkill(skill_index, id)

    def isCasting(self):
        if self.d.c.casting > time.time() * 1000:
            return True
        return False
    
    async def basicAttack(self):
        target = self.findClosestTarget("monster")
        if not target['found']:
            self.log('<span style="color: yellow; background-color: black;">No target found</span>')
            x, y = self.random_xy()
            self.move(x,y)
            self.log(f"<span style='color: gray; background-color: black;'>moving character randomly ({x}, {y})")
            return
        if self.getId() != target['id']:
            if str(target['id']) not in self.ignore:
                self.setTarget(target)
            if str(self.getId()) in self.ignore:
                self.d.targetId = 0

        skill_index = self.checkSkillToUse()
        if skill_index <0:
            self.log("skill not found")
            return
        if not self.isOnCooldown(skill_index):
            if not self.inRange(skill_index, id = target['id']):
                self.log(f"<span style='color: red; background-color: black;'>{target['name']}#{target['id']} to far moving closer</span>")
                self.moveToTarget(target)
                return
            
            can = self.canUseSkill(skill_index, id = target['id'])
            if can:
                await self.useSkill(skill_index, id = target['id'])
                self.log(f"<span style='color: blue; background-color: black;'>Attacking {target['name']}#{target['id']}")
        else: 
            self.log("<span style='color: red; background-color: black;'>Skill is on cooldown</span>")

    
    def isOnCooldown(self, skill_index: int) -> bool:
        return self.d.isOnCd(skill_index)
    
    def isOnGlobalCooldown(self) -> bool:
        return self.d.isOnGcd()

    async def main(self):
        while True:
            #await self.gather()
            await self.basicAttack()
            await asyncio.sleep(0.25)

if __name__=="__main__":
    b = Bot()
    asyncio.create_task(b.main())
    #asyncio.create_task(main())