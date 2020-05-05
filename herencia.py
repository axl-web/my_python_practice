class usuario:
    #metodo constructor
    def __init__(self,nombre):
        self.nombre = nombre

    def saludo(self):
        print("Hola mi nombre es : " + self.nombre)


class jugador(usuario):
    k=0
    d=0
    a=0
    def modifica_kda(self,k,d,a):
        self.k=k
        self.d=d
        self.a=a

    def ver_kda(self):
        print("Promedio KDA: "+ str(self.k)+"/"+str(self.d)+"/"+str(self.a))
        
    def saludo(self):
        print("Nombre de Invocador: " + self.nombre)

jugador1=jugador("Axelios")
jugador1.saludo()
jugador1.modifica_kda(5,6,10)
jugador1.ver_kda()