import json
import os
from flask import Flask
from flask import request
from flask import make_response

# Flask
app = Flask(__name__)
@app.route('/',methods=['POST']) # Using POST as a method

def MainFunction():
    #Getting intent from Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #Call generating_answer function to classify the question
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #Make a respond back to Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json' #Setting Content Type

    return r

