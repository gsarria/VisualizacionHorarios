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

def store_Profesores(db, sheetSuper):
    """
    Procedimiento que almacena la información de los profesores en la base de datos
    Entradas: db, la base de datos
              sheetSuper, la hoja de cálculo
    Salida: Base de datos actualizada
    """
    for filaSuper in range(1,sheetSuper.nrows):
        id_profesor = sheetSuper.cell_value(filaSuper, 8)
        nombre_profesor = sheetSuper.cell_value(filaSuper, 9)
        if not db.execute("select id from profesor where id = ?", [id_profesor]).fetchall():
            db.execute("insert into profesor values (?,?,NULL)", [id_profesor, nombre_profesor])
        db.commit()

def estandarizar(curso):
    """
    Función que estandariza el formato del código del curso para poder comparar
    Entradas: curso, texto que representa el código del curso
    Salida: el código estandarizado
    """
    if(curso[0] != ' '):
        return ' '+curso
    else:
        return curso

def store_Horarios(db, wbSuper, sheetSuper, sheetFIC, filtroPrograma):
    """
    Procedimiento que almacena la información de los horarios en la base de datos
    Entradas: db, la base de datos
              wbSuper, el libro del archivo superXcel
              sheetSuper, la hoja de cálculo de todos cursos de la Universidad
              sheetFIC, la hoja de cálculo de los cursos de la Facultad
              filtroPrograma, el programa que debe ser almacenado
    Salida: Base de datos actualizada
    """
    # Se empieza a leer la información del Excel de la Facultad
    # Sistemas es la columna 21 del Excel
    for filaFIC in range(1,sheetFIC.nrows):
        if(sheetFIC.cell_value(filaFIC, 21) != ''):
            curso = estandarizar(sheetFIC.cell_value(filaFIC, 2))
            # Se hace la comparación con los registros del SuperXcel
            for filaSuper in range(1,sheetSuper.nrows):
                if(curso == sheetSuper.cell_value(filaSuper, 4) and \
                        (sheetSuper.cell_value(filaSuper, 2) == "DEP-CIC" or \
                         sheetSuper.cell_value(filaSuper, 2) == "DEP-CNMT")):
                    # Código del curso
                    #print("Codigo: " + sheetSuper.cell_value(filaSuper, 4))
                    codigo = sheetSuper.cell_value(filaSuper, 4)
                    if(codigo[0] == ' '):
                        codigo = sheetSuper.cell_value(filaSuper, 4)[1:]
                    # Nombre del curso
                    #print("Nombre: " + sheetSuper.cell_value(filaSuper, 6))
                    # Grupo
                    #print("Grupo: " + sheetSuper.cell_value(filaSuper, 5))
                    grupo = sheetSuper.cell_value(filaSuper, 5)
                    # ID del profesor
                    #print("Profesor: " + sheetSuper.cell_value(filaSuper, 8))
                    id_profesor = sheetSuper.cell_value(filaSuper, 8)
                    nombre_profesor = sheetSuper.cell_value(filaSuper, 9)
                    # Dia
                    #print("Dia: " + sheetSuper.cell_value(filaSuper, 15))
                    dia = sheetSuper.cell_value(filaSuper, 15)
                    if(dia == 'Verificar'):
                        # Si en el superXcel no hay un dia establecido se poner este por defecto
                        dia = 'Domingo'
                    # Hora inicio
                    tmp = sheetSuper.cell_value(filaSuper, 16)
                    if(tmp == ''):
                        # Si en el superXcel no hay un horario establecido se poner este por defecto
                        hora = 7.0
                    else:
                        hora = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().hour
                        minuto = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().minute
                        if(minuto == 30):
                            hora = hora + 0.5
                        else:
                            hora = hora + 0.0
                    #print("Hora inicio: " + str(hora))
                    hora_inicio = hora
                    # Hora final
                    tmp = sheetSuper.cell_value(filaSuper, 17)
                    if(tmp == ''):
                        # Si en el superXcel no hay un horario establecido se poner este por defecto
                        hora = 9.0
                    else:
                        hora = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().hour
                        minuto = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).time().minute
                        if (minuto == 30):
                            hora = hora + 0.5
                        else:
                            hora = hora + 0.0
                    #print("Hora inicio: " + str(hora))
                    hora_final = hora

                    # Inserta los registros en las tablas
                    if not db.execute("select codigo from grupo_periodo \
                                where codigo = ? and grupo = ? and id_carrera = 40 and id_profesor = ? \
                                and codigo_periodo = 1008",[codigo, grupo, id_profesor]).fetchall():
                        db.execute("insert into grupo_periodo values (?,?,?,?,1008)",[codigo, grupo, filtroPrograma,id_profesor])

                    if not db.execute("select codigo_curso from horario \
                                where codigo_curso = ? and grupo_curso = ? and dia = ? and horainicio = ? \
                                and horafin = ?",[codigo, grupo, dia, hora_inicio, hora_final]).fetchall():
                        db.execute("insert into horario values (?,?,?,?,?)",[codigo, grupo, dia, hora_inicio, hora_final])

                    db.commit()


def get_excel(filtroPrograma):
    """
    Procedimiento que abre los archivos excel correspondiente a los cursos, organiza su información
    y la almacena en la base de datos
    Entradas: La información de los archivos excel
    Salida: Base de datos actualizada
    """

    # Accede a la base de datos
    db = get_db()

    # Se abre el archivo Super Excel
    wbSuper = xlrd.open_workbook("excel/SuperXcel.xlsx")
    sheetSuper = wbSuper.sheet_by_index(0)

    # Se abre el archivo excel de la Facultad
    wbFIC = xlrd.open_workbook("excel/AsignaturasFIC.xlsx")
    sheetFIC = wbFIC.sheet_by_index(0)

    # Almacena la información de los profesores
    store_Profesores(db,sheetSuper)

    # Almacena la información de los horarios
    store_Horarios(db,wbSuper,sheetSuper,sheetFIC,filtroPrograma)




def procesarProgramas():
    """
    Función que extrae de la base de datos la información de los programas académicos.
    Entradas: Ninguna.
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
    Función que procesa la información de la base de datos correspondiente a los cursos,
        transformándola en datos para enviar a la página.
    Entradas: filtroSemestre, variable que representa qué semestre se escogió para visualizar los cursos.
              filtroPrograma, variable que representa qué programa se escogió para visualizar los cursos.
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
        elif(curso[4] == "Miercoles"):
            miercoles.append(temp)
        elif(curso[4] == "Jueves"):
            jueves.append(temp)
        elif(curso[4] == "Viernes"):
            viernes.append(temp)
        elif(curso[4] == "Sabado"):
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

    # Se procesan los filtros de la página
    filtroSemestre = 0
    filtroPrograma = 40
    if flask.request.method == 'POST':
        filtroSemestre = int(flask.request.form["filtroSemestre"])
        filtroPrograma = int(flask.request.form["filtroPrograma"])

    # Almacena la información de los archivos excel en la base de datos
    get_excel(filtroPrograma)

    # Recupera la información de los cursos
    datos = procesarCursos(filtroSemestre,filtroPrograma)

    # Recupera la información de los programas
    programas = procesarProgramas()

    # Retorna la página web completada
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

# Si se llama la aplicación directamente desde python
if(__name__ == "__main__"):
    app.run(host="127.0.0.1", port=5016, debug=True)
