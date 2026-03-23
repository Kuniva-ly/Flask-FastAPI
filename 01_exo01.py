from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Exercise!"

@app.route('/hello/<language>', methods=['GET'])
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

if __name__ == '__main__':
    print("=" * 60)
    print("Flask Exercise: Hello World with Multiple Languages")
    print("=" * 60)
    app.run(debug=True, port=5000)

