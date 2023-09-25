from Model.ConexionDB import *

def login():
    conexion = get_conexion()
    cursor = conexion.cursor()

    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    consulta = "SELECT id FROM usuarios WHERE username = %s AND password = %s"
    valores = (usuario, contrasena)

    try:
        cursor.execute(consulta, valores)

        fila = cursor.fetchone()
        if fila:
            id = fila[0]
            if id == 1:
                print("Inicio de sesión exitoso. Eres un administrador.")
                return "admin"
            else:
                print("Inicio de sesión exitoso. Eres un usuario normal.")
                return "normal"
        else:
            print("Credenciales inválidas. Inicio de sesión fallido.")
            return "fallido"

    except mysql.connector.Error as error:
        print("Error al realizar el inicio de sesión:", error)

    finally:
        cursor.close()
        close_conexion(conexion)

    return "fallido"