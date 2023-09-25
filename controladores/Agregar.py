from Model.ConexionDB import *
from Model.Empleados import *
from Model.Contactos_Emergencia import *
from Model.Cargafamilar import *


def agregarEmpleados():
    agregarempleado = Empleados()
    conexion = get_conexion()
    cursor = conexion.cursor()

    agregar_usuario = ("INSERT INTO Empleados "
                      "(nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento) "
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    nombre_completo = input("Ingrese el nombre del nuevo empleado: ")
    agregarempleado.nombre_completo = nombre_completo
    rut = input("Ingrese el rut del empleado en formato 12.345.678-9: ")
    agregarempleado.rut = rut
    sexo = input("Ingrese el sexo del nuevo empleado: ")
    agregarempleado.sexo = sexo
    direccion = input("Ingrese la dirección del nuevo empleado: ")
    agregarempleado.direccion = direccion
    telefono = input("Ingrese el teléfono del nuevo empleado: ")
    agregarempleado.telefono = telefono
    cargo = input("Ingrese el cargo del nuevo empleado: ")
    agregarempleado.cargo = cargo
    fecha_ingreso = input("Ingrese la fecha de ingreso del empleado en formato DD/MM/AAAA: ")
    agregarempleado.fecha_ingreso = fecha_ingreso
    area = input("Ingrese el área del nuevo empleado: ")
    agregarempleado.area = area
    departamento = input("Ingrese el departamento del nuevo empleado: ")
    agregarempleado.departamento = departamento

    valores = (agregarempleado.nombre_completo, agregarempleado.rut, agregarempleado.sexo, agregarempleado.direccion,
               agregarempleado.telefono, agregarempleado.cargo, agregarempleado.fecha_ingreso, agregarempleado.area,
               agregarempleado.departamento)

    try:
        cursor.execute(agregar_usuario, valores)
        conexion.commit()
        print("Datos guardados")
    except mysql.connector.Error as error:
        print("Error al guardar los datos:", error)

    cursor.close()
    close_conexion(conexion)


def agregarContactos_emergencia():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        agregar_contacto = ("INSERT INTO Contactos_Emergencia "
                            "(nombre, relacion, telefono) "
                            "VALUES (%s, %s, %s)")

        nombre = input("Ingrese el nombre del Contacto de emergencia: ")
        relacion = input("Ingrese la relación con el empleado: ")
        telefono = input("Ingrese el teléfono del contacto de emergencia: ")

        contacto = ContactosEmergencia(nombre, relacion, telefono)

        print("Insertando datos")
        cursor.execute(agregar_contacto, (contacto.get_nombre(), contacto.get_relacion(), contacto.get_telefono()))

        conexion.commit()
        cursor.close()
        close_conexion(conexion)

        print("Datos guardados")

    except mysql.connector.Error as error:
        print("Error al insertar datos:", error)

def agregarCargas_familiares():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()
        agregar_carga_familiar = ("INSERT INTO Cargas_Familiares "
                                  "(nombre, parentesco, sexo, rut) "
                                  "VALUES (%s, %s, %s, %s)")

        nombre = input("Ingrese el nombre de la carga familiar: ")
        parentesco = input("Ingrese el parentesco con el empleado: ")
        sexo = input("Ingrese el sexo de la carga familiar: ")
        rut = input("Ingrese el rut de la carga familiar en formato 12.345.678-9: ")

        carga_familiar = CargaFamiliar(nombre, parentesco, sexo, rut)

        print("Insertando datos")
        cursor.execute(agregar_carga_familiar, (carga_familiar.get_nombre(), carga_familiar.get_parentesco(),
                                                carga_familiar.get_sexo(), carga_familiar.get_rut()))

        conexion.commit()
        cursor.close()
        close_conexion(conexion)

        print("Datos guardados")

    except mysql.connector.Error as error:
        print("Error al insertar datos:", error)