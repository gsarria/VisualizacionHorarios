# all the imports
import sqlite3
from contextlib import closing

# Base de datos oficial
#DATABASE = '/Users/gsarria/Dropbox/Work/ABETForm/github/abetpujc/abet.db'
#DATABASE = 'C:/Users/Usuario/Desktop/abetpujc-master/abet.db'
DATABASE = 'cursos.db'

#DATA_DATABASE = 'C:/Users/Usuario/Desktop/abetpujc-master/scripts/addData2db_main.sql'
MAINDATA_DATABASE = 'scripts/addData2db_main.sql'
HORARIOS_DATABASE = 'scripts/addData2db_horarios.sql'

#ABET_DATABASE = 'C:/Users/Usuario/Desktop/abetpujc-master/scripts/DB_SQLite.sql'
CURSOS_DATABASE = 'scripts/DB_SQLite.sql'


def connect_db():
    return sqlite3.connect(DATABASE)


def add_maindata(db):
    with open(MAINDATA_DATABASE, mode='r') as f:
        print("Filling DB")
        db.executescript(f.read())
    db.commit()


def add_horarios(db):
    with open(HORARIOS_DATABASE, mode='r') as f:
        print("Filling DB")
        db.executescript(f.read())
    db.commit()


def init_db():
    with closing(connect_db()) as db:
        with open(CURSOS_DATABASE, mode='r') as f:
            print("Creating DB")
            db.executescript(f.read())
            add_maindata(db)
            # El siguiente llamado a funcion solo se debe hacer si no hay otra fuente de datos para los horarios
            #add_horarios(db)
        db.commit()


if __name__ == "__main__":
    init_db()
