from flask import Flask, render_template
from flask import request
import math

app = Flask(__name__)

@app.route('/puntos')
def puntos():
    return render_template('puntos.html')

@app.route('/puntosRes', methods=['post'])
def puntosRes():
    x1 = float(request.form.get('x1'))
    y1 = float(request.form.get('y1'))
    x2 = float(request.form.get('x2'))
    y2 = float(request.form.get('y2'))
    res = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    return render_template('puntosRes.html', x1=x1, y1=y1, x2=x2, y2=y2, res= res)


if __name__ == '__main__':
    app.run(debug=True, port=8080)