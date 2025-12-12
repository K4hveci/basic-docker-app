from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Frontend'den gelen isteklere izin ver

# Oyun durumlarını saklamak için basit bir in-memory storage
# Gerçek uygulamada Redis veya veritabanı kullanılabilir
games = {}

@app.route('/api/health', methods=['GET'])
def health():
    """Backend sağlık kontrolü"""
    return jsonify({
        'status': 'healthy',
        'service': 'backend',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/game/start', methods=['POST'])
def start_game():
    """Yeni oyun başlat"""
    game_id = str(uuid.uuid4())
    secret_number = random.randint(1, 100)
    
    games[game_id] = {
        'secret_number': secret_number,
        'attempts': 0,
        'status': 'playing',
        'min_range': 1,
        'max_range': 100
    }
    
    return jsonify({
        'game_id': game_id,
        'message': 'Oyun başladı! 1 ile 100 arasında bir sayı tuttum. Tahmin et!',
        'range': {
            'min': 1,
            'max': 100
        }
    })

@app.route('/api/game/guess', methods=['POST'])
def make_guess():
    """Tahmin yap"""
    data = request.get_json()
    game_id = data.get('game_id')
    guess = data.get('guess')
    
    if not game_id or game_id not in games:
        return jsonify({'error': 'Geçersiz oyun ID'}), 400
    
    if guess is None:
        return jsonify({'error': 'Tahmin gerekli'}), 400
    
    try:
        guess = int(guess)
    except ValueError:
        return jsonify({'error': 'Lütfen geçerli bir sayı girin'}), 400
    
    game = games[game_id]
    
    if game['status'] != 'playing':
        return jsonify({'error': 'Oyun bitmiş'}), 400
    
    game['attempts'] += 1
    secret = game['secret_number']
    
    if guess < game['min_range'] or guess > game['max_range']:
        return jsonify({
            'error': f"Lütfen {game['min_range']} ile {game['max_range']} arasında bir sayı girin",
            'attempts': game['attempts']
        }), 400
    
    if guess == secret:
        game['status'] = 'won'
        return jsonify({
            'result': 'correct',
            'message': f'🎉 Tebrikler! {game["attempts"]} denemede buldun!',
            'secret_number': secret,
            'attempts': game['attempts'],
            'status': 'won'
        })
    elif guess < secret:
        game['min_range'] = max(game['min_range'], guess + 1)
        return jsonify({
            'result': 'higher',
            'message': f'⬆️ Daha yüksek bir sayı dene! ({game["min_range"]}-{game["max_range"]} arası)',
            'attempts': game['attempts'],
            'range': {
                'min': game['min_range'],
                'max': game['max_range']
            }
        })
    else:
        game['max_range'] = min(game['max_range'], guess - 1)
        return jsonify({
            'result': 'lower',
            'message': f'⬇️ Daha düşük bir sayı dene! ({game["min_range"]}-{game["max_range"]} arası)',
            'attempts': game['attempts'],
            'range': {
                'min': game['min_range'],
                'max': game['max_range']
            }
        })

@app.route('/api/game/status/<game_id>', methods=['GET'])
def get_game_status(game_id):
    """Oyun durumunu kontrol et"""
    if game_id not in games:
        return jsonify({'error': 'Oyun bulunamadı'}), 404
    
    game = games[game_id]
    return jsonify({
        'game_id': game_id,
        'status': game['status'],
        'attempts': game['attempts'],
        'range': {
            'min': game['min_range'],
            'max': game['max_range']
        }
    })

@app.route('/api/game/end/<game_id>', methods=['POST'])
def end_game(game_id):
    """Oyunu bitir ve temizle"""
    if game_id in games:
        del games[game_id]
    return jsonify({'message': 'Oyun sonlandırıldı'})

if __name__ == '__main__':
    # Backend 5001 portunda çalışacak
    app.run(host='0.0.0.0', port=5001, debug=True)

