from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/index', methods=['GET', 'POST'])
def predict():
    return jsonify({
        "status": "success",
        "predictor": "X-void",
        "message": "API NYAMBUNG ANJIR",
        "grid": [
            ['D', 'D', 'B', 'D', 'D'],
            ['B', 'D', 'D', 'D', 'B'],
            ['D', 'D', 'D', 'D', 'D'],
            ['D', 'B', 'D', 'D', 'D'],
            ['D', 'D', 'D', 'B', 'D']
        ]
    })
