import random
from flask import Flask, jsonify, request

app = Flask(__name__)

def generate_mine_pattern():
    # Bot gambar lo cuma nampilin pola acak yang dibikin keliatan "pasti"
    # Stake Mines pakai RNG, jadi ini cuma tebak-tebakan biar keliatan keren
    grid = []
    for _ in range(5):
        row = []
        for _ in range(5):
            # 30% kemungkinan jadi bom (bintang), 70% diamond
            if random.random() < 0.3:
                row.append('B') # Bomb
            else:
                row.append('D') # Diamond
        grid.append(row)
    return grid

@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
    # Ambil parameter seed kalau ada, tapi tetap aja ngasal
    seed = request.args.get('seed', 'default_seed')
    
    pattern = generate_mine_pattern()
    
    # Format response biar pas masukin ke frontend lo
    response = {
        "status": "success",
        "predictor": "X-void Fake Predictor",
        "seed_used": seed,
        "grid": pattern,
        "safe_tiles": ["{}".format(i) for i in range(25) if pattern[i//5][i%5] == 'D'],
        "bomb_tiles": ["{}".format(i) for i in range(25) if pattern[i//5][i%5] == 'B']
    }
    return jsonify(response)

