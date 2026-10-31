from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/api/index', methods=['GET'])
def predict():
    try:
        # Ambil parameter jumlah bom dari URL, default 3
        num_bombs = int(request.args.get('bombs', 3))
        
        # Batasin 1 sampai 24 bom
        if num_bombs > 24: num_bombs = 24
        if num_bombs < 1: num_bombs = 1

        # Bikin list 25 kotak (0 = aman, 1 = bom)
        tiles = [0] * 25
        bomb_indices = random.sample(range(25), num_bombs)
        for idx in bomb_indices:
            tiles[idx] = 1

        # Ubah jadi grid 5x5 (D = Diamond, B = Bomb)
        grid = []
        for i in range(5):
            row = []
            for j in range(5):
                if tiles[i*5 + j] == 1:
                    row.append('B')
                else:
                    row.append('D')
            grid.append(row)

        return jsonify({
            "status": "success",
            "bombs": num_bombs,
            "grid": grid
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
