class   Usuario:
    __edad = 0
    def __init__(self,nombre):#metodo constructor
        self._nombre = nombre

    def saludo(self,saludo):
        print(saludo + self._nombre)

    @property
    def edad(self):#getter
        return self.__edad
    @edad.setter
    def edad(self,valor):#setter
        if (valor < 18):
            raise ValueError("El empleado no puede ser menor de 18 años")
        self.__edad= valor


class Empleado(Usuario):
     __salario=0

     def modificarSalario(self,salario):
         self.__salario = salario
    
     def verSalario(self):
         print(self.__salario)

     def saludo(self):
        super().saludo("Hola! ")
        print("Mi nombre es: " + self._nombre + "y gano: " + str(self.__salario))


empleado=Empleado("Axel")
empleado.edad = 12
print(empleado.edad)
