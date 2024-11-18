import sys


def mostrar_menu(): 
    
    while True:
        print("\n=== Menú Principal ===")
        print("1. Herramienta de Ayuda Matemática")
        print("2. Juego de Adivinanza")
        print("3. Juego de Preguntas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            from herramientadeayudamat import herramienta_matematica
        elif opcion == "2":
            from juegopreguntas import juego_adivinanza

        elif opcion == "3":
            from juegopreguntas import cargar_preguntas_desde_archivo

        elif opcion == "4":
            print("¡Gracias por jugar! Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    mostrar_menu()
