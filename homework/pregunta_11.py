"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
import csv

def pregunta_11():
    ruta = "files/input/data.csv"
    # Diccionario que almacena los registros
    diccionario = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Obtenemos las letra de la columna 4, y se itera sobre ellos
            lettercol4 = fila[3].split(',')

            for letter in lettercol4:
                # Si no exta en el diccionario, se agrega
                if letter not in diccionario:
                    diccionario[letter] = int(fila[1])
                else:
                    diccionario[letter] += int(fila[1])
    
    return diccionario
print(pregunta_11())