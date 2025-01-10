
import js

class Misc:
    def __init__(self):
        self.d = js.dw
    
    def cancelOrder(self, order_id: int):
        "Requires a nearby market station"
        "@param order_id: the id of the order which is of type int"
        self.d.cancelOrder(order_id)
    
    def combine(self):
        "Combines all stackable items present in the recycler input"
        
        self.d.combine()
    
    def craft(self, opts):
        "Requires a nearby crafting station"
        "@param opts opts: more infomation found here https://deepestworld.com/api under Item>craft"
        self.d.craft(opts)
    
    def deleteItem(self, bag, index):
        "Possible bag values: d.c.inventory d.c.mailbox d.c.recycler.input d.c.bankTabs[i].items"
        
        self.d.deleteItem(bag, index)
    
    def enchant(self, opts):
        "Requires a nearby enchanting station"
        "@param opts opts: more infomation found here https://deepestworld.com/api under Item>enchant"
        
        self.d.enchant(opts)
    
    def equip(self, inventory_index: int, slot:str = None):
        "equip something"
        "@param inventory_index: where the items at (int)[required]"
        "@param slot: where to equip (str)[optional]"

        if slot:
            self.d.equip(inventory_index, slot)
        else:
            self.d.equip(inventory_index)

    def loadout(self, station_id:int):
        "changes gear sets"
        
        self.d.loadout(station_id)
    
    def moveItem(self, bag, index:int, dist_bag, dist_index:int = None):
        "Possible bag values: d.c.inventory d.c.mailbox d.c.recycler.input d.c.recycler.output d.c.bankTabs[i].items"

        if dist_index is not None:
            self.d.moveItem(bag, index, dist_bag, dist_index)
        else:
            self.d.moveItem(bag, index, dist_bag)
    
    def openItem(self, inventory_index:int):
        "To open items such as mission bags, packages, etc"

        self.d.openItem(inventory_index)
    
    def placeOrder(self, sell_options: dict={}, buy_options:dict={}):
        "more infomation found here https://deepestworld.com/api under Item>placeOrder"

        self.d.placeOrder(sell_options, buy_options)
    
    def recycle(self):
        "Recycles all valid items present in the recycler input"

        self.d.recycle()
    
    def sendItem(self, recipient_name:str, inventory_index: int):
        "The recipient has to be in your party"

        self.d.sendItem(recipient_name, inventory_index)
    
    def sendMail(self, recipient_name: str, inventory_indexes: list):
        "Requires a nearby mailbox station and costs 1 Silver"

        self.d.sendMail(recipient_name, inventory_indexes)
    
    def sortInventory(self):
        "Sort inventory"
        
        self.d.sortInventory()
    
    def takeAllItems(self, bag):
        "Possible bag values: d.c.mailbox d.c.recycler.output"

        self.d.takeAllItems(bag)
    
    def takeOrder(self, order_id:int):
        "Requires a nearby market station"

        self.d.takeOrder(order_id)
    
    def unequip(self, slot: str, inventory_index:int = None):
        "unequip something"
        "@param inventory_index: where to put item (int)[optional]"
        "@param slot: where to equip (str)[required]"

        if inventory_index is not None:
            self.d.unequip(slot, inventory_index)
        else:
            self.d.unequip(slot)
    


    
