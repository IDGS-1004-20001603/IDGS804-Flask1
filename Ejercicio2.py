from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=["GET", 'POST'])
def puntos():
    if request.method == 'POST':
        compradores = int(request.form.get('txtCantidadCompradores'))
        boletos = int(request.form.get('txtCantidadBoletos'))
        tarjeta = request.form.get("tarjeta")

        BoletosPorPersona= boletos / compradores
        if(BoletosPorPersona <= 7):
            total = 12 * boletos

            if(boletos > 5):
                totalConDescuento = total * .85
            elif(boletos >= 3 and boletos <=5):
                totalConDescuento = total * .10
            elif(boletos <= 2):
                totalConDescuento = total
            
            print(totalConDescuento)
            
            if(tarjeta == "si"):
                txtTotal = totalConDescuento * .90
            elif(tarjeta == "no"):
                txtTotal = totalConDescuento
            
            return render_template('cinepolis.html', txtTotal = txtTotal)
        else:
            txtTotal = "NO ES POSIBLE COMPRAR MÁS DE 7 BOLETOS POR PERSONA"
            return render_template('cinepolis.html', txtTotal = txtTotal)
    else:
        return render_template("cinepolis.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080)