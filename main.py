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

    #Ejecutamos el juego e iteramos hasta que se anule una condicion
    #El juego termina si el jugador gana el juego o falla en la primera pregunta

    onGame = True


    while onGame == True:

        print (menu)
        eleccion = str(input("Eleccion : "))
        
        
        if eleccion=="1":
            partidaPreguntas.configuracion()
        

        elif eleccion=="2":
            
            for rondas in range(1,6):
                # cada ronda irá aumentando de 1 en 1 la dificultad del banco de preguntas de forma automatica.
                # llamamos al juego a que nos arroje la pregunta y nos devulva unicamente 
                # True   ---> si acierto 
                # False  ---> si fallo 
                # None   ---> si no hay preguntas de ese nivel  ( salta al proximo )
                resultado = partidaPreguntas.obtenerPreguntas(rondas)

                if resultado==False:    
                    
                    print("[ EL JUEGO HA FINALIZADO. LA RESPUESTA NO ES CORRECTA ]")
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
