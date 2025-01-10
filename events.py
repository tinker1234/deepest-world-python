import config
from pyodide.ffi import create_proxy

class Event:
    def __init__(self, bot):
        self.bot = bot
        self.d = bot.d
        self.party = bot.party
        self.register()
        self.events = [
            "skillUsed",
            "drawOver",
            "drawUnder",
            "effectCreated",
            "effectDeleted", 
            "effectUpdated",
            "skillTriggered",
            "partyInvite",
            "whisper"
            ]
    
    def unregisterAll(self):
        self.d.offAll(self.events)

    def register(self):
        self.onSkillUsedProxy = create_proxy(self.onSkillUsed)
        self.onDrawOverProxy = create_proxy(self.onDrawOver)
        self.onDrawUnderProxy = create_proxy(self.onDrawUnder)
        self.onEffectCreatedProxy = create_proxy(self.onEffectCreated)
        self.onEffectUpdatedProxy = create_proxy(self.onEffectUpdated)
        self.onEffectDeletedProxy = create_proxy(self.onEffectDeleted)
        self.onSkillTriggeredProxy = create_proxy(self.onSkillTriggered)
        self.onParyInviteProxy = create_proxy(self.onParyInvite)
        self.onWhisperProxy = create_proxy(self.onWhisper)
        self.d.on("skillUsed", self.onSkillUsedProxy)
        self.d.on("drawOver", self.onDrawOverProxy)
        self.d.on("drawUnder", self.onDrawUnderProxy)
        self.d.on("effectCreated", self.onEffectCreatedProxy)
        self.d.on("effectUpdated", self.onEffectUpdatedProxy)
        self.d.on("effectDeleted", self.onEffectDeletedProxy)
        self.d.on("skillTriggered", self.onSkillTriggeredProxy)
        self.d.on("whisper", self.onWhisperProxy)
        self.d.on("partyInvite", self.onParyInviteProxy)

    def onSkillUsed(self, data):
        pass

    def onDrawOver(self, ctx, cx, cy, *args):
        pass
    
    def onDrawUnder(self, ctx, cx, cy, *args):
        pass

    def onEffectCreated(self, data):
        pass

    def onEffectDeleted(self, data):
        pass

    def onEffectUpdated(self, data):
        pass

    def onSkillTriggered(self, data):
        pass
    
    def onParyInvite(self, data):
        pass

    def onWhisper(self, data):
        if data.name.lower() in config.allowed:
            dt = data.message.split(" ")
            if "-sk" in data.message:
                 self.bot.log(f"<span style='color: white; background-color: black;'>{[skill.md for skill in self.bot.getSkills() if skill]}</span>")
            if dt[0] == "-aig":
                self.bot.ignore.append(dt[1])
            elif "-cig" in data.message:
                self.bot.ignore = []
            elif "-gig" in data.message:
                self.bot.log(f"<span style='color: white; background-color: black;'>{self.bot.ignore}</span>")
        else:
            self.bot.log(f"<span style='color: blue; font-size: 20px; background-color: white;'>{data.name}: {data.message}")