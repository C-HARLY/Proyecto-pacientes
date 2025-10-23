import sqlite3

DB_NAME = 'Hospital.db'

def conect():
    conexion = sqlite3.connect(DB_NAME)
    return conexion
    
    
def crear_tabla():
    conexion = conect()
    cursor = conexion.cursor()
    cursor.execute("""
         CREATE TABLE IN NOT EXISTS Pacientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dpi INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        edad INTEGER NOT NULL,
        genero TEXT NOT NULL,
        telefono INTEGER NOT NULL,
        motivoConsulta TEXT NOT NULL,
        
        
                       
        )
                   
""")
    conexion.commit()
    conexion.close()



def agregar_paciente(dpi, nombre, apellido, edad, genero, telefono, motivoConsulta):
    conexion = conect()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO Pacientes (dpi, nombre, apellido, edad, genero, telefono, motivoConsulta)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (dpi, nombre, apellido, edad, genero, telefono, motivoConsulta))
    conexion.commit()
    conexion.close()
    
    
def obtener_pacientes():
    conexion = conect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados