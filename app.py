from flask import Flask
server = Flask(__name__)

@server.route('/', methods=['GET'])
def getRoot():
    return "Hello World from getRoot"


@server.route('/<name>', methods=['GET'])
def getsub1(name):
    return "Hello World from " + name  + " !" 

if __name__ == '__main__':
    server.run(host='127.0.0.1', port=80, debug=True)
    