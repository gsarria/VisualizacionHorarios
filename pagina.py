#!/usr/bin/python
# -*- coding: latin1 -*-

import flask
import sqlite3
import sys

app = flask.Flask(__name__)
app.config.update(dict(
    DATABASE='cursos.db',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

##cursos = [{"codigo":"300ITA001",
##           "nombre":"Introducción al Modelado de Sistemas",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":7.0,"horaFin":9.0},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"},
##          {"codigo":"300ITA001",
##           "nombre":"Introducción al Modelado de Sistemas",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":7.5,"horaFin":9.5},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"},
##          {"codigo":"300CIP001",
##           "nombre":"Introducción a la Programación",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":9.0,"horaFin":11.0},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"}]

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def get_db():
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(flask.g, 'sqlite_db'):
        flask.g.sqlite_db = connect_db()
    return flask.g.sqlite_db

def procesarProgramas():
    """
    Función que extrae de la base de datos la información de los programas académicos.
    Entrada: Ninguna.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los programas
    cur1 = db.execute("select id_carrera, nombre_carrera from definicion")
    programas = cur1.fetchall()

    # Retorna los programas encontrados en la base de datos
    return programas

def procesarCursos(filtroSemestre, filtroPrograma):
    """
    Función que procesa la información de la base de datos correspondiente a los cursos,
        transformándola en datos para enviar a la página.
    Entrada: filtroSemestre, variable que representa qué semestre se escogió para visualizar los cursos.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los cursos, sus profesores y sus horarios
    if(filtroSemestre == 0):
        cur1 = db.execute("select d.codigo, d.nombre, d.grupo, e.nombre, f.dia, f.horainicio, f.horafin \
                           from curso as d, profesor as e, horario as f \
                           where d.id_profesor = e.id and d.codigo = f.codigo_curso \
                           and d.grupo = f.grupo_curso and d.id_carrera = ?",[filtroPrograma])
    else:
        cur1 = db.execute("select d.codigo, d.nombre, d.grupo, e.nombre, f.dia, f.horainicio, f.horafin \
                           from curso as d, profesor as e, horario as f \
                           where d.id_profesor = e.id and d.codigo = f.codigo_curso and d.grupo = f.grupo_curso \
                           and d.id_carrera = ? and d.semestre = ?",[filtroPrograma, filtroSemestre])
    cursos = cur1.fetchall()

    # Listas que contendran las clases que se dictan en dicho dia
    lunes = []
    martes = []
    miercoles = []
    jueves = []
    viernes = []
    sabado = []
    domingo = []

    # Ciclo para insertar cada horario en la lista apropiada
    for curso in cursos:
        temp = {"codigo":curso[0],
                "nombre":curso[1],
                "grupo":curso[2],
                "profesor":curso[3],
                "horaInicio":curso[5],
                "span":(curso[6]-curso[5])*2}
        if(curso[4] == "Lunes"):
            lunes.append(temp)
        elif(curso[4] == "Martes"):
            martes.append(temp)
        elif(curso[4] == "Miércoles"):
            miercoles.append(temp)
        elif(curso[4] == "Jueves"):
            jueves.append(temp)
        elif(curso[4] == "Viernes"):
            viernes.append(temp)
        elif(curso[4] == "Sábado"):
            sabado.append(temp)
        else:
            domingo.append(temp)

    # Retorna los dias agrupados
    return [lunes,martes,miercoles,jueves,viernes,sabado,domingo]

@app.route("/",methods=["GET","POST"])
def pagina_principal():
    """
    Función que envia la información a la pagina web.
    Entradas: Ninguna
    Salida: La página web
    """

    filtroSemestre = 0
    filtroPrograma = 40
    if flask.request.method == 'POST':
        filtroSemestre = int(flask.request.form["filtroSemestre"])
        filtroPrograma = int(flask.request.form["filtroPrograma"])

    datos = procesarCursos(filtroSemestre,filtroPrograma)
    programas = procesarProgramas()
    
    return flask.render_template("main.html",datos={"Lunes":datos[0],
                                                    "Martes":datos[1],
                                                    "Miercoles":datos[2],
                                                    "Jueves":datos[3],
                                                    "Viernes":datos[4],
                                                    "Sabado":datos[5],
                                                    "Domingo":datos[6],
                                                    "semestre":filtroSemestre,
                                                    "programaActual":filtroPrograma,
                                                    "programas":programas})


if(__name__ == "__main__"):
    app.run(host="127.0.0.1", port=5013)
