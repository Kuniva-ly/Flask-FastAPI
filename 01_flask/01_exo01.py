from flask import Blueprint, jsonify

# 1. Créer le blueprint (nom, module)
bp = Blueprint('hello', __name__)

# 2. Utiliser @bp.route au lieu de @app.route
@bp.route('/hello/<language>', methods=['GET'])
def hello(language):
    greetings = {
        'english': 'Hello',
        'french': 'Bonjour'
    }
    greeting = greetings.get(language.lower(), greetings['english'])
    return jsonify({
        "message": f"{greeting}!",
        "language": language
    })

