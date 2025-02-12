"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
import csv

def pregunta_06():
    ruta = "files/input/data.csv"
    # Diccionario que almacena los registros
    diccionario = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
        for fila in lector_csv:
            # Se toma una linea de la columna 5
            chain= fila[4]
            # Se divide la cadena, separa por comas
            datos = chain.split(',')
            
            #
            # Se itera sobre cada uno de los datos separados
            #
            for dato in datos:
                # Se separan en pares de clave valor
                clave, valor = dato.split(':')
                valor = int(valor)
                

                # Si no esta en el diccionario, se crea
                if clave not in diccionario:
                    diccionario[clave] = [valor, valor]

                # Si esta, se comprueban sus tuplas para tomar valores máximos y minimos
                else:
                    if valor <= diccionario[clave][0]:
                        diccionario[clave][0] = valor

                    elif valor >= diccionario[clave][1]:
                        diccionario[clave][1] = valor

    # Retorna en el orden pedido
    # En onde se mete, que se mete, ciclo for
    lista = [(clave, valor[0], valor[1]) for clave, valor in sorted(diccionario.items())]
    
    return lista
print(pregunta_06())
