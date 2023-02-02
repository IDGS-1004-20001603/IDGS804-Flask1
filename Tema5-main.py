from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alumnos')
def alumnos():
    return render_template('alumnos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)