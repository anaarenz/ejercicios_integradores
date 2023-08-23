'''
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva.

Recursividad: situación en la que una función se llama a sí misma una y otra vez.
Iteración: permite repetir una sentencias o conjunto de ellas.

¿Qué ventajas tiene la programación recursiva frente a la iterativa?
Usualmente, el código con recursividad es más consistente que el código con iteración.
Solo hay una sentencia en el método de recursividad, y existe más de una sentencia en el método con iteraciones.
Adicionalmente, los bucles, que incluyen varios bucles son complejos de leer y entender.
'''

def get_int_iterativa():
    while True:
        try:
            n = int(input("Ingrese un número entero: "))
            return n
        except ValueError:
            print("Valor no válido, por favor ingrese número entero")

def get_int_recursiva():
    try:
        n=int(input("Ingrese un número entero: "))
        return n
    except ValueError:
        print("Valor no válido , por favor ingrese un número entero") 
        return get_int_recursiva()

print("De forma recursiva: ")
print("---------------------")

get_int_recursiva()

print("############################################################")

print("De forma iterativa: ")
print("---------------------")
get_int_iterativa()