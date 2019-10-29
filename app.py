from flask import Flask, request, jsonify
import os
import socket
import math

app = Flask(__name__)


@app.route("/")
def hello():
    x0 = request.args.get('a', default=1.0, type=float)
    x1 = request.args.get('b', default=10.0, type=float)
    qtde_slices = request.args.get('n', default=100, type=int)
    h_slice = (x1 - x0) / qtde_slices
    _x1 = x0
    result = 0
    for i in range(qtde_slices):
        _x0 = _x1
        _x1 = _x0 + h_slice
        fx0 = f(_x0)
        fx1 = f(_x1)
        if fx0 > fx1:
            result = result + retangulo(h_slice, fx1)
        else:
            result = result + retangulo(h_slice, fx0)
        if fx0 > fx1:
            result = result + triangulo(h_slice, fx0 - fx1)           
        elif fx0 < fx1:
            result = result + triangulo(h_slice, fx1 - fx0)

    return jsonify(
        hostname=socket.gethostname(),
        result=result
    )


def f(x):
    result = math.pow(x, 5) * 5
    result = result + math.pow(x, 2)
    result = result + x
    return result


def retangulo(base, altura):
    return base * altura


def triangulo(base, altura):
    return (base * altura) / 2


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
