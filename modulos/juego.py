import random


class Juego():

    def __init__(self): 
        #El banco de preguntas sera un diccionario que contiene listas
        #banco_preguntas  = { 1:[[pregunta,r1,r2,r3,r4,respusta],[pregunta,r1,r2,r3,r4,respusta] ], 2:[ etc.... ]}
        self.banco_preguntas = {1: [], 2: [], 3: [], 4: [], 5: []}
       


    def verBancoPreguntas(self): 
        print("\n\n")
        print("-----------------------------------------")
        print("          PREGUNTAS GUARDADAS           ")
        print("-----------------------------------------")
        for items, values in self.banco_preguntas.items():
            #extramos los key del diccionario y los arrojamos en "items"
            print("######   Preguntas del nivel  {} ########".format(items)) 

            for preguntas in values:
                print("----> ",preguntas[0])
            print("")



    def configuracion(self):
        #Menu para llamar a los metodos de esta clase. 
        print("-----------------------------------------")
        print("        MENU DE CONFIGURACION            ")
        print("-----------------------------------------")
        print("")
        print("1) Para agregar una pregunta ")
        print("2) Ver todas preguntas ")
        print("3) Salir ")
        eleccion = str(input("Elija :"))
        if eleccion == "1":
            self.ingresarPreguntasManualmente()
        elif eleccion == "2":
            
            self.verBancoPreguntas()
        else:
            s = str(input("Eleccion Incorrecta [Enter continuar]"))



    def ingresarPreguntasManualmente(self):
        #Metodo para agregar preguntas
        #Se agregaran las preguntas y respuestas a la lista y posteriormente se guardaran en el archivo de texto.
        
        try:
            
            print("-----------------------------------------")
            print("        PREGUNTAS PARA EL SISTEMA        ")
            print("-----------------------------------------")

            preguntas = []
             
            nivel = int(input("Nivel        : "))
            pregunta = str(input("Pregunta     : "))

            preguntas.append(str(nivel))
            preguntas.append(str(pregunta))


            print("------------------------------------------")
            for i in range(4):
                res = str(input("respuesta {}  : ".format(i+1)))
                preguntas.append(res)
            print("------------------------------------------")

            correcta = int(input("¿correcta?   : "))
            preguntas.append(preguntas[correcta+1])


            archivo = open("preguntas/preguntas.txt", "a")
           
            archivo.write("\n")
            texto = ";".join(preguntas)
            archivo.write(texto)
            archivo.close()

            print("Pregunta añadida correctamente")

        except Exception as e:
            print("[ Ocurrió un error procesando la pregunta ]")



    def obtenerPreguntas(self, nivel):
        try:
            #Existe la posibilidad de no tener preguntas de un nivel en el banco por lo que el programa se prepara para una excepcion.
            #Obtenemos una pregunta aleatoria de un nivel especifico.
            pregunta = self.banco_preguntas[nivel][random.randint(0, len(self.banco_preguntas[nivel])-1)]

            while True:
                
                for i in range(0, 5):
                    if i == 0:
                        print(
                            " ##############################################################")
                        print("")
                        print(" ", pregunta[0])
                        print("")
                        print(
                            " ##############################################################")
                        print("")
                    else:
                        print("(", i, ") ", pregunta[i])

                valida = int(input("Su respuesta : "))
                if valida >= 1 and valida <= 4:
                    
                    break

            #Aqui se evalua si la respuesta es correcta o incorrecta
            if pregunta[valida] == pregunta[5]:
                print("[ Bien hecho! ] ")
                return True
            else:
                
                print("[ Fallaste por poco! ]")
                return False
        except:
            
            return None



    def procesar_guion(self,  guion):
        if len(guion) > 0:
            p = guion.split(";")
            pregunta = [p[1], p[2], p[3], p[4], p[5], p[6]]
            self.banco_preguntas[int(p[0])].append(pregunta)


    
    def cargarBancoPreguntas(self):
        #Cargamos las preguntas y utilizamos split ";" para separarlas
        
        try:
            archivo = open("preguntas/preguntas.txt").read().split("\n")
            for preguntas in archivo:
                self.procesar_guion(preguntas)
        except Exception as e:
            print(e)
