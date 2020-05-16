#!/usr/bin/python
# -*- coding: latin1 -*-

import flask
import sqlite3
import sys
import xlrd
import datetime

app = flask.Flask(__name__)
app.config.update(dict(
    DATABASE='cursos.db',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

##cursos = [{"codigo":"300ITA001",
##           "nombre":"Introducci�n al Modelado de Sistemas",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":7.0,"horaFin":9.0},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"},
##          {"codigo":"300ITA001",
##           "nombre":"Introducci�n al Modelado de Sistemas",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":7.5,"horaFin":9.5},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"},
##          {"codigo":"300CIP001",
##           "nombre":"Introducci�n a la Programaci�n",
##           "clase":"A",
##           "profesor":"Gerardo M. Sarria M.",
##           "horarios":[{"dia":"lunes","horaInicio":9.0,"horaFin":11.0},
##                     {"dia":"jueves","horaInicio":14.0,"horaFin":16.0}],
##           "semestre":1,
##           "departamento":"DECC"}]

def get_excel():
    """
    Funci�n que abre los archivos excel correspondiente a los cursos y los organiza
    :return:
    """

    # Se abre el archivo Super Excel
    wbSuper = xlrd.open_workbook("excel/SuperXcel.xlsx")
    sheetSuper = wbSuper.sheet_by_index(0)

    # Se abre el archivo excel de la Facultad
    wbFIC = xlrd.open_workbook("excel/AsignaturasFIC.xlsx")
    sheetFIC = wbFIC.sheet_by_index(0)

    # Se empieza a leer la informaci�n del Excel de la Facultad
    # Sistemas es la columna 21 del Excel
    for filaFIC in range(1,sheetFIC.nrows):
        if(sheetFIC.cell_value(filaFIC, 21) != ''):
            #print(sheetFIC.cell_value(fila, 3))

            for filaSuper in range(1,sheetSuper.nrows):
                if(sheetFIC.cell_value(filaFIC, 2) == sheetSuper.cell_value(filaSuper, 4) and \
                        (sheetSuper.cell_value(filaSuper, 2) == "DEP-CIC" or \
                         sheetSuper.cell_value(filaSuper, 2) == "DEP-CNMT")):
                    # C�digo del curso
                    print("Codigo: " + sheetSuper.cell_value(filaSuper, 4))
                    # C�digo del curso
                    print("Nombre: " + sheetSuper.cell_value(filaSuper, 6))
                    # Grupo
                    print("Grupo: " + sheetSuper.cell_value(filaSuper, 5))
                    # ID del profesor
                    print("Profesor: " + sheetSuper.cell_value(filaSuper, 8))
                    # Dia
                    print("Dia: " + sheetSuper.cell_value(filaSuper, 15))
                    # Hora inicio
                    tmp = sheetSuper.cell_value(filaSuper, 16)
                    hora = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().hour
                    minuto = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().minute
                    if(minuto == 30):
                        hora = hora + 0.5
                    else:
                        hora = hora + 0.0
                    print("Hora inicio: " + str(hora))
                    # Hora final
                    tmp = sheetSuper.cell_value(filaSuper, 17)
                    hora = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().hour
                    minuto = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().minute
                    if (minuto == 30):
                        hora = hora + 0.5
                    else:
                        hora = hora + 0.0
                    print("Hora inicio: " + str(hora))


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
    Funci�n que extrae de la base de datos la informaci�n de los programas acad�micos.
    Entrada: Ninguna.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los programas
    cur1 = db.execute("select id_carrera, nombre_carrera from programa")
    programas = cur1.fetchall()

    # Retorna los programas encontrados en la base de datos
    return programas

def procesarCursos(filtroSemestre, filtroPrograma):
    """
    Funci�n que procesa la informaci�n de la base de datos correspondiente a los cursos,
        transform�ndola en datos para enviar a la p�gina.
    Entrada: filtroSemestre, variable que representa qu� semestre se escogi� para visualizar los cursos.
             filtroPrograma, variable que representa qu� programa se escogi� para visualizar los cursos.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los cursos, sus profesores y sus horarios
    if(filtroSemestre == 0):
        cur1 = db.execute("select d.codigo, d.nombre, g.grupo, e.nombre, f.dia, f.horainicio, f.horafin \
                           from curso as d, profesor as e, horario as f, grupo_periodo as g \
                           where g.id_profesor = e.id and g.codigo = f.codigo_curso \
                           and g.grupo = f.grupo_curso and d.codigo = g.codigo \
                           and d.id_carrera = ?",[filtroPrograma])
    else:
        cur1 = db.execute("select d.codigo, d.nombre, g.grupo, e.nombre, f.dia, f.horainicio, f.horafin \
                           from curso as d, profesor as e, horario as f, grupo_periodo as g \
                           where g.id_profesor = e.id and g.codigo = f.codigo_curso \
                           and g.grupo = f.grupo_curso and d.codigo = g.codigo \
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
        elif(curso[4] == "Mi�rcoles"):
            miercoles.append(temp)
        elif(curso[4] == "Jueves"):
            jueves.append(temp)
        elif(curso[4] == "Viernes"):
            viernes.append(temp)
        elif(curso[4] == "S�bado"):
            sabado.append(temp)
        else:
            domingo.append(temp)

    # Retorna los dias agrupados
    return [lunes,martes,miercoles,jueves,viernes,sabado,domingo]

@app.route("/",methods=["GET","POST"])
def pagina_principal():
    """
    Funci�n que envia la informaci�n a la pagina web.
    Entradas: Ninguna
    Salida: La p�gina web
    """

    get_excel()

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
    app.run(host="127.0.0.1", port=5007, debug=True)
