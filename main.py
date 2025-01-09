import js
import asyncio
import math
import time
import events


class Bot:
    def __init__(self):
        self.d = js.dw
        events.Event(self)


    def getId(self):
        return self.d.targetId

    def findClosestTarget(self, type: str) -> dict:
        if type == "monster":
            target = self.d.findClosestMonster()
            if target:
                return {"found": True, "id": target.id, "object": target, "name": target.name}
            else:
                return {"found": False}
        else:
            target = self.d.findClosestEntity(lambda ent: type == ent.classMd)
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

    def inRange(self, skill: int,  pos: tuple = None, target: any = None, id: int = None) -> bool:
        if pos:
            x,y = pos
            return self.d.isInRange(skill, x, y)
        elif target:
            return self.d.isInRange(skill, target)
        elif id:
            return self.d.isInRange(skill, id)
    
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
        if self.d.character.casting > time.time() * 1000:
            return True
        return False
    
    async def basicAttack(self):
        target = self.findClosestTarget("monster")
        if not target['found']:
            self.log('<span style="color: yellow; background-color: black;">No target found</span>')
            return
        if self.getId() != target['id']:
            self.setTarget(target)

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
            await self.basicAttack()
            await asyncio.sleep(0.25)

if __name__=="__main__":
    b = Bot()
    asyncio.create_task(b.main())
    #asyncio.create_task(main())