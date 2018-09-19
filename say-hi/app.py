import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

NAME = os.environ['NAME']

@app.route("/")
def hello():
    return "Hi, %s, you got a flag: hello-world. Cheers!\r\n" % NAME

@app.route("/flag")
def flag():
    host = os.getenv('REDIS_HOST', None)
    port = os.getenv('REDIS_PORT', None)
    password = os.getenv('REDIS_PASSWORD', None)
    if None in (host, port, password):
        return "Looks like you don't have REDIS_PASSWORD, keep trying!\r\n"
    r = Redis(host=host, port=port, password=password)
    count = r.incr('pv', 1)
    if count == 30:
        flag = r.get('flag')
        return "Bingo~ You got it: keep-secret\r\n"
    return "Your access no is %d, try harder, the flag is hidden at 30" % count


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)