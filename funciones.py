import pandas as pd, constantes, random, mysql.connector
from datetime import datetime, timedelta


""" Este es la función principal en la que vamos a leer los datos de un archivo xslx y lo vamos a pasar 
a una base de datos mysql, la base de datos y la tabla tiene que estar creada en el sistema y coincidir
los nombres de las columnas con los nombres de los campos de la tabla, en caso contrario dará error. 
Todos los datos a insertar van entre comillas, varchar y date para insertar int habría que modificar el programa
y el formato de fecha está en el archivo .xslx en el mismo formato que necesita mysql. """

# Para insertar 6 columnas con 15000 filas tarda exactamente 1 minuto y 33 segundos 
def copiarDatosAMysql(pas):
    # convertimos la contrasesña recibida a string para no tener problemas 
    pasStr = str(pas)

    conexion = mysql.connector.connect(host="localhost", user="root", passwd=pasStr, database='usuarios')
    cursor1 = conexion.cursor()

    dfArchivo = pd.read_excel('./datos.xlsx')

    columnas_mysql = ', '.join(dfArchivo.columns)

    # Itera sobre cada fila del DataFrame
    for index, fila in dfArchivo.iterrows():
        # Genera la lista de valores de la fila entre comillas
        valores_fila = "', '".join(str(valor) for valor in fila.values)

        # Genera el comando INSERT
        comando_insert = f"INSERT INTO user ({columnas_mysql}) VALUES ('{valores_fila}')"

        # Ejecuta el comando INSERT
        cursor1.execute(comando_insert)
        conexion.commit()


""" La idea principal es leer un archivo excel con datos de clientes y pasarlos a una base de datos mysql.
    
    Aquí, como no tengo un archivo excel con datos, lo que vamos a hacer es crearlo y llenarlo con datos 
    inventados de forma aleatoria """
def crearXslx(cantidad):
    try:
        # Vamos a crear un diccionario con los datos que vamos a escribir en el archivo excel
        # Estos datos los vamos a crear de forma aleatoria para llenar el excel 
        datos = {'Nombre': obtenerLista(constantes.NOMBRE, cantidad),
                'Apellido': obtenerLista(constantes.APELLIDO, cantidad),
                'Pueblo': obtenerLista(constantes.PUEBLO, cantidad),
                'Ciudad': obtenerLista(constantes.CIUDAD, cantidad),
                'Teléfono' : generadorTelefonos(cantidad),
                'Fecha_Nacimiento': fechasNacimiento(cantidad)}

        #convertimos el diccionario a DataFrame con pandas 
        df = pd.DataFrame(datos)

        # Especificamos la ruta donde vamos a crear el archivo y el nombre del archivo
        ruta_archivo = './datos.xlsx'

        # Escribimos el DataFrame en el archivo de Excel
        # El parámetro index sirve para crear y almacenar un indice en el arcivo exel en caso de necesitarlo
        df.to_excel(ruta_archivo, index=False)
        print('\n Archivo creado correctamente \n')
    except ValueError:
        print('Ha ocurrido un error y el archivo no ha sido creado')

# función que recibe dos parametros, una lista de elementos de cualquier tipo y un número
# Retorna una lista con tantos elementos aleatorios de la lista recibida como se indique en el número 

def obtenerLista(lista, cantidad):
    listaResultado = []  
    for i in range (cantidad):
        listaResultado.append(random.choice(lista)) 
        # vamos almacenando en la lista valores aleatorios de la lista recibida, tantos como indique el parametro cantidad
    
    return listaResultado


# función que genera una lista de números aleatorios entre dos números

def generadorTelefonos(cantidad):
    listaResultado = []  
    for i in range(cantidad):
        listaResultado.append(random.randint(600000000, 699999999)) 
        # generamos tantos números aleatorios para almacenarlos en la lista de resultado, como nos han indicado en en la llamada a la fincion
    
    return listaResultado



# función que genera una lista de fechas de nacimiento aleatorias entre dos fechas indicadas, almacena 
# las fechas en el formato de fecha indicado 

def fechasNacimiento(cantidad):
    listaResultado = []
    for i in range(cantidad):
        inicio = datetime(2005, 1, 1)
        final =  datetime(1938, 12, 31)
        fecha_aleatoria = inicio + timedelta(seconds=int((final - inicio).total_seconds() * random.random()))
        listaResultado.append(fecha_aleatoria.strftime('%Y-%m-%d'))

    return listaResultado



# Función que evita un error si no se introduce un número entero 

def comprobarInt():
    correcto=False
    while(not correcto):
        try:
            cantidad = int(input('Escriba la cantidad de filas que quiere insertar en el archivo .xslx:  '))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero.')
    
    return cantidad