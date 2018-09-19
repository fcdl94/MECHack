import time


class Car:
    def __init__(self, idx):
        self.idx = idx
        self.lat = []
        self.lng = []
        self.vel = []
        self.ts = []
        self.last_ts = time.time()
        self.len = 0
    
    def update_position(self, lat, lng, vel, ts):
        self.lat.append(lat)
        self.lng.append(lng)
        self.vel.append(vel)
        self.ts.append(ts)
        self.last_ts = ts
        self.len += 1
        if self.len > 10:
            self.lat.pop(0)
            self.lng.pop(0)
            self.vel.pop(0)
            self.ts.pop(0)
    
    def get_position(self):
        r = []
        r.append(self.lat[::-1])
        r.append(self.lng[::-1])
        r.append(self.vel[::-1])
        r.append(self.ts[::-1])
        return r
