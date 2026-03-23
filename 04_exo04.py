from flask import Blueprint, jsonify, request

bp = Blueprint('register', __name__)

# Créez une route `/register` qui accepte un POST avec les champs:
# - `username` (2-20 caractères)
# - `email` (format valide)
# - `password` (minimum 8 caractères)
# - `age` (18-100)


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')

    if not (2 <= len(username) <= 20):
        return jsonify({"error": "Username must be between 2 and 20 characters."}), 400

    if '@' not in email or '.' not in email:
        return jsonify({"error": "Invalid email format."}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long."}), 400

    if not (18 <= age <= 100):
        return jsonify({"error": "Age must be between 18 and 100."}), 400

    return jsonify({
        "message": "Registration successful!",
        "username": username,
        "email": email,
        "age": age
    }), 201




    