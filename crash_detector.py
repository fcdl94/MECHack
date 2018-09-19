from car import Car
from cross import Cross
from math import sin, cos, sqrt, atan2, radians
from numpy import array, dot, arccos, clip
from numpy.linalg import norm


def distance(lat, lng, lat2, lng2):
    # approximate radius of earth in km
    R = 6373.0
    
    lat1 = radians(lat)
    lon1 = radians(lng)
    lat2 = radians(lat2)
    lon2 = radians(lng2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance_ = R * c
    return distance_*1000


def check_proximity(car, crosses):
    pos = car.get_position()  # lat, long, vel, ts
    
    for c in crosses.values():
        dst = distance(pos[0][0], pos[1][0], c.lat, c.lng)
        print(dst)
        if dst < c.r:
            try:
                dst_old = distance(pos[0][1], pos[1][1], c.lat, c.lng)
            except:
                return False
            if dst_old > dst:  # avvicinamento
                print("avvicinamento")
                if not car.idx in c.cars.keys():
                    c.add_car(car.idx, dst)
                return c.idx
            # else:
            #     c.remove_car(car.idx)
    return False

def check_convergence(u,v):
    c = dot(u, v) / norm(u) / norm(v)  # -> cosine of the angle
    angle = arccos(clip(c, -1, 1))  # if you really want the angle
    
    if radians(-15) < angle < radians(15):
        return True
    else:
        return True

class CrashDetector:
    def __init__(self):
        self.cars = dict()
        self.crosses = dict()
        self.idx = 0
        self.idc = 0
    
    def get_crosses(self):
        return self.crosses

    def get_cars(self):
        return self.cars

    def update_crosses(self, lat, long, r):
        lat = float(lat)
        long = float(long)
        r = float(r)
        idc = self.idc
        self.crosses[self.idc] = Cross(self.idc, lat, long, r)
        self.idc += 1
        return idc
    
    def position_update(self, idx, lat, long, vel, ts):
        # add position in dict
        # if forecast is in some crossing -> add to crossing
        #       if other cars in crossing
        #           check if in the same time
        #               if yes respond with "WARNING"
        # otherwise
        #   respond with "ok"
        idx = float(idx)
        lat = float(lat)
        long = float(long)
        vel = float(vel)
        
        if idx in self.cars.keys():
            self.cars[idx].update_position(lat, long, vel, ts)
            # application logic to manage crashes
            cross_id = check_proximity(self.cars[idx], self.crosses)
            if cross_id + 1:
                print(int(cross_id))
                cross = self.crosses[int(cross_id)]
                if len(cross.cars) > 1:
                    print("check_convergence")
                    for c in cross.cars.keys():
                        if check_convergence([self.cars[idx].lat[0], self.cars[idx].lng[0],
                                           self.cars[idx].lat[1], self.cars[idx].lng[1]],
                                          [self.cars[c].lat[0], self.cars[c].lng[0],
                                           self.cars[c].lat[1], self.cars[c].lng[1]]
                                          ):
                            return "WARNING"
            return "OK"
        else:
            return "NOT SUBSCRIBED"

    def new_car(self):
        idx = self.idx
        self.idx += 1
        self.cars[idx] = Car(idx)
        return idx

