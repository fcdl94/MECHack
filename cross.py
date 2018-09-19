
class Cross:
    def __init__(self, idx, lat, long, r):
        self.cars = {}
        self.idx = idx
        self.lat = lat
        self.lng = long
        self.r = r
        
    def add_car(self, car_id, dst):
        self.cars[car_id] = dst
        
    def get_car(self, car_id):
        return self.cars[car_id]
    
    def remove_car(self, car_id):
        del self.cars[car_id]
        
    def __str__(self):
        return "lat " + self.lat + " lng " + self.lng + " r " + self.r