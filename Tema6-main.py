from flask import Flask, render_template

app = Flask(__name__)

@app.route('/datos')
def index():
    nombre = 'Mauricio'
    lista = ["uno", "dos", "tres", "cuatro"]
    return render_template('datos.html', nombre = nombre, lista = lista)

if __name__ == '__main__':
    app.run(debug=True, port=8080)