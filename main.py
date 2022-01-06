from modulos import juego
from modulos import jugador


menu = """
+------------------------------------------------------------+


         BIENVENIDO AL JUEGO DE PREGUNTAS Y RESPUESTAS


+------------------------------------------------------------+

1) Configuraciones del juego 
2) Iniciar Juego
3) Para salir 


"""


if __name__ == '__main__':
    partidaPreguntas = juego.Juego()
    
    partidaPreguntas.cargarBancoPreguntas()

    
    player  = jugador.Jugador()
    player.llenarInformacion()

    
    onGame = True


    while onGame == True:

        print (menu)
        eleccion = str(input("Eleccion : "))
        
        
        if eleccion=="1":
            partidaPreguntas.configuracion()
        

        elif eleccion=="2":
            
            for rondas in range(1,6):
                resultado = partidaPreguntas.obtenerPreguntas(rondas)

                if resultado==False:    
                    
                    print("[ EL JUEGO HA FINALIZADO. LA PREGUNTA NO ES CORRECTA ]")
                    break

                elif resultado==True: 
                    player.aumentarPuntaje()

                else: 
                    print("[Esta ronda no posee preguntas] RONDA  : ",rondas)
                    

        
            onGame = False

        elif eleccion=="3":
            break


        else:
            print("[Hasta luego!]")
        
    player.guardar_informacion_partida()