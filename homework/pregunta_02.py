"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

import csv

def pregunta_02():
    ruta = "files/input/data.csv"
    # Diccionario que almacena los registros
    diccionario = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Añade los valores de la columna 2 y los convierte en enteros
            # Si existe
            if fila[0] in diccionario:
                diccionario[fila[0]] += 1
            # Si no existe
            else:
                diccionario[fila[0]] = 1

    # Se obtienen los objetos del diccionario, y se ordenan en base a su letra
    lista = list(diccionario.items())
    lista.sort()

    return lista

print(pregunta_02())
