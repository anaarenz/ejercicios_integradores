'''
1. Escribir una función que calcule el máximo común divisor entre dos números.

MCD = mayor número que divide exactamente a dos o más números a la vez.

Ej:
Divisores de 18 = 1,2,3,(6),9,18.
Divisores de 24= 1,2,3,4,(6),8,12,24.
MCD (18,24) = 6

'''
from math import floor

def  mcd(x,y):
    if x > y:
        return mcd(y, x)
    while y !=0:
        x, y = y, x % y
    return x


print("mcd: ", mcd(18,24))
print("mcd: ", mcd(3,2))
print("mcd: ", mcd(8,4))
print("mcd: ", mcd(13,17))