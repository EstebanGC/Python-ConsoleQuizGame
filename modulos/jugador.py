class Jugador():
    
    def __init__(self):
        self.nombre   = ""
        self.puntaje  = 0.0
        self.aciertos = 0


    def llenarInformacion(self):
        self.nombre = str(input("Nombre Jugador : "))


    def aumentarPuntaje(self):
        self.puntaje = self.puntaje + 1000
        self.aciertos = self.aciertos + 1


    def guardar_informacion_partida(self):
        archivo = open("puntajes.txt","a")

        archivo.write("\n")
        archivo.write("Nombre jugador : ")
        archivo.write(str(self.nombre))
        archivo.write("\n")
        archivo.write("Puntaje        : ")
        archivo.write(str(self.puntaje))
        archivo.write("\n")
        archivo.write("Aciertos       : ")
        archivo.write(str(self.aciertos))
        archivo.write("\n")
        archivo.write("-----------------------------------")
        archivo.close()


