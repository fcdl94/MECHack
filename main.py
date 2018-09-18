from flask import Flask
from flask import request
from crash_detector import CrashDetector

app = Flask(__name__)

cd = CrashDetector()


@app.route('/subscribe')
def index():
    return str(cd.new_car())


@app.route('/<id>/position', methods=['POST'])
def position(id):
    # id : 01
    # lat : 10
    # long: 20
    # vel: 86
    # timestamp: 10003405.00
    # add position in dict
    # if forecast is in some crossing -> add to crossing
    #       if other cars in crossing
    #           check if in the same time
    #               if yes respond with "WARNING"
    # otherwise
    #   respond with "ok"
    
    print(request.is_json)
    content = request.get_json()
    lat, long, vel, ts = content["lat"], content["long"], content["vel"], content["timestamp"]
    # call the function of the application logic
    crash_imminent = cd.position_update(id, lat, long, vel, ts)
    
    return crash_imminent

if __name__ == '__main__':
    # run the app
    app.run(host="10.101.0.66", port=8080, debug=True)