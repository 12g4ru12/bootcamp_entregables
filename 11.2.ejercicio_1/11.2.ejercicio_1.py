"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo
entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import sqlite3


def main():

    alumnos = [[1, 'Carlos', 'Gallego'],
               [2, 'Andres', 'Henao'],
               [3, 'Anna', 'Jade'],
               [4, 'John', 'Doe'],
               [5, 'Julanito', 'Perano'],
               [6, 'Jenny', 'Escobar'],
               [7, 'Julia', 'Franco'],
               [8, 'Andres', 'Pique']]

    for alumno in alumnos:
        insert_student(alumno[0], alumno[1], alumno[2])

    student_search('John', 'Doe')


def insert_student(identificador, nombre, apellido):
    conn = sqlite3.connect('universidad.db', isolation_level=None)

    cursor = conn.cursor()

    schema = 'CREATE TABLE IF NOT EXISTS Alumnos(' \
             'id INTEGER PRIMARY KEY, ' \
             'nombre TEXT NOT NULL,' \
             'apellido TEXT NOT NULL)'

    cursor.execute(schema)

    insert_query = '''INSERT INTO Alumnos(id, nombre, apellido) VALUES (?, ?, ?)'''
    rows = cursor.execute(insert_query, (identificador, nombre, apellido))

    cursor.close()
    conn.close()


def student_search(nombre, apellido):
    conn = sqlite3.connect('universidad.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"SELECT * FROM Alumnos WHERE nombre='{nombre}' AND apellido='{apellido}'"
    rows = cursor.execute(query)  # Ejecuta el query para consultar la base de datos.
    data = rows.fetchone()  # El metodo fetchone solo devuelve un elemento

    print(data)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()




