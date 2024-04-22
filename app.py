from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/<float:fahrenheit>', methods=['GET'])
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return jsonify({
        'celsius': celsius,
        'app_identifier': random.randint(1000, 9999)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)