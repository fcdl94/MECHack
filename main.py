# !flask/bin/python
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

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
    # call the function of the application logic
    print(content)
    return 'JSON posted'

if __name__ == '__main__':
    # instance the application logic
    
    # run the app
    app.run(port=5000, debug=True)
