'''app.py
Terminal Commands:
    py -3 -m venv venv
    flask run
'''

from flask import Flask, render_template, request
import bot
import json
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    #Can't write to Json because js request won't prompt python script
    print (bot.process_request(processed_text))
