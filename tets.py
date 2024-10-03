from flask import Flask, request, jsonify
from base64 import b64decode
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))



app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    
    res = [{'title': 'Бисквитный торт с банановым бисквитом и клубничной начинкой', 'creator_id': 1231231231}, {'title': 'Муссовый торт с малиновым муссом и банановой начинкой', 'creator_id': 1231231231}]
    print(res)

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)