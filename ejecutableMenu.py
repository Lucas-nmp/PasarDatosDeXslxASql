import funciones

# hay que crear una excepcion en caso de pulsar otra cosa que no sean las opciones dadas
# hay que crear las funciones en el archivo funciones para crear la base de datos, crear el .xslx y pasar los datos
# subir lo que llevamos a git
# tal vez crear versiones para windows y linux de la creacion del arhivo xslc con diferentes tutas / o \ 
# en la funcion de crear la base de datos solicitar la contraseña del usuario root
# en la de crear el archivo xslx pedir la cantidad de datos a generar y luego informar del tiempo 
# mas o menos que tardaria en pasar esos datos a la bd

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
            correcto=False
            while(not correcto):
                try:
                    cantidad = int(input('Escriba la cantidad de filas que quiere insertar en el archivo .xslx:  '))
                    correcto=True
                except ValueError:
                    print('Error, introduce un numero entero.')
            # si el número ha sido introducido correctamente llamamos a la función para crear el archivo .xslx y le pasamos por 
            # parámetro la cantidad de filas que queramos que tenga.
            funciones.crearXslx(cantidad)

        elif seleccion == "2":
            print('\n opción por implementar \n ')
            
        elif seleccion == "3":
            password = input('Escriba la contraseña de su usuario root en mysql:  ')
            funciones.copiarDatosAMysql(password)
        else:
            print("Opción inválida. Por favor, elija una opción válida (0-3).")

if __name__ == "__main__":
    main()
