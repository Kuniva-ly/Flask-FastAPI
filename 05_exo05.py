from flask import Blueprint, jsonify, request

bp = Blueprint('calculator', __name__)

@bp.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    a_raw = request.args.get('a')
    b_raw = request.args.get('b')

    if not operation or a_raw is None or b_raw is None:
        return jsonify({
            "error": "Missing required query params: operation, a, b"
        }), 400

    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return jsonify({"error": "a and b must be numbers"}), 400

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation. Use add, subtract, multiply, or divide"}), 400

    return jsonify({
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    })

