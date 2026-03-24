from flask import Blueprint, request, jsonify

bp = Blueprint('convert', __name__)

# Créez une route `/convert/temp` qui accepte deux paramètres query:
# - `value`: la température (nombre)
# - `unit`: "c2f" (Celsius to Fahrenheit) ou "f2c" (Fahrenheit to Celsius)

@bp.route('/convert/temp', methods=['GET'])
def convert_temp():
    value = request.args.get('value', type=float)
    unit = request.args.get('unit', type=str)

    if value is None or unit is None:
        return jsonify({"error": "Missing required parameters"}), 400

    if unit == "c2f":
        result = (value * 9/5) + 32
        return jsonify({"celsius": value, "fahrenheit": result})
    elif unit == "f2c":
        result = (value - 32) * 5/9
        return jsonify({"fahrenheit": value, "celsius": result})
    else:
        return jsonify({"error": "Invalid unit. Use 'c2f' or 'f2c'"}), 400

