from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/operasbas')
def operasbas():
    return render_template('operasbas.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    n1 = request.form.get('txtNum1')
    n2 = request.form.get('txtNum2')
    res = int(n1) * int(n2)

    return render_template('resultado.html', n1 = n1, n2 = n2, res = res)

if __name__ == '__main__':
    app.run(debug=True, port=8080)