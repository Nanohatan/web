import os

from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'こんこん!'

@app.route('/wadai_deck')
def wadai_page():
    return render_template('wadai_deck.html')
 

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)