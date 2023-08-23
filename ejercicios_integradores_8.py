'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta.
'''
from ejercicios_integradores_7 import Cuenta

class CuentaJoven(Cuenta):

    def __init__(self,nombre, edad, dni, cantidad, bonificacion):
        Cuenta.__init__(self,nombre,edad,dni,cantidad)
        self._bonificacion=bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self,porcentaje):
        self._bonificacion=porcentaje

    def es_titular_valido(self):
        if self.edad < 25:
            return True
        else:
            return False
        
    def retirar(self,cantidad):
        if self.es_titular_valido():
             super().retirar(cantidad) #La función incorporada super() permite invocar un método de una clase padre desde una clase hija.
        else:
            print(f"No es un titular válido para retirar ${cantidad}")

    def detalle(self):
        print(f"Cuenta joven")        
        print(f"Bonificación: {self._bonificacion}%")