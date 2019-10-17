from flask import Flask, request, jsonify
import os
import socket
import math

app = Flask(__name__)

@app.route("/")
def hello():
    a = request.args.get('a', default = 1, type = float)
    b = request.args.get('b', default = 10, type = float)
    n = request.args.get('n', default = 100, type = int)
    h = float((b - a) / n)
    sum = 0.5 * (f(a) + f(b))
    for i in range (n):
        x = a + (h * i)
        sum = sum + f(x)
    valor = sum * h
    return jsonify(
        hostname=socket.gethostname(),
        result=valor
    )
#    html = "<h3>Hello {name}!</h3>" \
#           "<b>Hostname:</b> {hostname}<br/>" \
#           "<b>Result:</b> {result}<br/>"
#    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), result=valor)

def f(x):
    return math.exp(- x * x / 2) / math.sqrt(2 * math.pi)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
