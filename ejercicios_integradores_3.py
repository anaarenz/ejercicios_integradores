'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

'''
def frecuencia_palabras(cadena):
    lista_palabras = cadena.split()
    return{palabra: lista_palabras.count(palabra) for palabra in lista_palabras}

cadena = input("Ingrese una cadena de caracteres: ") #lala lele lili lili lili lele
print(frecuencia_palabras(cadena)) #{'lala': 1,'lele': 2,'lili': 3}