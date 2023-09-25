from Model.Empleados import *
from Model.ConexionDB import *
def modificarEmpleadosAdmin():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT id nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento "
                        "FROM empleados")

        cursor.execute(cmd_consulta)

        for (id,nombre_completo, rut, sexo, direccion, telefono, cargo, fecha_ingreso, area, departamento) in cursor:
            print(id,"-",nombre_completo, "-", rut, "-", sexo, "-", direccion, "-", telefono, "-", cargo, "-", fecha_ingreso, "-", departamento,"---------------")

        rut = input("Ingrese el rut del usuario que desea modificar: ")

        # Opciones para editar los parámetros
        opciones = {
            "nombre_completo": "Nombre completo",
            "rut": "RUT",
            "sexo": "Sexo",
            "direccion": "Dirección",
            "telefono": "Teléfono",
            "cargo": "Cargo",
            "fecha_ingreso": "Fecha de ingreso",
            "area": "Área",
            "departamento": "Departamento"
        }

        datos_nuevos = {}

        for parametro, descripcion in opciones.items():
            valor = input(f"Ingrese el nuevo valor para {descripcion} (Presione Enter para omitir): ")
            if valor:
                datos_nuevos[parametro] = valor

        if datos_nuevos:
            cmd_modificar = "UPDATE empleados SET "
            valores = []

            for parametro, valor in datos_nuevos.items():
                cmd_modificar += f"{parametro} = %s, "
                valores.append(valor)

            cmd_modificar = cmd_modificar.rstrip(", ")
            cmd_modificar += " WHERE rut = %s"
            valores.append(rut)

            print("Actualizando datos")
            cursor.execute(cmd_modificar, valores)
            conexion.commit()
            print("Datos guardados")
        else:
            print("No se realizaron modificaciones")

        cursor.close()
        close_conexion(conexion)

    except mysql.connector.Error as error:
        print("Error al modificar los datos:", error)

def modificarEmpleadosEmpleado():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT id, nombre_completo, rut, sexo, direccion, telefono "
                        "FROM empleados")

        cursor.execute(cmd_consulta)

        for (id,nombre_completo, rut, sexo, direccion, telefono) in cursor:
            print(id,"-",nombre_completo, "-", rut, "-", sexo, "-", direccion, "-", telefono)

        rut = input("Ingrese el email del usuario que desea modificar: ")

        opciones = {
            "nombre_completo": "Nombre completo",
            "sexo": "Sexo",
            "direccion": "Dirección",
            "telefono": "Teléfono"
        }

        datos_nuevos = {}

        for parametro, descripcion in opciones.items():
            valor = input(f"Ingrese el nuevo valor para {descripcion} (Presione Enter para omitir): ")
            if valor:
                datos_nuevos[parametro] = valor

        if datos_nuevos:
            cmd_modificar = "UPDATE empleados SET "
            valores = []

            for parametro, valor in datos_nuevos.items():
                cmd_modificar += f"{parametro} = %s, "
                valores.append(valor)

            cmd_modificar = cmd_modificar.rstrip(", ")
            cmd_modificar += " WHERE rut = %s"
            valores.append(rut)

            print("Actualizando datos")
            cursor.execute(cmd_modificar, valores)
            conexion.commit()
            print("Datos guardados")
        else:
            print("No se realizaron modificaciones")

        cursor.close()
        close_conexion(conexion)

    except mysql.connector.Error as error:
        print("Error al modificar los datos:", error)

def modificarContactoEmergencia():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT id, nombre, relacion, telefono "
                        "FROM ContactosEmergencia")

        cursor.execute(cmd_consulta)

        for (id, nombre, relacion, telefono) in cursor:
            print(id, "-", nombre, "-", relacion, "-", telefono)

        id = input("Ingrese el ID del contacto de emergencia que desea modificar: ")

        opciones = {
            "nombre": "Nombre",
            "relacion": "Relación",
            "telefono": "Teléfono"
        }

        datos_nuevos = {}

        for parametro, descripcion in opciones.items():
            valor = input(f"Ingrese el nuevo valor para {descripcion} (Presione Enter para omitir): ")
            if valor:
                datos_nuevos[parametro] = valor

        if datos_nuevos:
            cmd_modificar = "UPDATE ContactosEmergencia SET "
            valores = []

            for parametro, valor in datos_nuevos.items():
                cmd_modificar += f"{parametro} = %s, "
                valores.append(valor)

            cmd_modificar = cmd_modificar.rstrip(", ")
            cmd_modificar += " WHERE id = %s"
            valores.append(id)

            print("Actualizando datos")
            cursor.execute(cmd_modificar, valores)
            conexion.commit()
            print("Datos guardados")
        else:
            print("No se realizaron modificaciones")

        cursor.close()
        close_conexion(conexion)

    except mysql.connector.Error as error:
        print("Error al modificar los datos:", error)

def modificarCargaFamiliar():
    try:
        conexion = get_conexion()
        cursor = conexion.cursor()

        cmd_consulta = ("SELECT id, nombre, parentesco, sexo, rut "
                        "FROM cargas_familiares")
        cursor.execute(cmd_consulta)

        for (id, nombre, parentesco, sexo, rut) in cursor:
            print(id, "-", nombre, "-", parentesco, "-", sexo, "-", rut)

        id_carga = input("Ingrese el ID de la carga familiar que desea modificar: ")

        opciones = {
            "nombre": "Nombre",
            "parentesco": "Parentesco",
            "sexo": "Sexo",
            "rut": "RUT"
        }

        datos_nuevos = {}

        for parametro, descripcion in opciones.items():
            valor = input(f"Ingrese el nuevo valor para {descripcion} (Presione Enter para omitir): ")
            if valor:
                datos_nuevos[parametro] = valor

        if datos_nuevos:
            cmd_modificar = "UPDATE cargas_familiares SET "
            valores = []

            for parametro, valor in datos_nuevos.items():
                cmd_modificar += f"{parametro} = %s, "
                valores.append(valor)

            cmd_modificar = cmd_modificar.rstrip(", ")
            cmd_modificar += " WHERE id = %s"
            valores.append(id_carga)

            print("Actualizando datos")
            cursor.execute(cmd_modificar, valores)
            conexion.commit()
            print("Datos guardados")
        else:
            print("No se realizaron modificaciones")

        cursor.close()
        close_conexion(conexion)

    except mysql.connector.Error as error:
        print("Error al modificar los datos:", error)