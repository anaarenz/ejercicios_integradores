'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''
class Persona:
    def __init__(self, nombre="",edad=0,dni=""): #constructor
        self._nombre=nombre
        self._edad=edad
        self._dni=dni

    @property #getters
    def nombre(self):
        return self._nombre    
    
    @nombre.setter
    def nombre(self,nombre):
        if nombre != "":
            self._nombre=nombre
        else:
            print("Por favor escriba su nombre")    

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        try:
            if edad < 0:
                print("Ingrese su edad")
            else:
                self._edad=edad
        except TypeError:
            print("Ingrese un número entero")        
        
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        if len(dni) < 8:
           print("El DNI debe tener 8 números")
        else:
           self._dni=dni

    def mostrar(self):
        print(f"Nombre: {self._nombre} - Edad: {self._edad} - DNI: {self._dni}")

    def es_mayor_de_edad(self):
        if self._edad >=18:
            return True
        else:
            return False
        

persona1=Persona()
nombre1=persona1.nombre("Ana")
edad1=persona1.edad(36)
dni1=persona1.dni(33000111)
persona1.mostrar()
persona1.es_mayor_de_edad(edad1)