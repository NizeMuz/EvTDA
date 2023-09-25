from Model.ConexionDB import *
from Model.Empleados import *
from Model.Contactos_Emergencia import *
from Model.Cargafamilar import *

def listarEmpleados():
    conexion = get_conexion()
    cursor = conexion.cursor()

    consultar_empleados = "SELECT * FROM Empleados"

    try:
        cursor.execute(consultar_empleados)
        empleados = cursor.fetchall()

        if empleados:
            for empleado in empleados:
                print("Nombre completo:", empleado[1])
                print("RUT:", empleado[2])
                print("Sexo:", empleado[3])
                print("Dirección:", empleado[4])
                print("Teléfono:", empleado[5])
                print("Cargo:", empleado[6])
                print("Fecha de ingreso:", empleado[7])
                print("Área:", empleado[8])
                print("Departamento:", empleado[9])
                print("------------------------")
        else:
            print("No hay empleados registrados.")

    except mysql.connector.Error as error:
        print("Error al listar los empleados:", error)

    cursor.close()
    close_conexion(conexion)

def listarcontactos_emergencia():
    conexion = get_conexion()
    cursor = conexion.cursor()

    consultar_contactos_emergencia = "SELECT * FROM contactos_emergencia"

    try:
        cursor.execute(consultar_contactos_emergencia)
        contactos_emergencia = cursor.fetchall()

        if contactos_emergencia:
            for contacto in contactos_emergencia:
                print("Nombre :", contacto[1])
                print("Relacion:", contacto[2])
                print("Telefono:", contacto[3])
                print("------------------------")
        else:
            print("No hay contactos de emergencia registrados.")

    except mysql.connector.Error as error:
        print("Error al listar los contactos de emergencia:", error)

    cursor.close()
    close_conexion(conexion)

def listarcargas_familiares():
    conexion = get_conexion()
    cursor = conexion.cursor()

    consultar_cargas_familiares = "SELECT * FROM cargas_familiares"

    try:
        cursor.execute(consultar_cargas_familiares)
        cargas_familiares = cursor.fetchall()

        if cargas_familiares:
            for carga in cargas_familiares:
                print("Nombre :", carga[1])
                print("Parentesco:", carga[2])
                print("Sexo:", carga[3])
                print("Rut:", carga[4] )
                print("------------------------")
        else:
            print("No hay cargas familiares registradas.")

    except mysql.connector.Error as error:
        print("Error al listar las cargas familiares:", error)

    cursor.close()
    close_conexion(conexion)