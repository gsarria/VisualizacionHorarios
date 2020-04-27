#!/usr/bin/python
# -*- coding: latin1 -*-

import flask
import sqlite3
import sys
#from flask import Flask, request, g, redirect, url_for, \
##    render_template, flash, session, send_from_directory, make_response

app = flask.Flask(__name__)
app.config.update(dict(
    # Base de datos oficial
    # DATABASE = '/home/abetpujc/abetpujc/abet.db',
    # Para hacer pruebas
    #DATABASE='/Users/gsarria/Dropbox/Work/ABETForm/github/abetpujc/abet.db',
    #DATABASE='C:/Users/Usuario/Desktop/abetpujc-master/abet.db',

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

        
def procesarCursos():
    """
    Función que procesa la información de la base de datos, transformándola en datos para enviar a la página.
    Entrada: Ninguna.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los periodos
    cur1 = db.execute("select d.codigo, d.nombre, d.grupo, e.nombre, f.dia, f.horainicio, f.horafin \
                       from curso as d, profesor as e, horario as f \
                       where d.id_profesor=e.id and d.id = f.id_curso")
    cursos = cur1.fetchall()

    # for i in cursos:
    #     print(i)

    # Listas que contendran las clases que se dictan en dicho dia
    lunes = []
    martes = []
    miercoles = []
    jueves = []
    viernes = []
    sabado = []
    domingo = []

    for curso in cursos:
        temp = {"codigo":curso[0],
                "nombre":curso[1],
                "grupo":curso[2],
                "profesor":curso[3],
                "horaInicio":curso[5],
                "span":(curso[6]-curso[5])*2}
#        print(temp)
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

#    for i in lunes:
#        print(i)

    return [lunes,martes,miercoles,jueves,viernes,sabado,domingo]

@app.route("/",methods=["GET","POST"])
def pagina_principal():
    """
    Función que envia la información a la pagina web.
    Entradas: Ninguna
    Salida: La página web
    """

    datos = procesarCursos()
    
    return flask.render_template("main.html",datos={"Lunes":datos[0],
                                                    "Martes":datos[1],
                                                    "Miercoles":datos[2],
                                                    "Jueves":datos[3],
                                                    "Viernes":datos[4],
                                                    "Sabado":datos[5],
                                                    "Domingo":datos[6],})


if(__name__ == "__main__"):
    if len(sys.argv) > 2 and sys.argv[1] == 'initdb':
        init_db()

    app.run(host="127.0.0.1", port=5051)
