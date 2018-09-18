
class CrashDetector:
    def __init__(self):
        self.map = dict()
        self.crosses = dict()
        self.idx = 0
    
    def position_update(self, id, lat, long, vel, ts):
        if id == 0:
            return True
        else:
            return False

    def new_car(self):
        idx = self.idx
        self.idx += 1
        return idx
