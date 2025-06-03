# pylint: skip-file

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():

    return jsonify(success=True,message='Hello Tomer the king!')

@app.route('/<name>')
def hello(name):

    return jsonify(success=True,message=f'Hello {name}')



if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8000)
