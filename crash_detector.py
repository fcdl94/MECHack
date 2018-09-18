from car import Car
from cross import Cross


class CrashDetector:
    def __init__(self):
        self.map = dict()
        self.crosses = dict()
        self.idx = 0
        self.idc = 0
        
    def update_crosses(self, lat, long, r):
        idc = self.idc
        self.crosses[self.idc] = Cross(self.idc, lat, long, r)
        self.idc += 1
        return idc
    
    def position_update(self, id, lat, long, vel, ts):
        if id in self.map:
            self.map[id].update_position(lat, long, vel, ts)
            # application logic to manage crashes
            return True
        else:
            return False
        # add position in dict
        # if forecast is in some crossing -> add to crossing
        #       if other cars in crossing
        #           check if in the same time
        #               if yes respond with "WARNING"
        # otherwise
        #   respond with "ok"

    def new_car(self):
        idx = self.idx
        self.idx += 1
        self.map[idx] = Car(idx)
        return idx
    
