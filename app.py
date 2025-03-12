import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, render_template
from flask_mysqldb import MySQL
from datetime import datetime, timedelta


app = Flask(__name__)


#### conexion a base de datos ##
app.config['MYSQL_HOST'] = 'sql207.infinityfree.com'
app.config['MYSQL_USER'] = 'if0_38505876'  # Reemplazá con tu usuario de MySQL
app.config['MYSQL_PASSWORD'] = 'pepycarp0'  # Reemplazá con tu contraseña de MySQL
app.config['MYSQL_DB'] = 'if0_38505876_pagina_rivers'

mysql = MySQL(app)

@app.route("/")
def home():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    
    # Consulta para obtener los próximos partidos ordenados por fecha y hora
    cursor.execute("SELECT * FROM proximos_partidos ORDER BY fecha, hora")
    proximos_partidos = cursor.fetchall()
    
    cursor.close()

    # Obtener la fecha y hora actual
    ahora = datetime.now()

    for partido in proximos_partidos:
        if isinstance(partido['hora'], timedelta):
            totalSeconds = int(partido['hora'].total_seconds())
            horaObj = (datetime.min + timedelta(seconds=totalSeconds)).time()
        else:
            horaObj = partido['hora']

        partidoDatetime = datetime.combine(partido['fecha'], horaObj)
        partido['fecha_hora'] = partidoDatetime

    return render_template("index.html", proximos_partidos = proximos_partidos, ahora = ahora)

@app.route("/tablaDePosiciones")
def tablaPosiciones():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM tabla_posiciones ORDER BY puntos DESC")
    equipos_a = cursor.fetchall()

    cursor.execute("SELECT * FROM tabla_posiciones_2 ORDER BY puntos DESC")
    equipos_b = cursor.fetchall()
    cursor.close()

    return render_template("tablaDePosiciones.html", equipos_a = equipos_a, equipos_b = equipos_b)



@app.route("/copaArgentina")
def copaArgentina():
    cursor = mysql.connection.cursor(pymysql.cursors.DictCursor)
    
    # Consulta para los partidos de la Copa Argentina
    cursor.execute("SELECT * FROM partidos_copa_argentina ORDER BY fecha, hora")
    partidos_copa_argentina = cursor.fetchall()
    
    cursor.close()

    # Obtener la fecha y hora actual
    ahora = datetime.now()  # Esto es un objeto datetime con fecha y hora actual

    # Convertir las fechas y horas de los partidos en objetos datetime para comparación
    for partido in partidos_copa_argentina:
        # Verificar si 'hora' es un timedelta y convertirlo a 'time'
        if isinstance(partido['hora'], timedelta):
            # Convertir timedelta a segundos
            total_seconds = int(partido['hora'].total_seconds())
            # Crear un objeto time a partir de los segundos
            hora_obj = (datetime.min + timedelta(seconds=total_seconds)).time()
        else:
            # Si ya es un time, simplemente lo usamos
            hora_obj = partido['hora']

        # Combina la fecha y la hora en un solo datetime
        partido_datetime = datetime.combine(partido['fecha'], hora_obj)
        partido['fecha_hora'] = partido_datetime

    return render_template("copa-argentina.html", partidos_copa_argentina = partidos_copa_argentina, ahora = ahora)

if __name__ == "__main__":
    app.run(debug=True)
