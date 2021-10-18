from flask import Flask, jsonify
from flask import request
import re
#encoding
import sys
sys.stdout.encoding


app = Flask(__name__)

@app.route('/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        print(user_id)
        return 'ok'
        
    if request.method == 'POST':
        data = request.form
        print(data)
        return 'aaaaaaaaaa'
    
@app.route('/asd', methods=['POST'])
def add_message(uuid):
    resp = app.response_class(
                response = json.dumps(   
        [
  {
    "groupId": 1,
    "raspisanie": [
      {
        "dayArray": [
          {
            "group": "ХУИКО-021-20",
            "room": "2601",
            "subject": "ШИЗИКА",
            "teacherName": "ВЛАД НА СЕРВЕРЕ КОНЧАЮТСЯ ДЕНЬГИ, Я КОНЕЧНО НЕ НА ЧТО НЕ НАМЕКАЮ НО........",
            "time": "08.45-10.15",
            "timeId": 1
          },
          {
            "group": "ХУКО-021-20",
            "room": "259",
            "subject": "СОСАТЬ",
            "teacherName": "Фика Я БРАГО",
            "time": "14.88-000.00",
            "timeId": 2
          },
          {
            "group": "ХУКО-021-20",
            "room": "260",
            "subject": "ШИЗИКА",
            "teacherName": "Фика Турицин",
            "time": "12.40-14.10",
            "timeId": 3
          },
          {
            "group": "ХУКО-021-20",
            "room": "777",
            "subject": "ХУЙ",
            "teacherName": "ЙЦУЙЦУ",
            "time": "12.40-14.10",
            "timeId": 4
          },
          {
            "group": "ХУКО-021-20",
            "room": "555",
            "subject": "ШИЗИКА",
            "teacherName": "И ЭТО НЕ ОБСУЖДАЕТСЯ",
            "time": "12.40-14.10",
            "timeId": 5
          },
          {
            "group": "ХУКО-021-20",
            "room": "1234",
            "subject": "ШИЗИКА",
            "teacherName": "АБОБА Я ЕБЛАН СУКА",
            "time": "14.20-15.50",
            "timeId": 6
          }
        ],
        "dayId": 1
      }
    ]
  }
],ensure_ascii=False),
                mimetype='application/json'
                )
        return resp

        
        
     

if __name__ == '__main__':
    app.run()
