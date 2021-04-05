import json
import os
from flask import Flask
from flask import request
from flask import make_response

from random import randint
import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate("project/noomfuuproject-f3b69-firebase-adminsdk-mpbf0-f282f03bd0.json")
firebase_admin.initialize_app(cred)


# Flask
app = Flask(__name__)
#@app.route('/', methods=['POST']) can't use POST right now
@app.route('/')

def MainFunction():
    """
    #Getting intent from Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #Call generating_answer function to classify the question
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #Make a respond back to Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json' #Setting Content Type

    return r
    """
    return "Noomfuu Hello"

"""
def generating_answer(question_from_dailogflow_dict):
    
    #Print intent that recived from dialogflow.
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #Getting intent name form intent that recived from dialogflow.
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"] 

    #Select function for answering question
    if intent_group_question_str == :
        answer_str = 
    else: answer_str = "นุ่มฟูไม่เข้าใจ"

    #Build answer dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #Convert dict to JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot
"""


