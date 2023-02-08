from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hola mundo!'

if __name__ == '__main__':
    #Con esto ya no es necesario reiniciar el server
    app.run(debug=True, port=8080)