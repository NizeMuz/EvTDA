from Model.ConexionDB import *

def eliminarContactoemergencia():
    conexion = get_conexion()
    cursor = conexion.cursor()

    cmd_consulta = ("SELECT id, nombre, relacion, telefono "
                    "FROM usuarios")

    cursor.execute(cmd_consulta)

    for (id, nombre, relacion, telefono) in cursor:
        print(id, "-", nombre, "-", relacion, "-", telefono)

    id = input("Ingrese el ID del contacto de emergencia desea eliminar? ")

    cmd_eliminar = ("DELETE FROM usuarios "
                    "WHERE id = %s")

    valores = [id]

    cursor.execute(cmd_eliminar, valores)
    conexion.commit()
    cursor.close()
    print("Datos eliminados")

def eliminarCargasfamiliares():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT id, nombre, parentesco, sexo, rut "
                        "FROM cargas_familiares")

        cursor.execute(cmd_consulta)

        for (id, nombre, parentesco, sexo, rut) in cursor:
            print(id, "-", nombre, "-", parentesco, "-", sexo,"-" ,rut)

        id = input("Ingrese el ID de la carga familiar que desea eliminar: ")

        cmd_eliminar = ("DELETE FROM cargas_familiares "
                        "WHERE id = %s")

        valores = [id]

        cursor.execute(cmd_eliminar, valores)
        conexion.commit()
        cursor.close()
        close_conexion(conexion)
        print("Datos eliminados")

    except mysql.connector.Error as error:
        print("Error al eliminar los datos:", error)

def eliminarEmpleados():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento "
                        "FROM empleados")

        cursor.execute(cmd_consulta)

        for (nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento) in cursor:
            print(nombre_completo, "-", rut, "-", sexo, "-", direccion, "-", telefono, "-", cargo, "-", fecha_ingreso, "-",area,"-", departamento,)

        id = input("Ingrese el ID del empleado que desea eliminar: ")

        cmd_eliminar = ("DELETE FROM empleados "
                        "WHERE id = %s")

        valores = [id]

        cursor.execute(cmd_eliminar, valores)
        conexion.commit()
        cursor.close()
        close_conexion(conexion)
        print("Datos eliminados")

    except mysql.connector.Error as error:
        print("Error al eliminar los datos:", error)
