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


def addSpace(curso):
    """
    Funci�n que estandariza el formato del c�digo del curso para poder comparar
    Entradas: curso, texto que representa el c�digo del curso
    Salida: el c�digo estandarizado
    """
    if(curso[0] != ' '):
        return ' '+curso
    else:
        return curso

def delSpace(curso):
    """
    Funci�n que estandariza el formato del c�digo del curso para poder comparar
    Entradas: curso, texto que representa el c�digo del curso
    Salida: el c�digo estandarizado
    """
    if(curso[0] == ' '):
        return curso[1:]
    else:
        return curso


def programaXcolumna(filtroPrograma):
    """
    Funci�n que retorna la columna del archivo excel de la Facultad correspondiente a un programa dado
    Entradas: filtroPrograma, el c�digo del programa
    Salida: La columna correspondiente
    """
    if(filtroPrograma == 10):
        columnaPrograma = 15
    elif(filtroPrograma == 20):
        columnaPrograma = 9
    elif (filtroPrograma == 30):
        columnaPrograma = 12
    elif (filtroPrograma == 40):
        columnaPrograma = 21
    elif (filtroPrograma == 10001):
        columnaPrograma = 24
    elif (filtroPrograma == 10002):
        columnaPrograma = 6
    elif (filtroPrograma == 10003):
        columnaPrograma = 18
    elif (filtroPrograma == 10004):
        columnaPrograma = 27
    return columnaPrograma


def store_Profesores(db, sheetSuper):
    """
    Procedimiento que almacena la informaci�n de los profesores en la base de datos
    Entradas: db, la base de datos
              sheetSuper, la hoja de c�lculo
    Salida: Base de datos actualizada
    """
    for filaSuper in range(1,sheetSuper.nrows):
        id_profesor = sheetSuper.cell_value(filaSuper, 8)
        nombre_profesor = sheetSuper.cell_value(filaSuper, 9)
        if not db.execute("select id from profesor where id = ?", [id_profesor]).fetchall():
            db.execute("insert into profesor values (?,?,NULL)", [id_profesor, nombre_profesor])
        db.commit()


def store_Cursos(db, sheetFIC, filtroPrograma):
    """
    Procedimiento que almacena la informaci�n de los cursos en la base de datos
    Entradas: db, la base de datos
              sheetFIC, la hoja de c�lculo de los cursos de la Facultad
              filtroPrograma, el programa que debe ser almacenado
    Salida: Base de datos actualizada
    """

    # Se consigue la columna correspondiente al programa acad�mico
    columnaPrograma = programaXcolumna(filtroPrograma)

    # Se empieza a leer la informaci�n del Excel de la Facultad
    for filaFIC in range(1,sheetFIC.nrows):
        if(sheetFIC.cell_value(filaFIC, columnaPrograma) != ''  and \
                        (sheetFIC.cell_value(filaFIC, 1) == "DEP-CIC" or \
                         sheetFIC.cell_value(filaFIC, 1) == "DEP-CNMT" or \
                         sheetFIC.cell_value(filaFIC, 1) == "DEP-CIP")):
            codigo = delSpace(sheetFIC.cell_value(filaFIC, 2))
            if(codigo != "Por Definir"):
                nombre = sheetFIC.cell_value(filaFIC, 3)
                semestre = sheetFIC.cell_value(filaFIC, columnaPrograma+1)
                # Inserta el registro en la tabla
                if not db.execute("select codigo from curso \
                            where codigo = ? and nombre = ? and \
                            id_carrera = ? and semestre = ?",[codigo, nombre, filtroPrograma, semestre]).fetchall():
                    db.execute("insert into curso values (?,?,?,?)",[codigo, nombre, filtroPrograma, semestre])

                db.commit()




def store_Horarios(db, wbSuper, sheetSuper, sheetFIC, filtroPrograma):
    """
    Procedimiento que almacena la informaci�n de los horarios en la base de datos
    Entradas: db, la base de datos
              wbSuper, el libro del archivo superXcel
              sheetSuper, la hoja de c�lculo de todos cursos de la Universidad
              sheetFIC, la hoja de c�lculo de los cursos de la Facultad
              filtroPrograma, el programa que debe ser almacenado
    Salida: Base de datos actualizada
    """

    # Se consigue la columna correspondiente al programa acad�mico
    columnaPrograma = programaXcolumna(filtroPrograma)

    # Se empieza a leer la informaci�n del Excel de la Facultad
    for filaFIC in range(1,sheetFIC.nrows):

        # Se revisa si el curso es del Programa y de los departamentos de la Facultad
        if(sheetFIC.cell_value(filaFIC, columnaPrograma) != '' and \
                        (sheetFIC.cell_value(filaFIC, 1) == "DEP-CIC" or \
                         sheetFIC.cell_value(filaFIC, 1) == "DEP-CNMT" or \
                         sheetFIC.cell_value(filaFIC, 1) == "DEP-CIP")):
            curso = addSpace(sheetFIC.cell_value(filaFIC, 2))

            # Se hace el ciclo para realizar la comparaci�n con los registros del SuperXcel
            for filaSuper in range(1,sheetSuper.nrows):

                # Se revisa si el horario va hasta mayo (i.e. no es una reserva peque�a)
                # ESTO TIENE QUE CAMBIAR PARA QUE SEA GENERAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                mes = 0
                tmp = sheetSuper.cell_value(filaSuper, 14)
                if(tmp != ''):
                    mes = xlrd.xldate.xldate_as_datetime(tmp, wbSuper.datemode).date().month
                if (mes >= 5):

                    # Se revisa si es un curso del Programa y de los departamentos de la Facultad
                    if(curso == sheetSuper.cell_value(filaSuper, 4) and \
                            (sheetSuper.cell_value(filaSuper, 2) == "DEP-CIC" or \
                             sheetSuper.cell_value(filaSuper, 2) == "DEP-CNMT" or \
                             sheetSuper.cell_value(filaSuper, 2) == "DEP-CIP")):
                        # C�digo del curso
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

                        # Sal�n
                        salon = sheetSuper.cell_value(filaSuper, 18)

                        # Inserta los registros en las tablas
                        if not db.execute("select codigo from grupo_periodo \
                                    where codigo = ? and grupo = ? and id_carrera = ? and id_profesor = ? \
                                    and codigo_periodo = 1008",[codigo, grupo, filtroPrograma, id_profesor]).fetchall():
                            db.execute("insert into grupo_periodo values (?,?,?,?,1008)",[codigo, grupo, filtroPrograma, id_profesor])

                        if not db.execute("select codigo_curso from horario \
                                    where codigo_curso = ? and grupo_curso = ? and dia = ? and horainicio = ? \
                                    and horafin = ? and salon = ?",[codigo, grupo, dia, hora_inicio, hora_final, salon]).fetchall():
                            db.execute("insert into horario values (?,?,?,?,?,?)",[codigo, grupo, dia, hora_inicio, hora_final, salon])

                        db.commit()


def get_excel(filtroPrograma):
    """
    Procedimiento que abre los archivos excel correspondiente a los cursos, organiza su informaci�n
    y la almacena en la base de datos
    Entradas: La informaci�n de los archivos excel
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

    # Almacena la informaci�n de los profesores
    store_Profesores(db,sheetSuper)

    # Almacena la informaci�n de los cursos
    store_Cursos(db,sheetFIC,filtroPrograma)

    # Almacena la informaci�n de los horarios
    store_Horarios(db,wbSuper,sheetSuper,sheetFIC,filtroPrograma)


def procesarProgramas():
    """
    Funci�n que extrae de la base de datos la informaci�n de los programas acad�micos.
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
    Funci�n que procesa la informaci�n de la base de datos correspondiente a los cursos,
        transform�ndola en datos para enviar a la p�gina.
    Entradas: filtroSemestre, variable que representa qu� semestre se escogi� para visualizar los cursos.
              filtroPrograma, variable que representa qu� programa se escogi� para visualizar los cursos.
    Salida: Datos procesados.
    """

    # Accede a la base de datos
    db = get_db()

    # Recupera (de la base de datos) los cursos, sus profesores y sus horarios
    if(filtroSemestre == 0):
        cur1 = db.execute("select d.codigo, d.nombre, g.grupo, e.nombre, f.dia, f.horainicio, f.horafin, f.salon \
                           from curso as d, profesor as e, horario as f, grupo_periodo as g \
                           where g.id_profesor = e.id and g.codigo = f.codigo_curso \
                           and g.grupo = f.grupo_curso and d.codigo = g.codigo and d.id_carrera = g.id_carrera \
                           and d.id_carrera = ?",[filtroPrograma])
    else:
        cur1 = db.execute("select d.codigo, d.nombre, g.grupo, e.nombre, f.dia, f.horainicio, f.horafin, f.salon \
                           from curso as d, profesor as e, horario as f, grupo_periodo as g \
                           where g.id_profesor = e.id and g.codigo = f.codigo_curso \
                           and g.grupo = f.grupo_curso and d.codigo = g.codigo and d.id_carrera = g.id_carrera \
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
                "span":(curso[6]-curso[5])*2,
                "salon":curso[7]}
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
    Funci�n que envia la informaci�n a la pagina web.
    Entradas: Ninguna
    Salida: La p�gina web
    """

    # Se procesan los filtros de la p�gina
    filtroSemestre = 0
    filtroPrograma = 40
    if flask.request.method == 'POST':
        filtroSemestre = int(flask.request.form["filtroSemestre"])
        filtroPrograma = int(flask.request.form["filtroPrograma"])

    # Almacena la informaci�n de los archivos excel en la base de datos
    get_excel(filtroPrograma)

    # Recupera la informaci�n de los cursos
    datos = procesarCursos(filtroSemestre,filtroPrograma)

    # Recupera la informaci�n de los programas
    programas = procesarProgramas()

    # Retorna la p�gina web completada
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


# Si se llama la aplicaci�n directamente desde python
if(__name__ == "__main__"):
    app.run(host="127.0.0.1", port=5020, debug=True)
