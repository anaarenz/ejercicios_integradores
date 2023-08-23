'''
2. Escribir una función que calcule el mínimo común múltiplo entre dos números.

El mínimo común múltiplo (mcm) es el número positivo más pequeño que es múltiplo de dos o más números.

Ej:

múltiplos de 2 = 2,4,(6),8,10...
múltiplos de 3 = 3,(6),9,12...

mcm(2,3) = 6

'''

def mcm(x,y):
    z = max(x,y)

    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        
        z += 1

print(mcm(2,3))
print(mcm(2,4))
print(mcm(17,15))
print(mcm(32,13))