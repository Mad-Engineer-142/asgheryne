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
    
@app.route('/api/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    if request.method == 'POST':
        content = request.json
        print(content)
        if content['groupId'] == 1:

            aa = jsonify({'groupId': 1,
 'groupName': 'ЩАКО-01-20(АКС-11)', 
 'raspisanie': [
     {'dayArray': [
         {'group': 'ЩАКО-01-20(АКС-11)', 'room': '123', 'subject': 'физика', 'teacherName': 'ЮРЕЦ КОНЕЧНО', 'time': '8:45-10:30', 'timeId': 1}
     ], 'dayId': 1}
 ]})
            return aa
        
        #return jsonify({"uuid":uuid})

if __name__ == '__main__':
    app.run()
