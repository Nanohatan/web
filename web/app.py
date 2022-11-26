import os

from flask import Flask

app = Flask(__name__)

@app.route('/home')
def hello():
    return 'Hello world~!'

@app.route('/smile')
def hi():
    return '^^!'
 

if __name__ == '__main__':
    app.run(host='0.0.0.0')