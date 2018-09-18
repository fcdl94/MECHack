import time


class Car:
    def __init__(self, idx):
        self.idx = idx
        self.lat = []
        self.long = []
        self.vel = []
        self.ts = []
        self.last_ts = time.time()
        self.len = 0
    
    def update_position(self, lat, long, vel, ts):
        self.lat.append(lat)
        self.long.append(long)
        self.vel.append(vel)
        self.ts.append(ts)
        self.last_ts = ts
        self.len += 1
        if self.len > 10:
            self.lat.pop()
            self.lat.pop()
            self.vel.pop()
            self.ts.pop()
    
    def get_position(self):
        r = []
        r.append(self.lat.reverse())
        r.append(self.long.reverse())
        r.append(self.vel.reverse())
        r.append(self.ts.reverse())
        return r
