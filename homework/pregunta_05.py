"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
import csv

def pregunta_05():
    ruta = "files/input/data.csv"
    # Diccionario que almacena los registros
    diccionario = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma la letra de la col 1, y el numero de la col 2
            letter = fila[0]
            number = int(fila[1])

            # Si no esta en el diccionario, se crea
            if letter not in diccionario:
                diccionario[letter] = [number, number]

            # Si esta, se comprueban sus tuplas para tomar valores máximos y minimos
            else:
                if number >= diccionario[letter][0]:
                    diccionario[letter][0] = number

                elif number <= diccionario[letter][1]:
                    diccionario[letter][1] = number

    # Retorna en el orden pedido
    # En onde se mete, que se mete, ciclo for
    lista = [(clave, valor[0], valor[1]) for clave, valor in sorted(diccionario.items())]
    
    return lista
print(pregunta_05())