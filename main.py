from flask import Flask
from flask import request
from flask import Response
from crash_detector import CrashDetector

app = Flask(__name__)

cd = CrashDetector()

@app.route('/subscribe')
def index():
    return str(cd.new_car())

@app.route('/crosses', methods=['GET'])
def get_crosses():
    crosses = cd.get_crosses()
    response = Response(str(crosses), status=200)
    return response

@app.route('/cars', methods=['GET'])
def get_cars():
    cars = cd.get_cars()
    response = Response(str(cars), status=200)
    return response

@app.route('/crosses', methods=['POST'])
def add_crosses():
    content = request.get_json()
    idc = cd.update_crosses(content["lat"], content["lng"], content["r"])
    
    if request.is_json:
        status = 201
    else:
        status = 400
    response = Response(str(idc), status=status)
    return response


@app.route('/<id>/position', methods=['POST'])
def position(id):
    # id : 01
    # lat : 10
    # long: 20
    # vel: 86
    # timestamp: 10003405.00

    print(request.is_json)
    content = request.get_json()
    
    print(content)
    lat, long, vel, ts = content["lat"], content["lng"], content["vel"], content["timestamp"]
    # call the function of the application logic
    crash_imminent = cd.position_update(id, lat, long, vel, ts)
    
    if request.is_json:
        status = 201
    else:
        status = 400
    response = Response(crash_imminent, status=status)

    return response
    
    
if __name__ == '__main__':
    # run the app
    app.run(host="10.101.0.66", port=8080, debug=True)