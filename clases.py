#creacion de clase
class User:
    nombre=""
    def saludo(self):
        print("Hola, mi nombre es " + self.nombre)
#creacion de objeto apartir de la clase User
axel= User()
axel.nombre="axelios"

axel.saludo()