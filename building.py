import js


class Building:
    def __init__(self):
        self.d = js.dw
    
    def destroy(self, station_id):
        self.d.destroyStation(station_id)
    
    def place(self, inventory_index: int, x: int, y: int, variation: int = 0):
        '''
        Place a station

        '''
        self.d.placeStation(inventory_index, x, y, variation)
    
    def repair(self, station_id: int):
        self.d.repair(station_id)
    
    def take(self, station_id: int):
        self.d.takeStation(station_id)
    
