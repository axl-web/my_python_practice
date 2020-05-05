class usuario:
    #metodo constructor
    def __init__(self,nombre):
        self.nombre = nombre

    def saludo(self):
        print("hola, mi nombre es " + self.nombre)

usuario01=usuario("axel")

usuario01.saludo()
