def mostrar_menu():
    print("\n=== Herramienta de Ayuda Matemática ===")
    print("1. Operaciones básicas")
    print("2. Resolver ecuaciones de primer grado")
    print("3. Conversión de unidades")
    print("4. Cálculo de perímetros")
    print("5. Resolver sistemas de ecuaciones lineales")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

def operaciones_basicas():
    print("\n--- Operaciones Básicas ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operacion = int(input("Elige la operación: "))

    if operacion == 1:
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif operacion == 2:
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif operacion == 3:
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif operacion == 4:
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: División por cero.")
    else:
        print("Operación no válida.")

def resolver_ecuacion():
    print("\n--- Resolver Ecuación de Primer Grado (ax + b = 0) ---")
    a = float(input("Ingresa el valor de 'a': "))
    b = float(input("Ingresa el valor de 'b': "))
    if a != 0:
        x = -b / a
        print(f"La solución de la ecuación es: x = {x}")
    else:
        print("Error: 'a' no puede ser 0.")

def conversion_unidades():
    print("\n--- Conversión de Unidades ---")
    print("1. Metros a kilómetros")
    print("2. Kilómetros a metros")

    opcion = int(input("Elige la conversión: "))
    
    if opcion == 1:
        metros = float(input("Ingresa la cantidad en metros: "))
        print(f"{metros} metros son {metros / 1000} kilómetros.")
    elif opcion == 2:
        kilometros = float(input("Ingresa la cantidad en kilómetros: "))
        print(f"{kilometros} kilómetros son {kilometros * 1000} metros.")

    else:
        print("Opción no válida.")

def calcular_area_perimetro():
    print("\n--- Cálculo de Perímetros ---")
    print("1. Cuadrado")
    print("2. Rectángulo")

    forma = int(input("Elige la forma: "))
    
    if forma == 1:
        lado = float(input("Ingresa la longitud del lado: "))
        area = lado ** 2
        perimetro = lado * 4
        print(f"Área del cuadrado: {area}")
        print(f"Perímetro del cuadrado: {perimetro}")
    elif forma == 2:
        largo = float(input("Ingresa el largo: "))
        ancho = float(input("Ingresa el ancho: "))
        area = largo * ancho
        perimetro = 2 * (largo + ancho)
        print(f"Área del rectángulo: {area}")
        print(f"Perímetro del rectángulo: {perimetro}")

    else:
        print("Opción no válida.")

def resolver_sistema_ecuaciones():
    print("\n--- Resolver Sistema de Ecuaciones Lineales ---")
    print("Sistema de ecuaciones:")
    print("1. a1*x + b1*y = c1")
    print("2. a2*x + b2*y = c2")
    a1 = float(input("Ingresa a1: "))
    b1 = float(input("Ingresa b1: "))
    c1 = float(input("Ingresa c1: "))
    a2 = float(input("Ingresa a2: "))
    b2 = float(input("Ingresa b2: "))
    c2 = float(input("Ingresa c2: "))

    determinante = a1 * b2 - a2 * b1
    
    if determinante == 0:
        print("El sistema no tiene solución única (puede ser dependiente o inconsistente).")
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        print(f"La solución del sistema es: x = {x}, y = {y}")

def herramienta_matematica():
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            operaciones_basicas()
        elif opcion == 2:
            resolver_ecuacion()
        elif opcion == 3:
            conversion_unidades()
        elif opcion == 4:
            calcular_area_perimetro()
        elif opcion == 5:
            resolver_sistema_ecuaciones()
        elif opcion == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

herramienta_matematica()
