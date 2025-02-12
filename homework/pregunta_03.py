"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
import csv

def pregunta_03():
    ruta = "files/input/data.csv"
    # diccionario que almacena los registros
    diccionario = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Añade los valores de la columna 2 y los convierte en enteros
            # Si existe
            if fila[0] in diccionario:
                diccionario[fila[0]] += int(fila[1])
            # Si no existe
            else:
                diccionario[fila[0]] = int(fila[1])

    # Se obtienen los objetos del diccionario, y se ordenan en base a su letra
    lista = list(diccionario.items())
    lista.sort()
    
    return lista

print(pregunta_03())