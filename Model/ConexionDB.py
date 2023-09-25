import mysql.connector

def get_conexion():
    conexion = mysql.connector.connect(host='localhost', database='yuri_correos', user='yuri_correos', password='1234')
    return conexion

def close_conexion(conexion):
    if conexion:
        conexion.close()
