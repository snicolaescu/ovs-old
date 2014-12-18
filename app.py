from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def getRoot():
    return "Hello World from getRoot"


@app.route('/<name>', methods=['GET'])
def getsub1(name):
    return "Hello World from " + name  + " !" 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
    