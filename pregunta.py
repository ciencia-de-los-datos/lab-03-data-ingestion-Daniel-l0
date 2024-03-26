"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    
    # Inserte su código aquí
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if not line.startswith('-')]
        lines = [line.replace(".","") for line in lines]
        lines = [line.strip() for line in lines if not line == lines[1]]
        lines = [line.strip() for line in lines if not line == lines[1]]
        lines = [re.sub(r'\s+', ' ', line) for line in lines]
        lines = [line.rpartition(' %') for line in lines[1:]]
        clusters_report = [[line[0].split(' '),line[2]] for line in lines]
    column_names = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    cluster = [int(line[0][0]) for line in clusters_report if line[0][0].isnumeric()]
    cantidad_de_palabras_clave = [int(line[0][1]) for line in clusters_report if line[0][0].isnumeric()]
    porcentaje_de_palabras_clave = [float(line[0][2].replace(",",".")) for line in clusters_report if line[0][0].isnumeric()]
    principales_palabras_clave = []
    for i, elemento in enumerate(clusters_report):
    # Si el primer elemento está vacío y no estamos en la primera línea
        if not elemento[0][0].isnumeric() and i > 0:
        # Concatenar el segundo elemento con el último no vacío
            principales_palabras_clave[-1] += " " + elemento[1]
    # Si no, simplemente agregar el segundo elemento a la lista de palabras
        else:
            principales_palabras_clave.append(elemento[1])
    principales_palabras_clave = [palabra.strip() for palabra in principales_palabras_clave]
    df = pd.DataFrame({
    'cluster': cluster,
    'cantidad_de_palabras_clave': cantidad_de_palabras_clave,
    'porcentaje_de_palabras_clave': porcentaje_de_palabras_clave,
    'principales_palabras_clave': principales_palabras_clave
    })
    return df
