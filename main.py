from flask import Flask
import importlib

app = Flask(__name__)

# Les fichiers commencent par un chiffre → on utilise importlib pour les importer
hello_bp   = importlib.import_module("01_exo01").bp
convert_bp = importlib.import_module("02_exo02").bp
books_bp    = importlib.import_module("03_exo03").bp
register_bp = importlib.import_module("04_exo04").bp
calc_bp  = importlib.import_module("05_exo05").bp  
blog_bp  = importlib.import_module("06_exo06").bp 

# Enregistrer les blueprints avec un préfixe URL
app.register_blueprint(hello_bp,   url_prefix='/api')
app.register_blueprint(convert_bp, url_prefix='/api')
app.register_blueprint(books_bp,    url_prefix='/api')
app.register_blueprint(register_bp, url_prefix='/api')
app.register_blueprint(calc_bp,   url_prefix='/api')
app.register_blueprint(blog_bp,   url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

