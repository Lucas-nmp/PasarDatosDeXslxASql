import funciones

# hay que crear las funciones en el archivo funciones para crear la base de datos
# informar del tiempo mas o menos que tardaría en pasar los datos a la bd

""" Menú desde el que vamos a llamar a las diferentes funciones almacenadas en el archivo funciones.py para ir realizando 
    las acciones que necesitemos. 
    Si creamos el archivo .xslx dos veces sin cambiar la ruta el último borrará al generado anteriormente"""

def mostrar_menu():
    print("------ Menú ------")
    print("1. Crear un archivo .xslx")
    print("2. Crear la base de datos en mysql")
    print("3. Pasar los datos del .xslx a la base de datos")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        seleccion = input("Elija una opción: ")
        if seleccion == "0":
            print("Hasta luego. ¡Vuelve pronto!")
            break
        elif seleccion == "1":
            funciones.crearXslx(funciones.comprobarInt())

        elif seleccion == "2":
            contr = input('Escriba la contraseña de su usuario root en mysql:  ')
            funciones.crearBdyTabla(contr)
            
        elif seleccion == "3":
            contr = input('Escriba la contraseña de su usuario root en mysql:  ')
            funciones.copiarDatosAMysql(contr)
        else:
            print("Opción inválida. Por favor, elija una opción válida (0-3).")

if __name__ == "__main__":
    main()
