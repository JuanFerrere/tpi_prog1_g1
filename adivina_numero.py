def iniciar_juego():
    import random

    def juego_adivinanza():
        numero_secreto = random.randint(1, 100)
        intentos = 7
    
        while intentos > 0:
            print("Intentos restantes:", intentos)
            adivinanza = int(input("Adivina el numero (entre 1 y 100): "))
            intentos -= 1
        
            if adivinanza < numero_secreto:
                print("Es mayor")
            elif adivinanza > numero_secreto:
                print("Es menor")
            else:
                print("¡Felicitaciones, le acertaste!")
                return
    
        print("Lo siento, has perdido. El numero era", numero_secreto)

    juego_adivinanza()
    
iniciar_juego()

