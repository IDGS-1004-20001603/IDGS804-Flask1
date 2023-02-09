from flask import Flask, redirect, render_template, make_response
from flask import request
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return render_template('inicio.html')


@app.route('/examen', methods=['POST'])
def examen():
    nombre = request.form.get('txtNombre')
    aPaterno = request.form.get('txtApaterno')
    aMaterno = request.form.get('txtAmaterno')
    dia = int(request.form.get('txtDia'))
    mes = int(request.form.get('txtMes'))
    anio = int(request.form.get('txtAnio'))

    nombreCompleto = nombre + " " + aPaterno + " " + aMaterno

    calcularEdad = relativedelta(datetime.now(), datetime(anio, mes, dia))
    edad = calcularEdad.years

    if (anio == 1924 or anio == 1936 or anio == 1948 or anio == 1960 or anio == 1972 or anio == 1984 or anio == 1996 or anio == 2008 or anio == 2020):
        signoZodiacal = 'Rata'
    elif (anio == 1925 or anio == 1937 or anio == 1949 or anio == 1961 or anio == 1973 or anio == 1985 or anio == 1997 or anio == 2009 or anio == 2021):
        signoZodiacal = 'Buey'
    elif (anio == 1926 or anio == 1938 or anio == 1950 or anio == 1962 or anio == 1974 or anio == 1986 or anio == 1998 or anio == 2010 or anio == 2022):
        signoZodiacal = 'Tigre'
    elif (anio == 1927 or anio == 1939 or anio == 1951 or anio == 1963 or anio == 1975 or anio == 1987 or anio == 1999 or anio == 2011 or anio == 2023):
        signoZodiacal = 'Conejo'
    elif (anio == 1928 or anio == 1940 or anio == 1952 or anio == 1964 or anio == 1976 or anio == 1988 or anio == 2000 or anio == 2012 or anio == 2024):
        signoZodiacal = 'Dragon'
    elif (anio == 1929 or anio == 1941 or anio == 1953 or anio == 1965 or anio == 1977 or anio == 1989 or anio == 2001 or anio == 2013 or anio == 2025):
        signoZodiacal = 'Serpiente'
    elif (anio == 1930 or anio == 1942 or anio == 1954 or anio == 1966 or anio == 1978 or anio == 1990 or anio == 2002 or anio == 2014 or anio == 2026):
        signoZodiacal = 'Caballo'
    elif (anio == 1931 or anio == 1943 or anio == 1955 or anio == 1967 or anio == 1979 or anio == 1991 or anio == 2003 or anio == 2015 or anio == 2027):
        signoZodiacal = 'Cabra'
    elif (anio == 1932 or anio == 1944 or anio == 1956 or anio == 1968 or anio == 1980 or anio == 1992 or anio == 2004 or anio == 2016 or anio == 2028):
        signoZodiacal = 'Mono'
    elif (anio == 1933 or anio == 1945 or anio == 1957 or anio == 1969 or anio == 1981 or anio == 1993 or anio == 2005 or anio == 2017 or anio == 2029):
        signoZodiacal = 'Gallo'
    elif (anio == 1934 or anio == 1946 or anio == 1958 or anio == 1970 or anio == 1982 or anio == 1994 or anio == 2006 or anio == 2018 or anio == 2030):
        signoZodiacal = 'Perro'
    elif (anio == 1935 or anio == 1947 or anio == 1959 or anio == 1971 or anio == 1983 or anio == 1995 or anio == 2007 or anio == 2019 or anio == 2031):
        signoZodiacal = 'Cerdo'

    resp = make_response(render_template('examen.html'))
    resp.set_cookie('nombreCompleto', nombreCompleto)
    resp.set_cookie('edad', str(edad))
    resp.set_cookie('signoZodiacal', signoZodiacal)

    return resp


@app.route('/resultados', methods=['POST'])
def resultados():
    q1 = request.form.get('q#1')
    q2 = request.form.get('q#2')
    q3 = request.form.get('q#3')
    q4 = request.form.get('q#4')
    print(q1)
    res = 0
    nombreCompleto = request.cookies.get('nombreCompleto')
    edad = request.cookies.get('edad')
    signoZodiacal = request.cookies.get('signoZodiacal')

    if (q1 == 'a'):
        res = res + 1

    if (q2 == 'b'):
        res = res + 1

    if (q3 == 'a'):
        res = res + 1

    if (q4 == 'c'):
        res = res + 1
    
    calificacion = (res * 10) / 4

    if(signoZodiacal == 'Rata'):
        url = '../static/img/rata.webp'
    elif(signoZodiacal == 'Buey'):
        url = '../static/img/buey.png'
    elif(signoZodiacal == 'Tigre'):
        url = '../static/img/tigre.jpg'
    elif(signoZodiacal == 'Conejo'):
        url = '../static/img/conejo.jpg'
    elif(signoZodiacal == 'Dragon'):
        url = '../static/img/dragon.jpg'
    elif(signoZodiacal == 'Serpiente'):
        url = '../static/img/serpiente.jpg'
    elif(signoZodiacal == 'Caballo'):
        url = '../static/img/caballo.webp'
    elif(signoZodiacal == 'Cabra'):
        url = '../static/img/cabra.jpg'
    elif(signoZodiacal == 'Mono'):
        url = '../static/img/mono.jpg'
    elif(signoZodiacal == 'Gallo'):
        url = '../static/img/gallo.jpg'
    elif(signoZodiacal == 'Perro'):
        url = '../static/img/perro.jpg'
    elif(signoZodiacal == 'Cerdo'):
        url = '../static/img/cerdo.jpg'

    return render_template('resultados.html', nombreCompleto=nombreCompleto, anios=edad, signoZodiacal=signoZodiacal, calificacion=calificacion, url = url)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
