import csv
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
def pregunta_01():
    ruta = "files/input/data.csv"
    # Almacena todos los valores de la columna 2
    sumas = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Añade los valores de la columna 2 y los convierte en enteros
            sumas.append(int(fila[1]))

        # Retorna resultado
        sumas = sum(sumas)
        
        return sumas

print (pregunta_01())