"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
import csv

def pregunta_10():
    ruta = "files/input/data.csv"
    listillas = []
    # Diccionario que almacena los registros
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma la letra, junto con las cantidades de datos de la columna 4 y 5
            letter = fila[0]
            ccol4 = len(fila[3].split(','))
            ccol5 = len(fila[4].split(','))
            listillas.append((letter, ccol4, ccol5))
    
    return listillas
print(pregunta_10())