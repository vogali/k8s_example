import os
from flask import Flask

app = Flask(__name__)

NAME = os.environ['NAME']

@app.route("/")
def hello():
    return "Hi, %s, you got a flag: hello-world. Cheers!" % NAME

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)