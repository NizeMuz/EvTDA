from controladores.login import *
from controladores.Agregar import *
from controladores.Consultas import *
from controladores.Eliminar import *
from controladores.Modificar import *
from View.menu import *

def main():
    tipo_usuario = login()

    if tipo_usuario == "admin":
        while True:
            opcion = menuAdmin()
            if opcion == 1:
                print("Opción Agregar seleccionada")
                opcion_agregar = menuAgregar()
                if opcion_agregar == 1:
                    print("Agregar Empleado seleccionado")
                    agregarEmpleados()
                elif opcion_agregar == 2:
                    print("Agregar Contacto de emergencia seleccionado")
                    agregarContactos_emergencia()
                elif opcion_agregar == 3:
                    print("Agregar Carga familiar seleccionada")
                    agregarCargas_familiares()
                elif opcion_agregar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 2:
                print("Opción Consultar seleccionada")
                opcion_consultar = menuConsultar()
                if opcion_consultar == 1:
                    print("Consultar Empleados seleccionado")
                    listarEmpleados()
                elif opcion_consultar == 2:
                    print("Consultar Contactos de emergencia seleccionado")
                    listarcontactos_emergencia()
                elif opcion_consultar == 3:
                    print("Consultar Cargas familiares seleccionado")
                    listarcargas_familiares()
                elif opcion_consultar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 3:
                print("Opción Modificar seleccionada")
                opcion_modificar = menuModificarAdmin()
                if opcion_modificar == 1:
                    print("Modificar Empleado seleccionado")
                    modificarEmpleadosAdmin()
                elif opcion_modificar == 2:
                    print("Modificar Contacto de emergencia seleccionado")
                    modificarContactoEmergencia()
                elif opcion_modificar == 3:
                    print("Modificar Carga familiar seleccionada")
                    modificarCargaFamiliar()
                elif opcion_modificar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 4:
                print("Opción Eliminar seleccionada")
                opcion_eliminar = menuEliminar()
                if opcion_eliminar == 1:
                    print("Eliminar Empleado seleccionado")
                    eliminarEmpleados()
                elif opcion_eliminar == 2:
                    print("Eliminar Contacto de emergencia seleccionado")
                    eliminarContactoemergencia()
                elif opcion_eliminar == 3:
                    print("Eliminar Carga familiar seleccionada")
                    eliminarCargasfamiliares()
                elif opcion_eliminar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 5:
                print("Saliendo...")
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    elif tipo_usuario == "normal":
        while True:
            opcion = menuEmpleado()
            if opcion == 1:
                print("Opción Agregar seleccionada")
                opcion_agregar = menuAgregarEmpleado()
                if opcion_agregar == 1:
                    print("Agregar Contacto de emergencia Seleccionada")
                    agregarContactos_emergencia()
                elif opcion_agregar == 2:
                    print("Agregar Carga familiar Seleccionada")
                    agregarCargas_familiares()
                elif opcion_agregar == 3:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 2:
                print("Opción Consultar seleccionada")
                opcion_consultar = menuConsultar()
                if opcion_consultar == 1:
                    print("Consultar Empleados seleccionado")
                    listarEmpleados()
                elif opcion_consultar == 2:
                    print("Consultar Contactos de emergencia seleccionado")
                    listarcontactos_emergencia()
                elif opcion_consultar == 3:
                    print("Consultar Cargas familiares seleccionado")
                    listarcargas_familiares()
                elif opcion_consultar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 3:
                print("Opción Modificar seleccionada")
                opcion_modificar = menuModificarEmpleado()
                if opcion_modificar == 1:
                    print("Modificar Datos de empleado Seleccionada")
                    modificarEmpleadosEmpleado()
                elif opcion_modificar == 2:
                    print("Modificar Contacto de emergencia Seleccionada")
                    modificarContactoEmergencia()
                elif opcion_modificar == 3:
                    print("Modificar Carga familiar Seleccionada")
                    modificarCargaFamiliar()
                elif opcion_modificar == 4:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 4:
                print("Opción Eliminar seleccionada")
                opcion_eliminar = menuEliminarEmpleado()
                if opcion_eliminar == 1:
                    print("Eliminar Contacto emergencia Seleccionada")
                    eliminarContactoemergencia()
                elif opcion_eliminar == 2:
                    print("Eliminar Carga familiar Seleccionada")
                    eliminarCargasfamiliares()
                elif opcion_eliminar == 3:
                    print("Volviendo al menú principal...")
                    continue
                else:
                    print("Opción inválida. Por favor, ingrese una opción válida.")

            elif opcion == 5:
                print("Saliendo...")
                break

            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    elif tipo_usuario == "fallido":
        print("Inicio de sesión fallido. Por favor, inténtelo de nuevo.")
    else:
        print("Error: Tipo de usuario desconocido.")

if __name__ == "__main__":
    main()