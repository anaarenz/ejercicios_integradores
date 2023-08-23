'''
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia.

(Busqué otra forma distinta del ejercicio 3,
utilizado la función de python Counter importada de la librería Ccollections)
'''

import collections

def frecuencia_palabras(cadena):
    c = collections.Counter(cadena)
    return(c)

def palabra_mas_frecuente(cadena):
    f = frecuencia_palabras(cadena)
    print(f.most_common()[0])

cadena = ['la', 'la', 'la', 'la', 'be', 'ci', 'ci']
print(frecuencia_palabras(cadena))
print(palabra_mas_frecuente(cadena))
#Counter tiene el método most_common(), que devuelve una lista de tuplas de la forma
#(elemento, número de ocurrencias) ordenadas por el número de ocurrencias.