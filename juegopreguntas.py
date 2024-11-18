import random

def cargar_preguntas_desde_archivo(nombre_archivo):
    preguntas = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    i = 0
    while i < len(lineas):
        if lineas[i].strip(): 
            pregunta = lineas[i].strip()
            if i + 4 < len(lineas): 
                opciones = [lineas[i + 1].strip(), lineas[i + 2].strip(), lineas[i + 3].strip(), lineas[i + 4].strip()]
                respuesta_correcta = lineas[i + 5].strip()
                preguntas.append({
                    "pregunta": pregunta,
                    "opciones": opciones,
                    "respuesta_correcta": respuesta_correcta
                })
                i += 6 
            else:
                print("Advertencia: La pregunta no tiene suficiente información.")
                break
        else:
            i += 1  
    return preguntas

print ("Bienvenido al juego de Preguntas")
print("Ingrese el número 1 para jugar y el 0 para terminar")
iniciar = int(input())

if iniciar == 1:
    preguntas = cargar_preguntas_desde_archivo(r"C:\Users\nicod\python.py\TPI JUEGOS\juegostpi\preguntas.txt")
    
    if not preguntas:
        print("No se cargaron preguntas. Revisa el archivo.txt.")
        exit()

  
    preguntas_a_presentar = random.sample(preguntas, 10) if len(preguntas) >= 10 else preguntas

    random.shuffle(preguntas_a_presentar)  

    puntaje = 0  
    for numero, pregunta_data in enumerate(preguntas_a_presentar):
        print("\nPregunta", numero + 1, ":", pregunta_data['pregunta'])

        for opcion in pregunta_data['opciones']:
            print(opcion)

        respuesta_usuario = input("Elige una opción (a, b, c, d): ").lower()

        if respuesta_usuario == pregunta_data['respuesta_correcta']:
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto. La respuesta correcta era:", pregunta_data['respuesta_correcta'])

    print("\nTu puntuación final es", puntaje, "de", len(preguntas_a_presentar))
elif iniciar == 0:
    print("¡Gracias por jugar!")
else:
    print("Opción inválida. Intente de nuevo.")
