'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos.

'''
from ejercicios_integradores_6 import Persona

class Cuenta(Persona):
    def __init__(self,nombre, edad, dni ,cantidad=0.0):
        Persona.__init__(self, nombre, edad, dni)
        self._cantidad = cantidad

    @property
    def cantidad(self):
        return self._cantidad
    
    def ingresar(self,cantidad):
        saldo_anterior = self._cantidad        
        if cantidad >0:
            self._cantidad +=cantidad
            print(f"El saldo se modificó de ${saldo_anterior} a ${self.cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}")

    def retirar(self,cantidad):
        saldo_anterior = self._cantidad        
        if cantidad >0:
            self._cantidad -=cantidad
            print(f"El saldo se modificó de ${saldo_anterior} a ${self.cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}")